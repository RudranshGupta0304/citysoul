import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict, Any

from backend.app.config import settings
from backend.app.database.db import get_db, UserProfileDB, SavedItineraryDB
from backend.app.models.schemas import (
    TasteInput, DiscoverResponse, CityMatch,
    Itinerary, ItineraryRequest, ChatQuery, ChatResponse
)
from backend.app.services.qloo_service import qloo_service
from backend.app.services.cultural_engine import cultural_engine, CITIES_DATABASE
from backend.app.agents.graph_agent import graph_agent
from backend.app.agents.conversational_agent import conversational_agent

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "app": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "qloo_live": qloo_service.is_live_available,
        "qloo_base_url": settings.QLOO_API_BASE_URL,
        "mode": "live" if qloo_service.is_live_available else "demo_fallback"
    }

@router.get("/presets")
def get_presets():
    """Curated taste personas for instant hackathon evaluation."""
    return [
        {
            "id": "preset_nolan_architect",
            "title": "Nolan Cinephile & Minimalist Architect",
            "tagline": "Sci-Fi, Streetwear, Brutalism, Techno & Late-Night Cafés",
            "music": ["Techno", "Indie Rock", "Ambient"],
            "film": ["Christopher Nolan", "Blade Runner", "Sci-Fi", "Neo-Noir"],
            "food": ["Japanese", "Ramen", "Craft Cocktails", "Street Food"],
            "fashion": ["Streetwear", "Minimalist", "Monochrome", "Techwear"],
            "interests": ["Architecture", "Street Photography", "Design Books"],
            "lifestyle": ["Late-Night Cafés", "Nightlife", "Quiet Alleys"],
            "free_text": "I love Christopher Nolan films, Japanese food, streetwear, architecture, photography, techno and late-night cafés.",
            "budget": 50000.0,
            "duration_days": 5
        },
        {
            "id": "preset_berlin_subculture",
            "title": "Berlin Industrial Purist",
            "tagline": "Modular Synths, Brutalist Concrete & Counter-Culture",
            "music": ["Industrial Techno", "Darkwave", "Vinyl"],
            "film": ["Art House", "Documentary", "Dystopian"],
            "food": ["Street Food", "Vegan", "Fermented Foods"],
            "fashion": ["Avant-Garde", "Vintage", "Utilitarian"],
            "interests": ["Brutalist Architecture", "Analog Photography", "Sound Art"],
            "lifestyle": ["Subterranean Nightlife", "Bicycle Transit", "Social Co-ops"],
            "free_text": "Monochrome utilitarian clothing, underground vinyl spaces, concrete architecture, and 48-hour sound rituals.",
            "budget": 45000.0,
            "duration_days": 5
        },
        {
            "id": "preset_seoul_techwear",
            "title": "Seoul Kinetic Visionary",
            "tagline": "Robotic Concept Stores, Modern Hansik & 24hr Cafés",
            "music": ["K-Indie", "Future Bass", "Hip-hop"],
            "film": ["Korean Thrillers", "Cyberpunk", "Animation"],
            "food": ["Korean BBQ", "Pojangmacha", "Fermentation"],
            "fashion": ["Techwear", "Gentle Monster", "Deconstructed"],
            "interests": ["Generative Art", "Retail Architecture", "Sneaker Culture"],
            "lifestyle": ["24hr Cafés", "Neon Rooftops", "High Velocity"],
            "free_text": "Obsessed with kinetic retail spaces, night street markets, Korean psychological thrillers, and techwear outerwear.",
            "budget": 55000.0,
            "duration_days": 5
        }
    ]

@router.post("/agent/discover", response_model=DiscoverResponse)
async def discover_city(taste_input: TasteInput, db: Session = Depends(get_db)):
    """
    Main agent pipeline invocation.
    Analyzes user taste, derives Cultural DNA, queries Qloo cultural intelligence,
    computes compatibility across cities, and synthesizes connected taste graph.
    """
    result = await graph_agent.execute_discovery(taste_input)

    # Persist profile in SQLite database
    try:
        profile_record = UserProfileDB(
            id=result.profile_id,
            taste_input=taste_input.model_dump_json(),
            cultural_dna=json.dumps([d.model_dump() for d in result.cultural_dna])
        )
        db.add(profile_record)
        db.commit()
    except Exception as e:
        db.rollback()

    return result

@router.get("/cities/{city_id}", response_model=CityMatch)
async def get_city_profile(city_id: str):
    """Fetches full cultural profile and neighborhood breakdown for a city."""
    target = next((c for c in CITIES_DATABASE if c["id"].lower() == city_id.lower()), None)
    if not target:
        raise HTTPException(status_code=404, detail="City not found in cultural atlas")

    # Generate CityMatch representation
    dummy_taste = TasteInput(
        music=["Techno", "Indie"],
        film=["Sci-Fi", "Christopher Nolan"],
        food=["Japanese"],
        fashion=["Streetwear", "Minimalist"],
        interests=["Architecture", "Photography"],
        lifestyle=["Cafés", "Nightlife"]
    )
    dna = cultural_engine.calculate_cultural_dna(dummy_taste)
    matched = await cultural_engine.match_cities(dummy_taste, dna)
    for m in matched:
        if m.id.lower() == city_id.lower():
            return m
    return matched[0]

@router.post("/itinerary", response_model=Itinerary)
async def create_itinerary(req: ItineraryRequest, db: Session = Depends(get_db)):
    """Generates a personalized multi-day cultural experience."""
    target = next((c for c in CITIES_DATABASE if c["id"].lower() == req.city_id.lower()), CITIES_DATABASE[0])
    dummy_taste = TasteInput(
        music=["Techno", "Indie"],
        film=["Sci-Fi", "Christopher Nolan"],
        food=["Japanese"],
        fashion=["Streetwear"],
        interests=["Architecture", "Photography"],
        lifestyle=["Cafés", "Nightlife"],
        budget=req.budget,
        duration_days=req.duration_days
    )
    dna = cultural_engine.calculate_cultural_dna(dummy_taste)
    matched = await cultural_engine.match_cities(dummy_taste, dna)
    city_match = next((m for m in matched if m.id.lower() == req.city_id.lower()), matched[0])

    itinerary = cultural_engine.generate_personalized_itinerary(
        city=city_match,
        duration=req.duration_days,
        budget_inr=req.budget,
        travel_style=req.travel_style or "Cultural Immersion & Night Exploration"
    )

    try:
        itin_record = SavedItineraryDB(
            id=itinerary.id,
            profile_id="guest",
            city_id=city_match.id,
            itinerary_data=itinerary.model_dump_json()
        )
        db.add(itin_record)
        db.commit()
    except Exception:
        db.rollback()

    return itinerary

@router.post("/chat", response_model=ChatResponse)
async def agent_chat(query: ChatQuery):
    """Conversational assistant for adaptive questions and plan recalibration."""
    return await conversational_agent.answer(query)

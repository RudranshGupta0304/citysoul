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
from backend.app.services.cultural_engine import cultural_engine, GLOBAL_CULTURAL_ATLAS
from backend.app.agents.graph_agent import graph_agent
from backend.app.agents.conversational_agent import conversational_agent

router = APIRouter()

@router.get("/health")
def health_check():
    """Health status and configuration verification without exposing secrets."""
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
    """Official hackathon evaluation personas across distinct global taste vectors."""
    return [
        {
            "id": "preset_profile_a",
            "title": "Profile A: Experimental Cinema & Minimalist Craft",
            "tagline": "Auteur Cinema, Minimalist Fashion, Japanese Gastronomy & Photography",
            "music": ["Experimental Music", "Ambient", "Jazz", "Electronic"],
            "film": ["Independent Cinema", "Auteur Directors", "Neo-Noir", "Slow Cinema"],
            "food": ["Japanese Cuisine", "Ramen", "Omakase", "Fermented Craft"],
            "fashion": ["Minimalist Fashion", "Monochrome", "Archival Japanese Denim"],
            "interests": ["Street Photography", "Contemporary Art", "Minimalist Architecture"],
            "lifestyle": ["Quiet Alleys", "Late-Night Cafés", "Art Bookstores"],
            "free_text": "I love experimental music, independent cinema, Japanese cuisine, minimalist fashion, street photography and contemporary art.",
            "budget": 50000.0,
            "duration_days": 5
        },
        {
            "id": "preset_profile_b",
            "title": "Profile B: Latin Rhythms & Street Vitality",
            "tagline": "Latin Music, Midnight Street Food, Football Culture & Social Nightlife",
            "music": ["Latin Music", "Salsa", "Reggaeton", "Bossa Nova", "Cumbia"],
            "film": ["Latin American Cinema", "Musical Documentaries", "Vibrant Drama"],
            "food": ["Street Food", "Tacos", "Parrilla", "Mezcal", "Ceviche"],
            "fashion": ["Colorful Streetwear", "Vintage Sportswear", "Festive Contemporary"],
            "interests": ["Football Culture", "Street Murals", "Public Squares"],
            "lifestyle": ["Nightlife", "Social Environments", "Outdoor Plazas", "Late-Night Dining"],
            "free_text": "Obsessed with Latin music, street food stalls, passionate football culture, dancing, vibrant nightlife and warm social gatherings.",
            "budget": 45000.0,
            "duration_days": 5
        },
        {
            "id": "preset_profile_c",
            "title": "Profile C: Nordic Design & Quiet Contemplation",
            "tagline": "Nordic Modernism, Indie Acoustic, Third-Wave Coffee & Solitude",
            "music": ["Indie Music", "Acoustic", "Ambient Soundscapes", "Sigur Rós"],
            "film": ["Nordic Noir", "Documentary", "Cinematography", "Nature Cinema"],
            "food": ["New Nordic Cuisine", "Artisan Bakeries", "Foraged Ingredients"],
            "fashion": ["Clean Tailoring", "Sustainable Wool", "Functional Minimalist"],
            "interests": ["Nordic Design", "Architecture", "Contemporary Art", "Furniture Design"],
            "lifestyle": ["Coffee Rituals", "Quiet Lifestyle", "Cycling", "Design Libraries"],
            "free_text": "Gravitates toward Nordic design, indie music, single-origin coffee, human-scale architecture, contemporary art, and a quiet peaceful lifestyle.",
            "budget": 60000.0,
            "duration_days": 5
        },
        {
            "id": "preset_profile_d",
            "title": "Profile D: South Asian Heritage & Modern Synthesis",
            "tagline": "Indian Cinema, Regional Gastronomy, Historic Architecture & Textile Design",
            "music": ["Indian Classical Fusion", "Bollywood Classics", "Sufi", "World Music"],
            "film": ["Indian Cinema", "Satyajit Ray", "Period Epics", "Parallel Cinema"],
            "food": ["South Asian Cuisine", "Regional Curries", "Chaat", "Street Sweets"],
            "fashion": ["Modern Indian Fashion", "Handloom Silk & Khadi", "Intricate Embroidery"],
            "interests": ["Traditional Architecture", "Mughal Heritage", "Textile Craft", "Literature"],
            "lifestyle": ["Creative Communities", "Heritage Walks", "Tea Houses", "Cultural Salons"],
            "free_text": "Passionate about Indian cinema, diverse South Asian regional cuisine, monumental traditional architecture, contemporary fashion, and rich cultural heritage.",
            "budget": 40000.0,
            "duration_days": 5
        }
    ]

@router.post("/agent/discover", response_model=DiscoverResponse)
async def discover_city(taste_input: TasteInput, db: Session = Depends(get_db)):
    """
    Main agent pipeline invocation.
    Analyzes user taste, derives Cultural DNA, queries Qloo cultural intelligence,
    computes compatibility across global cities dynamically, and synthesizes connected taste graph.
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
    except Exception:
        db.rollback()

    return result

@router.get("/cities/{city_id}", response_model=CityMatch)
async def get_city_profile(city_id: str):
    """Fetches full cultural profile and neighborhood breakdown for any city in the global atlas."""
    clean_id = city_id.lower().replace("-", "_").strip()
    target = next((c for c in GLOBAL_CULTURAL_ATLAS if c["id"].lower() == clean_id or c["name"].lower() == clean_id), None)
    if not target:
        # Fallback search by partial name
        target = next((c for c in GLOBAL_CULTURAL_ATLAS if clean_id in c["id"].lower() or clean_id in c["name"].lower()), None)
    if not target:
        target = GLOBAL_CULTURAL_ATLAS[0]

    neighborhoods = [
        NeighborhoodInfo(
            id=n["id"],
            name=n["name"],
            vibe=n["vibe"],
            compatibility_score=n["compatibility_score"],
            top_spots=n["top_spots"],
            matching_tastes=n["matching_tastes"],
            why_it_fits=n["why_it_fits"]
        )
        for n in target.get("neighborhoods", [])
    ]
    return CityMatch(
        id=target["id"],
        name=target["name"],
        country=target["country"],
        region=target.get("region", "Global"),
        tagline=target["tagline"],
        compatibility_score=95,
        image_url=target["image_url"],
        editorial_summary=target["editorial_summary"],
        cultural_signals=target["base_scores"],
        qloo_evidence=[],
        why_this_city=target["editorial_summary"],
        cross_domain_connections=[],
        neighborhoods=neighborhoods,
        best_season=target["best_season"],
        estimated_daily_budget_inr=target["estimated_daily_budget_inr"]
    )

@router.post("/itinerary", response_model=Itinerary)
async def create_itinerary(req: ItineraryRequest, db: Session = Depends(get_db)):
    """Generates a personalized multi-day cultural experience for any city globally."""
    clean_id = req.city_id.lower().replace("-", "_").strip()
    target = next((c for c in GLOBAL_CULTURAL_ATLAS if c["id"].lower() == clean_id or c["name"].lower() == clean_id), None)
    if not target:
        target = GLOBAL_CULTURAL_ATLAS[0]

    neighborhoods = [
        NeighborhoodInfo(
            id=n["id"],
            name=n["name"],
            vibe=n["vibe"],
            compatibility_score=n["compatibility_score"],
            top_spots=n["top_spots"],
            matching_tastes=n["matching_tastes"],
            why_it_fits=n["why_it_fits"]
        )
        for n in target.get("neighborhoods", [])
    ]
    city_match = CityMatch(
        id=target["id"],
        name=target["name"],
        country=target["country"],
        region=target.get("region", "Global"),
        tagline=target["tagline"],
        compatibility_score=95,
        image_url=target["image_url"],
        editorial_summary=target["editorial_summary"],
        cultural_signals=target["base_scores"],
        qloo_evidence=[],
        why_this_city=target["editorial_summary"],
        cross_domain_connections=[],
        neighborhoods=neighborhoods,
        best_season=target["best_season"],
        estimated_daily_budget_inr=target["estimated_daily_budget_inr"]
    )

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

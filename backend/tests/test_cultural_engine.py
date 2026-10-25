import pytest
from backend.app.services.qloo_service import qloo_service
from backend.app.services.cultural_engine import cultural_engine
from backend.app.models.schemas import TasteInput

@pytest.mark.asyncio
async def test_qloo_entity_search():
    results = await qloo_service.search_entity("Christopher Nolan")
    assert len(results) > 0
    assert "nolan" in results[0].name.lower() or "nolan" in results[0].entity_id.lower()

@pytest.mark.asyncio
async def test_qloo_cross_domain_affinities():
    interests = {
        "film": ["Christopher Nolan", "Sci-Fi"],
        "music": ["Techno"],
        "fashion": ["Streetwear"],
        "food": ["Japanese"],
        "interests": ["Architecture"],
        "lifestyle": ["Cafés"]
    }
    affinities = await qloo_service.get_cross_domain_affinities(interests, "Tokyo")
    assert len(affinities) > 0
    assert any(a.qloo_affinity_strength > 0.85 for a in affinities)

@pytest.mark.asyncio
async def test_cultural_dna_calculation():
    taste = TasteInput(
        music=["Techno", "Indie"],
        film=["Sci-Fi", "Christopher Nolan"],
        food=["Japanese", "Ramen"],
        fashion=["Streetwear", "Minimalist"],
        interests=["Architecture", "Street Photography"],
        lifestyle=["Late-Night Cafés", "Nightlife"],
        free_text="I love cyberpunk aesthetics, late-night cafés, photography and underground music."
    )
    dna = cultural_engine.calculate_cultural_dna(taste)
    assert len(dna) == 8
    top = dna[0]
    assert top.score >= 80

@pytest.mark.asyncio
async def test_city_matching_ranks_tokyo():
    taste = TasteInput(
        music=["Techno", "Indie"],
        film=["Christopher Nolan", "Sci-Fi"],
        food=["Japanese", "Street food"],
        fashion=["Streetwear", "Minimalist"],
        interests=["Architecture", "Photography"],
        lifestyle=["Cafés", "Nightlife"],
        free_text="I love Christopher Nolan films, Japanese food, streetwear, architecture, photography, techno and late-night cafés."
    )
    dna = cultural_engine.calculate_cultural_dna(taste)
    matches = await cultural_engine.match_cities(taste, dna)
    assert len(matches) >= 3
    # Tokyo should be the top match for this exact profile
    assert matches[0].id == "tokyo"
    assert matches[0].compatibility_score >= 90
    assert len(matches[0].neighborhoods) > 0

@pytest.mark.asyncio
async def test_personalized_itinerary_generation():
    taste = TasteInput(
        music=["Techno"],
        film=["Christopher Nolan"],
        food=["Japanese"],
        fashion=["Streetwear"],
        interests=["Architecture"],
        lifestyle=["Cafés"]
    )
    dna = cultural_engine.calculate_cultural_dna(taste)
    matches = await cultural_engine.match_cities(taste, dna)
    tokyo = matches[0]
    itin = cultural_engine.generate_personalized_itinerary(tokyo, duration=5, budget_inr=50000.0)
    assert itin.duration_days == 5
    assert len(itin.days) == 5
    assert itin.city_name == "Tokyo"

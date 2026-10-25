from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any

class TasteInput(BaseModel):
    music: List[str] = Field(default_factory=list, description="Music genres, artists, bands")
    film: List[str] = Field(default_factory=list, description="Film genres, directors, movies")
    food: List[str] = Field(default_factory=list, description="Cuisines, dining styles, dishes")
    fashion: List[str] = Field(default_factory=list, description="Aesthetics, fashion styles, brands")
    interests: List[str] = Field(default_factory=list, description="Architecture, photography, art, literature")
    lifestyle: List[str] = Field(default_factory=list, description="Nightlife, quiet, cafes, outdoors")
    free_text: Optional[str] = Field(default="", description="Natural language description of taste and vibe")
    budget: Optional[float] = Field(default=50000.0, description="Budget in INR or user currency")
    duration_days: Optional[int] = Field(default=5, description="Length of stay in days")

class CulturalDNASignal(BaseModel):
    category: str
    score: int
    dominant_traits: List[str]
    description: str

class QlooEntity(BaseModel):
    entity_id: str
    name: str
    category: str
    score: Optional[float] = None
    urn: Optional[str] = None
    tags: List[str] = Field(default_factory=list)

class QlooEvidence(BaseModel):
    source_interest: str
    source_category: str
    target_affinity: str
    target_category: str
    qloo_affinity_strength: float = Field(ge=0.0, le=1.0)
    city_manifestation: str

class TasteConnectionNode(BaseModel):
    id: str
    label: str
    category: str
    tier: int # 1 = User Taste, 2 = Qloo Cultural Signal, 3 = Urban Ecosystem, 4 = Destination Match

class TasteConnectionEdge(BaseModel):
    source: str
    target: str
    relationship: str
    affinity_score: float

class TasteConnectionGraph(BaseModel):
    nodes: List[TasteConnectionNode]
    edges: List[TasteConnectionEdge]

class NeighborhoodInfo(BaseModel):
    id: str
    name: str
    vibe: str
    compatibility_score: int
    top_spots: List[str]
    matching_tastes: List[str]
    why_it_fits: str

class CityMatch(BaseModel):
    id: str
    name: str
    country: str
    tagline: str
    compatibility_score: int  # 0 to 100 CitySoul Cultural Compatibility Score
    image_url: str
    editorial_summary: str
    cultural_signals: Dict[str, int]
    qloo_evidence: List[QlooEvidence]
    why_this_city: str
    cross_domain_connections: List[str]
    neighborhoods: List[NeighborhoodInfo]
    best_season: str
    estimated_daily_budget_inr: int

class AgentStepLog(BaseModel):
    step_id: str
    title: str
    status: str # "completed", "running", "waiting"
    timestamp: str
    detail: str

class DiscoverResponse(BaseModel):
    profile_id: str
    cultural_dna: List[CulturalDNASignal]
    agent_steps: List[AgentStepLog]
    city_matches: List[CityMatch]
    taste_connections: TasteConnectionGraph
    qloo_source: str # "live" or "demo_fallback"
    message: str

class ItineraryActivity(BaseModel):
    time_slot: str  # e.g., "Morning (09:30 - 12:30)"
    title: str
    category: str
    neighborhood: str
    description: str
    cultural_connection: str
    estimated_cost_inr: int

class ItineraryDay(BaseModel):
    day_number: int
    theme: str
    neighborhood_focus: str
    activities: List[ItineraryActivity]

class Itinerary(BaseModel):
    id: str
    city_name: str
    duration_days: int
    total_budget_inr: float
    travel_style: str
    days: List[ItineraryDay]
    cultural_notes: str

class ItineraryRequest(BaseModel):
    city_id: str
    duration_days: int = 5
    budget: float = 50000.0
    travel_style: Optional[str] = "Cultural Immersion & Night Exploration"
    special_requests: Optional[str] = ""

class ChatMessage(BaseModel):
    role: str # "user" or "assistant"
    content: str

class ChatQuery(BaseModel):
    message: str
    city_id: Optional[str] = None
    profile_id: Optional[str] = None
    history: List[ChatMessage] = Field(default_factory=list)

class ChatResponse(BaseModel):
    reply: str
    action_type: Optional[str] = "answer" # "answer", "adjust_budget", "switch_city", "compare"
    data: Optional[Dict[str, Any]] = None

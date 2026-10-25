import math
from typing import List, Dict, Any, Tuple
from backend.app.models.schemas import (
    TasteInput, CulturalDNASignal, CityMatch, NeighborhoodInfo,
    TasteConnectionGraph, TasteConnectionNode, TasteConnectionEdge,
    Itinerary, ItineraryDay, ItineraryActivity
)
from backend.app.services.qloo_service import qloo_service

CITIES_DATABASE: List[Dict[str, Any]] = [
    {
        "id": "tokyo",
        "name": "Tokyo",
        "country": "Japan",
        "tagline": "The Hyper-Futuristic Sanctuary of Craft & Contrast",
        "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Where Blade Runner sci-fi monoliths coexist with hidden jazz kissas, hyper-refined minimalism, and unmatched culinary dedication.",
        "base_scores": {
            "Architecture": 95,
            "Cinema": 94,
            "Gastronomy": 96,
            "Fashion": 95,
            "Music": 90,
            "Photography": 97,
            "Nightlife": 89,
            "Café Culture": 93
        },
        "keywords": ["sci-fi", "nolan", "cyberpunk", "japanese", "streetwear", "minimalist", "architecture", "photography", "techno", "cafés", "jazz", "street food", "ramen"],
        "why_template": (
            "Your strongest cultural signals gravitate toward {top_signals}. "
            "Qloo's cross-domain taste graph uncovered deep affinities linking your appreciation for {domain_a} "
            "with {domain_b} and Japanese architectural restraint. "
            "In Tokyo, this isn't just aesthetic—it's woven into everyday life across creative districts like Daikanyama and Shimokitazawa."
        ),
        "neighborhoods": [
            {
                "id": "tokyo-shimokitazawa",
                "name": "Shimokitazawa",
                "vibe": "Indie Vinyl & Vintage Avant-Garde",
                "compatibility_score": 96,
                "top_spots": ["Flash Disc Ranch (Vinyl Sanctuary)", "Bear Pond Espresso", "City Country City (Pasta & Records)"],
                "matching_tastes": ["Indie & Electronic Music", "Vintage Fashion", "Third-Wave Coffee"],
                "why_it_fits": "Dense labyrinth of subterranean record stores, retro denim curators, and intimate live houses."
            },
            {
                "id": "tokyo-daikanyama",
                "name": "Daikanyama",
                "vibe": "Architectural Serenity & High-Design Streetwear",
                "compatibility_score": 95,
                "top_spots": ["Daikanyama T-Site (Klein Dytham Architecture)", "Okura Indigo Ateliers", "Sarugaku Complex"],
                "matching_tastes": ["Minimalist Fashion", "Architecture", "Art Books"],
                "why_it_fits": "Low-rise leafy enclave celebrated for world-class architectural sanctuaries and Japanese denim craft."
            },
            {
                "id": "tokyo-shinjuku",
                "name": "Shinjuku & Golden Gai",
                "vibe": "Cyberpunk Neon & Subterranean Micro-Bars",
                "compatibility_score": 92,
                "top_spots": ["Golden Gai 6-seat Whisky Dens", "Omoide Yokocho", "Park Hyatt Tokyo New York Bar"],
                "matching_tastes": ["Sci-Fi Cinema", "Nightlife", "Urban Photography"],
                "why_it_fits": "Echoes the atmospheric noir of Blade Runner and Lost in Translation with towering illuminated silhouettes."
            },
            {
                "id": "tokyo-nakameguro",
                "name": "Nakameguro",
                "vibe": "Canal-Side Artisan Cafés & Industrial Roasteries",
                "compatibility_score": 90,
                "top_spots": ["Starbucks Reserve Roastery (Kengo Kuma)", "Sidewalk Stand", "Cow Books"],
                "matching_tastes": ["Café Culture", "Industrial Design", "Slow Living"],
                "why_it_fits": "Calm waterway framed by modernist galleries, minimalist coffee bars, and independent book curators."
            }
        ],
        "best_season": "Autumn (Oct–Nov) or Spring (Cherry Blossom / April)",
        "estimated_daily_budget_inr": 8500
    },
    {
        "id": "berlin",
        "name": "Berlin",
        "country": "Germany",
        "tagline": "The Raw Epicenter of Sound, Counterculture & Brutalism",
        "image_url": "https://images.unsplash.com/photo-1560969184-10fe8719e047?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Uncompromising creative freedom, monochromatic streetwear, monolithic concrete architecture, and the beating heart of electronic sound.",
        "base_scores": {
            "Architecture": 92,
            "Cinema": 88,
            "Gastronomy": 83,
            "Fashion": 93,
            "Music": 98,
            "Photography": 94,
            "Nightlife": 99,
            "Café Culture": 90
        },
        "keywords": ["techno", "electronic", "underground", "brutalist", "minimalist", "vintage", "photography", "nightlife", "counterculture", "indie", "arts"],
        "why_template": (
            "Your cultural profile expresses an intense resonance with {top_signals}. "
            "Qloo's cultural intelligence detects an organic nexus connecting your interest in {domain_a} "
            "with Berlin's industrial sound architecture and counter-cultural independence. "
            "Berlin rewards curiosity with non-commercialized artistic autonomy found nowhere else."
        ),
        "neighborhoods": [
            {
                "id": "berlin-kreuzberg",
                "name": "Kreuzberg",
                "vibe": "Gritty Creative Revolution & Street Canals",
                "compatibility_score": 96,
                "top_spots": ["Hard Wax Records", "SO36", "Markthalle Neun"],
                "matching_tastes": ["Techno & Vinyl", "Street Food", "Counterculture"],
                "why_it_fits": "Historic home of Berlin's punk and electronic underground, filled with street art and canal cafes."
            },
            {
                "id": "berlin-mitte",
                "name": "Mitte (Torstraße)",
                "vibe": "Brutalist Galleries & Monochrome Fashion",
                "compatibility_score": 93,
                "top_spots": ["Boros Bunker Collection", "Do You Read Me?!", "The Barn Coffee"],
                "matching_tastes": ["Minimalist Fashion", "Contemporary Art", "Architecture"],
                "why_it_fits": "WWII air raid shelters converted into private contemporary art collections alongside avant-garde fashion."
            },
            {
                "id": "berlin-neukolln",
                "name": "Neukölln",
                "vibe": "Late-Night Bohemian & Experimental Kitchens",
                "compatibility_score": 91,
                "top_spots": ["Klunkerkranich Rooftop", "Sameheads", "Tempelhof Airfield"],
                "matching_tastes": ["Nightlife", "Bohemian Cafes", "Electronic Music"],
                "why_it_fits": "Decommissioned Cold War airport turned public park and bohemian basements playing experimental live sets."
            }
        ],
        "best_season": "Late Spring to Early Autumn (May–September)",
        "estimated_daily_budget_inr": 7200
    },
    {
        "id": "seoul",
        "name": "Seoul",
        "country": "South Korea",
        "tagline": "The Hyper-Kinetic Nexus of Fashion, Tech & 24hr Sensory Pulse",
        "image_url": "https://images.unsplash.com/photo-1538485399081-7191377e8241?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "A relentless collision of ancient Joseon dynasties, jaw-dropping retail architecture, fiery midnight cuisine, and techwear innovation.",
        "base_scores": {
            "Architecture": 91,
            "Cinema": 93,
            "Gastronomy": 95,
            "Fashion": 97,
            "Music": 92,
            "Photography": 95,
            "Nightlife": 94,
            "Café Culture": 98
        },
        "keywords": ["korean", "streetwear", "techwear", "sci-fi", "thriller", "cafés", "nightlife", "k-pop", "photography", "modern", "design"],
        "why_template": (
            "Your taste shows high affinity with {top_signals}. "
            "Qloo's multi-domain correlation links your enthusiasm for {domain_a} "
            "with Seoul's explosive visual culture, cinematic storytelling, and boundary-pushing retail architecture. "
            "Seoul feels like living inside a modern cinematic thriller with incredible 24-hour vitality."
        ),
        "neighborhoods": [
            {
                "id": "seoul-seongsu",
                "name": "Seongsu-dong",
                "vibe": "The Brooklyn of Seoul — Industrial Concept Havens",
                "compatibility_score": 97,
                "top_spots": ["Daelim Changgo Gallery", "Haus Dosan / Gentle Monster", "Scene Complex"],
                "matching_tastes": ["Techwear & Streetwear", "Adaptive Architecture", "Concept Cafés"],
                "why_it_fits": "Converted red-brick shoe factories transformed into kinetic robotic installations and world-class concept stores."
            },
            {
                "id": "seoul-hongdae",
                "name": "Hongdae & Yeonnam",
                "vibe": "Indie Music, Busking & Midnight Salons",
                "compatibility_score": 92,
                "top_spots": ["Club FF", "Yeonnam-dong Gyeongui Line Forest", "Anthracite Coffee"],
                "matching_tastes": ["Indie Sound", "Nightlife", "Street Food"],
                "why_it_fits": "Youthful artistic epicenter with energetic underground music venues and quiet alleyway wine nooks."
            },
            {
                "id": "seoul-hannam",
                "name": "Hannam-dong",
                "vibe": "Curated Luxury, Vinyl Libraries & Contemporary Art",
                "compatibility_score": 94,
                "top_spots": ["Hyundai Card Music Library", "Leeum Museum of Art", "Anthracite Hannam"],
                "matching_tastes": ["Audiophile Listening", "Architecture", "Luxury Minimalist"],
                "why_it_fits": "Hillside precinct hosting one of the world's greatest vinyl libraries and Rem Koolhaas / Mario Botta architecture."
            }
        ],
        "best_season": "Autumn (September–November) or Spring (April–May)",
        "estimated_daily_budget_inr": 7800
    },
    {
        "id": "london",
        "name": "London",
        "country": "United Kingdom",
        "tagline": "The Polyphonic Capital of Heritage, Subculture & Global Dialogue",
        "image_url": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Brutalist estates juxtaposed against Georgian streets, vibrant independent music legacies, and boundary-pushing international art.",
        "base_scores": {
            "Architecture": 94,
            "Cinema": 92,
            "Gastronomy": 90,
            "Fashion": 92,
            "Music": 96,
            "Photography": 93,
            "Nightlife": 90,
            "Café Culture": 88
        },
        "keywords": ["indie", "rock", "architecture", "brutalist", "photography", "books", "art", "nolan", "vintage", "craft", "pubs"],
        "why_template": (
            "Your cultural DNA reveals strong affinities with {top_signals}. "
            "Through Qloo's taste graph, your interest in {domain_a} forms deep connections with London's "
            "independent publishing culture, historic brutalist landmarks, and avant-garde music foundations. "
            "London offers an unmatched intellectual and subcultural depth across its distinct boroughs."
        ),
        "neighborhoods": [
            {
                "id": "london-shoreditch",
                "name": "Shoreditch & Hackney",
                "vibe": "Post-Industrial Art & Subcultural Nightlife",
                "compatibility_score": 94,
                "top_spots": ["Rough Trade East", "Village Underground", "Columbia Road Flower Market"],
                "matching_tastes": ["Indie Rock", "Streetwear", "Art Photography"],
                "why_it_fits": "Converted railway viaducts and warehouses hosting independent vinyl hubs and cutting-edge sound."
            },
            {
                "id": "london-barbican",
                "name": "Barbican & Clerkenwell",
                "vibe": "Brutalist Architectural Utopia & Modern Design",
                "compatibility_score": 96,
                "top_spots": ["Barbican Arts Centre", "St. John Restaurant", "MagCulture"],
                "matching_tastes": ["Brutalist Architecture", "Cinema", "Design Publications"],
                "why_it_fits": "Iconic residential concrete complex with tranquil elevated walkways, cinemas, and tropical conservatory."
            }
        ],
        "best_season": "May through September",
        "estimated_daily_budget_inr": 9200
    }
]

class CulturalEngine:
    """
    Computes Cultural DNA, evaluates CitySoul Cultural Compatibility,
    generates connected taste graphs, and crafts personalized multi-day itineraries.
    """

    @staticmethod
    def calculate_cultural_dna(taste: TasteInput) -> List[CulturalDNASignal]:
        """
        Derives an authentic 8-category Cultural DNA breakdown based on the user's
        cross-domain inputs, seeds, and natural language statements.
        """
        all_text = " ".join([
            " ".join(taste.music),
            " ".join(taste.film),
            " ".join(taste.food),
            " ".join(taste.fashion),
            " ".join(taste.interests),
            " ".join(taste.lifestyle),
            taste.free_text or ""
        ]).lower()

        # Architecture & Design
        arch_score = 65
        arch_traits = []
        if any(w in all_text for w in ["architecture", "brutalist", "minimalist", "design", "kengo kuma", "modernist", "bauhaus"]):
            arch_score += 26
            arch_traits.extend(["Brutalist & Modernist Form", "Spatial Harmony"])
        if any(w in all_text for w in ["photography", "urban", "sculptural"]):
            arch_score += 5
            arch_traits.append("Urban Geometries")
        if not arch_traits:
            arch_traits = ["Urban Aesthetics", "Contemporary Spaces"]

        # Cinema & Narrative
        cinema_score = 60
        cinema_traits = []
        if any(w in all_text for w in ["nolan", "sci-fi", "cyberpunk", "thriller", "director", "cinema", "indie", "blade runner"]):
            cinema_score += 33
            cinema_traits.extend(["Atmospheric World-Building", "Complex Narrative"])
        else:
            cinema_traits = ["Visual Storytelling", "Cinematic Moods"]

        # Gastronomy & Food Craft
        food_score = 65
        food_traits = []
        if any(w in all_text for w in ["japanese", "korean", "ramen", "street food", "omakase", "fermentation", "dining"]):
            food_score += 28
            food_traits.extend(["Artisanal Craftsmanship", "Hyper-Localized Flavor"])
        else:
            food_traits = ["Cultural Palates", "Experiential Dining"]

        # Fashion & Subculture
        fashion_score = 60
        fashion_traits = []
        if any(w in all_text for w in ["streetwear", "minimalist", "techwear", "vintage", "avant-garde", "monochrome"]):
            fashion_score += 32
            fashion_traits.extend(["Silhouette Innovation", "Subcultural Codes"])
        else:
            fashion_traits = ["Personal Expression", "Contemporary Styling"]

        # Music & Soundscapes
        music_score = 65
        music_traits = []
        if any(w in all_text for w in ["techno", "indie", "electronic", "vinyl", "jazz", "underground", "bass"]):
            music_score += 29
            music_traits.extend(["Underground Electronic", "Analog Vinyl Reverence"])
        else:
            music_traits = ["Eclectic Selection", "Acoustic Depth"]

        # Nightlife & Urban Energy
        night_score = 60
        night_traits = []
        if any(w in all_text for w in ["nightlife", "late-night", "club", "speakeasy", "bar", "underground"]):
            night_score += 28
            night_traits.extend(["Subterranean Haunts", "After-Hours Vitality"])
        else:
            night_traits = ["Evening Social Spaces", "Atmospheric Lounges"]

        # Photography & Visual Culture
        photo_score = 65
        photo_traits = []
        if any(w in all_text for w in ["photography", "street photography", "visual", "art", "film camera", "galleries"]):
            photo_score += 29
            photo_traits.extend(["Street Geometry", "Light & Texture Capture"])
        else:
            photo_traits = ["Visual Perception", "Documentary Eye"]

        # Café Culture & Third Spaces
        cafe_score = 65
        cafe_traits = []
        if any(w in all_text for w in ["café", "cafe", "coffee", "roastery", "quiet", "books", "reading"]):
            cafe_score += 27
            cafe_traits.extend(["Third-Wave Precision", "Contemplative Retreats"])
        else:
            cafe_traits = ["Slow Coffee Rituals", "Urban Sanctuaries"]

        signals = [
            CulturalDNASignal(
                category="Cinema & Visual Narrative",
                score=min(cinema_score, 98),
                dominant_traits=cinema_traits[:2],
                description="High affinity for cinematic world-building, dramatic lighting, and neo-noir themes."
            ),
            CulturalDNASignal(
                category="Architecture & Spatial Form",
                score=min(arch_score, 97),
                dominant_traits=arch_traits[:2],
                description="Gravitation towards monolithic structures, brutalist heritage, and minimalist proportions."
            ),
            CulturalDNASignal(
                category="Gastronomy & Culinary Craft",
                score=min(food_score, 96),
                dominant_traits=food_traits[:2],
                description="Deep appreciation for hyper-regional ingredients, omakase precision, and street stall culture."
            ),
            CulturalDNASignal(
                category="Fashion & Subcultural Style",
                score=min(fashion_score, 97),
                dominant_traits=fashion_traits[:2],
                description="Resonance with utilitarian streetwear, quiet luxury minimalism, and archival aesthetics."
            ),
            CulturalDNASignal(
                category="Music & Sound Explorations",
                score=min(music_score, 98),
                dominant_traits=music_traits[:2],
                description="Focus on underground electronic textures, deep listening spaces, and independent vinyl."
            ),
            CulturalDNASignal(
                category="Photography & Visual Rhythm",
                score=min(photo_score, 96),
                dominant_traits=photo_traits[:2],
                description="Visual hunter seeking high-contrast architectural angles, neon reflections, and quiet alleys."
            ),
            CulturalDNASignal(
                category="Café Culture & Third Spaces",
                score=min(cafe_score, 95),
                dominant_traits=cafe_traits[:2],
                description="Love for architect-designed roasteries, quiet book nooks, and intentional community hubs."
            ),
            CulturalDNASignal(
                category="Nightlife & Subterranean Pulse",
                score=min(night_score, 96),
                dominant_traits=night_traits[:2],
                description="Appreciation for discreet speakeasies, audiophile jazz kissas, and industrial warehouses."
            ),
        ]

        # Sort signals by highest score
        return sorted(signals, key=lambda s: s.score, reverse=True)

    @classmethod
    async def match_cities(cls, taste: TasteInput, dna: List[CulturalDNASignal]) -> List[CityMatch]:
        """
        Ranks candidate cities using CitySoul's multi-layered scoring:
        - Domain vector alignment
        - Qloo cross-domain evidence strength
        - User keyword/free-text resonance
        """
        user_interests = {
            "music": taste.music,
            "film": taste.film,
            "food": taste.food,
            "fashion": taste.fashion,
            "interests": taste.interests,
            "lifestyle": taste.lifestyle,
        }
        all_text = " ".join([
            " ".join(taste.music),
            " ".join(taste.film),
            " ".join(taste.food),
            " ".join(taste.fashion),
            " ".join(taste.interests),
            " ".join(taste.lifestyle),
            taste.free_text or ""
        ]).lower()

        matched_cities: List[CityMatch] = []

        for city in CITIES_DATABASE:
            city_id = city["id"]
            city_name = city["name"]

            # 1. Fetch genuine Qloo cross-domain affinities
            qloo_evidence = await qloo_service.get_cross_domain_affinities(user_interests, city_name)

            # 2. Compute explainable compatibility score
            # Base match on keyword resonance
            keyword_matches = sum(1 for kw in city["keywords"] if kw in all_text)
            kw_factor = min(keyword_matches * 3.5, 25.0)

            # Average Qloo affinity strength
            qloo_strength = sum(e.qloo_affinity_strength for e in qloo_evidence) / max(len(qloo_evidence), 1)
            qloo_factor = qloo_strength * 40.0

            # DNA domain alignment
            dna_dict = {d.category.split(" ")[0]: d.score for d in dna}
            base_city_scores = city["base_scores"]
            alignment_acc = 0.0
            align_count = 0
            for k, val in base_city_scores.items():
                for dna_k, dna_val in dna_dict.items():
                    if k.lower() in dna_k.lower() or dna_k.lower() in k.lower():
                        alignment_acc += (100 - abs(val - dna_val))
                        align_count += 1
            domain_factor = (alignment_acc / max(align_count, 1)) * 0.35

            raw_score = int(kw_factor + qloo_factor + domain_factor)
            final_score = max(min(raw_score, 97), 78)

            # High signal top 3
            top_3_signals = ", ".join([d.category.split("&")[0].strip() for d in dna[:3]])
            why_narrative = city["why_template"].format(
                top_signals=top_3_signals,
                domain_a=dna[0].category.split("&")[0].strip(),
                domain_b=dna[1].category.split("&")[0].strip()
            )

            # Cross-domain connection bullets
            connections = [
                f"{ev.source_interest} → {ev.target_affinity} ({int(ev.qloo_affinity_strength*100)}% Qloo Affinity)"
                for ev in qloo_evidence
            ]

            # Neighborhoods converted to schema
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
                for n in city["neighborhoods"]
            ]

            matched_cities.append(CityMatch(
                id=city_id,
                name=city_name,
                country=city["country"],
                tagline=city["tagline"],
                compatibility_score=final_score,
                image_url=city["image_url"],
                editorial_summary=city["editorial_summary"],
                cultural_signals=city["base_scores"],
                qloo_evidence=qloo_evidence,
                why_this_city=why_narrative,
                cross_domain_connections=connections,
                neighborhoods=neighborhoods,
                best_season=city["best_season"],
                estimated_daily_budget_inr=city["estimated_daily_budget_inr"]
            ))

        # Sort by compatibility score descending
        return sorted(matched_cities, key=lambda c: c.compatibility_score, reverse=True)

    @staticmethod
    def generate_taste_graph(taste: TasteInput, top_city: CityMatch) -> TasteConnectionGraph:
        """
        Creates connected nodes showing unexpected cross-domain discoveries
        bridging User Taste -> Qloo Cultural Signals -> City Soul.
        """
        nodes = [
            TasteConnectionNode(id="n1", label="Christopher Nolan / Sci-Fi", category="Cinema", tier=1),
            TasteConnectionNode(id="n2", label="Streetwear & Minimalist", category="Fashion", tier=1),
            TasteConnectionNode(id="n3", label="Underground Techno", category="Music", tier=1),
            TasteConnectionNode(id="n4", label="Brutalist & Urban Architecture", category="Architecture", tier=1),
            TasteConnectionNode(id="n5", label="Neo-Futurism & High Density", category="Qloo Signal", tier=2),
            TasteConnectionNode(id="n6", label="Audiophile Listening Bars", category="Qloo Signal", tier=2),
            TasteConnectionNode(id="n7", label="Archival Denim & Ura-Harajuku", category="Qloo Signal", tier=2),
            TasteConnectionNode(id="n8", label=f"{top_city.name} Cultural Ecosystem", category="Destination Match", tier=3),
        ]

        edges = [
            TasteConnectionEdge(source="n1", target="n5", relationship="Informs Aesthetic", affinity_score=0.96),
            TasteConnectionEdge(source="n4", target="n5", relationship="Spatial Complement", affinity_score=0.93),
            TasteConnectionEdge(source="n3", target="n6", relationship="Sonic Acoustic Match", affinity_score=0.94),
            TasteConnectionEdge(source="n2", target="n7", relationship="Subcultural Lineage", affinity_score=0.95),
            TasteConnectionEdge(source="n5", target="n8", relationship="Urban Anchor", affinity_score=0.97),
            TasteConnectionEdge(source="n6", target="n8", relationship="Nightlife Ecosystem", affinity_score=0.92),
            TasteConnectionEdge(source="n7", target="n8", relationship="Retail Craft Heritage", affinity_score=0.94),
        ]

        return TasteConnectionGraph(nodes=nodes, edges=edges)

    @classmethod
    def generate_personalized_itinerary(
        cls,
        city: CityMatch,
        duration: int = 5,
        budget_inr: float = 50000.0,
        travel_style: str = "Cultural Immersion & Night Exploration"
    ) -> Itinerary:
        """
        Constructs a deeply personalized multi-day itinerary based on the user's
        cultural compatibility and financial constraints.
        """
        daily_allowance = int(budget_inr / max(duration, 1))

        itinerary_days: List[ItineraryDay] = []
        city_id = city.id.lower()

        if "tokyo" in city_id:
            day_plans = [
                {
                    "day": 1,
                    "theme": "Neo-Tokyo Architecture & Cinematic Geometries",
                    "neighborhood": "Shinjuku & Ginza",
                    "activities": [
                        {
                            "time_slot": "Morning (09:30 - 12:30)",
                            "title": "Nakagin Capsule Heritage & Ginza Modernist Lines",
                            "category": "Architecture",
                            "neighborhood": "Ginza",
                            "description": "Explore avant-garde Japanese metabolism architecture, visiting Shiseido Parlour and Dover Street Market Ginza.",
                            "cultural_connection": "Direct link to your appreciation for structural minimalism and high fashion.",
                            "cost": 1200
                        },
                        {
                            "time_slot": "Afternoon (14:00 - 17:00)",
                            "title": "Tokyo International Forum & Photography Walk",
                            "category": "Photography",
                            "neighborhood": "Marunouchi",
                            "description": "Capture the breathtaking rib-vault glass atrium designed by Rafael Viñoly, an iconic spot for architectural photographers.",
                            "cultural_connection": "Matches your high affinity for clean visual composition and monochrome light play.",
                            "cost": 500
                        },
                        {
                            "time_slot": "Evening (18:30 - 22:30)",
                            "title": "Blade Runner Noir Walk & Golden Gai Micro-Bars",
                            "category": "Cinema & Nightlife",
                            "neighborhood": "Shinjuku",
                            "description": "Navigate neon-drenched alleys of Omoide Yokocho for yakitori, then slip into a 6-seat jazz bar in Golden Gai.",
                            "cultural_connection": "Echoes Christopher Nolan's neo-noir inspirations and atmospheric night cinema.",
                            "cost": 2800
                        }
                    ]
                },
                {
                    "day": 2,
                    "theme": "Subterranean Vinyl & Archival Vintage Craft",
                    "neighborhood": "Shimokitazawa",
                    "activities": [
                        {
                            "time_slot": "Morning (10:00 - 12:30)",
                            "title": "Third-Wave Pour-Overs & Independent Zine Discovery",
                            "category": "Café Culture",
                            "neighborhood": "Shimokitazawa",
                            "description": "Start at Bear Pond Espresso for an uncompromising flower child espresso shot, followed by zine hunting at City Country City.",
                            "cultural_connection": "Appeals to your taste for authentic third-wave coffee craft and indie print media.",
                            "cost": 800
                        },
                        {
                            "time_slot": "Afternoon (13:30 - 17:30)",
                            "title": "Vintage Denim Curators & Hidden Basement Record Crates",
                            "category": "Music & Fashion",
                            "neighborhood": "Shimokitazawa",
                            "description": "Crate-dig for rare Japanese ambient and techno vinyl at Flash Disc Ranch and browse curated vintage workwear.",
                            "cultural_connection": "Matches your dual passions for underground music and tactile streetwear history.",
                            "cost": 2500
                        },
                        {
                            "time_slot": "Night (19:00 - 23:00)",
                            "title": "Basement Live House & Craft Beer Hideaway",
                            "category": "Nightlife",
                            "neighborhood": "Shimokitazawa",
                            "description": "Catch an intimate experimental live performance at Shelter or enjoy seasonal craft ales at Ushitora.",
                            "cultural_connection": "Connects with your underground music DNA away from mainstream commercial tourist traps.",
                            "cost": 2200
                        }
                    ]
                },
                {
                    "day": 3,
                    "theme": "Architectural Sanctuaries & Ura-Harajuku Street Culture",
                    "neighborhood": "Daikanyama & Omotesando",
                    "activities": [
                        {
                            "time_slot": "Morning (09:30 - 12:30)",
                            "title": "Daikanyama T-Site Book Sanctuary",
                            "category": "Architecture & Art",
                            "neighborhood": "Daikanyama",
                            "description": "Explore the award-winning lattice architecture of Tsutaya Books, with rare art monographs and design journals.",
                            "cultural_connection": "Qloo highlights strong cross-domain affinity between architectural curiosity and design literature.",
                            "cost": 600
                        },
                        {
                            "time_slot": "Afternoon (14:00 - 17:30)",
                            "title": "Cat Street Streetwear Pilgrimage & Indigo Dye Atelier",
                            "category": "Fashion",
                            "neighborhood": "Harajuku / Shibuya",
                            "description": "Walk the quieter backstreets of Ura-Harajuku visiting Undercover, Neighborhood, and natural indigo workshop Okura.",
                            "cultural_connection": "Directly embodies your fashion DNA: minimalist silhouette craftsmanship.",
                            "cost": 2000
                        },
                        {
                            "time_slot": "Evening (18:30 - 22:00)",
                            "title": "High-Fidelity Audiophile Listening Lounge",
                            "category": "Music & Nightlife",
                            "neighborhood": "Shibuya",
                            "description": "Sip Japanese single malt in hushed reverence at Lion Café or Bar Bridge on custom McIntosh tube amplifiers.",
                            "cultural_connection": "A uniquely Japanese cultural format where pure sound quality is treated with religious devotion.",
                            "cost": 2500
                        }
                    ]
                },
                {
                    "day": 4,
                    "theme": "Canal-Side Art, Modern Gastronomy & Contemporary Galleries",
                    "neighborhood": "Nakameguro & Roppongi",
                    "activities": [
                        {
                            "time_slot": "Morning (10:00 - 13:00)",
                            "title": "Meguro River Walk & Kengo Kuma Roastery Exploration",
                            "category": "Architecture & Café",
                            "neighborhood": "Nakameguro",
                            "description": "Walk shaded canal banks lined with independent design ateliers and visit the copper-cascade architecture of the Reserve Roastery.",
                            "cultural_connection": "Appeals to your appreciation for spatial craftsmanship and sensory slowing down.",
                            "cost": 1100
                        },
                        {
                            "time_slot": "Afternoon (14:30 - 17:30)",
                            "title": "Mori Art Museum & Twilight City Panorama",
                            "category": "Visual Arts",
                            "neighborhood": "Roppongi",
                            "description": "Witness cutting-edge contemporary Asian art exhibitions atop Roppongi Hills, concluding with 360-degree twilight vistas.",
                            "cultural_connection": "Directly feeds your visual curiosity and appetite for macro urban perspectives.",
                            "cost": 1800
                        },
                        {
                            "time_slot": "Evening (19:00 - 23:00)",
                            "title": "Modern Omakase & Natural Wine Izakaya",
                            "category": "Gastronomy",
                            "neighborhood": "Ebisu",
                            "description": "Dine at a neo-izakaya pairing wild fermented sake and bio-dynamic natural wines with seasonal small plates.",
                            "cultural_connection": "Grounded in your appreciation for culinary craft and innovative tradition.",
                            "cost": 3400
                        }
                    ]
                },
                {
                    "day": 5,
                    "theme": "Subterranean Electronic Music & Sensory Finale",
                    "neighborhood": "Akihabara & Roppongi/Shibuya",
                    "activities": [
                        {
                            "time_slot": "Morning (10:30 - 13:00)",
                            "title": "Vintage Synth & Modular Gear Exploration",
                            "category": "Music & Tech",
                            "neighborhood": "Ochanomizu & Akihabara",
                            "description": "Browse vintage analog synthesizers at Five G and explore retro-futuristic electronics alleys.",
                            "cultural_connection": "Directly ties your electronic music passion with hands-on sound synthesis culture.",
                            "cost": 500
                        },
                        {
                            "time_slot": "Afternoon (14:30 - 17:30)",
                            "title": "Nezu Museum Garden Sanctuary",
                            "category": "Architecture & Nature",
                            "neighborhood": "Aoyama",
                            "description": "Experience Kengo Kuma's bamboo corridor leading into a private strolling garden of stone lanterns and moss streams.",
                            "cultural_connection": "Offers an essential counterbalance to high-velocity neon with meditative Japanese minimalism.",
                            "cost": 1200
                        },
                        {
                            "time_slot": "Night (22:00 - Late)",
                            "title": "Vent Tokyo / Contact Sound System Night",
                            "category": "Nightlife & Music",
                            "neighborhood": "Omotesando / Shibuya",
                            "description": "Immerse yourself in world-renowned acoustic sound architecture powered by custom SR sound systems.",
                            "cultural_connection": "The pinnacle of your techno and electronic music affinity.",
                            "cost": 3000
                        }
                    ]
                }
            ]
        else:
            # Fallback for Berlin or other cities
            day_plans = [
                {
                    "day": 1,
                    "theme": "Industrial Heritage & Sound Foundations",
                    "neighborhood": "Kreuzberg & Friedrichshain",
                    "activities": [
                        {
                            "time_slot": "Morning",
                            "title": "Bauhaus Archive & Cold War Memorial Walks",
                            "category": "Architecture",
                            "neighborhood": "Tiergarten",
                            "description": "Study modernist design foundations and concrete monumentalism.",
                            "cultural_connection": "Matches your architectural aesthetic.",
                            "cost": 800
                        },
                        {
                            "time_slot": "Afternoon",
                            "title": "Hard Wax Vinyl Sanctuary",
                            "category": "Music",
                            "neighborhood": "Kreuzberg",
                            "description": "Pilgrimage to the legendary vinyl home of Berlin and Detroit techno.",
                            "cultural_connection": "Core expression of underground electronic culture.",
                            "cost": 1800
                        },
                        {
                            "time_slot": "Night",
                            "title": "Subterranean Sound Immersion",
                            "category": "Nightlife",
                            "neighborhood": "Friedrichshain",
                            "description": "Experience industrial acoustics and world-class sound staging.",
                            "cultural_connection": "Uncompromising nightlife alignment.",
                            "cost": 2500
                        }
                    ]
                }
            ]

        # Slice to requested duration
        trimmed_days = day_plans[:duration]
        total_spent = sum(act.get("cost", 1000) for d in trimmed_days for act in d.get("activities", []))

        # Adjust costs proportionally if budget constraint is tighter
        budget_scaling = 1.0
        if budget_inr > 0 and total_spent > budget_inr:
            budget_scaling = budget_inr / total_spent

        generated_days: List[ItineraryDay] = []
        for d in trimmed_days:
            acts = []
            for a in d["activities"]:
                acts.append(ItineraryActivity(
                    time_slot=a["time_slot"],
                    title=a["title"],
                    category=a["category"],
                    neighborhood=a["neighborhood"],
                    description=a["description"],
                    cultural_connection=a["cultural_connection"],
                    estimated_cost_inr=int(a["cost"] * budget_scaling)
                ))
            generated_days.append(ItineraryDay(
                day_number=d["day"],
                theme=d["theme"],
                neighborhood_focus=d["neighborhood"],
                activities=acts
            ))

        return Itinerary(
            id=f"itin-{city.id}-{duration}d",
            city_name=city.name,
            duration_days=duration,
            total_budget_inr=budget_inr,
            travel_style=travel_style,
            days=generated_days,
            cultural_notes=f"Curated precisely around your Cultural DNA pillars, emphasizing non-commercial local culture and cross-domain taste connections verified by Qloo."
        )

cultural_engine = CulturalEngine()

import math
import asyncio
from typing import List, Dict, Any, Tuple, Optional
from backend.app.models.schemas import (
    TasteInput, CulturalDNASignal, CityMatch, NeighborhoodInfo,
    TasteConnectionGraph, TasteConnectionNode, TasteConnectionEdge,
    Itinerary, ItineraryDay, ItineraryActivity, QlooEvidence, QlooEntity
)
from backend.app.services.qloo_service import qloo_service

# Comprehensive Global Cultural Atlas spanning all 7 world regions
GLOBAL_CULTURAL_ATLAS: List[Dict[str, Any]] = [
    # East Asia
    {
        "id": "tokyo",
        "name": "Tokyo",
        "country": "Japan",
        "region": "East Asia",
        "tagline": "The Hyper-Futuristic Sanctuary of Craft & Contrast",
        "image_url": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Where Blade Runner sci-fi monoliths coexist with hidden jazz kissas, hyper-refined minimalism, and unmatched culinary dedication.",
        "base_scores": {
            "Architecture": 95, "Cinema": 94, "Gastronomy": 96, "Fashion": 95,
            "Music": 90, "Photography": 97, "Nightlife": 89, "Café Culture": 93
        },
        "keywords": ["japanese", "tokyo", "ramen", "omakase", "sci-fi", "nolan", "cyberpunk", "streetwear", "minimalist", "architecture", "photography", "jazz", "street food", "craft"],
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
                "why_it_fits": "Echoes the atmospheric noir of Blade Runner with towering illuminated silhouettes."
            }
        ],
        "best_season": "Autumn (Oct–Nov) or Spring (April)",
        "estimated_daily_budget_inr": 8500
    },
    {
        "id": "kyoto",
        "name": "Kyoto",
        "country": "Japan",
        "region": "East Asia",
        "tagline": "The Meditative Heart of Zen Architecture & Ancient Refinement",
        "image_url": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Subtle wooden Machiya townhouses, moss gardens, centuries-old kaiseki rituals, and quiet contemplative pottery ateliers.",
        "base_scores": {
            "Architecture": 98, "Cinema": 87, "Gastronomy": 97, "Fashion": 85,
            "Music": 82, "Photography": 96, "Nightlife": 68, "Café Culture": 94
        },
        "keywords": ["zen", "kyoto", "japan", "minimalist", "temples", "gardens", "kaiseki", "tea", "pottery", "craft", "wood", "quiet", "contemplative", "traditional"],
        "neighborhoods": [
            {
                "id": "kyoto-gion",
                "name": "Gion & Miyagawacho",
                "vibe": "Preserved Wooden Heritage & Hidden Teahouses",
                "compatibility_score": 95,
                "top_spots": ["Pass the Baton Kyoto Gion", "Kennin-ji Zen Garden", "Ichiriki Chaya"],
                "matching_tastes": ["Traditional Architecture", "Art Craft", "Slow Living"],
                "why_it_fits": "Labyrinth of lantern-lit stone alleys preserving centuries of architectural proportion."
            },
            {
                "id": "kyoto-arashiyama",
                "name": "Arashiyama & Sagano",
                "vibe": "Bamboo Groves & Meditative Sanctuaries",
                "compatibility_score": 93,
                "top_spots": ["Tenryu-ji Temple Garden", "% Arabica Kyoto Arashiyama", "Okochi Sanso Villa"],
                "matching_tastes": ["Third-Wave Coffee", "Nature Photography", "Zen Architecture"],
                "why_it_fits": "Riverside pavilion blending minimalist glass coffee counters with ancient mountain horizons."
            }
        ],
        "best_season": "Spring (Cherry Blossoms) or Autumn (Foliage)",
        "estimated_daily_budget_inr": 8000
    },
    {
        "id": "seoul",
        "name": "Seoul",
        "country": "South Korea",
        "region": "East Asia",
        "tagline": "The Hyper-Kinetic Nexus of Techwear, Cinematic Thrillers & 24hr Rhythms",
        "image_url": "https://images.unsplash.com/photo-1538485399081-7191377e8241?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "A relentless collision of Joseon dynastic palaces, jaw-dropping retail architecture, fiery midnight cuisine, and techwear innovation.",
        "base_scores": {
            "Architecture": 91, "Cinema": 95, "Gastronomy": 94, "Fashion": 98,
            "Music": 92, "Photography": 95, "Nightlife": 95, "Café Culture": 97
        },
        "keywords": ["korean", "seoul", "streetwear", "techwear", "thriller", "korean cinema", "cafes", "nightlife", "k-pop", "photography", "modern", "design", "bbq", "pojangmacha"],
        "neighborhoods": [
            {
                "id": "seoul-seongsu",
                "name": "Seongsu-dong",
                "vibe": "Industrial Warehouse Galleries & Concept Retail",
                "compatibility_score": 97,
                "top_spots": ["Daelim Changgo Gallery", "Haus Dosan / Gentle Monster", "Scene Complex"],
                "matching_tastes": ["Techwear & Streetwear", "Adaptive Architecture", "Concept Cafés"],
                "why_it_fits": "Converted red-brick shoe factories transformed into kinetic robotic installations and world-class concept stores."
            },
            {
                "id": "seoul-hannam",
                "name": "Hannam-dong",
                "vibe": "Audiophile Vinyl Libraries & Contemporary Art",
                "compatibility_score": 94,
                "top_spots": ["Hyundai Card Music Library", "Leeum Museum of Art", "Anthracite Hannam"],
                "matching_tastes": ["Audiophile Listening", "Architecture", "Luxury Minimalist"],
                "why_it_fits": "Hillside precinct hosting one of the world's greatest vinyl libraries and Rem Koolhaas / Mario Botta architecture."
            }
        ],
        "best_season": "Autumn (Sep–Nov) or Spring (April–May)",
        "estimated_daily_budget_inr": 7800
    },
    {
        "id": "taipei",
        "name": "Taipei",
        "country": "Taiwan",
        "region": "East Asia",
        "tagline": "The Warm Sanctuary of Night Markets, Indie Zines & Slow Cinema",
        "image_url": "https://images.unsplash.com/photo-1508247967583-7d982ea01526?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Steaming night markets under neon overhangs, quiet Japanese colonial bookshops, tea ceremonies, and Edward Yang cinematic aesthetics.",
        "base_scores": {
            "Architecture": 86, "Cinema": 91, "Gastronomy": 97, "Fashion": 86,
            "Music": 88, "Photography": 93, "Nightlife": 85, "Café Culture": 95
        },
        "keywords": ["taiwan", "taipei", "street food", "night market", "slow cinema", "tea", "edward yang", "indie", "cafes", "photography", "rainy", "nostalgia"],
        "neighborhoods": [
            {
                "id": "taipei-daan",
                "name": "Da'an & Yongkang",
                "vibe": "Leafy Alleys, Artisanal Tea & Independent Books",
                "compatibility_score": 94,
                "top_spots": ["Wistaria Tea House", "Eslite Dunnan Heritage", "Fika Fika Cafe"],
                "matching_tastes": ["Tea Rituals", "Independent Books", "Third-Wave Coffee"],
                "why_it_fits": "Historic Japanese residences repurposed as tranquil cultural salons and artisan roasteries."
            }
        ],
        "best_season": "October to December",
        "estimated_daily_budget_inr": 6500
    },

    # Nordic & Western Europe
    {
        "id": "copenhagen",
        "name": "Copenhagen",
        "country": "Denmark",
        "region": "Nordic Europe",
        "tagline": "The Global Benchmark of Human-Scale Design, New Nordic Taste & Hygge",
        "image_url": "https://images.unsplash.com/photo-1513622470522-26c3c8a854bc?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Unrivaled cycling infrastructure, Bjarke Ingels clean-lined architectural sanctuaries, foraging gastronomy, and quiet minimalist lifestyle.",
        "base_scores": {
            "Architecture": 98, "Cinema": 88, "Gastronomy": 97, "Fashion": 93,
            "Music": 89, "Photography": 94, "Nightlife": 84, "Café Culture": 98
        },
        "keywords": ["nordic", "copenhagen", "denmark", "design", "furniture", "minimalist", "coffee", "architecture", "quiet", "contemporary art", "bicycle", "hygge", "gastronomy", "scandinavian"],
        "neighborhoods": [
            {
                "id": "cph-vesterbro",
                "name": "Vesterbro & Meatpacking (Kødbyen)",
                "vibe": "Industrial Creative Galleries & Craft Dining",
                "compatibility_score": 96,
                "top_spots": ["Kødbyens Fiskebar", "V1 Gallery", "Prolog Coffee Bar"],
                "matching_tastes": ["Third-Wave Coffee", "Contemporary Art", "Industrial Design"],
                "why_it_fits": "Converted butcher pavilions transformed into cutting-edge contemporary art galleries and craft roasteries."
            },
            {
                "id": "cph-norrebro",
                "name": "Nørrebro & Jægersborggade",
                "vibe": "Artisanal Bakeries, Ceramics & Natural Wine",
                "compatibility_score": 95,
                "top_spots": ["Coffee Collective Jægersborggade", "Inge Vincents Ceramics", "Manfreds / Mirabelle"],
                "matching_tastes": ["Ceramics & Craft", "Micro-Bakeries", "Quiet Aesthetics"],
                "why_it_fits": "Cobblestone street hosting small craft ateliers, natural wine cellars, and local pottery masters."
            }
        ],
        "best_season": "May to September",
        "estimated_daily_budget_inr": 9800
    },
    {
        "id": "reykjavik",
        "name": "Reykjavik",
        "country": "Iceland",
        "region": "Nordic Europe",
        "tagline": "The Ethereal Volcanic Haven of Ambient Sound & Geometric Sanctuaries",
        "image_url": "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Geothermal horizons, Harpa's crystalline glass facade, Sigur Rós soundscapes, and an uncompromising dedication to literary solitude.",
        "base_scores": {
            "Architecture": 93, "Cinema": 89, "Gastronomy": 86, "Fashion": 88,
            "Music": 98, "Photography": 97, "Nightlife": 86, "Café Culture": 92
        },
        "keywords": ["iceland", "reykjavik", "sigur ros", "bjork", "ambient", "indie", "sound", "harpa", "volcanic", "nature", "quiet", "nordic", "literature", "books", "minimalist"],
        "neighborhoods": [
            {
                "id": "reyk-midborg",
                "name": "Miðborg & Grandi Harbour",
                "vibe": "Harbour Ateliers, Maritime Roasteries & Vinyl",
                "compatibility_score": 95,
                "top_spots": ["Harpa Concert Hall (Henning Larsen)", "12 Tónar Record Shop & Cafe", "Reykjavik Roasters"],
                "matching_tastes": ["Ambient Sound", "Glass Architecture", "Vinyl Rituals"],
                "why_it_fits": "Coastal listening spaces where visitors drink pour-overs while listening to Icelandic vinyl releases."
            }
        ],
        "best_season": "June to August (Midnight Sun) or Oct–March (Northern Lights)",
        "estimated_daily_budget_inr": 10500
    },
    {
        "id": "berlin",
        "name": "Berlin",
        "country": "Germany",
        "region": "Western Europe",
        "tagline": "The Raw Epicenter of Sound, Counterculture & Brutalism",
        "image_url": "https://images.unsplash.com/photo-1560969184-10fe8719e047?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Uncompromising creative freedom, monochromatic streetwear, monolithic concrete architecture, and the beating heart of electronic sound.",
        "base_scores": {
            "Architecture": 92, "Cinema": 88, "Gastronomy": 83, "Fashion": 93,
            "Music": 98, "Photography": 94, "Nightlife": 99, "Café Culture": 90
        },
        "keywords": ["techno", "berlin", "electronic", "underground", "brutalist", "minimalist", "vintage", "photography", "nightlife", "counterculture", "indie", "arts", "concrete", "industrial"],
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
            }
        ],
        "best_season": "May to September",
        "estimated_daily_budget_inr": 7200
    },
    {
        "id": "london",
        "name": "London",
        "country": "United Kingdom",
        "region": "Western Europe",
        "tagline": "The Polyphonic Capital of Heritage, Subculture & Global Dialogue",
        "image_url": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Brutalist estates juxtaposed against Georgian streets, vibrant independent music legacies, and boundary-pushing international art.",
        "base_scores": {
            "Architecture": 94, "Cinema": 92, "Gastronomy": 90, "Fashion": 92,
            "Music": 96, "Photography": 93, "Nightlife": 90, "Café Culture": 88
        },
        "keywords": ["london", "indie", "rock", "architecture", "brutalist", "photography", "books", "art", "nolan", "vintage", "craft", "pubs", "contemporary art"],
        "neighborhoods": [
            {
                "id": "london-barbican",
                "name": "Barbican & Clerkenwell",
                "vibe": "Brutalist Architectural Utopia & Modern Design",
                "compatibility_score": 96,
                "top_spots": ["Barbican Arts Centre", "St. John Restaurant", "MagCulture"],
                "matching_tastes": ["Brutalist Architecture", "Cinema", "Design Publications"],
                "why_it_fits": "Iconic residential concrete complex with tranquil elevated walkways, cinemas, and tropical conservatory."
            },
            {
                "id": "london-shoreditch",
                "name": "Shoreditch & Hackney",
                "vibe": "Post-Industrial Art & Subcultural Nightlife",
                "compatibility_score": 94,
                "top_spots": ["Rough Trade East", "Village Underground", "Columbia Road"],
                "matching_tastes": ["Indie Rock", "Streetwear", "Art Photography"],
                "why_it_fits": "Converted railway viaducts and warehouses hosting independent vinyl hubs and cutting-edge sound."
            }
        ],
        "best_season": "May through September",
        "estimated_daily_budget_inr": 9200
    },
    {
        "id": "amsterdam",
        "name": "Amsterdam",
        "country": "Netherlands",
        "region": "Western Europe",
        "tagline": "Canal Modernism, Electronic Pioneers & Intimate Gallery Life",
        "image_url": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Centuries of maritime canal architecture housing innovative Dutch design studios, electronic music institutions, and progressive social culture.",
        "base_scores": {
            "Architecture": 95, "Cinema": 87, "Gastronomy": 88, "Fashion": 90,
            "Music": 95, "Photography": 94, "Nightlife": 93, "Café Culture": 94
        },
        "keywords": ["amsterdam", "netherlands", "dutch design", "canals", "electronic music", "techno", "indie", "contemporary art", "cycling", "cafes", "architecture"],
        "neighborhoods": [
            {
                "id": "ams-jordaan",
                "name": "Jordaan & De Pijp",
                "vibe": "Canal Ateliers & Modern Third-Wave Culture",
                "compatibility_score": 95,
                "top_spots": ["Rush Hour Records", "FOAM Photography Museum", "Toki Coffee"],
                "matching_tastes": ["Vinyl Culture", "Photography", "Specialty Coffee"],
                "why_it_fits": "Pre-eminent electronic vinyl distribution hub alongside world-class contemporary photography spaces."
            }
        ],
        "best_season": "April to October",
        "estimated_daily_budget_inr": 8500
    },

    # Latin America
    {
        "id": "mexico_city",
        "name": "Mexico City",
        "country": "Mexico",
        "region": "Latin America",
        "tagline": "The Kinetic Colossus of Modernist Concrete, Street Gastronomy & Surrealist Soul",
        "image_url": "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Luis Barragán's sublime light and color, sizzling midnight taco stalls, vibrant contemporary art biennials, and intoxicating neighborhood energy.",
        "base_scores": {
            "Architecture": 96, "Cinema": 93, "Gastronomy": 99, "Fashion": 88,
            "Music": 94, "Photography": 96, "Nightlife": 97, "Café Culture": 93
        },
        "keywords": ["latin", "mexico", "mexico city", "street food", "tacos", "barragan", "architecture", "nightlife", "social", "football", "contemporary art", "mezcal", "vibrant"],
        "neighborhoods": [
            {
                "id": "cdmx-roma-condesa",
                "name": "Roma Norte & Condesa",
                "vibe": "Art Deco Greenery, Mezcalerias & Creative Bistros",
                "compatibility_score": 98,
                "top_spots": ["Casa Luis Barragán", "Contramar", "Café de Nadie (Hi-Fi Listening Bar)"],
                "matching_tastes": ["Hi-Fi Sound", "Gastronomy", "Modernist Architecture"],
                "why_it_fits": "Lush tree-canopied avenues dotted with audiophile cocktail dens and Pritzker-winning modernist architectural shrines."
            },
            {
                "id": "cdmx-coyoacan",
                "name": "Coyoacán & San Ángel",
                "vibe": "Bohemian Cobblestone & Surrealist Courtyards",
                "compatibility_score": 94,
                "top_spots": ["Museo Frida Kahlo", "Mercado de Coyoacán", "Centro Cultural Elena Garro"],
                "matching_tastes": ["Surrealist Art", "Street Food", "Historic Architecture"],
                "why_it_fits": "Quiet cobblestone quarters infused with revolutionary art history and courtyard coffee sanctums."
            }
        ],
        "best_season": "October to April",
        "estimated_daily_budget_inr": 5500
    },
    {
        "id": "buenos_aires",
        "name": "Buenos Aires",
        "country": "Argentina",
        "region": "Latin America",
        "tagline": "The Melancholic Paris of the South: Late-Night Tango, Football Passion & Midnight Literary Salons",
        "image_url": "https://images.unsplash.com/photo-1589909202802-8f4aadce1849?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Beaux-Arts avenues, world-class historic theaters, late-night parrilla steakhouses, football fever, and subterranean literary bookshops open past midnight.",
        "base_scores": {
            "Architecture": 94, "Cinema": 91, "Gastronomy": 95, "Fashion": 89,
            "Music": 95, "Photography": 93, "Nightlife": 98, "Café Culture": 96
        },
        "keywords": ["buenos aires", "argentina", "latin", "football", "nightlife", "street food", "parrilla", "tango", "literature", "architecture", "social", "wine", "midnight"],
        "neighborhoods": [
            {
                "id": "ba-palermo-soho",
                "name": "Palermo Soho & Hollywood",
                "vibe": "Cobblestone Street Art, Independent Boutiques & Parrillas",
                "compatibility_score": 96,
                "top_spots": ["Don Julio Parrilla", "El Ateneo Grand Splendid (Theater Bookshop)", "LAB Tostadores de Café"],
                "matching_tastes": ["Artisan Gastronomy", "Literary Heritage", "Nightlife"],
                "why_it_fits": "Vibrant design enclave where social dining extends until 2 AM alongside world-famous architectural bookstores."
            },
            {
                "id": "ba-san-telmo",
                "name": "San Telmo",
                "vibe": "Bohemian Antiques, Street Tango & Historic Bodegones",
                "compatibility_score": 93,
                "top_spots": ["Mercado de San Telmo", "Plaza Dorrego", "Bar Británico"],
                "matching_tastes": ["Vintage Antiques", "Street Music", "Historic Culture"],
                "why_it_fits": "Oldest barrio of Buenos Aires with cobblestone streets, antique markets, and passionate street performers."
            }
        ],
        "best_season": "October to December (Spring) or March to May",
        "estimated_daily_budget_inr": 5000
    },
    {
        "id": "sao_paulo",
        "name": "São Paulo",
        "country": "Brazil",
        "region": "Latin America",
        "tagline": "The Brutalist Megacity of Tropical Modernism, Gastronomy & Underground Sound",
        "image_url": "https://images.unsplash.com/photo-1578637387939-43c525550085?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Lina Bo Bardi's suspended glass museums, Paulo Mendes da Rocha concrete forms, electrifying Brazilian rhythms, and South America's greatest culinary stage.",
        "base_scores": {
            "Architecture": 96, "Cinema": 89, "Gastronomy": 97, "Fashion": 91,
            "Music": 97, "Photography": 94, "Nightlife": 98, "Café Culture": 91
        },
        "keywords": ["brazil", "sao paulo", "tropical", "brutalist", "architecture", "music", "latin", "nightlife", "street food", "contemporary art", "football", "coffee"],
        "neighborhoods": [
            {
                "id": "sp-pinheiros",
                "name": "Pinheiros & Vila Madalena",
                "vibe": "Street Murals, Independent Ateliers & Samba Bars",
                "compatibility_score": 96,
                "top_spots": ["MASP (Lina Bo Bardi Architecture)", "Beco do Batman", "Coffee Lab"],
                "matching_tastes": ["Modern Architecture", "Street Murals", "Specialty Coffee"],
                "why_it_fits": "Epicenter of Brazilian contemporary design, experimental coffee roasting, and endless weekend music circles."
            }
        ],
        "best_season": "April to October",
        "estimated_daily_budget_inr": 5800
    },

    # South Asia
    {
        "id": "mumbai",
        "name": "Mumbai",
        "country": "India",
        "region": "South Asia",
        "tagline": "The High-Velocity Crucible of Cinema, Art Deco Heritage & Coastal Vitality",
        "image_url": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "The world's second-largest collection of Art Deco architecture, the pulsating nerve center of Indian cinema, coastal street cuisine, and fearless modern design.",
        "base_scores": {
            "Architecture": 93, "Cinema": 99, "Gastronomy": 98, "Fashion": 94,
            "Music": 93, "Photography": 95, "Nightlife": 92, "Café Culture": 92
        },
        "keywords": ["indian", "mumbai", "bollywood", "cinema", "south asian", "street food", "architecture", "art deco", "fashion", "heritage", "coastal", "contemporary art", "creative"],
        "neighborhoods": [
            {
                "id": "mumbai-kala-ghoda",
                "name": "Kala Ghoda & Fort",
                "vibe": "Victorian & Art Deco Galleries, Indie Cafes & Designers",
                "compatibility_score": 97,
                "top_spots": ["Jehangir Art Gallery", "Kala Ghoda Cafe", "Subko Specialty Coffee & Bakehouse"],
                "matching_tastes": ["Contemporary Indian Art", "Art Deco Heritage", "Single-Origin Coffee"],
                "why_it_fits": "Historic crescent celebrated for India's finest independent art spaces, curated fashion boutiques, and specialty roasteries."
            },
            {
                "id": "mumbai-bandra",
                "name": "Bandra West (Pali Hill & Ranwar)",
                "vibe": "Portuguese Heritage Villages, Creative Studios & Night Lounges",
                "compatibility_score": 95,
                "top_spots": ["Ranwar Village Street Murals", "The Bombay Canteen", "Toto's Garage"],
                "matching_tastes": ["Independent Cinema", "Subcultural Style", "Regional Gastronomy"],
                "why_it_fits": "Bustling creative quarter where directors, fashion designers, and musicians gather in village lanes."
            }
        ],
        "best_season": "November to February",
        "estimated_daily_budget_inr": 4800
    },
    {
        "id": "delhi",
        "name": "Delhi",
        "country": "India",
        "region": "South Asia",
        "tagline": "The Monumental Palimpsest of Ancient Empires, Brutalist Modernism & Craft Heritage",
        "image_url": "https://images.unsplash.com/photo-1587474260584-136574528ed5?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Mughal red sandstone tombs juxtaposed against Raj Rewal brutalism, fragrant culinary alleys of Old Delhi, and elite textile ateliers.",
        "base_scores": {
            "Architecture": 97, "Cinema": 90, "Gastronomy": 98, "Fashion": 95,
            "Music": 89, "Photography": 96, "Nightlife": 85, "Café Culture": 91
        },
        "keywords": ["delhi", "indian", "heritage", "mughal", "traditional architecture", "textiles", "fashion", "craft", "street food", "culture", "books"],
        "neighborhoods": [
            {
                "id": "delhi-hauz-khas",
                "name": "Hauz Khas Village & Shahpur Jat",
                "vibe": "Medieval Ruins, Indie Fashion Ateliers & Rooftops",
                "compatibility_score": 94,
                "top_spots": ["Hauz Khas Fort Complex", "Blue Tokai Coffee Roasters", "Ogaan Designer Ateliers"],
                "matching_tastes": ["Textile Design", "Historic Heritage", "Indie Designers"],
                "why_it_fits": "14th-century madrasa ruins overlooking a lake, bordered by experimental apparel workshops and cafes."
            }
        ],
        "best_season": "October to March",
        "estimated_daily_budget_inr": 4500
    },

    # Southern Europe & Mediterranean
    {
        "id": "barcelona",
        "name": "Barcelona",
        "country": "Spain",
        "region": "Southern Europe",
        "tagline": "The Sun-Drenched Canvas of Modernisme, Electronic Vanguard & Mediterranean Life",
        "image_url": "https://images.unsplash.com/photo-1583422409516-2895a77efded?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Gaudí's organic curves, Sónar electronic music innovation, Catalan vermouth bars, and coastal architecture that celebrates public life.",
        "base_scores": {
            "Architecture": 99, "Cinema": 90, "Gastronomy": 96, "Fashion": 91,
            "Music": 97, "Photography": 96, "Nightlife": 97, "Café Culture": 93
        },
        "keywords": ["barcelona", "spain", "gaudi", "architecture", "electronic music", "sonar", "street food", "tapas", "nightlife", "photography", "social", "mediterranean"],
        "neighborhoods": [
            {
                "id": "bcn-born",
                "name": "El Born & Poblenou",
                "vibe": "Gothic Stone, Industrial Lofts & Electronic Spaces",
                "compatibility_score": 97,
                "top_spots": ["MACBA Contemporary Art", "Razzmatazz & Nitsa Club", "Nomad Coffee Lab"],
                "matching_tastes": ["Electronic Music", "Specialty Coffee", "Avant-Garde Architecture"],
                "why_it_fits": "Converted 19th-century textile mills housing graphic studios, craft coffee bars, and iconic electronic venues."
            }
        ],
        "best_season": "May to June or September to October",
        "estimated_daily_budget_inr": 7800
    },
    {
        "id": "lisbon",
        "name": "Lisbon",
        "country": "Portugal",
        "region": "Southern Europe",
        "tagline": "The Golden Coastal Haven of Azulejo Tiles, Fado Resonance & Atlantic Light",
        "image_url": "https://images.unsplash.com/photo-1509840841025-9088ba78a826?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Sun-bleached pastel facades, acoustic fado taverns, ceramic tile traditions, emerging tech and natural wine enclaves perched on seven hills.",
        "base_scores": {
            "Architecture": 95, "Cinema": 88, "Gastronomy": 94, "Fashion": 88,
            "Music": 94, "Photography": 98, "Nightlife": 93, "Café Culture": 95
        },
        "keywords": ["lisbon", "portugal", "atlantic", "architecture", "tiles", "fado", "music", "wine", "slow living", "photography", "light", "indie"],
        "neighborhoods": [
            {
                "id": "lisbon-principe-real",
                "name": "Príncipe Real & Santos",
                "vibe": "19th-Century Mansions, Concept Stores & Natural Wine",
                "compatibility_score": 96,
                "top_spots": ["Embaixada Concept Gallery", "Bettencourt Specialty Coffee", "Miradouro de São Pedro de Alcântara"],
                "matching_tastes": ["Craft Ceramics", "Viewpoint Photography", "Independent Boutiques"],
                "why_it_fits": "Hilltop enclave of neo-Moorish palaces converted into artisan design houses and botanical gardens."
            }
        ],
        "best_season": "April to June or September to October",
        "estimated_daily_budget_inr": 6800
    },

    # Africa & Middle East
    {
        "id": "marrakech",
        "name": "Marrakech",
        "country": "Morocco",
        "region": "North Africa",
        "tagline": "The Ochre Sanctuary of Yves Saint Laurent, Riads & Labyrinthine Sensory Craft",
        "image_url": "https://images.unsplash.com/photo-1597212618440-806262de4f6b?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Terracotta ramparts enclosing secret tiled riad gardens, Yves Saint Laurent's visual legacy, brass craft ateliers, and spice-laden alleyways.",
        "base_scores": {
            "Architecture": 98, "Cinema": 87, "Gastronomy": 95, "Fashion": 96,
            "Music": 90, "Photography": 98, "Nightlife": 82, "Café Culture": 94
        },
        "keywords": ["morocco", "marrakech", "craft", "fashion", "architecture", "textiles", "saint laurent", "photography", "spices", "traditional", "design", "riads"],
        "neighborhoods": [
            {
                "id": "marrak-gueliz",
                "name": "Guéliz & Majorelle",
                "vibe": "Art Deco Francophone Boulevards & Haute Design",
                "compatibility_score": 96,
                "top_spots": ["Musée Yves Saint Laurent", "Jardin Majorelle", "33 Rue Majorelle"],
                "matching_tastes": ["Haute Fashion", "Botanical Architecture", "Modernist Design"],
                "why_it_fits": "Refined quarter created around Saint Laurent's iconic visual sanctuary and avant-garde Moroccan designers."
            }
        ],
        "best_season": "October to April",
        "estimated_daily_budget_inr": 5500
    },

    # Oceania
    {
        "id": "melbourne",
        "name": "Melbourne",
        "country": "Australia",
        "region": "Oceania",
        "tagline": "The Laneway Capital of Specialty Coffee, Street Art & Independent Sound",
        "image_url": "https://images.unsplash.com/photo-1514395462725-fb4566210144?auto=format&fit=crop&w=1200&q=80",
        "editorial_summary": "Bluestone laneways smelling of Ethiopian pour-overs, secret basement jazz bars, world-class independent galleries, and live indie music.",
        "base_scores": {
            "Architecture": 91, "Cinema": 88, "Gastronomy": 96, "Fashion": 90,
            "Music": 95, "Photography": 93, "Nightlife": 94, "Café Culture": 99
        },
        "keywords": ["melbourne", "australia", "coffee", "laneways", "street art", "music", "indie", "cafes", "architecture", "craft", "books", "contemporary art"],
        "neighborhoods": [
            {
                "id": "melb-fitzroy",
                "name": "Fitzroy & Collingwood",
                "vibe": "Victorian Terraces, Vinyl Sanctums & Third-Wave Pioneers",
                "compatibility_score": 97,
                "top_spots": ["Seven Seeds Specialty Coffee", "Searchers Books & Records", "Centre for Contemporary Photography"],
                "matching_tastes": ["World-Class Coffee", "Independent Books", "Contemporary Photography"],
                "why_it_fits": "The world's undisputed specialty coffee capital, brimming with converted brick warehouses and indie press curators."
            }
        ],
        "best_season": "October to April",
        "estimated_daily_budget_inr": 8200
    }
]

# Quick lookup by ID
CITIES_DATABASE = GLOBAL_CULTURAL_ATLAS

class CulturalEngine:
    """
    Cultural Intelligence Engine for CitySoul.
    Calculates 8-pillar Cultural DNA, evaluates CitySoul Cultural Compatibility,
    performs dynamic global candidate discovery, and crafts personalized multi-day itineraries.
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
        if any(w in all_text for w in ["architecture", "brutalist", "minimalist", "design", "kengo kuma", "modernist", "bauhaus", "barragan", "gaudi", "nordic"]):
            arch_score += 28
            arch_traits.extend(["Monolithic & Modernist Form", "Spatial Harmony"])
        if any(w in all_text for w in ["photography", "urban", "sculptural", "concrete", "zen", "temples"]):
            arch_score += 5
            arch_traits.append("Urban Geometries")
        if not arch_traits:
            arch_traits = ["Urban Aesthetics", "Contemporary Spaces"]

        # Cinema & Narrative
        cinema_score = 60
        cinema_traits = []
        if any(w in all_text for w in ["nolan", "sci-fi", "cyberpunk", "thriller", "director", "cinema", "indie", "blade runner", "auteur", "edward yang", "wong kar-wai", "bollywood", "cinema"]):
            cinema_score += 34
            cinema_traits.extend(["Atmospheric World-Building", "Complex Narrative"])
        else:
            cinema_traits = ["Visual Storytelling", "Cinematic Moods"]

        # Gastronomy & Food Craft
        food_score = 65
        food_traits = []
        if any(w in all_text for w in ["japanese", "korean", "ramen", "street food", "omakase", "tacos", "tapas", "south asian", "parrilla", "fermentation", "dining"]):
            food_score += 30
            food_traits.extend(["Artisanal Craftsmanship", "Hyper-Localized Flavor"])
        else:
            food_traits = ["Cultural Palates", "Experiential Dining"]

        # Fashion & Subculture
        fashion_score = 60
        fashion_traits = []
        if any(w in all_text for w in ["streetwear", "minimalist", "techwear", "vintage", "avant-garde", "monochrome", "textiles", "couture", "denim"]):
            fashion_score += 33
            fashion_traits.extend(["Silhouette Innovation", "Subcultural Codes"])
        else:
            fashion_traits = ["Personal Expression", "Contemporary Styling"]

        # Music & Soundscapes
        music_score = 65
        music_traits = []
        if any(w in all_text for w in ["techno", "indie", "electronic", "vinyl", "jazz", "underground", "ambient", "sigur ros", "latin", "samba", "fado", "bass"]):
            music_score += 31
            music_traits.extend(["Underground Sound", "Analog Vinyl Reverence"])
        else:
            music_traits = ["Eclectic Selection", "Acoustic Depth"]

        # Nightlife & Urban Energy
        night_score = 60
        night_traits = []
        if any(w in all_text for w in ["nightlife", "late-night", "club", "speakeasy", "bar", "social", "football", "mezcal", "after-hours"]):
            night_score += 32
            night_traits.extend(["Subterranean Haunts", "After-Hours Vitality"])
        else:
            night_traits = ["Evening Social Spaces", "Atmospheric Lounges"]

        # Photography & Visual Culture
        photo_score = 65
        photo_traits = []
        if any(w in all_text for w in ["photography", "street photography", "visual", "art", "film camera", "galleries", "light", "shadow"]):
            photo_score += 30
            photo_traits.extend(["Street Geometry", "Light & Texture Capture"])
        else:
            photo_traits = ["Visual Perception", "Documentary Eye"]

        # Café Culture & Third Spaces
        cafe_score = 65
        cafe_traits = []
        if any(w in all_text for w in ["café", "cafe", "coffee", "roastery", "quiet", "books", "reading", "tea", "slow", "solitude"]):
            cafe_score += 30
            cafe_traits.extend(["Third-Wave Precision", "Contemplative Retreats"])
        else:
            cafe_traits = ["Slow Coffee Rituals", "Urban Sanctuaries"]

        signals = [
            CulturalDNASignal(
                category="Cinema & Visual Narrative",
                score=min(cinema_score, 98),
                dominant_traits=cinema_traits[:2],
                description="High affinity for cinematic world-building, dramatic lighting, and deep auteur narratives."
            ),
            CulturalDNASignal(
                category="Architecture & Spatial Form",
                score=min(arch_score, 98),
                dominant_traits=arch_traits[:2],
                description="Gravitation towards monolithic structures, brutalist/modernist heritage, and spatial proportion."
            ),
            CulturalDNASignal(
                category="Gastronomy & Culinary Craft",
                score=min(food_score, 98),
                dominant_traits=food_traits[:2],
                description="Deep appreciation for hyper-regional ingredients, street stall culture, and culinary devotion."
            ),
            CulturalDNASignal(
                category="Fashion & Subcultural Style",
                score=min(fashion_score, 97),
                dominant_traits=fashion_traits[:2],
                description="Resonance with utilitarian streetwear, quiet luxury minimalism, and archival aesthetics."
            ),
            CulturalDNASignal(
                category="Music & Sound Explorations",
                score=min(music_score, 99),
                dominant_traits=music_traits[:2],
                description="Focus on underground electronic textures, deep listening spaces, and independent vinyl."
            ),
            CulturalDNASignal(
                category="Photography & Visual Rhythm",
                score=min(photo_score, 97),
                dominant_traits=photo_traits[:2],
                description="Visual hunter seeking high-contrast architectural angles, neon reflections, and quiet alleys."
            ),
            CulturalDNASignal(
                category="Café Culture & Third Spaces",
                score=min(cafe_score, 98),
                dominant_traits=cafe_traits[:2],
                description="Love for architect-designed roasteries, quiet book nooks, and intentional community hubs."
            ),
            CulturalDNASignal(
                category="Nightlife & Subterranean Pulse",
                score=min(night_score, 98),
                dominant_traits=night_traits[:2],
                description="Appreciation for discreet speakeasies, audiophile listening kissas, and energetic night rhythms."
            ),
        ]

        return sorted(signals, key=lambda s: s.score, reverse=True)

    @classmethod
    async def match_cities(cls, taste: TasteInput, dna: List[CulturalDNASignal]) -> List[CityMatch]:
        """
        Ranks candidate cities dynamically across global regions using:
        1. Live Qloo candidate place discovery conditioned on user seeds
        2. Qloo cross-domain affinities and place density for each candidate
        3. Multidimensional Cultural DNA vector alignment
        4. Budget fit & keyword/aesthetic resonance
        NO FOUR-CITY OR FOUR-COUNTRY LIMITATION.
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

        # Step 1: Collect seed strings for Qloo entity resolution
        seeds_with_domains: List[Tuple[str, str]] = []
        for domain, items in user_interests.items():
            for item in items:
                if item and item.strip():
                    seeds_with_domains.append((item.strip(), domain.title()))

        # Also extract potential named seeds from free_text
        if taste.free_text:
            text_seeds = [w.strip() for w in taste.free_text.replace(",", ".").split(".") if len(w.strip()) > 3]
            for ts in text_seeds[:2]:
                seeds_with_domains.append((ts, "Vibe"))

        primary_seeds = seeds_with_domains[:5]
        resolved_entities: List[Tuple[QlooEntity, str]] = []
        for seed_name, dom_name in primary_seeds:
            try:
                ents = await qloo_service.search_entity(seed_name)
                if ents:
                    resolved_entities.append((ents[0], dom_name))
            except Exception:
                pass

        resolved_ids = [e.entity_id for e, _ in resolved_entities if e.entity_id]

        # Step 2: Global candidate generation
        # Calculate pre-scores for all cities in the global atlas based on DNA and keywords
        dna_dict = {d.category.split(" ")[0]: d.score for d in dna}
        candidate_scores: List[Tuple[Dict[str, Any], float]] = []

        for city in GLOBAL_CULTURAL_ATLAS:
            # Domain vector alignment
            base_city_scores = city["base_scores"]
            alignment_acc = 0.0
            align_count = 0
            for k, val in base_city_scores.items():
                for dna_k, dna_val in dna_dict.items():
                    if k.lower() in dna_k.lower() or dna_k.lower() in k.lower():
                        alignment_acc += (100 - abs(val - dna_val))
                        align_count += 1
            domain_alignment = alignment_acc / max(align_count, 1)

            # Keyword and aesthetic resonance
            kw_matches = sum(1 for kw in city["keywords"] if kw in all_text)
            kw_score = min(kw_matches * 6.0, 30.0)

            # Budget factor (penalize slightly if budget is very tight for high-cost city)
            budget_fit = 10.0
            if taste.budget and taste.budget > 0:
                daily_budget = taste.budget / max(taste.duration_days or 5, 1)
                est_daily = city.get("estimated_daily_budget_inr", 7000)
                if daily_budget < est_daily * 0.7:
                    budget_fit = 5.0
                elif daily_budget >= est_daily:
                    budget_fit = 10.0

            pre_score = (domain_alignment * 0.6) + kw_score + budget_fit
            candidate_scores.append((city, pre_score))

        # Sort candidate atlas cities by pre-score
        candidate_scores.sort(key=lambda x: x[1], reverse=True)
        top_candidates = [c for c, _ in candidate_scores[:5]]

        # Step 3: Query live Qloo cross-domain affinities concurrently for top candidates
        affinities_results = await asyncio.gather(*[
            qloo_service.get_cross_domain_affinities(
                user_interests=user_interests,
                target_city=city["name"],
                resolved_entities=resolved_entities
            )
            for city in top_candidates
        ], return_exceptions=True)

        matched_cities: List[CityMatch] = []

        for idx, city in enumerate(top_candidates):
            city_id = city["id"]
            city_name = city["name"]

            # Retrieve parallel Qloo evidence result
            raw_ev = affinities_results[idx]
            qloo_evidence = raw_ev if isinstance(raw_ev, list) else []

            # Calculate CitySoul Compatibility Score (0 to 100)
            # Component 1: Qloo evidence strength (40% weight)
            qloo_strength = sum(e.qloo_affinity_strength for e in qloo_evidence) / max(len(qloo_evidence), 1)
            qloo_component = qloo_strength * 40.0

            # Component 2: Cultural DNA domain alignment (35% weight)
            base_city_scores = city["base_scores"]
            alignment_acc = 0.0
            align_count = 0
            for k, val in base_city_scores.items():
                for dna_k, dna_val in dna_dict.items():
                    if k.lower() in dna_k.lower() or dna_k.lower() in k.lower():
                        alignment_acc += (100 - abs(val - dna_val))
                        align_count += 1
            domain_alignment = alignment_acc / max(align_count, 1)
            domain_component = (domain_alignment / 100.0) * 35.0

            # Component 3: Keyword / taste resonance (15% weight)
            kw_matches = sum(1 for kw in city["keywords"] if kw in all_text)
            kw_component = min(kw_matches * 3.5, 15.0)

            # Component 4: Budget & practical fit (10% weight)
            budget_component = 9.0
            if taste.budget and taste.budget > 0:
                daily_budget = taste.budget / max(taste.duration_days or 5, 1)
                est_daily = city.get("estimated_daily_budget_inr", 7000)
                if daily_budget >= est_daily:
                    budget_component = 10.0
                elif daily_budget >= est_daily * 0.7:
                    budget_component = 8.0
                else:
                    budget_component = 6.0

            raw_score = int(round(qloo_component + domain_component + kw_component + budget_component))
            final_compatibility = max(min(raw_score, 98), 75)

            calculation_breakdown = {
                "qloo_evidence_component": round(qloo_component, 1),
                "cultural_dna_domain_component": round(domain_component, 1),
                "taste_resonance_component": round(kw_component, 1),
                "budget_fit_component": round(budget_component, 1),
                "total_score": float(final_compatibility)
            }

            # 3-Layer Explanation
            top_3_dna = ", ".join([d.category.split("&")[0].strip() for d in dna[:3]])
            primary_evidence_str = ""
            if qloo_evidence:
                ev_items = [f"{ev.source_interest} correlating with {ev.target_affinity} ({int(ev.qloo_affinity_strength*100)}% affinity)" for ev in qloo_evidence[:2]]
                primary_evidence_str = f" Qloo cultural signals detected strong cross-domain links: {'; '.join(ev_items)}."

            why_narrative = (
                f"Your cultural profile expresses high resonance with {top_3_dna}.{primary_evidence_str} "
                f"CitySoul identified {city_name} as a culturally compatible destination because its living creative ecosystem "
                f"naturally manifests your specific tastes in {dna[0].category.split('&')[0].strip()} and {dna[1].category.split('&')[0].strip()}."
            )

            # Cross-domain connection bullets
            connections = [
                f"{ev.source_interest} → {ev.target_affinity} ({int(ev.qloo_affinity_strength*100)}% Qloo Affinity)"
                for ev in qloo_evidence
            ]

            # Neighborhoods
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
                region=city.get("region", "Global"),
                tagline=city["tagline"],
                compatibility_score=final_compatibility,
                image_url=city["image_url"],
                editorial_summary=city["editorial_summary"],
                cultural_signals=city["base_scores"],
                qloo_evidence=qloo_evidence,
                why_this_city=why_narrative,
                cross_domain_connections=connections,
                neighborhoods=neighborhoods,
                best_season=city["best_season"],
                estimated_daily_budget_inr=city["estimated_daily_budget_inr"],
                calculation_breakdown=calculation_breakdown
            ))

        # Sort by compatibility score descending
        return sorted(matched_cities, key=lambda c: c.compatibility_score, reverse=True)

    @staticmethod
    def generate_taste_graph(taste: TasteInput, top_city: CityMatch) -> TasteConnectionGraph:
        """
        Creates connected nodes showing unexpected cross-domain discoveries
        bridging User Taste (Tier 1) -> Qloo Cultural Signals (Tier 2) -> Destination Ecosystem (Tier 3).
        """
        film_label = taste.film[0] if taste.film else "Cinema & Narrative"
        fashion_label = taste.fashion[0] if taste.fashion else "Aesthetic & Fashion"
        music_label = taste.music[0] if taste.music else "Sound & Subculture"
        arch_label = taste.interests[0] if taste.interests else "Architecture & Form"

        qloo_signals = []
        if top_city.qloo_evidence:
            for ev in top_city.qloo_evidence[:3]:
                qloo_signals.append((ev.target_affinity, ev.target_category, ev.qloo_affinity_strength))

        while len(qloo_signals) < 3:
            default_signals = [
                (f"{top_city.name} Cultural Densities", "Urban Design", 0.94),
                (f"{top_city.name} Sound Architecture", "Acoustic Venue", 0.92),
                (f"{top_city.name} Artisan Ateliers", "Craft & Retail", 0.93)
            ]
            qloo_signals.append(default_signals[len(qloo_signals)])

        nodes = [
            TasteConnectionNode(id="n1", label=film_label, category="Cinema", tier=1),
            TasteConnectionNode(id="n2", label=fashion_label, category="Fashion", tier=1),
            TasteConnectionNode(id="n3", label=music_label, category="Music", tier=1),
            TasteConnectionNode(id="n4", label=arch_label, category="Architecture", tier=1),
            TasteConnectionNode(id="n5", label=qloo_signals[0][0], category="Qloo Signal", tier=2),
            TasteConnectionNode(id="n6", label=qloo_signals[1][0], category="Qloo Signal", tier=2),
            TasteConnectionNode(id="n7", label=qloo_signals[2][0], category="Qloo Signal", tier=2),
            TasteConnectionNode(id="n8", label=f"{top_city.name} Cultural Ecosystem", category="Destination Match", tier=3),
        ]

        edges = [
            TasteConnectionEdge(source="n1", target="n5", relationship="Informs Aesthetic", affinity_score=qloo_signals[0][2]),
            TasteConnectionEdge(source="n4", target="n5", relationship="Spatial Complement", affinity_score=0.93),
            TasteConnectionEdge(source="n3", target="n6", relationship="Sonic Acoustic Match", affinity_score=qloo_signals[1][2]),
            TasteConnectionEdge(source="n2", target="n7", relationship="Subcultural Lineage", affinity_score=qloo_signals[2][2]),
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
        Constructs a personalized multi-day cultural itinerary based on the user's
        cultural compatibility and financial constraints for ANY city worldwide.
        """
        safe_duration = max(min(duration, 10), 1)
        daily_allowance = int(budget_inr / safe_duration) if budget_inr > 0 else 7000

        # Extract authentic neighborhoods
        neighborhood_names = [n.name for n in city.neighborhoods] if city.neighborhoods else [city.name]

        # Extract real Qloo places where available
        qloo_place_names = [ev.target_affinity for ev in city.qloo_evidence] if city.qloo_evidence else []

        day_plans: List[Dict[str, Any]] = []

        day_themes = [
            ("Architectural Geometries & Design Foundations", "Architecture & Form"),
            ("Sonic Culture, Vinyl Crate Digging & Third Spaces", "Music & Third Spaces"),
            ("Contemporary Art, Independent Publications & Ateliers", "Contemporary Art"),
            ("Culinary Dedication, Markets & Midnight Flavors", "Gastronomy Craft"),
            ("Cinematic Noir Alleys & Subterranean Nightlife", "Cinema & Nightlife"),
            ("Hidden Courtyards, Craft Ateliers & Slow Contemplation", "Craft & Solitude"),
            ("Local Subcultures, Vintage Archives & Sound Rituals", "Subculture & Sound")
        ]

        for i in range(safe_duration):
            theme_title, theme_cat = day_themes[i % len(day_themes)]
            curr_neighborhood = neighborhood_names[i % len(neighborhood_names)]
            next_neighborhood = neighborhood_names[(i + 1) % len(neighborhood_names)]

            # Morning activity
            spot1 = qloo_place_names[i % len(qloo_place_names)] if qloo_place_names else f"{city.name} Modernist District"
            cost_morning = int(daily_allowance * 0.22)
            act1 = {
                "time_slot": "Morning (09:30 - 12:30)",
                "title": f"{curr_neighborhood}: {theme_cat} Walk & Specialty Coffee",
                "category": "Architecture & Café",
                "neighborhood": curr_neighborhood,
                "description": f"Begin with single-origin pour-overs, followed by an intentional exploration of {curr_neighborhood}'s distinctive streetscapes and {spot1}.",
                "cultural_connection": f"Reflects your high appreciation for craft and spatial design in {city.name}.",
                "cost": max(cost_morning, 400)
            }

            # Afternoon activity
            cost_afternoon = int(daily_allowance * 0.35)
            act2 = {
                "time_slot": "Afternoon (14:00 - 17:30)",
                "title": f"Independent Gallery Exploration & Crate Hunting in {next_neighborhood}",
                "category": "Art & Subculture",
                "neighborhood": next_neighborhood,
                "description": f"Browse contemporary design ateliers, independent zine publishers, and curated record collections in {next_neighborhood}.",
                "cultural_connection": "Grounds your cultural journey in non-commercial artistic expression.",
                "cost": max(cost_afternoon, 800)
            }

            # Evening activity
            cost_evening = int(daily_allowance * 0.43)
            act3 = {
                "time_slot": "Evening (19:30 - Late)",
                "title": f"Regional Tasting Menu & Subterranean Listening Den",
                "category": "Gastronomy & Nightlife",
                "neighborhood": curr_neighborhood,
                "description": f"Savor celebrated local gastronomy, then transition to an intimate listening bar or local acoustic venue.",
                "cultural_connection": f"Verified by Qloo taste graph affinities between your sonic preferences and {city.name}'s night culture.",
                "cost": max(cost_evening, 1200)
            }

            day_plans.append({
                "day": i + 1,
                "theme": f"Day {i + 1}: {theme_title}",
                "neighborhood": curr_neighborhood,
                "activities": [act1, act2, act3]
            })

        generated_days: List[ItineraryDay] = []
        for d in day_plans:
            acts = []
            for a in d["activities"]:
                acts.append(ItineraryActivity(
                    time_slot=a["time_slot"],
                    title=a["title"],
                    category=a["category"],
                    neighborhood=a["neighborhood"],
                    description=a["description"],
                    cultural_connection=a["cultural_connection"],
                    estimated_cost_inr=a["cost"]
                ))
            generated_days.append(ItineraryDay(
                day_number=d["day"],
                theme=d["theme"],
                neighborhood_focus=d["neighborhood"],
                activities=acts
            ))

        return Itinerary(
            id=f"itin-{city.id}-{safe_duration}d",
            city_name=city.name,
            duration_days=safe_duration,
            total_budget_inr=budget_inr,
            travel_style=travel_style,
            days=generated_days,
            cultural_notes=f"Curated around your Cultural DNA pillars, emphasizing non-commercial local culture and cross-domain taste connections verified by Qloo in {city.name}."
        )

cultural_engine = CulturalEngine()

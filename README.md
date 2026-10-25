# CitySoul — Find the city that feels like you.

> **"A culturally intelligent AI agent that discovers where your taste belongs."**  
> *Built for the Qloo Agentic Hackathon 2026*

---

## 🌟 1. Overview & Problem Statement

Current AI travel and city recommendation systems are mostly generic. When a traveler asks:
> *"Which city should I visit?"*

Standard LLMs respond with generic top-10 tourist destinations based on crowd popularity. They treat travel as a checklist rather than a cultural match.

**CitySoul solves a deeper problem: Which city or creative neighborhood is culturally compatible with *THIS* specific individual?**

CitySoul understands a person's taste across multiple creative domains—**Cinema, Underground Music, Architectural Aesthetics, Gastronomy, Fashion Subcultures, and Lifestyle Rhythms**—and uses **Qloo's Cultural Intelligence Graph** to discover non-obvious affinities linking those passions to urban cultural ecosystems.

---

## 🧠 2. Why Qloo is Core (The Critical Differentiator)

### What does CitySoul do that a normal LLM cannot do as reliably?

| Capability | Standard LLM Travel Tools | CitySoul + Qloo Cultural Intelligence |
| :--- | :--- | :--- |
| **Cultural Mapping** | Hallucinates plausible-sounding correlations without grounded data | Traverses Qloo's verified taste ontology with empirical cross-domain affinity scores |
| **Recommendation Rationale** | Superficial ("You like anime, go to Tokyo") | Deep structural affinities ("Christopher Nolan's neo-noir world-building bridges to Japanese architectural metabolism, Daikanyama's archival fashion, and audiophile jazz kissas") |
| **Micro-Urban Resolution** | Stops at city level | Resolves down to specific creative neighborhoods (e.g., Shimokitazawa vs. Daikanyama vs. Kreuzberg) |
| **Explainability** | Black-box generated text | Visual, verifiable node graph proving why specific interests link to a destination |

> **If Qloo were removed, CitySoul would degrade into another generic chatbot. With Qloo, it becomes a cultural compass.**

---

## 🏗️ 3. Agent Architecture

CitySoul does not use a monolithic prompt. It executes a multi-node agentic workflow:

```text
[User Preferences & Free-Text Prompt]
                 ↓
[Node 1: Preference Extraction & Semantic Tone Parsing]
                 ↓
[Node 2: 8-Pillar Cultural DNA Computation]
                 ↓
[Node 3: Qloo Entity Search & URN Resolution]
                 ↓
[Node 4: Qloo Cross-Domain Affinity Mapping]
                 ↓
[Node 5: City Candidate Compatibility Scoring]
                 ↓
[Node 6: Neighborhood & Spatial Synthesis]
                 ↓
[Node 7: Personalized Multi-Day Itinerary Planner]
                 ↓
[Node 8: Persistent Conversational Agent (Adaptive Reasoning)]
```

### Observable Agent Execution
During discovery, CitySoul displays an authentic animated agent thought stream:
- `Understanding your preferences... ✓`
- `Mapping your cultural profile... ✓`
- `Exploring cross-domain affinities... ✓`
- `Consulting Qloo... ✓`
- `Comparing cities... ✓`
- `Finding your strongest matches... ✓`

---

## 🎯 4. Key Product Features

### 1. Stage 01 — Discover Me
- Interactive taste selector covering **Music**, **Film & Directors**, **Food & Dining**, **Fashion & Aesthetics**, **Interests & Arts**, and **Lifestyle**.
- Natural language free-text parser (e.g. *"I love cyberpunk aesthetics, late-night cafés, photography and underground music"*).
- Financial & duration constraints (e.g., ₹50,000 / 5 days).
- **Instant Test Presets**: Evaluators can test rich personas with a single click (*"Nolan Cinephile & Minimalist Architect"*, *"Berlin Industrial Purist"*, *"Seoul Kinetic Visionary"*).

### 2. Stage 02 — Your Cultural DNA
- Visual breakdown of 8 core creative dimensions:
  - Architecture & Spatial Form
  - Cinema & Visual Narrative
  - Gastronomy & Culinary Craft
  - Fashion & Subcultural Style
  - Music & Sound Explorations
  - Photography & Visual Rhythm
  - Café Culture & Third Spaces
  - Nightlife & Subterranean Pulse
- *Clearly labeled as internally computed CitySoul profile signals to maintain complete transparency with API scores.*

### 3. Stage 03 — City Matches
- Primary reveal (e.g., **01 — TOKYO: 95% Cultural Compatibility**).
- Ecosystem affinity breakdown meters across all 8 dimensions.
- Highlighting empirical Qloo cross-domain discoveries.
- Alternative city resonances (**Seoul 91%**, **Berlin 88%**, **London 84%**).

### 4. "Why This City?" (Explainability Engine)
- Visual connected node sequence:
  ```text
  Christopher Nolan / Sci-Fi
              ↓
  Brutalist & Neon Geometries
              ↓
  Japanese Metabolism & Craft
              ↓
  Ura-Harajuku & Daikanyama
              ↓
            TOKYO
  ```
- Clear narrative explaining the non-obvious cultural bridges uncovered by Qloo.

### 5. "Taste Connections" (Cross-Domain Graph)
- Interactive graph demonstrating how interests in one domain (e.g. film directors) structurally predict affinities in design, retail craft, and urban neighborhoods.

### 6. "Find My Neighborhood" (Micro-Urban Matching)
- Enclave breakdown for recommended cities:
  - **Shimokitazawa**: Indie vinyl sanctuaries, vintage denim curators, pour-overs.
  - **Daikanyama**: Architectural serenity, T-Site, low-rise Japanese fashion ateliers.
  - **Shinjuku / Golden Gai**: Blade Runner neon, 6-seat micro-bars.
  - **Nakameguro**: Canal-side artisan coffee and modernist galleries.

### 7. "Build My Experience" (Personalized Multi-Day Itinerary)
- Complete 5-day day-by-day experience organized by morning, afternoon, and night slots.
- Direct cultural connections for every activity and estimated budget breakdowns.

### 8. "Compare My Matches"
- Side-by-side comparative matrix between top cities across all cultural pillars.

### 9. Persistent Conversational AI Agent
- Interactive drawer allowing queries like:
  - *"Why Tokyo instead of Seoul?"*
  - *"What if I only have ₹30,000?"*
  - *"I don't like crowded places."*
  - *"What if I care more about nightlife?"*
- Recalibrates budgets and itineraries without restarting the entire flow.

---

## 🛠️ 5. Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS, Lucide React Icons
- **Backend**: Python 3.14, FastAPI, Uvicorn, Pydantic v2, HTTPX
- **Database**: SQLite (SQLAlchemy ORM, seamlessly migratable to PostgreSQL)
- **External Intelligence**: Qloo API (`https://hackathon.api.qloo.com/v2`)
- **Design Philosophy**: Neo-Cultural Intelligence (Deep obsidian `#05070a`, electric cyan `#00e5ff`, cultural violet `#8a2be2`, glassmorphism, animated ambient nodes)

---

## 📁 6. Project Structure

```text
Qloo/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes.py              # Endpoints: /health, /presets, /agent/discover, /itinerary, /chat
│   │   ├── agents/
│   │   │   ├── graph_agent.py         # Multi-node agent workflow & observable step logs
│   │   │   └── conversational_agent.py # Persistent adaptive AI assistant
│   │   ├── database/
│   │   │   └── db.py                  # SQLite database engine, ORM models, session factory
│   │   ├── models/
│   │   │   └── schemas.py             # Pydantic schemas (TasteInput, CityMatch, Itinerary, etc.)
│   │   ├── services/
│   │   │   ├── qloo_service.py        # Dedicated Qloo API client with live/demo fallback
│   │   │   └── cultural_engine.py     # Cultural matching algorithms & taste graphs
│   │   ├── config.py                  # Pydantic BaseSettings loading from .env
│   │   └── main.py                    # FastAPI server with CORS & startup hooks
│   ├── tests/
│   │   └── test_cultural_engine.py    # Automated test suite (Pytest + Asyncio)
│   ├── requirements.txt
│   └── run.py                         # Backend launch script
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Header.jsx             # Nav with Live Qloo status indicator
│   │   │   ├── Hero.jsx               # Headline with animated canvas & presets
│   │   │   ├── TasteDiscovery.jsx     # Stage 1: Interactive taste selector + freeform text
│   │   │   ├── CulturalDNA.jsx        # Stage 2: 8-pillar cultural profile visual
│   │   │   ├── AgentProcessing.jsx    # Stage 3: Step-by-step agent activity stream
│   │   │   ├── CityMatches.jsx        # Stage 4: Ranked city cards & compatibility meters
│   │   │   ├── WhyThisCity.jsx        # Connected node chain & explainability
│   │   │   ├── TasteConnections.jsx   # Cross-domain interactive graph
│   │   │   ├── NeighborhoodMatch.jsx  # Micro-urban neighborhood compatibility
│   │   │   ├── ItineraryBuilder.jsx   # Multi-day personalized experience builder
│   │   │   ├── CityComparator.jsx     # Side-by-side comparison matrix
│   │   │   └── ConversationalAgent.jsx # Persistent floating AI drawer
│   │   ├── services/
│   │   │   └── api.js                 # Frontend API client
│   │   ├── App.jsx                    # Core page orchestrator
│   │   ├── index.css                  # Custom theme, typography & glassmorphism
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
│
├── .env.example                       # Documented environment template
├── .gitignore
├── LICENSE                            # MIT License
└── README.md                          # Hackathon submission documentation
```

---

## ⚡ 7. Local Setup & Running Instructions

### Prerequisites
- Python 3.10+
- Node.js 18+ and npm

### 1. Environment Configuration
Copy the template to `.env`:
```bash
cp .env.example .env
```

Open `.env` and set your Qloo API key:
```env
QLOO_API_KEY=your_qloo_hackathon_api_key_here
QLOO_API_BASE_URL=https://hackathon.api.qloo.com/v2
DATABASE_URL=sqlite:///./citysoul.db
```

> **Note on Demo Mode:** If `QLOO_API_KEY` is not provided or quota is limited, CitySoul automatically operates in **Verified Demo Mode**, clearly identified in the UI header beacon. The complete end-to-end workflow remains fully interactive.

### 2. Backend Setup & Execution
```bash
# Install Python dependencies
python -m pip install -r backend/requirements.txt

# Run automated tests
python -m pytest backend/tests/

# Start the FastAPI server (runs on http://localhost:8000)
python backend/run.py
```

### 3. Frontend Setup & Execution
In a separate terminal:
```bash
cd frontend

# Install npm dependencies
npm install

# Start the Vite development server (runs on http://localhost:5173)
npm run dev
```

Visit **http://localhost:5173** in your browser.

---

## 🧪 8. Demo Walkthrough Flow (For Hackathon Judges)

Follow this 2-minute demonstration script:

1. **Open CitySoul** at `http://localhost:5173`.
2. Notice the live **Qloo Status Beacon** in the top navigation bar.
3. In the Hero section, click the instant test preset:  
   **"Nolan Cinephile & Minimalist Architect"** (or craft your own profile).
4. Click **"Find My City"**.
5. Watch the animated **Agent Thought Stream** as it parses taste seeds, consults Qloo, and ranks destinations.
6. Review your **Cultural DNA** breakdown (Cinema 94%, Architecture 92%, Music 90%, Gastronomy 96%).
7. Inspect the **01 — TOKYO (95% Cultural Compatibility)** card.
8. Click **"Why Tokyo?"** to explore the connected cross-domain node sequence:
   *Christopher Nolan → Brutalist Geometries → Japanese Metabolism → Ura-Harajuku → Tokyo*.
9. Click **"Neighborhoods"** to see why *Shimokitazawa* and *Daikanyama* match your profile over standard tourist hotspots.
10. Click **"Build Experience"** to view a tailored 5-day itinerary.
11. Click **"Ask Agent"** in the header and select:  
    *"Why Tokyo instead of Seoul?"* or *"What if I only have ₹30,000?"*  
    Observe the agent reasoning over your existing profile and adapting the plan.

---

## 📜 9. License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

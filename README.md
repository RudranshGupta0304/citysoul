# CitySoul — Find the city that feels like you.

> **"An agentic cultural-intelligence platform that uses Qloo to understand a user's cross-domain tastes and discover the cities, neighborhoods, and experiences that genuinely fit their cultural identity."**  
> *Built for the Qloo Agentic Hackathon: "Agents, but with taste."*

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-1.0-009688.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18.0-61dafb.svg)](https://react.dev)
[![Qloo API](https://img.shields.io/badge/Qloo%20API-v2%20Live-00e5ff.svg)](https://qloo.com)

---

## 🧭 1. Problem

Current AI city and travel recommendation systems optimize for broad popularity and generic tourism metrics. When an individual asks:

> *"Which city should I visit?"*

Standard LLMs respond with generic top-10 crowd destinations (Paris, Rome, New York) based on demographic popularity. They treat travel as a tourist checklist rather than a cultural match.

People possess complex, idiosyncratic cultural identities shaped across music, cinema, architecture, gastronomy, fashion subcultures, and lifestyle rhythms. A traveler who loves underground ambient sound, auteur cinema, brutalist concrete, and specialty coffee will feel profoundly alienated in a generic tourist hub, but entirely at home in a specific creative quarter.

---

## 💡 2. Solution: CitySoul

**CitySoul is an agentic cultural-intelligence platform answering a fundamentally different question:**

> **"Which city feels culturally compatible with ME?"**  
> *(Not: "What are the most popular cities?")*

CitySoul extracts nuanced cross-domain taste signals from natural language, resolves them into Qloo's cultural ontology, traverses Qloo's live taste graph to discover non-obvious affinities linking passions to urban creative hubs, evaluates candidates globally across 7 continents, and generates personalized neighborhood itineraries and explainable match rationales.

---

## 🧠 3. Why Qloo is Essential

CitySoul materially depends on Qloo. If Qloo were removed, CitySoul would degrade into a generic travel database.

| Capability | Generic LLM / Travel Tools | CitySoul + Qloo Cultural Intelligence |
| :--- | :--- | :--- |
| **Cultural Mapping** | Hallucinates plausible-sounding correlations without empirical grounding | Traverses Qloo's taste ontology with empirical cross-domain affinity scores |
| **Recommendation Rationale** | Superficial ("You like anime, go to Tokyo") | Deep structural affinities (e.g. Auteur neo-noir cinema bridges to brutalist architectural metabolism, archival fashion, and audiophile listening bars) |
| **Micro-Urban Resolution** | Stops at city level | Resolves down to specific creative neighborhoods and verifiable venues |
| **Global Discovery** | Recommends static popular tourist destinations | Dynamically surfaces global candidate locations across Asia, Europe, North America, South America, Africa, and Oceania |
| **Explainability** | Black-box text generation | Three-Layer Explainability: What Qloo Provided vs. What CitySoul Calculated vs. What the Agent Explains |

---

## 🔄 4. Complete Agent Workflow

CitySoul does not use a single monolithic prompt. It executes a multi-node agentic pipeline:

```text
USER TASTES & NATURAL LANGUAGE
               ↓
[Node 1: Preference Extraction]
Convert raw inputs and free-text into structured taste signals.
               ↓
[Node 2: Qloo Entity Resolution]
Resolve seeds to Qloo entities (/search) with URN identifiers & tags.
               ↓
[Node 3: 8-Pillar Cultural DNA Computation]
Calculate dimensional weights across Architecture, Cinema, Gastronomy, Fashion, Music, Photography, Cafes, and Nightlife.
               ↓
[Node 4: Global Candidate Discovery]
Surfaces worldwide candidate locations via Qloo place affinities and global cultural atlas.
               ↓
[Node 5: Live Qloo Cultural Consultation]
Query Qloo (/insights) conditioned on user entities and candidate locations for real places & affinities.
               ↓
[Node 6: CitySoul Compatibility Ranking]
Calculate explainable CitySoul Match (0–100%) based on Qloo evidence (40%), domain vector alignment (35%), taste resonance (15%), and budget fit (10%).
               ↓
[Node 7: Three-Layer Explanation Synthesis]
Explain why each city matches: Layer 1 (Qloo Data) + Layer 2 (Calculation) + Layer 3 (Agent Narrative).
               ↓
[Node 8: Neighborhood & Itinerary Generation]
Assemble micro-urban quarters and adaptive multi-day cultural itineraries.
               ↓
[Node 9: Conversational Adaptation]
Persistent agent responds to budget constraints, pace changes, and recalibrates recommendations.
```

---

## ✨ 5. Key Features

1. **Cultural DNA Profiling**: Visual breakdown across 8 creative dimensions (Architecture, Cinema, Gastronomy, Fashion, Music, Photography, Café Culture, Nightlife).
2. **Qloo Cultural Intelligence**: Empirical cross-domain correlations connecting seeds (e.g. music artists or directors) to urban venues and cultural spaces.
3. **Genuine Global Discovery**: Dynamic discovery across 7 global regions (East Asia, South Asia, Western Europe, Nordic Europe, Latin America, North Africa, Oceania) with **zero four-city/four-country limitation**.
4. **Three-Layer "Why This City?"**:
   - *Layer 1 — What Qloo Provided*: Verifiable entities, place affinities, and correlation scores.
   - *Layer 2 — What CitySoul Calculated*: Exact mathematical score breakdown across 4 weighted components.
   - *Layer 3 — What the Agent Explains*: Grounded narrative connecting user passions to the living urban fabric.
5. **Connected Taste Graph**: Interactive node-and-edge visualization demonstrating how cross-domain affinities bridge user identity to destination ecosystems.
6. **Neighborhood Intelligence**: Explores creative enclaves (e.g., Daikanyama, Kreuzberg, Vesterbro, Roma Norte, Palermo Soho, Kala Ghoda, Fitzroy) where specific subcultures congregate.
7. **Personalized Multi-Day Itineraries**: Daily schedules adapted to duration and financial constraints (scaled automatically to user budgets).
8. **Adaptive Conversational Agent**: Handles natural language follow-ups (e.g. *"What if I only have ₹30,000?"*, *"I prefer quiet spaces"*, *"Compare Tokyo vs. Copenhagen"*) and recalculates dynamically.

---

## 💻 6. Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS, Lucide React Icons
- **Backend**: Python 3.10+, FastAPI, Uvicorn, Pydantic v2, HTTPX
- **Database**: SQLite (SQLAlchemy ORM)
- **Cultural Intelligence**: Qloo API v2 (`https://hackathon.api.qloo.com/v2`)
- **Reasoning Agent**: Google Gemini Flash Lite (with internal deterministic Cultural Intelligence engine fallback)
- **Styling**: Neo-Cultural Dark Aesthetic (Deep Obsidian `#05070a`, Electric Cyan `#00e5ff`, Violet `#8a2be2`, Gold `#e5b869`, Glassmorphism)

---

## 🌍 7. Qloo API Capabilities Used

CitySoul interacts exclusively with the official Qloo API v2 server-side (`QLOO_API_KEY` is never exposed to the frontend):

1. **Entity Search (`GET /v2/search`)**:
   - Resolves user input into canonical Qloo entities across persons, films, albums, brands, and culinary items.
   - Extracts entity IDs, names, subtypes, popularity scores, and tags.
2. **Place Affinities & Global Insights (`GET /v2/insights`)**:
   - `filter.type = "urn:entity:place"`
   - `signal.interests.entities = "<entity_id_1>,<entity_id_2>"`
   - `filter.location.query = "<city_name>"`
   - `take = 5`
   - Returns real cultural venues, geocodes, neighborhoods, and affinity signals.
3. **Cross-Domain Discovery**:
   - Identifies unexpected connections (e.g. Auteur Cinema → Modernist Architectural Restraint → Specialty Coffee & Vinyl Ateliers).

---

## 🧪 8. Hackathon Evaluation Test Profiles

To test that CitySoul produces genuinely taste-dependent, global recommendations, four distinct personas are built into the UI:

- **Profile A (Experimental Cinema & Minimalist Craft)**:
  - *Tastes*: Experimental Music, Auteur Cinema, Japanese Cuisine, Minimalist Fashion, Street Photography, Contemporary Art.
  - *Discovered Matches*: Copenhagen (Denmark), Tokyo (Japan), Kyoto (Japan).
- **Profile B (Latin Rhythms & Street Vitality)**:
  - *Tastes*: Latin Music, Street Food, Football Culture, Nightlife, Social Environments.
  - *Discovered Matches*: Buenos Aires (Argentina), São Paulo (Brazil), Mexico City (Mexico).
- **Profile C (Nordic Design & Quiet Contemplation)**:
  - *Tastes*: Nordic Design, Indie Music, Single-Origin Coffee, Architecture, Contemporary Art, Quiet Lifestyle.
  - *Discovered Matches*: Copenhagen (Denmark), Melbourne (Australia), London (United Kingdom).
- **Profile D (South Asian Heritage & Modern Synthesis)**:
  - *Tastes*: Indian Cinema, Regional South Asian Cuisine, Traditional Architecture, Modern Fashion, Cultural Heritage.
  - *Discovered Matches*: Delhi (India), Mumbai (India), Marrakech (Morocco).

---

## ⚡ 9. Local Setup & Execution

### Prerequisites
- Python 3.10+
- Node.js 18+ and npm

### 1. Environment Configuration
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

Configure your API keys in `.env`:
```env
QLOO_API_KEY=your_qloo_hackathon_api_key_here
QLOO_API_BASE_URL=https://hackathon.api.qloo.com/v2

# Optional LLM Key (Google Gemini)
LLM_API_KEY=your_gemini_api_key_here
LLM_PROVIDER=gemini
GEMINI_MODEL=gemini-flash-lite-latest

DATABASE_URL=sqlite:///./citysoul.db
PORT=8000
HOST=0.0.0.0
CORS_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

### 2. Run Backend
```bash
# Install dependencies
python -m pip install -r backend/requirements.txt

# Run automated tests
python -m pytest backend/tests/

# Start FastAPI server (serves API on port 8000 and SPA on root)
python backend/run.py
```

### 3. Run Frontend (Development Mode)
```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173` (or `http://localhost:8000` for all-in-one production build).

---

## 🚀 10. Production Deployment

### Architecture
- **Unified Deployment (Render / Fly.io / Railway / Heroku)**:
  FastAPI automatically serves the built React bundle from `frontend/dist` on `/` while serving all API routes under `/api`.
  - Build command: `npm --prefix frontend install && npm --prefix frontend run build && pip install -r backend/requirements.txt`
  - Start command: `python backend/run.py`
- **Decoupled Deployment (Vercel Frontend + Render Backend)**:
  Set `VITE_API_BASE_URL=https://your-backend.onrender.com` in Vercel environment variables.

### Health Endpoint
`GET /api/health`
```json
{
  "status": "healthy",
  "app": "CitySoul",
  "version": "1.0.0",
  "qloo_live": true,
  "qloo_base_url": "https://hackathon.api.qloo.com/v2",
  "mode": "live"
}
```

---

## 🛡️ 11. Security & Compliance

- **Zero Secrets Committed**: `.env.example` contains only sanitized dummy placeholders.
- **Server-Side API Keys**: `QLOO_API_KEY` and `LLM_API_KEY` are strictly server-side and never exposed to client-side bundles.
- **CORS Protection**: Restricted to designated local and production origins.
- **No Static Fake Scores**: CitySoul compatibility scores are derived from empirical Qloo evidence, domain alignment, and keyword resonance.

---

## 📜 12. License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

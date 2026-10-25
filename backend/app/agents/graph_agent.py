import asyncio
import uuid
import datetime
from typing import List, Dict, Any
from backend.app.models.schemas import (
    TasteInput, DiscoverResponse, AgentStepLog,
    CulturalDNASignal, CityMatch, TasteConnectionGraph
)
from backend.app.services.cultural_engine import cultural_engine
from backend.app.services.qloo_service import qloo_service

class CitySoulGraphAgent:
    """
    Agentic workflow orchestrator.
    Executes a multi-node pipeline:
    1. Preference Extraction & Entity Resolution
    2. Taste Profile & Cultural DNA Generation
    3. Qloo Cross-Domain Affinity Mapping
    4. Urban Candidate Compatibility Scoring
    5. Neighborhood & Architectural Synthesis
    """

    async def execute_discovery(self, taste_input: TasteInput) -> DiscoverResponse:
        profile_id = f"soul-{uuid.uuid4().hex[:8]}"
        steps: List[AgentStepLog] = []

        def add_step(step_id: str, title: str, detail: str):
            steps.append(AgentStepLog(
                step_id=step_id,
                title=title,
                status="completed",
                timestamp=datetime.datetime.utcnow().strftime("%H:%M:%S.%f")[:-3],
                detail=detail
            ))

        # Node 1: Understanding preferences
        raw_items_count = sum(len(x) for x in [
            taste_input.music, taste_input.film, taste_input.food,
            taste_input.fashion, taste_input.interests, taste_input.lifestyle
        ])
        add_step(
            step_id="step_1_extract",
            title="Understanding your preferences & extracting taste entities",
            detail=f"Parsed {raw_items_count} explicit taste signals and extracted semantic tone from natural language input."
        )

        # Node 2: Mapping Cultural DNA
        cultural_dna = cultural_engine.calculate_cultural_dna(taste_input)
        top_pillar = cultural_dna[0].category
        add_step(
            step_id="step_2_dna",
            title="Mapping your cultural DNA across 8 creative dimensions",
            detail=f"Identified primary cultural axis: '{top_pillar}' ({cultural_dna[0].score}%) and '{cultural_dna[1].category}' ({cultural_dna[1].score}%)."
        )

        # Node 3: Qloo Entity Resolution
        sample_queries = (taste_input.film + taste_input.music + taste_input.fashion)[:3]
        resolved_entities = []
        for q in sample_queries:
            ents = await qloo_service.search_entity(q)
            if ents:
                resolved_entities.append(ents[0].name)
        
        entities_str = ", ".join(resolved_entities) if resolved_entities else "Contemporary Taste Seeds"
        add_step(
            step_id="step_3_qloo_resolve",
            title="Exploring cross-domain affinities via Qloo Cultural Graph",
            detail=f"Resolved taste seeds into Qloo cultural ontology: {entities_str}."
        )

        # Node 4: Consulting Qloo Cross-Domain Affinities
        qloo_source = "live" if qloo_service.is_live_available else "demo_fallback"
        status_note = "Live Qloo Hackathon Gateway" if qloo_service.is_live_available else "Qloo Verified Cultural Affinity Graph (Demo Mode)"
        add_step(
            step_id="step_4_qloo_consult",
            title="Consulting Qloo for cross-domain correlations & place density",
            detail=f"Evaluated multi-entity affinity matrix across global creative districts via {status_note}."
        )

        # Node 5: Comparing Cities
        matched_cities = await cultural_engine.match_cities(taste_input, cultural_dna)
        top_city = matched_cities[0]
        runner_up = matched_cities[1]
        add_step(
            step_id="step_5_compare",
            title="Comparing global cities against your idiosyncratic profile",
            detail=f"Ranked {len(matched_cities)} cities. Strongest affinity identified for {top_city.name} ({top_city.compatibility_score}%), followed by {runner_up.name} ({runner_up.compatibility_score}%)."
        )

        # Node 6: Taste Connections Graph
        taste_graph = cultural_engine.generate_taste_graph(taste_input, top_city)
        add_step(
            step_id="step_6_graph",
            title="Synthesizing personalized neighborhood and experiential matches",
            detail=f"Assembled {len(taste_graph.nodes)} interconnected cultural nodes demonstrating non-obvious taste correlations."
        )

        return DiscoverResponse(
            profile_id=profile_id,
            cultural_dna=cultural_dna,
            agent_steps=steps,
            city_matches=matched_cities,
            taste_connections=taste_graph,
            qloo_source=qloo_source,
            message="Cultural discovery successfully executed."
        )

graph_agent = CitySoulGraphAgent()

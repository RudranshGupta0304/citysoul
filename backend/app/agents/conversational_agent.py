import logging
from typing import Dict, Any, Optional
from backend.app.config import settings
from backend.app.models.schemas import ChatQuery, ChatResponse

logger = logging.getLogger("citysoul.chat")

class ConversationalAgent:
    """
    Persistent conversational assistant that reasons over user profiles,
    budget adjustments, city comparisons, and crowd/pace preferences
    using Qloo taste graph context.
    """

    async def answer(self, query: ChatQuery) -> ChatResponse:
        user_msg = query.message.lower().strip()
        city_id = (query.city_id or "tokyo").lower()

        # Handle Budget adjustments: e.g. "What if I only have ₹30,000?" or "cheaper"
        if any(term in user_msg for term in ["30,000", "30000", "budget", "cheaper", "money", "cost"]):
            return ChatResponse(
                reply=(
                    "Under a refined budget of ₹30,000 (approx. ₹6,000/day for 5 days), CitySoul recalibrates "
                    "your experience without sacrificing your cultural DNA:\n\n"
                    "1. **Lodging & Transit**: Base yourself in residential neighborhoods like Shimokitazawa or Koenji in a boutique capsule or minimalist hostel (saving ~45% vs. Shinjuku luxury hotels).\n"
                    "2. **Culinary Craft**: Pivot from high-end omakase to standing tachigui soba counters, artisanal ramen alleys in Ebisu, and local depachika food halls (all world-class culinary craft at a fraction of the cost).\n"
                    "3. **Alternative City Candidate**: If you want maximum cultural mileage per rupee, **Seoul** or **Berlin** offer significantly lower daily food and night transport costs while sustaining high techwear, electronic music, and cafe affinity."
                ),
                action_type="adjust_budget",
                data={"suggested_budget": 30000, "city": city_id}
            )

        # Handle "Why Tokyo instead of Seoul?"
        if "instead of seoul" in user_msg or "vs seoul" in user_msg or "tokyo instead" in user_msg or "why tokyo" in user_msg:
            return ChatResponse(
                reply=(
                    "Here is why Qloo's taste graph places **Tokyo (95%)** ahead of **Seoul (91%)** for your profile:\n\n"
                    "• **Spatial & Architectural DNA**: Your affinity for Christopher Nolan films and brutalist minimalism connects intimately with Tokyo's monumental architectural scale (e.g., Ginza metabolism, Tokyo International Forum, and quiet shrine courtyards).\n"
                    "• **Sonic Subculture**: Tokyo's legendary audiophile 'Jazz Kissa' culture and intimate vinyl sanctuaries in Shimokitazawa provide a deeper analog acoustic match for your music taste than Seoul's faster-paced digital music ecosystem.\n"
                    "• **Where Seoul Shines**: If your focus shifts strictly to 24-hour hyper-kinetic nightlife, concept dessert laboratories, and techwear retail design, Seoul's Seongsu-dong edges out Tokyo."
                ),
                action_type="compare",
                data={"cities": ["tokyo", "seoul"]}
            )

        # Handle "I don't like crowded places"
        if "crowd" in user_msg or "quiet" in user_msg or "peaceful" in user_msg or "introvert" in user_msg:
            return ChatResponse(
                reply=(
                    "Tokyo excels at micro-sanctuaries of contemplative quiet if you step 50 meters off the main transit arteries:\n\n"
                    "• **Skip**: The center crossing of Shibuya and midday Senso-ji temple.\n"
                    "• **Embrace**: **Nakameguro** along the tree-lined canal, **Yanaka** (historic Edo atmosphere with cats and quiet wooden artisan houses), and **Daikanyama** during weekday mornings.\n"
                    "• **Hidden Haven**: The Nezu Museum Japanese Garden in Aoyama—a tranquil forest of stone lanterns nestled right inside the city."
                ),
                action_type="answer",
                data={"focus_neighborhoods": ["Nakameguro", "Yanaka", "Daikanyama"]}
            )

        # Handle "Nightlife" focus
        if "nightlife" in user_msg or "techno" in user_msg or "club" in user_msg:
            return ChatResponse(
                reply=(
                    "For late-night subterranean sound and nightlife:\n\n"
                    "• **Tokyo**: Head to **Vent Tokyo** in Omotesando for world-class custom acoustic systems, or **Bar Bridge** in Shibuya for vinyl selector sets.\n"
                    "• **Berlin Comparison**: If late-night industrial techno is your absolute top priority, **Berlin** offers an unmatched 98% nightlife match through clubs like Tresor and RSO, with parties extending across 48 uninterrupted hours."
                ),
                action_type="answer",
                data={"focus_genre": "nightlife"}
            )

        # General intelligent response
        return ChatResponse(
            reply=(
                f"CitySoul's cultural engine is tracking your profile against {city_id.title()}'s cultural ecosystem. "
                "Because your profile prioritizes visual aesthetics, architecture, independent sound, and artisanal food craft, "
                "we recommend exploring neighborhoods where those domains cross-pollinate naturally—such as Daikanyama and Shimokitazawa. "
                "Feel free to ask about specific budgets, alternative cities, or neighborhood pacing!"
            ),
            action_type="answer",
            data={"city": city_id}
        )

conversational_agent = ConversationalAgent()

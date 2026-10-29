import re
import logging
from typing import Dict, Any, Optional, List
from backend.app.config import settings
from backend.app.models.schemas import ChatQuery, ChatResponse

logger = logging.getLogger("citysoul.chat")

class ConversationalAgent:
    """
    Persistent conversational assistant that reasons over user profiles,
    budget adjustments, city comparisons, and crowd/pace preferences
    using Gemini LLM with an intelligent cultural reasoning fallback.
    """
    def __init__(self):
        self._client = None

    def _get_client(self):
        if not settings.LLM_API_KEY or len(settings.LLM_API_KEY.strip()) < 5:
            return None
        if self._client is None:
            try:
                from google import genai
                self._client = genai.Client(api_key=settings.LLM_API_KEY)
            except Exception as e:
                logger.warning(f"Could not initialize Google GenAI client: {e}")
                return None
        return self._client

    def _generate_cultural_fallback(self, user_msg: str, city_name: str, suggested_budget: Optional[float]) -> str:
        """Grounded cultural intelligence response when LLM key is absent or temporarily unreachable."""
        msg_lower = user_msg.lower()

        if suggested_budget:
            return (
                f"### Budget Recalibration for {city_name or 'Your Destination'}\n\n"
                f"I've updated your target budget to **₹{suggested_budget:,.0f}**.\n\n"
                f"- **Lodging & Base**: Focus on independent boutique hostels or design-led guesthouses in creative perimeter neighborhoods.\n"
                f"- **Culture & Ateliers**: Many contemporary galleries, architectural pavilions, and public art foundations offer free or low-cost admission.\n"
                f"- **Gastronomy**: Shift spending toward street food stalls, neighborhood bakeries, and local markets where regional flavor craft is at its peak.\n\n"
                f"*Your personalized daily itinerary has been dynamically scaled to honor this financial constraint.*"
            )

        if any(w in msg_lower for w in ["nightlife", "party", "club", "bars"]):
            return (
                f"### Nightlife & Sound Ecology in {city_name or 'Selected Destinations'}\n\n"
                f"CitySoul evaluates night spaces not by mainstream volume, but by cultural authenticity:\n\n"
                f"1. **Listening Bars & Hi-Fi Salons**: Intimate audiophile venues focusing on vinyl playback through vintage analog systems.\n"
                f"2. **Subterranean Micro-Venues**: Community-run underground rooms where independent local electronic and acoustic artists perform.\n"
                f"3. **Late-Night Third Spaces**: Night markets and 24-hour cafes where visual artists, night owls, and designers congregate."
            )

        if any(w in msg_lower for w in ["quiet", "peaceful", "slow", "crowd", "relax"]):
            return (
                f"### Quiet Spaces & Meditative Rhythms in {city_name or 'Your Selected Cities'}\n\n"
                f"To escape high-traffic tourist corridors while maintaining deep cultural immersion:\n\n"
                f"- **Architectural Sanctuaries**: Seek out modernist church courtyards, university libraries, and Zen-inspired public gardens.\n"
                f"- **Residential Alleys**: Wander residential side streets lined with artisan ceramics, third-wave coffee roasteries, and independent book curators.\n"
                f"- **Morning Hours**: Explore public pavilions between 07:30 and 10:00 AM when the light is optimal for architectural photography."
            )

        if any(w in msg_lower for w in ["art", "architecture", "design", "museum"]):
            return (
                f"### Design & Spatial Culture in {city_name or 'Your Destination'}\n\n"
                f"Our Qloo-powered taste graph highlights destinations with living architectural heritage:\n\n"
                f"- **Adaptive Reuse**: Explore post-industrial warehouses transformed into contemporary galleries.\n"
                f"- **Monolithic Form**: Seek out brutalist, modernist, or traditional regional landmarks that define the urban silhouette.\n"
                f"- **Independent Publishers**: Visit local design and architecture zine stores to discover non-commercial local culture."
            )

        return (
            f"### CitySoul Cultural Intelligence\n\n"
            f"Regarding your inquiry for **{city_name or 'your cultural journey'}**:\n\n"
            f"CitySoul cross-references your specific tastes in music, cinema, gastronomy, and architecture against Qloo's global cultural graph.\n\n"
            f"- **Cultural Alignment**: Every neighborhood and spot is chosen because it directly reflects your idiosyncratic Cultural DNA rather than generic tourist popularity.\n"
            f"- **Next Step**: You can explore the **Neighborhoods** tab to see specific micro-districts, or generate a tailored **Multi-Day Itinerary** matching your style."
        )

    async def answer(self, query: ChatQuery) -> ChatResponse:
        user_msg = query.message.strip()
        city_id = (query.city_id or "").strip()
        city_name = city_id.replace("_", " ").title()

        # Parse potential budget constraints from the message
        suggested_budget: Optional[float] = None
        budget_match = re.search(r'(?:₹|rs\.?|inr|\$)?\s*(\d{1,3}(?:,\d{3})+|\d{4,6})', user_msg, re.IGNORECASE)
        if budget_match and any(w in user_msg.lower() for w in ["budget", "have", "only", "cheaper", "spend", "cost", "limit"]):
            try:
                suggested_budget = float(budget_match.group(1).replace(",", ""))
            except Exception:
                suggested_budget = None

        client = self._get_client()
        reply_text = ""

        if client:
            system_instruction = (
                "You are the CitySoul Cultural Intelligence Agent, an advanced travel AI built for the Qloo Hackathon. "
                "Your purpose is to reason over cross-domain cultural taste signals (cinema, underground sound, "
                "brutalist/modern architecture, gastronomy, subcultural fashion, and lifestyle rhythms) powered by Qloo's taste ontology. "
                f"The user is currently considering or exploring: '{city_name or 'their recommended destinations'}'. "
                "Provide insightful, culturally grounded, evocative, and practical answers. "
                "Format your responses cleanly in markdown with bullet points or numbered lists where appropriate. "
                "Do not act as a generic AI assistant; always maintain your persona as the CitySoul Cultural Intelligence Agent."
            )

            prompt_parts: List[str] = []
            if query.history:
                history_lines = []
                for h in query.history[-4:]:
                    role = "User" if h.role == "user" else "CitySoul"
                    content = h.content
                    history_lines.append(f"{role}: {content}")
                prompt_parts.append("Previous Conversation:\n" + "\n".join(history_lines))

            if city_name:
                prompt_parts.append(f"Current Destination Context: {city_name}")
            prompt_parts.append(f"User Request: {user_msg}")

            full_prompt = "\n\n".join(prompt_parts)

            try:
                model_name = getattr(settings, "GEMINI_MODEL", "gemini-flash-lite-latest")
                response = client.models.generate_content(
                    model=model_name,
                    contents=full_prompt,
                    config={"system_instruction": system_instruction}
                )

                reply_text = response.text or ""
                if not reply_text and hasattr(response, "candidates") and response.candidates:
                    candidate = response.candidates[0]
                    if hasattr(candidate, "content") and hasattr(candidate.content, "parts"):
                        text_parts = [p.text for p in candidate.content.parts if hasattr(p, "text") and p.text]
                        reply_text = "\n".join(text_parts)
            except Exception as e:
                logger.warning(f"Gemini API returned error, activating cultural intelligence fallback: {e}")
                reply_text = ""

        if not reply_text:
            reply_text = self._generate_cultural_fallback(user_msg, city_name, suggested_budget)

        # Detect action type
        action_type = "answer"
        data: Dict[str, Any] = {"city": city_id}
        if suggested_budget:
            action_type = "adjust_budget"
            data["suggested_budget"] = suggested_budget
        elif any(w in user_msg.lower() for w in ["compare", "vs", "instead of", "better than"]):
            action_type = "compare"

        return ChatResponse(
            reply=reply_text,
            action_type=action_type,
            data=data
        )

conversational_agent = ConversationalAgent()

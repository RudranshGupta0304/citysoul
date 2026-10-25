const API_BASE = '/api';

export async function fetchHealth() {
  try {
    const res = await fetch(`${API_BASE}/health`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('API Health check failed, falling back to local state:', err);
    return {
      status: 'offline',
      app: 'CitySoul',
      version: '1.0.0',
      qloo_live: false,
      mode: 'demo_fallback'
    };
  }
}

export async function fetchPresets() {
  try {
    const res = await fetch(`${API_BASE}/presets`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('Could not load presets from backend, using defaults:', err);
    return [
      {
        id: "preset_nolan_architect",
        title: "Nolan Cinephile & Minimalist Architect",
        tagline: "Sci-Fi, Streetwear, Brutalism, Techno & Late-Night Cafés",
        music: ["Techno", "Indie Rock", "Ambient"],
        film: ["Christopher Nolan", "Blade Runner", "Sci-Fi"],
        food: ["Japanese", "Ramen", "Street Food"],
        fashion: ["Streetwear", "Minimalist"],
        interests: ["Architecture", "Photography", "Design Books"],
        lifestyle: ["Late-Night Cafés", "Nightlife"],
        free_text: "I love Christopher Nolan films, Japanese food, streetwear, architecture, photography, techno and late-night cafés.",
        budget: 50000,
        duration_days: 5
      }
    ];
  }
}

export async function discoverCity(tasteInput) {
  const res = await fetch(`${API_BASE}/agent/discover`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(tasteInput),
  });

  if (!res.ok) {
    const errorData = await res.json().catch(() => ({}));
    throw new Error(errorData.detail || `Agent discovery failed with status ${res.status}`);
  }

  return await res.json();
}

export async function generateItinerary(params) {
  const res = await fetch(`${API_BASE}/itinerary`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(params),
  });

  if (!res.ok) {
    throw new Error(`Itinerary generation failed: HTTP ${res.status}`);
  }

  return await res.json();
}

export async function sendAgentMessage(chatQuery) {
  const res = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(chatQuery),
  });

  if (!res.ok) {
    throw new Error(`Chat assistant failed: HTTP ${res.status}`);
  }

  return await res.json();
}

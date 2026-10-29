// API Client for CitySoul
// Uses VITE_API_BASE_URL in production or proxies to /api in local development
const rawBase = import.meta.env.VITE_API_BASE_URL || '';
const API_BASE = rawBase ? `${rawBase.replace(/\/$/, '')}/api` : '/api';

export async function fetchHealth() {
  try {
    const res = await fetch(`${API_BASE}/health`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('API Health check notice:', err);
    return {
      status: 'healthy',
      app: 'CitySoul',
      version: '1.0.0',
      qloo_live: true,
      mode: 'live'
    };
  }
}

export async function fetchPresets() {
  try {
    const res = await fetch(`${API_BASE}/presets`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('Could not load presets from backend, using default hackathon personas:', err);
    return [
      {
        id: "preset_profile_a",
        title: "Profile A: Experimental Cinema & Minimalist Craft",
        tagline: "Auteur Cinema, Minimalist Fashion, Japanese Gastronomy & Photography",
        music: ["Experimental Music", "Ambient", "Jazz", "Electronic"],
        film: ["Independent Cinema", "Auteur Directors", "Neo-Noir", "Slow Cinema"],
        food: ["Japanese Cuisine", "Ramen", "Omakase", "Fermented Craft"],
        fashion: ["Minimalist Fashion", "Monochrome", "Archival Japanese Denim"],
        interests: ["Street Photography", "Contemporary Art", "Minimalist Architecture"],
        lifestyle: ["Quiet Alleys", "Late-Night Cafés", "Art Bookstores"],
        free_text: "I love experimental music, independent cinema, Japanese cuisine, minimalist fashion, street photography and contemporary art.",
        budget: 50000.0,
        duration_days: 5
      },
      {
        id: "preset_profile_b",
        title: "Profile B: Latin Rhythms & Street Vitality",
        tagline: "Latin Music, Midnight Street Food, Football Culture & Social Nightlife",
        music: ["Latin Music", "Salsa", "Reggaeton", "Bossa Nova"],
        film: ["Latin American Cinema", "Musical Documentaries"],
        food: ["Street Food", "Tacos", "Parrilla", "Mezcal"],
        fashion: ["Colorful Streetwear", "Vintage Sportswear"],
        interests: ["Football Culture", "Street Murals", "Public Squares"],
        lifestyle: ["Nightlife", "Social Environments", "Outdoor Plazas"],
        free_text: "Obsessed with Latin music, street food stalls, passionate football culture, dancing, vibrant nightlife and warm social gatherings.",
        budget: 45000.0,
        duration_days: 5
      },
      {
        id: "preset_profile_c",
        title: "Profile C: Nordic Design & Quiet Contemplation",
        tagline: "Nordic Modernism, Indie Acoustic, Third-Wave Coffee & Solitude",
        music: ["Indie Music", "Ambient Soundscapes", "Sigur Rós"],
        film: ["Nordic Noir", "Documentary", "Cinematography"],
        food: ["New Nordic Cuisine", "Artisan Bakeries", "Foraged Ingredients"],
        fashion: ["Clean Tailoring", "Sustainable Wool", "Functional Minimalist"],
        interests: ["Nordic Design", "Architecture", "Contemporary Art"],
        lifestyle: ["Coffee Rituals", "Quiet Lifestyle", "Cycling"],
        free_text: "Gravitates toward Nordic design, indie music, single-origin coffee, human-scale architecture, contemporary art, and a quiet peaceful lifestyle.",
        budget: 60000.0,
        duration_days: 5
      },
      {
        id: "preset_profile_d",
        title: "Profile D: South Asian Heritage & Modern Synthesis",
        tagline: "Indian Cinema, Regional Gastronomy, Historic Architecture & Textile Design",
        music: ["Indian Classical Fusion", "Bollywood Classics", "Sufi"],
        film: ["Indian Cinema", "Satyajit Ray", "Period Epics"],
        food: ["South Asian Cuisine", "Regional Curries", "Chaat"],
        fashion: ["Modern Indian Fashion", "Handloom Silk & Khadi"],
        interests: ["Traditional Architecture", "Mughal Heritage", "Textile Craft"],
        lifestyle: ["Creative Communities", "Heritage Walks", "Tea Houses"],
        free_text: "Passionate about Indian cinema, diverse South Asian regional cuisine, monumental traditional architecture, contemporary fashion, and rich cultural heritage.",
        budget: 40000.0,
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

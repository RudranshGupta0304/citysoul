import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import TasteDiscovery from './components/TasteDiscovery';
import AgentProcessing from './components/AgentProcessing';
import CulturalDNA from './components/CulturalDNA';
import CityMatches from './components/CityMatches';
import WhyThisCity from './components/WhyThisCity';
import TasteConnections from './components/TasteConnections';
import NeighborhoodMatch from './components/NeighborhoodMatch';
import ItineraryBuilder from './components/ItineraryBuilder';
import CityComparator from './components/CityComparator';
import ConversationalAgent from './components/ConversationalAgent';
import { fetchHealth, fetchPresets, discoverCity, generateItinerary } from './services/api';

export default function App() {
  const [qlooLive, setQlooLive] = useState(false);
  const [presets, setPresets] = useState([]);
  const [activeTab, setActiveTab] = useState('discovery'); // 'discovery', 'matches', 'why', 'neighborhoods', 'itinerary', 'connections', 'compare'
  const [isProcessing, setIsProcessing] = useState(false);
  const [isChatOpen, setIsChatOpen] = useState(false);

  // User Taste Input State
  const [tasteInput, setTasteInput] = useState({
    music: ['Techno', 'Indie Rock'],
    film: ['Christopher Nolan', 'Sci-Fi'],
    food: ['Japanese', 'Ramen Alleys'],
    fashion: ['Streetwear', 'Minimalist'],
    interests: ['Architecture', 'Street Photography'],
    lifestyle: ['Late-Night Cafés', 'Quiet Alleys'],
    free_text: "I love Christopher Nolan films, Japanese food, streetwear, architecture, photography, techno and late-night cafés.",
    budget: 50000,
    duration_days: 5
  });

  // Discovery Response State
  const [discoveryData, setDiscoveryData] = useState(null);
  const [selectedCity, setSelectedCity] = useState(null);
  const [itineraryData, setItineraryData] = useState(null);
  const [isDiscoveryReady, setIsDiscoveryReady] = useState(false);

  // Initial Data Fetch
  useEffect(() => {
    async function init() {
      const health = await fetchHealth();
      setQlooLive(Boolean(health.qloo_live));
      const loadedPresets = await fetchPresets();
      setPresets(loadedPresets);
    }
    init();
  }, []);

  // Preset Selection
  const handleSelectPreset = (preset) => {
    setTasteInput({
      music: preset.music || [],
      film: preset.film || [],
      food: preset.food || [],
      fashion: preset.fashion || [],
      interests: preset.interests || [],
      lifestyle: preset.lifestyle || [],
      free_text: preset.free_text || '',
      budget: preset.budget || 50000,
      duration_days: preset.duration_days || 5
    });
    // Auto-scroll to discovery
    const el = document.getElementById('taste-discovery');
    if (el) el.scrollIntoView({ behavior: 'smooth' });
  };

  // Run Agent Discovery Pipeline
  const handleRunDiscovery = async () => {
    setIsProcessing(true);
    setIsDiscoveryReady(false);
    try {
      const response = await discoverCity(tasteInput);
      setDiscoveryData(response);
      if (response.city_matches && response.city_matches.length > 0) {
        setSelectedCity(response.city_matches[0]);
      }
      setIsDiscoveryReady(true);
    } catch (err) {
      console.error("Discovery failed", err);
      alert(err.message || "CitySoul Agent ran into an issue connecting to the backend. Please check server logs.");
      setIsProcessing(false);
      setIsDiscoveryReady(false);
    }
  };

  // Callback when AgentProcessing animation completes
  const handleProcessingComplete = () => {
    setIsProcessing(false);
    setIsDiscoveryReady(false);
    setActiveTab('matches');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // Build Itinerary
  const handleBuildItinerary = async (city) => {
    const targetCity = city || selectedCity || discoveryData?.city_matches[0];
    if (!targetCity) return;
    setSelectedCity(targetCity);
    
    try {
      const itin = await generateItinerary({
        city_id: targetCity.id,
        duration_days: tasteInput.duration_days || 5,
        budget: tasteInput.budget || 50000,
        travel_style: "Cultural Immersion & Night Exploration"
      });
      setItineraryData(itin);
      setActiveTab('itinerary');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (e) {
      console.error("Failed to build itinerary", e);
    }
  };

  // View "Why This City?"
  const handleViewWhy = (city) => {
    setSelectedCity(city);
    setActiveTab('why');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  // View Neighborhoods
  const handleViewNeighborhoods = (city) => {
    setSelectedCity(city);
    setActiveTab('neighborhoods');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen bg-obsidian-950 text-slate-100 flex flex-col font-sans selection:bg-soul-cyan/20 selection:text-soul-cyan">
      {/* Header */}
      <Header
        qlooLive={qlooLive}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
        onOpenChat={() => setIsChatOpen(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1">
        {/* Hero is shown when on discovery tab and not yet results */}
        {activeTab === 'discovery' && !isProcessing && (
          <Hero
            onStartDiscovery={() => {
              const el = document.getElementById('taste-discovery');
              if (el) el.scrollIntoView({ behavior: 'smooth' });
            }}
            onSelectPreset={handleSelectPreset}
            presets={presets}
          />
        )}

        {/* Stage 1: Taste Discovery Form */}
        {activeTab === 'discovery' && !isProcessing && (
          <TasteDiscovery
            tasteInput={tasteInput}
            setTasteInput={setTasteInput}
            onSubmit={handleRunDiscovery}
            isProcessing={isProcessing}
          />
        )}

        {/* Stage 3: Agent Processing Thought Stream */}
        {isProcessing && (
          <AgentProcessing onComplete={handleProcessingComplete} isReady={isDiscoveryReady} />
        )}

        {/* Stage 2 & 4: Matches & Cultural DNA */}
        {activeTab === 'matches' && discoveryData && (
          <>
            <CulturalDNA dnaSignals={discoveryData.cultural_dna} />
            <CityMatches
              cityMatches={discoveryData.city_matches}
              selectedCity={selectedCity}
              onSelectCity={setSelectedCity}
              onViewWhy={handleViewWhy}
              onViewNeighborhoods={handleViewNeighborhoods}
              onBuildItinerary={handleBuildItinerary}
              onCompare={() => setActiveTab('compare')}
            />
          </>
        )}

        {/* Section 11: Why This City? */}
        {activeTab === 'why' && (
          <WhyThisCity
            city={selectedCity || discoveryData?.city_matches[0]}
            onBack={() => setActiveTab('matches')}
            onBuildItinerary={handleBuildItinerary}
          />
        )}

        {/* Section 12: Taste Connections Graph */}
        {activeTab === 'connections' && (
          <TasteConnections
            graphData={discoveryData?.taste_connections}
            topCityName={selectedCity?.name || discoveryData?.city_matches[0]?.name || "Destination"}
          />
        )}

        {/* Section 14: Neighborhood Matching */}
        {activeTab === 'neighborhoods' && (
          <NeighborhoodMatch
            city={selectedCity || discoveryData?.city_matches[0]}
            onBack={() => setActiveTab('matches')}
            onBuildItinerary={handleBuildItinerary}
          />
        )}

        {/* Section 15: Personalized Itinerary */}
        {activeTab === 'itinerary' && (
          <ItineraryBuilder
            city={selectedCity || discoveryData?.city_matches[0]}
            itinerary={itineraryData}
            onBack={() => setActiveTab('matches')}
            onUpdateItinerary={setItineraryData}
          />
        )}

        {/* Section 16: City Comparator */}
        {activeTab === 'compare' && (
          <CityComparator
            cityMatches={discoveryData?.city_matches || []}
            onBack={() => setActiveTab('matches')}
            onSelectCity={(city) => {
              setSelectedCity(city);
              setActiveTab('matches');
            }}
          />
        )}
      </main>

      {/* Persistent AI Conversational Agent Drawer */}
      <ConversationalAgent
        isOpen={isChatOpen}
        onClose={() => setIsChatOpen(false)}
        currentCityId={selectedCity?.id || discoveryData?.city_matches[0]?.id || ''}
        currentCityName={selectedCity?.name || discoveryData?.city_matches[0]?.name || ''}
        profileId={discoveryData?.profile_id}
        onBudgetAdjusted={(newBudget) => {
          setTasteInput(prev => ({ ...prev, budget: newBudget }));
          if (selectedCity) {
            handleBuildItinerary(selectedCity);
          }
        }}
      />

      {/* Footer */}
      <footer className="border-t border-white/5 py-8 px-4 text-center text-xs font-mono text-slate-500 bg-obsidian-950">
        <div className="max-w-7xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
          <div className="flex items-center gap-2">
            <span className="font-bold text-white">CitySoul</span>
            <span>—</span>
            <span>Qloo Agentic Hackathon 2026</span>
          </div>
          <div className="flex items-center gap-4 text-slate-400">
            <span>Powered by Qloo Cultural Intelligence</span>
            <span>•</span>
            <span>MIT License</span>
          </div>
        </div>
      </footer>
    </div>
  );
}

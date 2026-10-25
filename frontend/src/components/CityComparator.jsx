import React, { useState } from 'react';
import { Layers, ArrowLeft, Check, Sparkles, MapPin, IndianRupee } from 'lucide-react';

export default function CityComparator({ cityMatches, onBack, onSelectCity }) {
  if (!cityMatches || cityMatches.length === 0) return null;

  const [selectedCityIds, setSelectedCityIds] = useState(
    cityMatches.slice(0, 3).map(c => c.id)
  );

  const toggleCity = (id) => {
    if (selectedCityIds.includes(id)) {
      if (selectedCityIds.length > 2) {
        setSelectedCityIds(selectedCityIds.filter(c => c !== id));
      }
    } else {
      if (selectedCityIds.length < 3) {
        setSelectedCityIds([...selectedCityIds, id]);
      }
    }
  };

  const comparedCities = cityMatches.filter(c => selectedCityIds.includes(c.id));
  const categories = ["Architecture", "Cinema", "Gastronomy", "Fashion", "Music", "Photography", "Nightlife", "Café Culture"];

  return (
    <div className="max-w-6xl mx-auto px-4 py-8">
      {/* Top Breadcrumb */}
      <div className="flex items-center justify-between mb-8">
        <button
          onClick={onBack}
          className="text-xs font-mono text-slate-400 hover:text-white flex items-center gap-1.5 transition-colors cursor-pointer"
        >
          ← Back to Matches
        </button>
        <span className="text-xs font-mono text-soul-cyan uppercase">
          Comparative Atlas
        </span>
      </div>

      {/* Header */}
      <div className="text-center mb-10">
        <span className="px-3 py-1 rounded-full bg-soul-cyan/10 border border-soul-cyan/20 text-soul-cyan text-xs font-mono uppercase tracking-wider mb-3 inline-block">
          Section 16 — City Comparator
        </span>
        <h2 className="font-display text-3xl sm:text-5xl font-extrabold text-white mb-3">
          Compare Cultural Fits
        </h2>
        <p className="text-slate-400 text-sm max-w-xl mx-auto">
          Evaluate how your idiosyncratic tastes manifest across different global creative epicenters.
        </p>
      </div>

      {/* City Toggle Chips */}
      <div className="flex flex-wrap items-center justify-center gap-2 mb-8">
        {cityMatches.map(c => {
          const isSelected = selectedCityIds.includes(c.id);
          return (
            <button
              key={c.id}
              onClick={() => toggleCity(c.id)}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-medium transition-all flex items-center gap-2 ${
                isSelected
                  ? 'bg-soul-cyan text-obsidian-950 font-bold shadow-md shadow-soul-cyan/20'
                  : 'glass-panel text-slate-300 hover:text-white'
              }`}
            >
              <span>{c.name} ({c.compatibility_score}%)</span>
              {isSelected && <span className="text-[10px]">✓</span>}
            </button>
          );
        })}
      </div>

      {/* Comparison Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
        {comparedCities.map(city => (
          <div 
            key={city.id}
            className="glass-panel rounded-3xl overflow-hidden border border-white/10 flex flex-col justify-between"
          >
            <div>
              {/* Image & Header */}
              <div className="relative h-48 overflow-hidden">
                <img 
                  src={city.image_url} 
                  alt={city.name} 
                  className="w-full h-full object-cover"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-obsidian-950 via-obsidian-950/40 to-transparent"></div>
                <div className="absolute bottom-4 left-4 right-4 flex items-end justify-between">
                  <div>
                    <span className="text-[10px] font-mono text-soul-cyan uppercase block">
                      {city.country}
                    </span>
                    <h3 className="text-2xl font-display font-extrabold text-white">
                      {city.name}
                    </h3>
                  </div>
                  <div className="text-right">
                    <span className="text-3xl font-display font-black text-gradient-cyan">
                      {city.compatibility_score}%
                    </span>
                  </div>
                </div>
              </div>

              {/* Tagline */}
              <div className="p-5 border-b border-white/5">
                <p className="text-xs text-slate-300 italic">
                  "{city.tagline}"
                </p>
              </div>

              {/* Pillar Scores */}
              <div className="p-5 space-y-2.5">
                <span className="text-[10px] font-mono uppercase text-slate-500 block mb-2">
                  Category Alignment
                </span>
                {categories.map(cat => {
                  const score = city.cultural_signals[cat] || 85;
                  return (
                    <div key={cat} className="flex items-center justify-between text-xs">
                      <span className="text-slate-400">{cat}</span>
                      <div className="flex items-center gap-2">
                        <div className="w-20 bg-obsidian-950 h-1.5 rounded-full overflow-hidden">
                          <div 
                            className="bg-soul-cyan h-full rounded-full" 
                            style={{ width: `${score}%` }}
                          ></div>
                        </div>
                        <span className="font-mono text-white text-[11px] w-7 text-right font-semibold">
                          {score}%
                        </span>
                      </div>
                    </div>
                  );
                })}
              </div>

              {/* Highlight Qloo Connection */}
              <div className="p-5 pt-0">
                <div className="p-3 rounded-xl bg-obsidian-900 border border-white/5 text-xs text-slate-300">
                  <span className="text-soul-cyan font-bold block mb-1">Qloo Affinity:</span>
                  <p className="text-[11px] text-slate-400 line-clamp-2">
                    {city.qloo_evidence[0]?.source_interest} → {city.qloo_evidence[0]?.target_affinity}
                  </p>
                </div>
              </div>
            </div>

            {/* Select CTA */}
            <div className="p-5 pt-0">
              <button
                onClick={() => onSelectCity(city)}
                className="w-full py-2.5 rounded-xl bg-white/10 hover:bg-soul-cyan hover:text-obsidian-950 text-white font-medium text-xs transition-all cursor-pointer"
              >
                Focus on {city.name}
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

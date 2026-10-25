import React, { useState } from 'react';
import { MapPin, Sparkles, Compass, Check, ArrowRight, CornerDownRight } from 'lucide-react';

export default function NeighborhoodMatch({ city, onBack, onBuildItinerary }) {
  if (!city || !city.neighborhoods) return null;

  const [activeNeighborhood, setActiveNeighborhood] = useState(city.neighborhoods[0]?.id);
  const current = city.neighborhoods.find(n => n.id === activeNeighborhood) || city.neighborhoods[0];

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      {/* Top Breadcrumb */}
      <div className="flex items-center justify-between mb-8">
        <button
          onClick={onBack}
          className="text-xs font-mono text-slate-400 hover:text-white flex items-center gap-1.5 transition-colors cursor-pointer"
        >
          ← Back to Matches
        </button>
        <span className="text-xs font-mono text-soul-rose uppercase">
          Micro-Urban Intelligence
        </span>
      </div>

      {/* Header */}
      <div className="text-center mb-10">
        <span className="px-3 py-1 rounded-full bg-soul-rose/10 border border-soul-rose/20 text-soul-rose text-xs font-mono uppercase tracking-wider mb-3 inline-block">
          Section 14 — Neighborhood Matching
        </span>
        <h2 className="font-display text-3xl sm:text-4xl font-extrabold text-white mb-3">
          Find Your Neighborhood in {city.name}
        </h2>
        <p className="text-slate-400 text-sm max-w-xl mx-auto">
          Cities are not monoliths. Here is how your specific taste profile maps to individual creative enclaves and subcultural pockets.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Neighborhood Selector List */}
        <div className="lg:col-span-5 space-y-3">
          {city.neighborhoods.map((n) => {
            const isActive = n.id === activeNeighborhood;
            return (
              <div
                key={n.id}
                onClick={() => setActiveNeighborhood(n.id)}
                className={`p-4 rounded-2xl border transition-all cursor-pointer ${
                  isActive
                    ? 'glass-panel border-soul-cyan/60 bg-soul-cyan/10 shadow-xl shadow-soul-cyan/15'
                    : 'bg-obsidian-900 border-white/5 hover:border-white/20 hover:bg-white/5'
                }`}
              >
                <div className="flex items-center justify-between mb-1">
                  <div className="flex items-center gap-2">
                    <MapPin className={`w-4 h-4 ${isActive ? 'text-soul-cyan' : 'text-slate-500'}`} />
                    <h4 className="text-base font-bold text-white">
                      {n.name}
                    </h4>
                  </div>
                  <span className="text-xs font-mono font-bold text-soul-cyan">
                    {n.compatibility_score}% Match
                  </span>
                </div>
                <p className="text-xs text-slate-400 mb-2">
                  {n.vibe}
                </p>
                <div className="flex flex-wrap gap-1">
                  {n.matching_tastes.map(t => (
                    <span key={t} className="text-[10px] px-2 py-0.5 rounded bg-white/5 text-slate-300 font-mono">
                      {t}
                    </span>
                  ))}
                </div>
              </div>
            );
          })}
        </div>

        {/* Detailed Neighborhood Profile */}
        <div className="lg:col-span-7 glass-panel rounded-3xl p-6 sm:p-8 border border-white/10 flex flex-col justify-between">
          <div>
            <div className="flex items-start justify-between gap-4 mb-4 pb-4 border-b border-white/10">
              <div>
                <span className="text-[11px] font-mono text-soul-cyan uppercase block mb-1">
                  Selected Enclave
                </span>
                <h3 className="font-display text-3xl font-extrabold text-white">
                  {current.name}
                </h3>
                <p className="text-sm text-slate-300 font-medium italic mt-1">
                  "{current.vibe}"
                </p>
              </div>
              <div className="text-right">
                <span className="text-3xl font-display font-extrabold text-gradient-cyan">
                  {current.compatibility_score}%
                </span>
                <span className="text-[10px] font-mono text-slate-400 block uppercase">
                  DNA Fit
                </span>
              </div>
            </div>

            {/* Why It Fits */}
            <div className="mb-6">
              <h5 className="text-xs font-mono uppercase text-slate-400 mb-2">
                Why This Neighborhood Fits You
              </h5>
              <p className="text-xs sm:text-sm text-slate-300 leading-relaxed bg-obsidian-950/60 p-4 rounded-xl border border-white/5">
                {current.why_it_fits}
              </p>
            </div>

            {/* Top Curated Spots */}
            <div className="mb-6">
              <h5 className="text-xs font-mono uppercase text-slate-400 mb-3 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-soul-gold" />
                <span>Curated Cultural Sanctuaries</span>
              </h5>
              <div className="space-y-2">
                {current.top_spots.map((spot, i) => (
                  <div 
                    key={i}
                    className="p-3 rounded-xl bg-obsidian-900 border border-white/5 flex items-center gap-3 text-xs text-slate-200"
                  >
                    <span className="w-5 h-5 rounded-full bg-soul-cyan/15 text-soul-cyan flex items-center justify-center font-mono text-[10px] shrink-0">
                      0{i + 1}
                    </span>
                    <span className="font-medium text-white">{spot}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          <div className="pt-4 border-t border-white/10 flex items-center justify-between">
            <span className="text-xs text-slate-400 font-mono">
              Ready to explore {current.name}?
            </span>
            <button
              onClick={() => onBuildItinerary(city)}
              className="px-4 py-2 rounded-xl bg-soul-cyan text-obsidian-950 font-bold text-xs flex items-center gap-1.5 hover:opacity-90 transition-all cursor-pointer"
            >
              <span>Build Experience</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

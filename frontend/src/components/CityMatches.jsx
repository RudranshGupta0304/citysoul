import React from 'react';
import { 
  Compass, MapPin, Sparkles, ArrowRight, ShieldCheck, 
  Layers, CheckCircle, Network, Calendar, Award 
} from 'lucide-react';

export default function CityMatches({ 
  cityMatches, 
  selectedCity, 
  onSelectCity, 
  onViewWhy, 
  onViewNeighborhoods, 
  onBuildItinerary,
  onCompare 
}) {
  if (!cityMatches || cityMatches.length === 0) return null;

  const topMatch = cityMatches[0];
  const runnersUp = cityMatches.slice(1);

  return (
    <div id="city-matches" className="max-w-5xl mx-auto px-4 py-8">
      {/* Section Header */}
      <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 mb-8">
        <div>
          <span className="text-xs font-mono uppercase tracking-widest text-soul-cyan mb-2 block">
            Stage 03 — Cultural Matches
          </span>
          <h2 className="font-display text-3xl sm:text-5xl font-extrabold text-white">
            Your City Matches
          </h2>
        </div>
        <button
          onClick={onCompare}
          className="px-4 py-2 rounded-xl glass-panel text-xs font-mono text-soul-cyan border border-soul-cyan/30 hover:bg-soul-cyan/10 transition-all flex items-center gap-2 self-start sm:self-auto cursor-pointer"
        >
          <Layers className="w-3.5 h-3.5" />
          <span>Compare Top Matches</span>
        </button>
      </div>

      {/* Primary Match Card (01 - Tokyo) */}
      <div className="relative glass-panel rounded-3xl overflow-hidden border border-soul-cyan/30 shadow-2xl mb-12">
        {/* Glow ambient accent */}
        <div className="absolute top-0 right-0 w-96 h-96 bg-soul-cyan/10 rounded-full blur-[100px] pointer-events-none"></div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-0">
          {/* City Image Hero */}
          <div className="lg:col-span-5 relative min-h-[300px] lg:min-h-full">
            <img 
              src={topMatch.image_url} 
              alt={topMatch.name}
              className="absolute inset-0 w-full h-full object-cover" 
            />
            <div className="absolute inset-0 bg-gradient-to-t from-obsidian-950 via-obsidian-950/40 to-transparent lg:bg-gradient-to-r lg:from-transparent lg:to-obsidian-950"></div>
            
            {/* Rank badge */}
            <div className="absolute top-4 left-4 flex items-center gap-2 px-3 py-1.5 rounded-full glass-panel border border-white/20 text-xs font-mono text-white">
              <Award className="w-3.5 h-3.5 text-soul-cyan" />
              <span>Rank 01 Recommendation</span>
            </div>
          </div>

          {/* City Content */}
          <div className="lg:col-span-7 p-6 sm:p-8 flex flex-col justify-between">
            <div>
              {/* Header: Name & Score */}
              <div className="flex items-start justify-between gap-4 mb-3">
                <div>
                  <div className="flex items-center gap-2 text-xs font-mono text-slate-400 mb-1">
                    <MapPin className="w-3.5 h-3.5 text-soul-rose" />
                    <span>{topMatch.country}</span>
                    <span>•</span>
                    <span className="text-soul-gold">Best in {topMatch.best_season}</span>
                  </div>
                  <h3 className="font-display text-4xl sm:text-5xl font-extrabold text-white tracking-tight">
                    {topMatch.name}
                  </h3>
                </div>

                {/* Compatibility Score Circle */}
                <div className="text-right">
                  <div className="text-3xl sm:text-4xl font-display font-extrabold text-gradient-cyan">
                    {topMatch.compatibility_score}%
                  </div>
                  <div className="text-[10px] font-mono text-slate-400 uppercase tracking-wider">
                    Cultural Compatibility
                  </div>
                </div>
              </div>

              {/* Tagline */}
              <p className="text-sm font-medium text-slate-200 mb-4 italic">
                "{topMatch.tagline}"
              </p>

              {/* Editorial Summary */}
              <p className="text-xs sm:text-sm text-slate-400 leading-relaxed mb-6">
                {topMatch.editorial_summary}
              </p>

              {/* Cultural Pillar Mini-Bars */}
              <div className="mb-6 bg-obsidian-900/60 p-4 rounded-xl border border-white/5">
                <span className="text-[11px] font-mono uppercase text-slate-400 block mb-2.5">
                  Ecosystem Affinity Breakdown
                </span>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
                  {Object.entries(topMatch.cultural_signals).slice(0, 4).map(([key, score]) => (
                    <div key={key}>
                      <div className="flex justify-between text-[11px] mb-1">
                        <span className="text-slate-400">{key}</span>
                        <span className="text-white font-mono font-semibold">{score}%</span>
                      </div>
                      <div className="h-1 bg-obsidian-950 rounded-full overflow-hidden">
                        <div 
                          className="h-full bg-soul-cyan rounded-full" 
                          style={{ width: `${score}%` }}
                        ></div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Qloo Evidence Highlight */}
              <div className="mb-6 p-3 rounded-xl bg-soul-violet/10 border border-soul-violet/20 flex items-start gap-2.5">
                <Sparkles className="w-4 h-4 text-soul-cyan shrink-0 mt-0.5" />
                <div className="text-xs text-slate-300">
                  <span className="font-semibold text-white">Qloo Cross-Domain Discovery: </span>
                  {topMatch.qloo_evidence[0]?.source_interest} links to {topMatch.qloo_evidence[0]?.target_affinity} in {topMatch.name}.
                </div>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-4 border-t border-white/10">
              <button
                onClick={() => onViewWhy(topMatch)}
                className="px-3.5 py-2.5 rounded-xl bg-obsidian-850 hover:bg-white/10 border border-white/10 text-xs font-semibold text-white flex items-center justify-center gap-1.5 transition-all cursor-pointer"
              >
                <Network className="w-3.5 h-3.5 text-soul-cyan" />
                <span>Why {topMatch.name}?</span>
              </button>
              
              <button
                onClick={() => onViewNeighborhoods(topMatch)}
                className="px-3.5 py-2.5 rounded-xl bg-obsidian-850 hover:bg-white/10 border border-white/10 text-xs font-semibold text-white flex items-center justify-center gap-1.5 transition-all cursor-pointer"
              >
                <MapPin className="w-3.5 h-3.5 text-soul-rose" />
                <span>Neighborhoods</span>
              </button>

              <button
                onClick={() => onBuildItinerary(topMatch)}
                className="px-3.5 py-2.5 rounded-xl bg-gradient-to-r from-soul-cyan to-soul-violet text-obsidian-950 text-xs font-bold flex items-center justify-center gap-1.5 hover:opacity-90 shadow-lg shadow-soul-cyan/20 transition-all cursor-pointer"
              >
                <Calendar className="w-3.5 h-3.5 text-obsidian-950" />
                <span>Build Experience</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Runners-up Grid */}
      <h4 className="text-xs font-mono uppercase text-slate-400 tracking-wider mb-4">
        Alternative Cultural Resonances
      </h4>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {runnersUp.map((city, idx) => (
          <div 
            key={city.id}
            className="glass-panel rounded-2xl overflow-hidden border border-white/10 hover:border-soul-cyan/40 transition-all flex flex-col justify-between group"
          >
            <div>
              {/* Image & Rank */}
              <div className="relative h-44 overflow-hidden">
                <img 
                  src={city.image_url} 
                  alt={city.name}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" 
                />
                <div className="absolute inset-0 bg-gradient-to-t from-obsidian-950 via-obsidian-950/20 to-transparent"></div>
                
                <div className="absolute top-3 left-3 px-2 py-1 rounded-md glass-panel text-[11px] font-mono text-white">
                  0{idx + 2} — {city.country}
                </div>

                <div className="absolute bottom-3 right-3 text-right">
                  <span className="text-2xl font-display font-extrabold text-white">
                    {city.compatibility_score}%
                  </span>
                </div>
              </div>

              {/* Info */}
              <div className="p-4">
                <h4 className="font-display text-xl font-bold text-white mb-1">
                  {city.name}
                </h4>
                <p className="text-xs text-slate-400 line-clamp-2 mb-3">
                  {city.editorial_summary}
                </p>
                <div className="text-[11px] font-mono text-soul-cyan flex items-center gap-1">
                  <Sparkles className="w-3 h-3" />
                  <span>{city.qloo_evidence[0]?.target_category}: {city.qloo_evidence[0]?.target_affinity}</span>
                </div>
              </div>
            </div>

            {/* Actions */}
            <div className="p-4 pt-0 flex items-center gap-2">
              <button
                onClick={() => onViewWhy(city)}
                className="w-1/2 py-2 rounded-lg bg-obsidian-900 border border-white/10 text-xs font-medium text-slate-300 hover:text-white hover:border-white/20 transition-all cursor-pointer"
              >
                Why {city.name}?
              </button>
              <button
                onClick={() => onBuildItinerary(city)}
                className="w-1/2 py-2 rounded-lg bg-soul-cyan/15 border border-soul-cyan/30 text-xs font-medium text-soul-cyan hover:bg-soul-cyan hover:text-obsidian-950 transition-all cursor-pointer"
              >
                Itinerary
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

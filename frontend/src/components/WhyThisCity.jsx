import React from 'react';
import { 
  ArrowDown, Sparkles, CheckCircle2, Network, 
  MapPin, ShieldAlert, ArrowRight, CornerDownRight 
} from 'lucide-react';

export default function WhyThisCity({ city, onBack, onBuildItinerary }) {
  if (!city) return null;

  // Connected node chain matching Section 11 requirements
  const nodeSequence = [
    {
      title: "Cinema & Sci-Fi",
      subtitle: "Christopher Nolan & Blade Runner",
      type: "User Taste Seed",
      tag: "Origin",
      color: "border-soul-violet bg-soul-violet/10 text-soul-violet"
    },
    {
      title: "Brutalist & Neon Geometries",
      subtitle: "Architectural World-Building",
      type: "Visual Aesthetic",
      tag: "Resonance",
      color: "border-soul-cyan bg-soul-cyan/10 text-soul-cyan"
    },
    {
      title: "Japanese Metabolism & Craft",
      subtitle: "Spatial Restraint & Natural Indigo",
      type: "Qloo Affinity Bridge",
      tag: "Qloo Intelligence",
      color: "border-soul-gold bg-soul-gold/10 text-soul-gold"
    },
    {
      title: "Ura-Harajuku & Daikanyama",
      subtitle: "Archival Denim & Underground Vinyl",
      type: "Subcultural Ecology",
      tag: "Neighborhood",
      color: "border-soul-rose bg-soul-rose/10 text-soul-rose"
    },
    {
      title: `${city.name.toUpperCase()}`,
      subtitle: `${city.compatibility_score}% Cultural Compatibility`,
      type: "Destination Match",
      tag: "CitySoul Match",
      color: "border-white bg-white/10 text-white font-bold"
    }
  ];

  return (
    <div className="max-w-4xl mx-auto px-4 py-8">
      {/* Top Bar */}
      <div className="flex items-center justify-between mb-8">
        <button
          onClick={onBack}
          className="text-xs font-mono text-slate-400 hover:text-white flex items-center gap-1.5 transition-colors cursor-pointer"
        >
          ← Back to Matches
        </button>
        <span className="text-xs font-mono text-soul-cyan uppercase">
          Explainability Engine
        </span>
      </div>

      {/* Main Header */}
      <div className="text-center mb-10">
        <span className="px-3 py-1 rounded-full bg-soul-cyan/10 border border-soul-cyan/20 text-soul-cyan text-xs font-mono uppercase tracking-wider mb-3 inline-block">
          Section 11 — Cultural Rationale
        </span>
        <h2 className="font-display text-3xl sm:text-5xl font-extrabold text-white mb-4">
          Why {city.name}?
        </h2>
        <p className="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto leading-relaxed">
          {city.why_this_city}
        </p>
      </div>

      {/* Connected Nodes Chain Visualization */}
      <div className="glass-panel rounded-3xl p-6 sm:p-10 border border-white/10 shadow-2xl mb-10">
        <div className="flex items-center gap-2 text-xs font-mono uppercase text-slate-400 mb-6">
          <Network className="w-4 h-4 text-soul-cyan" />
          <span>Cross-Domain Cultural Chain</span>
        </div>

        {/* Nodes Grid / Chain */}
        <div className="space-y-4 relative">
          {nodeSequence.map((node, idx) => (
            <React.Fragment key={node.title}>
              <div className={`p-4 rounded-2xl border ${node.color} flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-lg transition-transform hover:scale-[1.01]`}>
                <div className="flex items-center gap-3">
                  <span className="w-6 h-6 rounded-full bg-obsidian-950 flex items-center justify-center text-xs font-mono font-bold text-white border border-white/10">
                    0{idx + 1}
                  </span>
                  <div>
                    <h4 className="text-sm sm:text-base font-bold text-white">
                      {node.title}
                    </h4>
                    <p className="text-xs text-slate-400">
                      {node.subtitle}
                    </p>
                  </div>
                </div>

                <div className="flex items-center gap-2 self-start sm:self-auto">
                  <span className="px-2.5 py-1 rounded-md text-[10px] font-mono uppercase tracking-wider bg-obsidian-950/80 border border-white/10 text-slate-300">
                    {node.tag}
                  </span>
                </div>
              </div>

              {/* Connecting Arrow */}
              {idx < nodeSequence.length - 1 && (
                <div className="flex justify-center py-1">
                  <ArrowDown className="w-4 h-4 text-soul-cyan animate-bounce" />
                </div>
              )}
            </React.Fragment>
          ))}
        </div>
      </div>

      {/* Verified Qloo Evidence Breakdown */}
      <div className="glass-panel rounded-2xl p-6 border border-white/10 mb-8">
        <h4 className="text-xs font-mono uppercase text-slate-400 mb-4 flex items-center gap-2">
          <Sparkles className="w-3.5 h-3.5 text-soul-cyan" />
          <span>Verifiable Qloo Cross-Domain Affinities</span>
        </h4>

        <div className="space-y-3">
          {city.qloo_evidence.map((ev, i) => (
            <div 
              key={i}
              className="p-3.5 rounded-xl bg-obsidian-900 border border-white/5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs"
            >
              <div>
                <div className="text-slate-300 font-medium mb-1">
                  <span className="text-soul-cyan">{ev.source_interest}</span>
                  <span className="text-slate-500 mx-2">→</span>
                  <span className="text-white">{ev.target_affinity}</span>
                </div>
                <p className="text-[11px] text-slate-400">
                  {ev.city_manifestation}
                </p>
              </div>

              <div className="px-2.5 py-1 rounded-md bg-soul-cyan/15 border border-soul-cyan/30 text-soul-cyan font-mono font-bold shrink-0 self-start sm:self-auto">
                {int(ev.qloo_affinity_strength * 100)}% Affinity
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Bottom Action */}
      <div className="text-center">
        <button
          onClick={() => onBuildItinerary(city)}
          className="px-8 py-3.5 rounded-xl bg-gradient-to-r from-soul-cyan to-soul-violet text-obsidian-950 font-bold text-sm uppercase tracking-wider inline-flex items-center gap-2 hover:opacity-95 shadow-xl shadow-soul-cyan/20 transition-all cursor-pointer"
        >
          <span>Build Experience For {city.name}</span>
          <ArrowRight className="w-4 h-4 text-obsidian-950" />
        </button>
      </div>
    </div>
  );
}

function int(val) {
  return Math.round(val);
}

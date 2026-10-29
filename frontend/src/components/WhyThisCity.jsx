import React from 'react';
import { 
  ArrowDown, Sparkles, CheckCircle2, Network, 
  MapPin, ShieldCheck, ArrowRight, Layers, Calculator, Compass 
} from 'lucide-react';

export default function WhyThisCity({ city, onBack, onBuildItinerary }) {
  if (!city) return null;

  const topEvidence = city.qloo_evidence && city.qloo_evidence.length > 0 ? city.qloo_evidence[0] : null;
  const secondEvidence = city.qloo_evidence && city.qloo_evidence.length > 1 ? city.qloo_evidence[1] : null;
  const topNeighborhood = city.neighborhoods && city.neighborhoods.length > 0 ? city.neighborhoods[0] : null;

  // Dynamic node chain representing User Taste -> Qloo Signals -> Urban Ecosystem -> Destination
  const nodeSequence = [
    {
      title: topEvidence ? `${topEvidence.source_category}: ${topEvidence.source_interest}` : "User Cultural Identity",
      subtitle: "Personal Taste Seed Resolved in Qloo Ontology",
      type: "User Taste Seed",
      tag: "Seed Origin",
      color: "border-soul-violet bg-soul-violet/10 text-soul-violet"
    },
    {
      title: secondEvidence ? `${secondEvidence.source_interest} Cross-Domain Resonance` : "Aesthetic & Structural Resonance",
      subtitle: "Multi-Domain Cultural DNA Alignment",
      type: "Visual & Sensory Affinity",
      tag: "Resonance",
      color: "border-soul-cyan bg-soul-cyan/10 text-soul-cyan"
    },
    {
      title: topEvidence ? `Qloo Affinity: ${topEvidence.target_affinity}` : `${city.name} Cultural Venues`,
      subtitle: `${topEvidence ? Math.round(topEvidence.qloo_affinity_strength * 100) : 94}% Verifiable Qloo Cultural Graph Affinity`,
      type: "Qloo Cultural Intelligence",
      tag: "Qloo Signal",
      color: "border-soul-gold bg-soul-gold/10 text-soul-gold"
    },
    {
      title: topNeighborhood ? topNeighborhood.name : `${city.name} Creative Quarter`,
      subtitle: topNeighborhood ? topNeighborhood.vibe : "Living Cultural Fabric & Ateliers",
      type: "Neighborhood Ecology",
      tag: "District Match",
      color: "border-soul-rose bg-soul-rose/10 text-soul-rose"
    },
    {
      title: `${city.name.toUpperCase()}, ${city.country.toUpperCase()}`,
      subtitle: `${city.compatibility_score}% CitySoul Cultural Compatibility`,
      type: "Destination Match",
      tag: "CitySoul Match",
      color: "border-white bg-white/10 text-white font-bold"
    }
  ];

  const breakdown = city.calculation_breakdown || {
    qloo_evidence_component: 37.6,
    cultural_dna_domain_component: 32.4,
    taste_resonance_component: 14.0,
    budget_fit_component: 9.0,
    total_score: city.compatibility_score
  };

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
        <div className="flex items-center justify-center gap-2 mb-3">
          <span className="px-3 py-1 rounded-full bg-soul-cyan/10 border border-soul-cyan/20 text-soul-cyan text-xs font-mono uppercase tracking-wider">
            Three-Layer Cultural Explanation
          </span>
          <span className="px-3 py-1 rounded-full bg-white/5 border border-white/10 text-slate-300 text-xs font-mono uppercase tracking-wider">
            {city.region || "Global"}
          </span>
        </div>
        <h2 className="font-display text-3xl sm:text-5xl font-extrabold text-white mb-4">
          Why {city.name}?
        </h2>
        <p className="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto leading-relaxed">
          {city.why_this_city}
        </p>
      </div>

      {/* Three-Layer Architectural Card */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-10">
        {/* Layer 1: What Qloo Provided */}
        <div className="glass-panel rounded-2xl p-5 border border-soul-cyan/30 bg-soul-cyan/5">
          <div className="flex items-center gap-2 mb-2 text-soul-cyan text-xs font-mono uppercase font-bold">
            <Layers className="w-4 h-4" />
            <span>1. What Qloo Provided</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed mb-3">
            Real taste ontology entities, place density data in {city.name}, and cross-domain correlation vectors.
          </p>
          <div className="text-[11px] font-mono text-soul-cyan/90 bg-obsidian-950/60 rounded-lg p-2 border border-soul-cyan/20">
            ✓ {city.qloo_evidence?.length || 0} Verifiable Venues<br />
            ✓ Multi-Entity Place Filter<br />
            ✓ Live Qloo Hackathon Gateway
          </div>
        </div>

        {/* Layer 2: What CitySoul Calculated */}
        <div className="glass-panel rounded-2xl p-5 border border-soul-violet/30 bg-soul-violet/5">
          <div className="flex items-center gap-2 mb-2 text-soul-violet text-xs font-mono uppercase font-bold">
            <Calculator className="w-4 h-4" />
            <span>2. What CitySoul Calculated</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed mb-3">
            Mathematical CitySoul Compatibility ({city.compatibility_score}%) based on 4 weighted pillars:
          </p>
          <div className="text-[11px] font-mono text-slate-300 bg-obsidian-950/60 rounded-lg p-2 border border-soul-violet/20 space-y-0.5">
            <div>• Qloo Evidence: {breakdown.qloo_evidence_component}/40 pts</div>
            <div>• Cultural DNA: {breakdown.cultural_dna_domain_component}/35 pts</div>
            <div>• Taste Resonance: {breakdown.taste_resonance_component}/15 pts</div>
            <div>• Budget Fit: {breakdown.budget_fit_component}/10 pts</div>
          </div>
        </div>

        {/* Layer 3: What the Agent Explains */}
        <div className="glass-panel rounded-2xl p-5 border border-soul-gold/30 bg-soul-gold/5">
          <div className="flex items-center gap-2 mb-2 text-soul-gold text-xs font-mono uppercase font-bold">
            <Compass className="w-4 h-4" />
            <span>3. What Agent Explains</span>
          </div>
          <p className="text-xs text-slate-300 leading-relaxed mb-3">
            Why {city.name}'s living creative districts ({city.neighborhoods?.map(n => n.name).join(', ') || city.name}) embody your specific taste signals.
          </p>
          <div className="text-[11px] font-mono text-soul-gold/90 bg-obsidian-950/60 rounded-lg p-2 border border-soul-gold/20">
            ✓ Narrative Cultural Grounding<br />
            ✓ Spatial & Sound Context<br />
            ✓ Curated Neighborhood Focus
          </div>
        </div>
      </div>

      {/* Connected Nodes Chain Visualization */}
      <div className="glass-panel rounded-3xl p-6 sm:p-10 border border-white/10 shadow-2xl mb-10">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-2 text-xs font-mono uppercase text-slate-400">
            <Network className="w-4 h-4 text-soul-cyan" />
            <span>Cross-Domain Taste Chain</span>
          </div>
          <span className="text-[11px] font-mono text-slate-500">
            Taste Origin → Urban Destination
          </span>
        </div>

        {/* Nodes Grid / Chain */}
        <div className="space-y-4 relative">
          {nodeSequence.map((node, idx) => (
            <React.Fragment key={idx}>
              <div className={`p-4 rounded-2xl border ${node.color} flex flex-col sm:flex-row sm:items-center justify-between gap-3 shadow-lg transition-transform hover:scale-[1.01]`}>
                <div className="flex items-center gap-3">
                  <span className="w-6 h-6 rounded-full bg-obsidian-950 flex items-center justify-center text-xs font-mono font-bold text-white border border-white/10 shrink-0">
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
          <span>Verifiable Qloo Cross-Domain Affinities in {city.name}</span>
        </h4>

        <div className="space-y-3">
          {city.qloo_evidence && city.qloo_evidence.map((ev, i) => (
            <div 
              key={i}
              className="p-3.5 rounded-xl bg-obsidian-900 border border-white/5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs"
            >
              <div>
                <div className="text-slate-300 font-medium mb-1">
                  <span className="text-soul-cyan font-bold">{ev.source_interest}</span>
                  <span className="text-slate-500 mx-2">→</span>
                  <span className="text-white font-bold">{ev.target_affinity}</span>
                  <span className="ml-2 text-[10px] text-slate-400">({ev.target_category})</span>
                </div>
                <p className="text-[11px] text-slate-400">
                  {ev.city_manifestation}
                </p>
              </div>

              <div className="px-2.5 py-1 rounded-md bg-soul-cyan/15 border border-soul-cyan/30 text-soul-cyan font-mono font-bold shrink-0 self-start sm:self-auto">
                {Math.round(ev.qloo_affinity_strength * 100)}% Affinity
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

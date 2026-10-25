import React from 'react';
import { Dna, ShieldCheck, Sparkles, Layers } from 'lucide-react';

export default function CulturalDNA({ dnaSignals }) {
  if (!dnaSignals || dnaSignals.length === 0) return null;

  return (
    <div className="max-w-5xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-6">
        <div>
          <div className="flex items-center gap-2 text-xs font-mono text-soul-cyan uppercase tracking-wider mb-1">
            <Dna className="w-3.5 h-3.5" />
            Stage 02 — User Profile
          </div>
          <h3 className="font-display text-2xl sm:text-3xl font-bold text-white">
            Your Cultural DNA
          </h3>
        </div>
        <div className="px-3 py-1.5 rounded-lg bg-obsidian-900 border border-white/10 text-xs font-mono text-slate-400">
          <span className="text-white font-semibold">{dnaSignals.length} Pillars</span> Decoded
        </div>
      </div>

      {/* Grid of DNA Signal Bars */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
        {dnaSignals.map((signal, idx) => (
          <div 
            key={signal.category}
            className="glass-panel rounded-xl p-4 border border-white/5 hover:border-soul-cyan/30 transition-all"
          >
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-semibold text-white tracking-wide">
                {signal.category}
              </span>
              <span className="text-xs font-mono font-bold text-soul-cyan">
                {signal.score}%
              </span>
            </div>

            {/* Score Bar */}
            <div className="w-full bg-obsidian-950 h-2 rounded-full overflow-hidden mb-3 border border-white/5">
              <div 
                className="h-full bg-gradient-to-r from-soul-violet via-soul-cyan to-soul-cyan rounded-full transition-all duration-1000 ease-out"
                style={{ width: `${signal.score}%` }}
              ></div>
            </div>

            {/* Dominant Traits */}
            <div className="flex items-center justify-between text-[11px] text-slate-400">
              <div className="flex flex-wrap gap-1.5">
                {signal.dominant_traits.map(trait => (
                  <span 
                    key={trait}
                    className="px-2 py-0.5 rounded bg-white/5 text-slate-300 font-sans"
                  >
                    {trait}
                  </span>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Transparent Labeling note per hackathon requirement */}
      <div className="flex items-center gap-2 p-3 rounded-xl bg-obsidian-900/60 border border-white/5 text-[11px] font-mono text-slate-400">
        <Layers className="w-3.5 h-3.5 text-soul-cyan shrink-0" />
        <span>
          <strong className="text-slate-300">CitySoul Profile Signals:</strong> Internally computed from user selections & semantic extraction to guide Qloo graph traversal. Distinct from raw Qloo place metrics.
        </span>
      </div>
    </div>
  );
}

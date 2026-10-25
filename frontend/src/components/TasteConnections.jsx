import React, { useState } from 'react';
import { Network, Sparkles, HelpCircle, Layers, ArrowRight } from 'lucide-react';

export default function TasteConnections({ graphData, topCityName = "Tokyo" }) {
  const [selectedNode, setSelectedNode] = useState(null);

  const defaultNodes = [
    { id: '1', label: 'Christopher Nolan', category: 'Cinema', level: 'User Seed', desc: 'Neo-noir scale, non-linear architecture, and atmospheric tension.' },
    { id: '2', label: 'Sci-Fi & Cyberpunk', category: 'Cinema Subgenre', level: 'Cultural Bridge', desc: 'High-density urban monoliths illuminated by neon reflections.' },
    { id: '3', label: 'Japanese Metabolism', category: 'Urban Design', level: 'Qloo Affinity', desc: '1960s architectural movement embracing modular capsules and biomimetic urban growth.' },
    { id: '4', label: 'Ura-Harajuku Streetwear', category: 'Fashion Subculture', level: 'Qloo Affinity', desc: 'Understated artisanal denim, technical fabrics, and secret alley boutiques.' },
    { id: '5', label: 'Audiophile Jazz Kissas', category: 'Acoustic Culture', level: 'Sound Sanctuary', desc: 'Subterranean sanctuaries dedicated to custom tube amps and vinyl reverence.' },
    { id: '6', label: `${topCityName} Creative Districts`, category: 'Destination Hub', level: 'Ecosystem Anchor', desc: 'Shimokitazawa, Daikanyama & Shinjuku alleys where these cultural currents converge.' },
  ];

  const defaultEdges = [
    { from: 'Christopher Nolan', to: 'Sci-Fi & Cyberpunk', note: 'Visual World-Building' },
    { from: 'Sci-Fi & Cyberpunk', to: 'Japanese Metabolism', note: 'Spatial Blueprint' },
    { from: 'Japanese Metabolism', to: 'Ura-Harajuku Streetwear', note: 'Design Philosophy' },
    { from: 'Ura-Harajuku Streetwear', to: 'Audiophile Jazz Kissas', note: 'Subcultural Overlap' },
    { from: 'Audiophile Jazz Kissas', to: `${topCityName} Creative Districts`, note: 'Urban Integration' },
  ];

  return (
    <div id="taste-connections" className="max-w-5xl mx-auto px-4 py-8">
      {/* Header */}
      <div className="text-center mb-8">
        <span className="px-3 py-1 rounded-full bg-soul-cyan/10 border border-soul-cyan/20 text-soul-cyan text-xs font-mono uppercase tracking-wider mb-3 inline-block">
          Section 12 — Cross-Domain Discovery
        </span>
        <h2 className="font-display text-3xl sm:text-4xl font-extrabold text-white mb-3">
          Taste Connections
        </h2>
        <p className="text-slate-400 text-sm max-w-xl mx-auto">
          How Qloo's taste graph traverses unseen boundaries between your favorite directors, fashion choices, and cities.
        </p>
      </div>

      {/* Main Interactive Map Card */}
      <div className="glass-panel rounded-3xl p-6 sm:p-8 border border-white/10 shadow-2xl mb-8">
        <div className="flex items-center justify-between text-xs font-mono text-slate-400 mb-6 pb-4 border-b border-white/5">
          <div className="flex items-center gap-2">
            <Network className="w-4 h-4 text-soul-cyan" />
            <span>Interactive Graph Traversal</span>
          </div>
          <span className="text-[11px] text-soul-cyan">
            Click any node to inspect Qloo reasoning
          </span>
        </div>

        {/* Nodes Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 mb-8">
          {defaultNodes.map((node) => {
            const isSelected = selectedNode?.id === node.id;
            return (
              <div
                key={node.id}
                onClick={() => setSelectedNode(node)}
                className={`p-4 rounded-xl border transition-all cursor-pointer ${
                  isSelected
                    ? 'bg-soul-cyan/20 border-soul-cyan shadow-lg shadow-soul-cyan/20'
                    : 'bg-obsidian-900 border-white/10 hover:border-soul-cyan/40 hover:bg-white/5'
                }`}
              >
                <div className="flex items-center justify-between mb-2">
                  <span className="text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-white/5 text-slate-300">
                    {node.level}
                  </span>
                  <span className="text-[10px] font-mono text-soul-cyan">
                    {node.category}
                  </span>
                </div>
                <h4 className="text-sm font-bold text-white mb-1">
                  {node.label}
                </h4>
                <p className="text-xs text-slate-400 line-clamp-2">
                  {node.desc}
                </p>
              </div>
            );
          })}
        </div>

        {/* Edge Flow Diagram */}
        <div className="p-4 rounded-2xl bg-obsidian-950/70 border border-white/5">
          <span className="text-[11px] font-mono text-slate-400 uppercase tracking-wider block mb-3">
            Qloo Discovered Lineage
          </span>
          <div className="flex flex-wrap items-center gap-2 text-xs font-mono">
            {defaultEdges.map((edge, i) => (
              <React.Fragment key={i}>
                <span className="px-2.5 py-1 rounded-md bg-white/5 text-slate-200">
                  {edge.from}
                </span>
                <span className="text-soul-cyan flex items-center gap-1 text-[11px]">
                  <span>→</span>
                  <span className="text-[10px] text-slate-400">({edge.note})</span>
                  <span>→</span>
                </span>
                {i === defaultEdges.length - 1 && (
                  <span className="px-2.5 py-1 rounded-md bg-soul-cyan text-obsidian-950 font-bold">
                    {edge.to}
                  </span>
                )}
              </React.Fragment>
            ))}
          </div>
        </div>

        {/* Node Detail Drawer (if selected) */}
        {selectedNode && (
          <div className="mt-6 p-4 rounded-xl bg-soul-violet/10 border border-soul-violet/30 animate-fade-in flex items-start justify-between gap-4">
            <div>
              <div className="flex items-center gap-2 text-xs font-mono text-soul-cyan mb-1">
                <Sparkles className="w-3.5 h-3.5" />
                <span>Qloo Cultural Node: {selectedNode.label}</span>
              </div>
              <p className="text-xs text-slate-300">
                {selectedNode.desc}
              </p>
            </div>
            <button
              onClick={() => setSelectedNode(null)}
              className="text-xs text-slate-400 hover:text-white px-2 py-1"
            >
              ✕
            </button>
          </div>
        )}
      </div>
    </div>
  );
}

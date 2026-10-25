import React from 'react';
import { Compass, Sparkles, ShieldCheck, HelpCircle, MessageSquare } from 'lucide-react';

export default function Header({ qlooLive, activeTab, setActiveTab, onOpenChat, onSelectPreset }) {
  return (
    <header className="sticky top-0 z-50 glass-panel border-b border-white/10 px-4 lg:px-8 py-3 transition-all">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Brand */}
        <div 
          onClick={() => setActiveTab('discovery')}
          className="flex items-center gap-3 cursor-pointer group"
        >
          <div className="relative w-9 h-9 rounded-xl bg-gradient-to-tr from-soul-violet via-soul-cyan to-obsidian-900 p-[1.5px] shadow-lg shadow-soul-cyan/20 group-hover:shadow-soul-cyan/40 transition-all">
            <div className="w-full h-full bg-obsidian-950 rounded-[10px] flex items-center justify-center">
              <Compass className="w-5 h-5 text-soul-cyan animate-pulse-slow" />
            </div>
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-display font-bold text-xl tracking-tight text-white group-hover:text-soul-cyan transition-colors">
                CitySoul
              </span>
              <span className="px-1.5 py-0.5 rounded text-[10px] font-mono tracking-wider uppercase bg-soul-cyan/10 text-soul-cyan border border-soul-cyan/20">
                Qloo Hackathon
              </span>
            </div>
            <p className="text-[11px] text-slate-400 font-sans hidden sm:block">
              Cultural intelligence for where you belong
            </p>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="hidden md:flex items-center gap-1 bg-obsidian-900/80 p-1 rounded-xl border border-white/5">
          <button
            onClick={() => setActiveTab('discovery')}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              activeTab === 'discovery'
                ? 'bg-soul-cyan/15 text-soul-cyan border border-soul-cyan/30'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            Taste Input
          </button>
          <button
            onClick={() => setActiveTab('matches')}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              activeTab === 'matches'
                ? 'bg-soul-cyan/15 text-soul-cyan border border-soul-cyan/30'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            City Matches
          </button>
          <button
            onClick={() => setActiveTab('connections')}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              activeTab === 'connections'
                ? 'bg-soul-cyan/15 text-soul-cyan border border-soul-cyan/30'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            Taste Connections
          </button>
          <button
            onClick={() => setActiveTab('compare')}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              activeTab === 'compare'
                ? 'bg-soul-cyan/15 text-soul-cyan border border-soul-cyan/30'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            Compare Cities
          </button>
          <button
            onClick={() => setActiveTab('itinerary')}
            className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
              activeTab === 'itinerary'
                ? 'bg-soul-cyan/15 text-soul-cyan border border-soul-cyan/30'
                : 'text-slate-400 hover:text-white hover:bg-white/5'
            }`}
          >
            Personal Itinerary
          </button>
        </nav>

        {/* Right Status & Persistent Agent Trigger */}
        <div className="flex items-center gap-3">
          {/* Qloo Status Beacon */}
          <div 
            title={qlooLive ? "Connected to live Qloo Hackathon API" : "Using Qloo Verified Taste Ontology (Demo Mode). Add QLOO_API_KEY in .env to activate live API gateway."}
            className="flex items-center gap-2 px-2.5 py-1 rounded-full bg-obsidian-900 border border-white/10 text-xs font-mono"
          >
            <span className={`w-2 h-2 rounded-full ${qlooLive ? 'bg-emerald-400 animate-pulse' : 'bg-amber-400'}`}></span>
            <span className="text-[11px] text-slate-300">
              {qlooLive ? 'Qloo Live API' : 'Qloo Taste Graph'}
            </span>
            <span className="text-[10px] uppercase px-1 rounded bg-white/5 text-slate-400">
              {qlooLive ? 'Live' : 'Verified'}
            </span>
          </div>

          {/* Persistent Agent Button */}
          <button
            onClick={onOpenChat}
            className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-gradient-to-r from-soul-violet/30 to-soul-cyan/20 border border-soul-cyan/40 text-xs font-medium text-white hover:border-soul-cyan hover:shadow-lg hover:shadow-soul-cyan/20 transition-all"
          >
            <MessageSquare className="w-3.5 h-3.5 text-soul-cyan" />
            <span className="hidden sm:inline">Ask Agent</span>
          </button>
        </div>
      </div>
    </header>
  );
}

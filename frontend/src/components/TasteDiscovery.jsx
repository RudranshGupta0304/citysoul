import React, { useState } from 'react';
import { 
  Music, Film, UtensilsCrossed, Shirt, Landmark, Coffee, 
  Sparkles, Plus, X, IndianRupee, Calendar, Send 
} from 'lucide-react';

const CATEGORIES = [
  {
    id: 'music',
    name: 'Music',
    icon: Music,
    color: 'text-soul-violet',
    suggestions: ['Techno', 'Indie Rock', 'Underground Electronic', 'Jazz Kissa', 'Ambient', 'Hip-Hop', 'Post-Punk', 'K-Pop']
  },
  {
    id: 'film',
    name: 'Film & Directors',
    icon: Film,
    color: 'text-soul-cyan',
    suggestions: ['Christopher Nolan', 'Sci-Fi', 'Blade Runner', 'Neo-Noir', 'Denis Villeneuve', 'Wong Kar-wai', 'Cyberpunk', 'Art House']
  },
  {
    id: 'food',
    name: 'Food & Dining',
    icon: UtensilsCrossed,
    color: 'text-soul-gold',
    suggestions: ['Japanese', 'Ramen Alleys', 'Omakase', 'Street Food', 'Korean BBQ', 'Natural Wine', 'Fermentation', 'Late-Night Soba']
  },
  {
    id: 'fashion',
    name: 'Fashion & Aesthetic',
    icon: Shirt,
    color: 'text-soul-rose',
    suggestions: ['Streetwear', 'Minimalist', 'Techwear', 'Monochrome', 'Vintage Denim', 'Avant-Garde', 'Archival Fashion']
  },
  {
    id: 'interests',
    name: 'Interests & Arts',
    icon: Landmark,
    color: 'text-soul-cyan',
    suggestions: ['Architecture', 'Street Photography', 'Brutalism', 'Analog Vinyl Crates', 'Design Books', 'Contemporary Art']
  },
  {
    id: 'lifestyle',
    name: 'Lifestyle & Rhythm',
    icon: Coffee,
    color: 'text-soul-emerald',
    suggestions: ['Late-Night Cafés', 'Underground Sound', 'Quiet Alleys', 'Third-Wave Coffee', 'Independent Bookshops', '24hr Neon']
  }
];

export default function TasteDiscovery({ tasteInput, setTasteInput, onSubmit, isProcessing }) {
  const [activeCategory, setActiveCategory] = useState('film');
  const [customTag, setCustomTag] = useState('');

  const toggleTag = (catId, tag) => {
    setTasteInput(prev => {
      const currentList = prev[catId] || [];
      const exists = currentList.includes(tag);
      return {
        ...prev,
        [catId]: exists 
          ? currentList.filter(t => t !== tag)
          : [...currentList, tag]
      };
    });
  };

  const handleAddCustomTag = (e) => {
    e.preventDefault();
    if (!customTag.trim()) return;
    const clean = customTag.trim();
    setTasteInput(prev => ({
      ...prev,
      [activeCategory]: [...(prev[activeCategory] || []), clean]
    }));
    setCustomTag('');
  };

  const currentCategory = CATEGORIES.find(c => c.id === activeCategory);

  return (
    <div id="taste-discovery" className="max-w-5xl mx-auto px-4 py-8">
      {/* Section Header */}
      <div className="text-center mb-8">
        <span className="text-xs font-mono uppercase tracking-widest text-soul-cyan mb-2 block">
          Stage 01 — Discover Me
        </span>
        <h2 className="font-display text-2xl sm:text-4xl font-bold text-white mb-3">
          Decode Your Cultural DNA
        </h2>
        <p className="text-slate-400 text-sm sm:text-base max-w-xl mx-auto">
          CitySoul doesn't ask for a destination. Share the artists, aesthetics, and rituals you care about. Qloo's taste graph will trace where they intersect in the world.
        </p>
      </div>

      <div className="glass-panel rounded-2xl p-6 sm:p-8 border border-white/10 shadow-2xl">
        {/* Category Tabs */}
        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2 mb-6">
          {CATEGORIES.map(cat => {
            const Icon = cat.icon;
            const count = (tasteInput[cat.id] || []).length;
            const isActive = activeCategory === cat.id;
            return (
              <button
                key={cat.id}
                onClick={() => setActiveCategory(cat.id)}
                className={`flex flex-col items-center justify-center p-3 rounded-xl border transition-all ${
                  isActive
                    ? 'bg-white/10 border-soul-cyan/50 text-white shadow-lg shadow-soul-cyan/10'
                    : 'bg-obsidian-900/50 border-white/5 text-slate-400 hover:text-white hover:bg-white/5'
                }`}
              >
                <Icon className={`w-5 h-5 mb-1.5 ${cat.color}`} />
                <span className="text-xs font-medium text-center">{cat.name}</span>
                {count > 0 && (
                  <span className="mt-1 px-1.5 py-0.2 rounded-full text-[10px] font-mono bg-soul-cyan/20 text-soul-cyan border border-soul-cyan/30">
                    {count}
                  </span>
                )}
              </button>
            );
          })}
        </div>

        {/* Active Category Content */}
        <div className="bg-obsidian-900/60 rounded-xl p-5 border border-white/5 mb-6">
          <div className="flex items-center justify-between mb-4">
            <div className="flex items-center gap-2">
              <span className="text-xs font-mono text-slate-400 uppercase">Selected in {currentCategory.name}:</span>
              <span className="text-xs font-bold text-soul-cyan">
                {(tasteInput[activeCategory] || []).length} items
              </span>
            </div>
            
            {/* Custom Tag Input */}
            <form onSubmit={handleAddCustomTag} className="flex items-center gap-1.5">
              <input
                type="text"
                placeholder={`Add custom ${currentCategory.name.toLowerCase()}...`}
                value={customTag}
                onChange={(e) => setCustomTag(e.target.value)}
                className="px-3 py-1.5 rounded-lg bg-obsidian-950 border border-white/10 text-xs text-white focus:outline-none focus:border-soul-cyan placeholder:text-slate-600 w-44 sm:w-56"
              />
              <button
                type="submit"
                className="p-1.5 rounded-lg bg-soul-cyan/20 text-soul-cyan border border-soul-cyan/40 hover:bg-soul-cyan hover:text-obsidian-950 transition-all"
              >
                <Plus className="w-4 h-4" />
              </button>
            </form>
          </div>

          {/* Tag Pills */}
          <div className="flex flex-wrap gap-2">
            {currentCategory.suggestions.map(tag => {
              const isSelected = (tasteInput[activeCategory] || []).includes(tag);
              return (
                <button
                  key={tag}
                  onClick={() => toggleTag(activeCategory, tag)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-medium transition-all flex items-center gap-1.5 ${
                    isSelected
                      ? 'bg-soul-cyan text-obsidian-950 font-semibold shadow-md shadow-soul-cyan/20'
                      : 'bg-obsidian-850 text-slate-300 border border-white/5 hover:border-white/20 hover:text-white'
                  }`}
                >
                  <span>{tag}</span>
                  {isSelected && <span className="text-[10px]">✕</span>}
                </button>
              );
            })}

            {/* Custom entered tags that weren't in default suggestions */}
            {(tasteInput[activeCategory] || [])
              .filter(t => !currentCategory.suggestions.includes(t))
              .map(t => (
                <button
                  key={t}
                  onClick={() => toggleTag(activeCategory, t)}
                  className="px-3 py-1.5 rounded-lg text-xs font-medium bg-soul-violet text-white shadow-md shadow-soul-violet/20 flex items-center gap-1.5"
                >
                  <span>{t}</span>
                  <span className="text-[10px]">✕</span>
                </button>
              ))}
          </div>
        </div>

        {/* Natural Language Free-Text Section */}
        <div className="mb-6">
          <label className="block text-xs font-mono uppercase text-slate-400 mb-2">
            Or Describe Your Taste in Natural Language
          </label>
          <div className="relative">
            <textarea
              rows={3}
              placeholder="e.g. I love Christopher Nolan films, Japanese food, streetwear, architecture, photography, techno and late-night cafés."
              value={tasteInput.free_text || ''}
              onChange={(e) => setTasteInput(prev => ({ ...prev, free_text: e.target.value }))}
              className="w-full px-4 py-3 rounded-xl bg-obsidian-900 border border-white/10 text-white text-sm focus:outline-none focus:border-soul-cyan placeholder:text-slate-600 transition-all resize-none"
            />
            <div className="absolute bottom-2.5 right-3 text-[11px] font-mono text-slate-500">
              Agent Semantic Parser Enabled
            </div>
          </div>
        </div>

        {/* Constraints: Budget & Duration */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
          <div className="p-4 rounded-xl bg-obsidian-900/60 border border-white/5">
            <div className="flex items-center justify-between text-xs font-mono text-slate-400 mb-2">
              <span className="flex items-center gap-1.5">
                <IndianRupee className="w-3.5 h-3.5 text-soul-gold" />
                Trip Budget (INR)
              </span>
              <span className="text-white font-bold">₹{(tasteInput.budget || 50000).toLocaleString('en-IN')}</span>
            </div>
            <input
              type="range"
              min="20000"
              max="200000"
              step="5000"
              value={tasteInput.budget || 50000}
              onChange={(e) => setTasteInput(prev => ({ ...prev, budget: Number(e.target.value) }))}
              className="w-full accent-soul-cyan bg-obsidian-950 h-1.5 rounded-lg cursor-pointer"
            />
            <div className="flex justify-between text-[10px] font-mono text-slate-500 mt-1">
              <span>₹20,000</span>
              <span>₹1,00,000</span>
              <span>₹2,00,000</span>
            </div>
          </div>

          <div className="p-4 rounded-xl bg-obsidian-900/60 border border-white/5">
            <div className="flex items-center justify-between text-xs font-mono text-slate-400 mb-2">
              <span className="flex items-center gap-1.5">
                <Calendar className="w-3.5 h-3.5 text-soul-cyan" />
                Duration (Days)
              </span>
              <span className="text-white font-bold">{tasteInput.duration_days || 5} Days</span>
            </div>
            <input
              type="range"
              min="3"
              max="14"
              step="1"
              value={tasteInput.duration_days || 5}
              onChange={(e) => setTasteInput(prev => ({ ...prev, duration_days: Number(e.target.value) }))}
              className="w-full accent-soul-cyan bg-obsidian-950 h-1.5 rounded-lg cursor-pointer"
            />
            <div className="flex justify-between text-[10px] font-mono text-slate-500 mt-1">
              <span>3 Days (Weekend)</span>
              <span>7 Days (Week)</span>
              <span>14 Days (Immersion)</span>
            </div>
          </div>
        </div>

        {/* Primary Find My City Button */}
        <button
          onClick={onSubmit}
          disabled={isProcessing}
          className="w-full py-4 rounded-xl bg-gradient-to-r from-soul-cyan via-soul-violet to-soul-cyan text-obsidian-950 font-bold text-base uppercase tracking-wider flex items-center justify-center gap-3 hover:opacity-95 shadow-xl shadow-soul-cyan/25 transition-all disabled:opacity-50 cursor-pointer"
        >
          {isProcessing ? (
            <>
              <div className="w-5 h-5 border-2 border-obsidian-950 border-t-transparent rounded-full animate-spin"></div>
              <span>Agent Processing Taste Graph...</span>
            </>
          ) : (
            <>
              <Sparkles className="w-5 h-5 text-obsidian-950" />
              <span>Find My City</span>
            </>
          )}
        </button>
      </div>
    </div>
  );
}

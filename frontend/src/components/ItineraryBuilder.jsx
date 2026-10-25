import React, { useState } from 'react';
import { 
  Calendar, Clock, MapPin, IndianRupee, Sparkles, 
  ArrowLeft, Download, RefreshCw, CheckCircle2 
} from 'lucide-react';
import { generateItinerary } from '../services/api';

export default function ItineraryBuilder({ city, itinerary, onBack, onUpdateItinerary }) {
  const [loading, setLoading] = useState(false);
  const [selectedDay, setSelectedDay] = useState(1);
  const [budget, setBudget] = useState(itinerary?.total_budget_inr || 50000);
  const [duration, setDuration] = useState(itinerary?.duration_days || 5);

  const handleRegenerate = async () => {
    if (!city) return;
    setLoading(true);
    try {
      const updated = await generateItinerary({
        city_id: city.id,
        duration_days: duration,
        budget: budget,
        travel_style: "Cultural Immersion & Night Exploration"
      });
      if (onUpdateItinerary) onUpdateItinerary(updated);
    } catch (e) {
      console.error("Failed to regenerate itinerary", e);
    } finally {
      setLoading(false);
    }
  };

  if (!itinerary) return null;

  const currentDayData = itinerary.days.find(d => d.day_number === selectedDay) || itinerary.days[0];

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
        <div className="flex items-center gap-2 text-xs font-mono text-soul-gold uppercase">
          <Calendar className="w-3.5 h-3.5" />
          <span>Stage 04 — Curated Experience</span>
        </div>
      </div>

      {/* Header */}
      <div className="text-center mb-8">
        <span className="px-3 py-1 rounded-full bg-soul-gold/10 border border-soul-gold/20 text-soul-gold text-xs font-mono uppercase tracking-wider mb-3 inline-block">
          Personalized Cultural Itinerary
        </span>
        <h2 className="font-display text-3xl sm:text-5xl font-extrabold text-white mb-3">
          {itinerary.duration_days} Days in {itinerary.city_name}
        </h2>
        <p className="text-slate-400 text-sm max-w-xl mx-auto">
          Tailored to your architectural curiosity, underground sound preferences, and culinary palates.
        </p>
      </div>

      {/* Constraints Bar */}
      <div className="glass-panel rounded-2xl p-4 sm:p-5 border border-white/10 mb-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex flex-wrap items-center gap-4 text-xs font-mono text-slate-300">
          <div className="flex items-center gap-1.5">
            <IndianRupee className="w-4 h-4 text-soul-gold" />
            <span>Budget: <strong className="text-white">₹{budget.toLocaleString('en-IN')}</strong></span>
          </div>
          <span className="text-slate-600">•</span>
          <div className="flex items-center gap-1.5">
            <Calendar className="w-4 h-4 text-soul-cyan" />
            <span>Pacing: <strong className="text-white">{duration} Days</strong></span>
          </div>
          <span className="text-slate-600">•</span>
          <div className="flex items-center gap-1.5">
            <Sparkles className="w-4 h-4 text-soul-violet" />
            <span>Style: <strong className="text-white">{itinerary.travel_style}</strong></span>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <button
            onClick={handleRegenerate}
            disabled={loading}
            className="px-3.5 py-1.5 rounded-xl bg-obsidian-900 hover:bg-white/10 border border-white/10 text-xs text-slate-300 hover:text-white flex items-center gap-1.5 transition-all cursor-pointer disabled:opacity-50"
          >
            <RefreshCw className={`w-3.5 h-3.5 text-soul-cyan ${loading ? 'animate-spin' : ''}`} />
            <span>Regenerate</span>
          </button>
        </div>
      </div>

      {/* Day Selector Buttons */}
      <div className="flex items-center gap-2 overflow-x-auto pb-3 mb-6 scrollbar-none">
        {itinerary.days.map((day) => {
          const isActive = day.day_number === selectedDay;
          return (
            <button
              key={day.day_number}
              onClick={() => setSelectedDay(day.day_number)}
              className={`px-4 py-2.5 rounded-xl text-xs font-medium whitespace-nowrap transition-all flex items-center gap-2 ${
                isActive
                  ? 'bg-soul-cyan text-obsidian-950 font-bold shadow-lg shadow-soul-cyan/20'
                  : 'glass-panel text-slate-400 hover:text-white hover:border-white/20'
              }`}
            >
              <span>DAY 0{day.day_number}</span>
              <span className={`text-[10px] ${isActive ? 'text-obsidian-900 font-semibold' : 'text-slate-500'}`}>
                {day.neighborhood_focus.split(' ')[0]}
              </span>
            </button>
          );
        })}
      </div>

      {/* Active Day Detail Card */}
      {currentDayData && (
        <div className="glass-panel rounded-3xl p-6 sm:p-8 border border-white/10 shadow-2xl mb-8">
          {/* Day Header */}
          <div className="mb-6 pb-4 border-b border-white/10 flex flex-col sm:flex-row sm:items-center justify-between gap-2">
            <div>
              <span className="text-xs font-mono text-soul-cyan uppercase block mb-1">
                Day 0{currentDayData.day_number} Focus
              </span>
              <h3 className="font-display text-2xl font-bold text-white">
                {currentDayData.theme}
              </h3>
            </div>
            <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
              <MapPin className="w-3.5 h-3.5 text-soul-rose" />
              <span>{currentDayData.neighborhood_focus}</span>
            </div>
          </div>

          {/* Activities Timeline */}
          <div className="space-y-4">
            {currentDayData.activities.map((act, idx) => (
              <div 
                key={idx}
                className="p-5 rounded-2xl bg-obsidian-900/80 border border-white/5 hover:border-soul-cyan/30 transition-all flex flex-col sm:flex-row sm:items-start justify-between gap-4"
              >
                <div className="space-y-1.5 flex-1">
                  <div className="flex items-center gap-2 text-xs font-mono text-slate-400">
                    <Clock className="w-3.5 h-3.5 text-soul-cyan" />
                    <span>{act.time_slot}</span>
                    <span>•</span>
                    <span className="px-2 py-0.5 rounded bg-white/5 text-slate-300">
                      {act.neighborhood}
                    </span>
                    <span className="px-2 py-0.5 rounded bg-soul-violet/20 text-soul-violet">
                      {act.category}
                    </span>
                  </div>

                  <h4 className="text-base font-bold text-white">
                    {act.title}
                  </h4>

                  <p className="text-xs sm:text-sm text-slate-300 leading-relaxed">
                    {act.description}
                  </p>

                  <div className="pt-2 flex items-center gap-1.5 text-xs text-soul-cyan font-mono">
                    <Sparkles className="w-3.5 h-3.5 shrink-0" />
                    <span>{act.cultural_connection}</span>
                  </div>
                </div>

                <div className="text-right shrink-0 self-start sm:self-auto bg-obsidian-950 px-3 py-1.5 rounded-lg border border-white/5">
                  <span className="text-[10px] font-mono text-slate-500 block uppercase">
                    Est. Cost
                  </span>
                  <span className="text-xs font-mono font-bold text-soul-gold">
                    ₹{act.estimated_cost_inr.toLocaleString('en-IN')}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Cultural Notes Footer */}
      <div className="p-4 rounded-xl bg-obsidian-900 border border-white/5 text-xs text-slate-400 font-mono flex items-center gap-3">
        <CheckCircle2 className="w-4 h-4 text-soul-cyan shrink-0" />
        <span>{itinerary.cultural_notes}</span>
      </div>
    </div>
  );
}

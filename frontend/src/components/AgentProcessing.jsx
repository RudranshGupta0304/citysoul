import React, { useState, useEffect } from 'react';
import { CheckCircle2, CircleDashed, Cpu, Network, Sparkles } from 'lucide-react';

const STEPS = [
  {
    id: 'step_1',
    label: 'Understanding your preferences...',
    detail: 'Parsing music, cinema, culinary, and architectural seeds'
  },
  {
    id: 'step_2',
    label: 'Mapping your cultural profile...',
    detail: 'Calculating 8-pillar Cultural DNA and aesthetic weights'
  },
  {
    id: 'step_3',
    label: 'Exploring cross-domain affinities...',
    detail: 'Tracing indirect bridges across sonic, visual & spatial dimensions'
  },
  {
    id: 'step_4',
    label: 'Consulting Qloo...',
    detail: 'Querying Qloo Cultural Intelligence live taste graph and place density'
  },
  {
    id: 'step_5',
    label: 'Comparing global candidate cities...',
    detail: 'Evaluating cultural ecosystem alignment and neighborhood resonance worldwide'
  },
  {
    id: 'step_6',
    label: 'Finding your strongest matches...',
    detail: 'Finalizing CitySoul compatibility scores & tailored narratives'
  }
];

export default function AgentProcessing({ onComplete, isReady = false }) {
  const [currentStepIndex, setCurrentStepIndex] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentStepIndex(prev => {
        if (prev < STEPS.length - 1) {
          return prev + 1;
        }
        return prev;
      });
    }, 600);

    return () => clearInterval(interval);
  }, []);

  // When backend data is ready and minimum steps reached, smoothly complete
  useEffect(() => {
    if (isReady && currentStepIndex >= 3) {
      const timer = setTimeout(() => {
        if (onComplete) onComplete();
      }, 500);
      return () => clearTimeout(timer);
    }
  }, [isReady, currentStepIndex, onComplete]);

  return (
    <div className="max-w-xl mx-auto px-4 py-16 text-center animate-fade-in">
      {/* Central Pulsing Brain / Graph Icon */}
      <div className="relative w-24 h-24 mx-auto mb-8 flex items-center justify-center">
        <div className="absolute inset-0 rounded-full bg-soul-cyan/20 animate-ping"></div>
        <div className="absolute inset-2 rounded-full bg-soul-violet/30 animate-pulse"></div>
        <div className="relative w-16 h-16 rounded-2xl glass-panel border border-soul-cyan/40 flex items-center justify-center shadow-xl shadow-soul-cyan/20">
          <Network className="w-8 h-8 text-soul-cyan animate-spin-slow" />
        </div>
      </div>

      <h3 className="font-display text-2xl font-bold text-white mb-2">
        CitySoul Agent at Work
      </h3>
      <p className="text-slate-400 text-sm mb-8">
        Traversing Qloo's cultural taste graph to discover your urban home
      </p>

      {/* Step List */}
      <div className="glass-panel rounded-2xl p-6 border border-white/10 text-left space-y-3.5 shadow-2xl">
        {STEPS.map((step, idx) => {
          const isDone = idx < currentStepIndex || (idx === currentStepIndex && isReady);
          const isCurrent = idx === currentStepIndex && !isReady;

          return (
            <div 
              key={step.id} 
              className={`flex items-start gap-3 transition-all duration-300 ${
                isDone || isCurrent ? 'opacity-100' : 'opacity-30'
              }`}
            >
              <div className="mt-0.5">
                {isDone ? (
                  <CheckCircle2 className="w-4 h-4 text-soul-cyan shrink-0 animate-scale" />
                ) : (
                  <CircleDashed className={`w-4 h-4 shrink-0 ${isCurrent ? 'text-soul-cyan animate-spin' : 'text-slate-500'}`} />
                )}
              </div>
              <div className="flex-1">
                <div className="flex items-center justify-between">
                  <span className={`text-xs font-mono font-medium ${isCurrent ? 'text-soul-cyan' : isDone ? 'text-white' : 'text-slate-500'}`}>
                    {step.label}
                  </span>
                  {isDone && (
                    <span className="text-[10px] font-mono text-soul-cyan/80">✓</span>
                  )}
                </div>
                {(isCurrent || (idx === currentStepIndex && isReady)) && (
                  <p className="text-[11px] text-slate-400 mt-0.5 font-sans animate-fade-in">
                    {step.detail}
                  </p>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

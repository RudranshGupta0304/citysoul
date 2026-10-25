import React, { useEffect, useRef } from 'react';
import { ArrowRight, Sparkles, Network, Zap } from 'lucide-react';

export default function Hero({ onStartDiscovery, onSelectPreset, presets }) {
  const canvasRef = useRef(null);

  // Subtle animated cultural graph canvas background
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let animationFrameId;

    const resize = () => {
      canvas.width = canvas.parentElement.offsetWidth;
      canvas.height = canvas.parentElement.offsetHeight;
    };
    resize();
    window.addEventListener('resize', resize);

    // Nodes representing cultural entities
    const nodes = Array.from({ length: 32 }, () => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4,
      radius: Math.random() * 2 + 1.5,
      color: Math.random() > 0.5 ? 'rgba(0, 229, 255, 0.6)' : 'rgba(138, 43, 226, 0.6)',
    }));

    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Draw connecting edges
      for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
          const dx = nodes[i].x - nodes[j].x;
          const dy = nodes[i].y - nodes[j].y;
          const dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 120) {
            ctx.beginPath();
            ctx.moveTo(nodes[i].x, nodes[i].y);
            ctx.lineTo(nodes[j].x, nodes[j].y);
            ctx.strokeStyle = `rgba(0, 229, 255, ${0.15 * (1 - dist / 120)})`;
            ctx.lineWidth = 0.8;
            ctx.stroke();
          }
        }
      }

      // Draw and update nodes
      nodes.forEach((node) => {
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fillStyle = node.color;
        ctx.fill();

        node.x += node.vx;
        node.y += node.vy;

        if (node.x < 0 || node.x > canvas.width) node.vx *= -1;
        if (node.y < 0 || node.y > canvas.height) node.vy *= -1;
      });

      animationFrameId = requestAnimationFrame(draw);
    };

    draw();

    return () => {
      window.removeEventListener('resize', resize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return (
    <div className="relative overflow-hidden pt-12 pb-16 lg:pt-20 lg:pb-24 border-b border-white/5 bg-gradient-to-b from-obsidian-950 via-obsidian-900 to-obsidian-950">
      {/* Dynamic Graph Canvas */}
      <canvas 
        ref={canvasRef} 
        className="absolute inset-0 pointer-events-none opacity-50 z-0" 
      />

      {/* Radial atmospheric glow */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 w-[600px] h-[300px] bg-gradient-to-r from-soul-violet/20 via-soul-cyan/15 to-transparent blur-[120px] pointer-events-none"></div>

      <div className="relative z-10 max-w-5xl mx-auto px-4 text-center">
        {/* Hackathon Badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-soul-cyan/10 border border-soul-cyan/20 text-soul-cyan text-xs font-mono uppercase tracking-wider mb-6 animate-pulse-slow">
          <Sparkles className="w-3.5 h-3.5" />
          Powered by Qloo Cultural Intelligence
        </div>

        {/* Editorial Heading */}
        <h1 className="font-display font-extrabold text-4xl sm:text-6xl lg:text-7xl tracking-tight text-white leading-[1.08] mb-6">
          Find the city that <br className="hidden sm:inline" />
          <span className="text-gradient-cyan">feels like you.</span>
        </h1>

        {/* Subtitle */}
        <p className="max-w-2xl mx-auto text-slate-300 text-base sm:text-lg lg:text-xl font-normal leading-relaxed mb-8">
          Generic travel tools tell you what's popular. CitySoul uses Qloo's cross-domain taste graph to discover where your architectural aesthetic, cinema palate, and underground passions genuinely belong.
        </p>

        {/* Action CTAs */}
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 mb-12">
          <button
            onClick={onStartDiscovery}
            className="w-full sm:w-auto px-7 py-3.5 rounded-xl bg-gradient-to-r from-soul-cyan to-soul-violet text-obsidian-950 font-bold text-sm sm:text-base flex items-center justify-center gap-2 hover:opacity-90 hover:shadow-xl hover:shadow-soul-cyan/30 transition-all cursor-pointer"
          >
            <span>Discover My City</span>
            <ArrowRight className="w-4 h-4 text-obsidian-950" />
          </button>
          <a
            href="#taste-connections"
            className="w-full sm:w-auto px-6 py-3.5 rounded-xl glass-panel text-slate-200 font-medium text-sm sm:text-base flex items-center justify-center gap-2 hover:border-soul-cyan/40 hover:text-white transition-all"
          >
            <Network className="w-4 h-4 text-soul-cyan" />
            <span>How Taste Matching Works</span>
          </a>
        </div>

        {/* One-Click Presets for Hackathon Judges */}
        <div className="pt-6 border-t border-white/10 max-w-3xl mx-auto">
          <div className="flex items-center justify-center gap-2 text-xs font-mono text-slate-400 uppercase tracking-wider mb-3">
            <Zap className="w-3.5 h-3.5 text-soul-gold" />
            <span>Instant Test Presets for Evaluators</span>
          </div>
          <div className="flex flex-wrap items-center justify-center gap-2">
            {presets.map((preset) => (
              <button
                key={preset.id}
                onClick={() => onSelectPreset(preset)}
                className="px-3 py-1.5 rounded-lg bg-obsidian-850 hover:bg-soul-cyan/15 border border-white/10 hover:border-soul-cyan/40 text-xs text-slate-300 hover:text-soul-cyan transition-all flex items-center gap-1.5"
              >
                <span className="font-medium">{preset.title}</span>
                <span className="text-[10px] text-slate-500">→</span>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

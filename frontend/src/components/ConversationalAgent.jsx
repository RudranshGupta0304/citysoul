import React, { useState, useRef, useEffect } from 'react';
import { MessageSquare, X, Send, Sparkles, User, Bot, CornerDownLeft } from 'lucide-react';
import { sendAgentMessage } from '../services/api';

const QUICK_PROMPTS = [
  "Why Tokyo instead of Seoul?",
  "What if I only have ₹30,000?",
  "I don't like crowded places.",
  "What if I care more about nightlife?"
];

export default function ConversationalAgent({ isOpen, onClose, currentCityId, profileId, onBudgetAdjusted }) {
  const [messages, setMessages] = useState([
    {
      role: 'assistant',
      content: "Hello! I am your CitySoul Cultural Intelligence Agent. I reason continuously over your taste profile and Qloo's taste graph. Ask me anything—like comparing cities, refining budget constraints, or uncovering quiet architectural enclaves."
    }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const scrollRef = useRef(null);

  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
    }
  }, [messages, isTyping]);

  const handleSend = async (textToSend) => {
    const queryText = textToSend || input;
    if (!queryText.trim()) return;

    const userMessage = { role: 'user', content: queryText };
    setMessages(prev => [...prev, userMessage]);
    if (!textToSend) setInput('');
    setIsTyping(true);

    try {
      const response = await sendAgentMessage({
        message: queryText,
        city_id: currentCityId || 'tokyo',
        profile_id: profileId,
        history: messages.slice(-4)
      });

      setMessages(prev => [...prev, {
        role: 'assistant',
        content: response.reply
      }]);

      if (response.action_type === 'adjust_budget' && response.data?.suggested_budget && onBudgetAdjusted) {
        onBudgetAdjusted(response.data.suggested_budget);
      }
    } catch (err) {
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: "I ran into a temporary hiccup communicating with the cultural reasoning service. Please check that the CitySoul backend is active."
      }]);
    } finally {
      setIsTyping(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-y-0 right-0 z-50 w-full sm:w-[440px] glass-panel border-l border-white/10 shadow-2xl flex flex-col justify-between bg-obsidian-950/95 backdrop-blur-2xl">
      {/* Header */}
      <div className="p-4 border-b border-white/10 flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-xl bg-soul-cyan/20 border border-soul-cyan/40 flex items-center justify-center">
            <Bot className="w-4 h-4 text-soul-cyan" />
          </div>
          <div>
            <h4 className="text-sm font-bold text-white flex items-center gap-1.5">
              <span>CitySoul Agent</span>
              <span className="w-2 h-2 rounded-full bg-emerald-400"></span>
            </h4>
            <p className="text-[10px] font-mono text-slate-400">
              Qloo-augmented reasoning
            </p>
          </div>
        </div>

        <button
          onClick={onClose}
          className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-white/5 transition-all"
        >
          <X className="w-5 h-5" />
        </button>
      </div>

      {/* Messages Scroll Area */}
      <div ref={scrollRef} className="flex-1 p-4 overflow-y-auto space-y-4">
        {messages.map((msg, idx) => {
          const isUser = msg.role === 'user';
          return (
            <div
              key={idx}
              className={`flex gap-3 ${isUser ? 'justify-end' : 'justify-start'}`}
            >
              {!isUser && (
                <div className="w-7 h-7 rounded-lg bg-soul-cyan/15 border border-soul-cyan/30 flex items-center justify-center shrink-0 mt-0.5">
                  <Sparkles className="w-3.5 h-3.5 text-soul-cyan" />
                </div>
              )}

              <div
                className={`max-w-[85%] p-3.5 rounded-2xl text-xs sm:text-sm leading-relaxed ${
                  isUser
                    ? 'bg-soul-cyan text-obsidian-950 font-medium rounded-tr-none'
                    : 'bg-obsidian-900 border border-white/10 text-slate-200 rounded-tl-none whitespace-pre-line'
                }`}
              >
                {msg.content}
              </div>

              {isUser && (
                <div className="w-7 h-7 rounded-lg bg-white/10 flex items-center justify-center shrink-0 mt-0.5">
                  <User className="w-3.5 h-3.5 text-white" />
                </div>
              )}
            </div>
          );
        })}

        {isTyping && (
          <div className="flex gap-3 justify-start">
            <div className="w-7 h-7 rounded-lg bg-soul-cyan/15 border border-soul-cyan/30 flex items-center justify-center shrink-0">
              <Sparkles className="w-3.5 h-3.5 text-soul-cyan animate-spin" />
            </div>
            <div className="p-3 rounded-2xl bg-obsidian-900 border border-white/10 text-xs text-slate-400 font-mono">
              Reasoning over cultural taste graph...
            </div>
          </div>
        )}
      </div>

      {/* Quick Prompts */}
      <div className="p-3 border-t border-white/5 bg-obsidian-900/50">
        <span className="text-[10px] font-mono text-slate-500 uppercase block mb-1.5">
          Suggested Cultural Inquiries
        </span>
        <div className="flex flex-wrap gap-1.5">
          {QUICK_PROMPTS.map((p) => (
            <button
              key={p}
              onClick={() => handleSend(p)}
              className="text-[11px] px-2.5 py-1 rounded-lg bg-obsidian-850 hover:bg-soul-cyan/20 border border-white/10 hover:border-soul-cyan/40 text-slate-300 hover:text-soul-cyan transition-all text-left"
            >
              {p}
            </button>
          ))}
        </div>
      </div>

      {/* Input Box */}
      <div className="p-4 border-t border-white/10 bg-obsidian-950">
        <form
          onSubmit={(e) => {
            e.preventDefault();
            handleSend();
          }}
          className="flex items-center gap-2"
        >
          <input
            type="text"
            placeholder="Ask agent about taste, budget, cities..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="flex-1 px-3.5 py-2.5 rounded-xl bg-obsidian-900 border border-white/10 text-xs sm:text-sm text-white focus:outline-none focus:border-soul-cyan placeholder:text-slate-600"
          />
          <button
            type="submit"
            disabled={!input.trim() || isTyping}
            className="p-2.5 rounded-xl bg-soul-cyan text-obsidian-950 hover:opacity-90 disabled:opacity-40 transition-all cursor-pointer"
          >
            <Send className="w-4 h-4" />
          </button>
        </form>
      </div>
    </div>
  );
}

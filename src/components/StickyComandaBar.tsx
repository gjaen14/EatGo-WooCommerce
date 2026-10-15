import React from 'react';
import { ShoppingBag, ArrowRight, Send, Flame } from 'lucide-react';
import { CartItem } from '../types';

interface StickyComandaBarProps {
  items: CartItem[];
  onOpenCart: () => void;
}

export const StickyComandaBar: React.FC<StickyComandaBarProps> = ({
  items,
  onOpenCart,
}) => {
  if (items.length === 0) return null;

  const totalQuantity = items.reduce((sum, item) => sum + item.quantity, 0);
  const subtotal = items.reduce((sum, item) => sum + item.totalPrice, 0);
  const packagingFee = 0.50;
  const estimatedTotal = subtotal + packagingFee;

  return (
    <aside 
      aria-label="Resumen de Comanda Activa"
      className="fixed bottom-4 left-4 right-4 max-w-2xl mx-auto z-40 animate-in slide-in-from-bottom-4 duration-200"
    >
      <div 
        id="sticky-comanda-bar"
        className="bg-stone-950 text-white rounded-2xl p-3 sm:p-3.5 border border-stone-800 shadow-2xl flex items-center justify-between gap-3"
      >
        {/* Real-time metrics */}
        <div className="flex items-center gap-3 pl-1">
          <div className="relative w-10 h-10 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center font-black">
            <ShoppingBag className="w-5 h-5" />
            <span className="absolute -top-1.5 -right-1.5 bg-white text-stone-950 text-[10px] font-black w-5 h-5 rounded-full flex items-center justify-center border-2 border-stone-950">
              {totalQuantity}
            </span>
          </div>

          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-extrabold text-sm sm:text-base text-stone-100">
                ${estimatedTotal.toFixed(2)}
              </span>
              <span className="text-[11px] text-amber-400 font-bold bg-amber-500/20 px-1.5 py-0.2 rounded border border-amber-500/30">
                Empaque Térmico Incl.
              </span>
            </div>
            <p className="text-[11px] text-stone-400">
              {totalQuantity} {totalQuantity === 1 ? 'plato' : 'platos'} • Despacho a oficina
            </p>
          </div>
        </div>

        {/* Action Button */}
        <button
          id="btn-sticky-comanda-dispatch"
          onClick={onOpenCart}
          className="flex items-center gap-2 px-4 sm:px-5 py-2.5 bg-emerald-500 hover:bg-emerald-400 text-stone-950 font-black text-xs sm:text-sm rounded-xl transition-all shadow-md active:scale-95 whitespace-nowrap"
        >
          <Send className="w-4 h-4 fill-current" />
          <span>Ver Comanda & Despachar</span>
          <ArrowRight className="w-4 h-4 hidden sm:inline" />
        </button>
      </div>
    </aside>
  );
};

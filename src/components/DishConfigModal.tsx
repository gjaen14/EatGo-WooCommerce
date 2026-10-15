import React, { useState, useEffect } from 'react';
import { X, Plus, Minus, Check, Sparkles, ShieldCheck, Flame } from 'lucide-react';
import { Dish, CartItem, SideOption, BeverageOption } from '../types';
import { BEVERAGE_ADDONS } from '../data/menuData';

interface DishConfigModalProps {
  dish: Dish | null;
  onClose: () => void;
  onAddToCart: (item: Omit<CartItem, 'cartItemId'>) => void;
}

export const DishConfigModal: React.FC<DishConfigModalProps> = ({
  dish,
  onClose,
  onAddToCart,
}) => {
  const [selectedSide, setSelectedSide] = useState<string>('');
  const [selectedBeverage, setSelectedBeverage] = useState<string>('');
  const [notes, setNotes] = useState<string>('');
  const [quantity, setQuantity] = useState<number>(1);

  useEffect(() => {
    if (dish) {
      // Set default side if dish has sides
      if (dish.availableSides && dish.availableSides.length > 0) {
        const defaultSide = dish.defaultSideId 
          ? dish.availableSides.find(s => s.id === dish.defaultSideId) 
          : dish.availableSides[0];
        setSelectedSide(defaultSide ? defaultSide.name : dish.availableSides[0].name);
      } else {
        setSelectedSide('');
      }
      setSelectedBeverage('');
      setNotes('');
      setQuantity(1);
    }
  }, [dish]);

  if (!dish) return null;

  // Calculate unit and total price
  const sideObj = dish.availableSides?.find(s => s.name === selectedSide);
  const sideExtra = sideObj?.extraPrice || 0;

  const bevObj = BEVERAGE_ADDONS.find(b => b.name === selectedBeverage);
  const bevExtra = bevObj?.price || 0;

  const unitPrice = dish.price + sideExtra + bevExtra;
  const totalPrice = unitPrice * quantity;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onAddToCart({
      dishId: dish.id,
      name: dish.name,
      basePrice: dish.price,
      unitPrice,
      quantity,
      selectedSide: selectedSide || undefined,
      selectedBeverage: selectedBeverage || undefined,
      notes: notes.trim() || undefined,
      totalPrice,
    });
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 bg-black/60 backdrop-blur-xs animate-in fade-in duration-150">
      <div 
        id="dish-config-modal"
        className="bg-white text-stone-900 w-full max-w-lg rounded-2xl shadow-2xl border border-stone-200 overflow-hidden flex flex-col max-h-[90vh]"
      >
        {/* Header image & close button */}
        <div className="relative h-48 sm:h-56 bg-stone-900 shrink-0">
          <img
            src={dish.image}
            alt={dish.name}
            className="w-full h-full object-cover"
            referrerPolicy="no-referrer"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent" />
          
          <button
            onClick={onClose}
            aria-label="Cerrar"
            className="absolute top-3 right-3 w-8 h-8 rounded-full bg-black/50 text-white flex items-center justify-center hover:bg-black/70 transition-colors"
          >
            <X className="w-4 h-4" />
          </button>

          {dish.badge && (
            <span className="absolute top-3 left-3 bg-amber-500 text-stone-950 text-xs font-black uppercase tracking-wider px-2.5 py-1 rounded-md shadow-sm">
              {dish.badge}
            </span>
          )}

          <div className="absolute bottom-3 left-4 right-4 text-white">
            <h3 className="text-xl font-extrabold leading-snug drop-shadow-sm">{dish.name}</h3>
            <p className="text-amber-400 font-black text-lg">${dish.price.toFixed(2)}</p>
          </div>
        </div>

        {/* Form Body with scroll */}
        <form onSubmit={handleSubmit} className="p-4 sm:p-6 overflow-y-auto space-y-5 divide-y divide-stone-100 flex-1">
          {/* Description & guarantee */}
          <div>
            <p className="text-sm text-stone-600 leading-relaxed">{dish.description}</p>
            <div className="mt-3 flex items-center gap-2 text-xs font-semibold text-emerald-700 bg-emerald-50 px-3 py-1.5 rounded-lg border border-emerald-100">
              <ShieldCheck className="w-4 h-4 shrink-0" />
              <span>Despachado en empaque térmico compartimentado de alta retención calórica</span>
            </div>
          </div>

          {/* Side options if available */}
          {dish.availableSides && dish.availableSides.length > 0 && (
            <div className="pt-4">
              <div className="flex items-center justify-between mb-2">
                <label className="text-xs font-bold uppercase tracking-wider text-stone-900 flex items-center gap-1.5">
                  <span>1. Selecciona tu Acompañamiento</span>
                  <span className="text-amber-600 font-normal normal-case text-[11px]">(Obligatorio)</span>
                </label>
              </div>

              <div className="space-y-1.5">
                {dish.availableSides.map((side) => {
                  const isSelected = selectedSide === side.name;
                  return (
                    <button
                      type="button"
                      key={side.id}
                      onClick={() => setSelectedSide(side.name)}
                      className={`w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl border text-sm transition-all text-left ${
                        isSelected
                          ? 'border-amber-600 bg-amber-50 text-stone-950 font-bold shadow-xs'
                          : 'border-stone-200 hover:border-stone-300 text-stone-700'
                      }`}
                    >
                      <div className="flex items-center gap-2.5">
                        <div
                          className={`w-4 h-4 rounded-full border flex items-center justify-center ${
                            isSelected
                              ? 'border-amber-600 bg-amber-600 text-white'
                              : 'border-stone-300'
                          }`}
                        >
                          {isSelected && <Check className="w-2.5 h-2.5 stroke-[3]" />}
                        </div>
                        <span>{side.name}</span>
                      </div>
                      <span className="text-xs font-bold text-stone-500">
                        {side.extraPrice > 0 ? `+$${side.extraPrice.toFixed(2)}` : 'Incluido'}
                      </span>
                    </button>
                  );
                })}
              </div>
            </div>
          )}

          {/* Add sealed beverage combo */}
          <div className="pt-4">
            <label className="text-xs font-bold uppercase tracking-wider text-stone-900 block mb-2">
              2. ¿Deseas agregar Chicha Artesanal Sellada?
            </label>
            <p className="text-xs text-stone-500 mb-2">Botella PET con precinto de seguridad, fría y sin derrames.</p>

            <div className="space-y-1.5">
              <button
                type="button"
                onClick={() => setSelectedBeverage('')}
                className={`w-full flex items-center justify-between px-3.5 py-2 rounded-xl border text-xs transition-all text-left ${
                  selectedBeverage === ''
                    ? 'border-stone-700 bg-stone-100 text-stone-900 font-bold'
                    : 'border-stone-200 text-stone-600 hover:border-stone-300'
                }`}
              >
                <span>Sin bebida adicional</span>
                <span>$0.00</span>
              </button>

              {BEVERAGE_ADDONS.map((bev) => {
                const isSelected = selectedBeverage === bev.name;
                return (
                  <button
                    type="button"
                    key={bev.id}
                    onClick={() => setSelectedBeverage(bev.name)}
                    className={`w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl border text-xs sm:text-sm transition-all text-left ${
                      isSelected
                        ? 'border-amber-600 bg-amber-50 text-stone-950 font-bold shadow-xs'
                        : 'border-stone-200 hover:border-stone-300 text-stone-700'
                    }`}
                  >
                    <div className="flex items-center gap-2">
                      <div
                        className={`w-4 h-4 rounded-full border flex items-center justify-center ${
                          isSelected
                            ? 'border-amber-600 bg-amber-600 text-white'
                            : 'border-stone-300'
                        }`}
                      >
                        {isSelected && <Check className="w-2.5 h-2.5 stroke-[3]" />}
                      </div>
                      <span>{bev.name}</span>
                    </div>
                    <span className="text-xs font-bold text-amber-700">
                      +${bev.price.toFixed(2)}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Notes */}
          <div className="pt-4">
            <label htmlFor="modal-notes" className="text-xs font-bold uppercase tracking-wider text-stone-900 block mb-1">
              Instrucciones para la cocina (Opcional)
            </label>
            <input
              id="modal-notes"
              type="text"
              placeholder="Ej: Poco arroz, salsa del guisado aparte, etc."
              value={notes}
              onChange={(e) => setNotes(e.target.value)}
              className="w-full px-3 py-2 text-sm border border-stone-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-amber-500 focus:border-amber-500"
            />
          </div>
        </form>

        {/* Footer with quantity & submit */}
        <div className="p-4 bg-stone-50 border-t border-stone-200 flex items-center justify-between gap-3 shrink-0">
          {/* Quantity selector */}
          <div className="flex items-center border border-stone-300 rounded-xl bg-white shadow-xs">
            <button
              type="button"
              onClick={() => setQuantity(Math.max(1, quantity - 1))}
              className="p-2 text-stone-600 hover:text-stone-950 active:bg-stone-100 rounded-l-xl"
              aria-label="Disminuir cantidad"
            >
              <Minus className="w-4 h-4" />
            </button>
            <span className="px-3 text-sm font-black text-stone-900">{quantity}</span>
            <button
              type="button"
              onClick={() => setQuantity(quantity + 1)}
              className="p-2 text-stone-600 hover:text-stone-950 active:bg-stone-100 rounded-r-xl"
              aria-label="Aumentar cantidad"
            >
              <Plus className="w-4 h-4" />
            </button>
          </div>

          {/* Add to Comanda Button */}
          <button
            id="modal-add-to-cart"
            onClick={handleSubmit}
            className="flex-1 flex items-center justify-between px-4 py-3 bg-amber-500 hover:bg-amber-400 text-stone-950 font-black text-sm rounded-xl shadow-md transition-all active:scale-[0.98]"
          >
            <span>Agregar a la Comanda</span>
            <span className="text-base">${totalPrice.toFixed(2)}</span>
          </button>
        </div>
      </div>
    </div>
  );
};

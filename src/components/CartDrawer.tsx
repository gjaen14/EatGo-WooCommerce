import React, { useState } from 'react';
import { 
  X, 
  Trash2, 
  Plus, 
  Minus, 
  Send, 
  ShoppingBag, 
  Building2, 
  Clock, 
  CreditCard, 
  Copy, 
  Check, 
  ShieldCheck,
  MapPin,
  Sparkles
} from 'lucide-react';
import { CartItem, DeliveryType, PaymentMethod, OrderDetails } from '../types';

interface CartDrawerProps {
  isOpen: boolean;
  onClose: () => void;
  items: CartItem[];
  onUpdateQuantity: (cartItemId: string, newQuantity: number) => void;
  onRemoveItem: (cartItemId: string) => void;
  onClearCart: () => void;
}

export const CartDrawer: React.FC<CartDrawerProps> = ({
  isOpen,
  onClose,
  items,
  onUpdateQuantity,
  onRemoveItem,
  onClearCart,
}) => {
  const [copied, setCopied] = useState(false);
  const [orderDetails, setOrderDetails] = useState<OrderDetails>({
    customerName: '',
    phone: '',
    deliveryType: 'delivery',
    officeBuilding: '',
    floorOffice: '',
    deliveryTime: 'Inmediato (15-25 min)',
    paymentMethod: 'yappy',
    notes: '',
  });

  if (!isOpen) return null;

  // Compute values
  const subtotal = items.reduce((acc, it) => acc + it.totalPrice, 0);
  const packagingFee = items.length > 0 ? 0.50 : 0;
  const deliveryFee = orderDetails.deliveryType === 'delivery' ? 1.50 : 0.00;
  const grandTotal = subtotal + packagingFee + deliveryFee;

  const generateWhatsAppMessage = () => {
    let msg = `*COMANDA EXPRESS - EAT & GO*\n`;
    msg += `--------------------------------\n`;
    msg += `📦 *Tipo:* ${orderDetails.deliveryType === 'delivery' ? 'Delivery Express a Oficina' : 'Retiro sin Fila (Pick & Go)'}\n`;
    msg += `⏰ *Hora de Entrega:* ${orderDetails.deliveryTime}\n`;
    msg += `👤 *Cliente:* ${orderDetails.customerName || 'No especificado'}\n`;
    msg += `📱 *Teléfono:* ${orderDetails.phone || 'No especificado'}\n`;
    
    if (orderDetails.deliveryType === 'delivery') {
      msg += `🏢 *Edificio / Torre:* ${orderDetails.officeBuilding || 'Pendiente'}\n`;
      msg += `🚪 *Piso / Oficina:* ${orderDetails.floorOffice || 'Pendiente'}\n`;
    }
    
    msg += `--------------------------------\n`;
    msg += `*DETALLE DE LA COMANDA:*\n`;
    
    items.forEach((item, idx) => {
      msg += `${idx + 1}. *${item.quantity}x ${item.name}* ($${item.totalPrice.toFixed(2)})\n`;
      if (item.selectedSide) {
        msg += `   • Acompañamiento: ${item.selectedSide}\n`;
      }
      if (item.selectedBeverage) {
        msg += `   • Bebida Sellada: ${item.selectedBeverage}\n`;
      }
      if (item.notes) {
        msg += `   • Nota: ${item.notes}\n`;
      }
    });

    msg += `--------------------------------\n`;
    msg += `*Subtotal:* $${subtotal.toFixed(2)}\n`;
    msg += `*Empaque Térmico:* $${packagingFee.toFixed(2)}\n`;
    msg += `*Envío:* $${deliveryFee.toFixed(2)}\n`;
    msg += `*TOTAL A PAGAR:* $${grandTotal.toFixed(2)}\n`;
    msg += `💳 *Método de Pago:* ${orderDetails.paymentMethod.toUpperCase()}\n`;
    
    if (orderDetails.notes) {
      msg += `📝 *Observaciones:* ${orderDetails.notes}\n`;
    }
    msg += `--------------------------------\n`;
    msg += `*¡Listo para despacho! Quedo a la espera de confirmación.*`;

    return msg;
  };

  const handleDispatchWhatsApp = () => {
    const message = generateWhatsAppMessage();
    const encoded = encodeURIComponent(message);
    window.open(`https://wa.me/50762345678?text=${encoded}`, '_blank');
  };

  const handleCopySummary = () => {
    const message = generateWhatsAppMessage();
    navigator.clipboard.writeText(message);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 overflow-hidden bg-black/60 backdrop-blur-xs flex justify-end animate-in fade-in duration-150">
      <div 
        id="cart-drawer-panel"
        className="w-full max-w-lg bg-white h-full shadow-2xl flex flex-col justify-between overflow-hidden"
      >
        {/* Header */}
        <div className="p-4 sm:p-5 bg-stone-900 text-white flex items-center justify-between shrink-0">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-amber-500 text-stone-950 flex items-center justify-center font-black text-sm">
              EG
            </div>
            <div>
              <h2 className="font-bold text-base leading-none">Comanda Digital</h2>
              <p className="text-[11px] text-stone-400 mt-1">
                {items.length} {items.length === 1 ? 'plato' : 'platos'} en tu pedido
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {items.length > 0 && (
              <button
                onClick={onClearCart}
                className="text-[11px] text-stone-400 hover:text-red-400 transition-colors mr-2"
              >
                Vaciar
              </button>
            )}
            <button
              onClick={onClose}
              aria-label="Cerrar comanda"
              className="p-1.5 rounded-lg bg-stone-800 text-stone-300 hover:text-white hover:bg-stone-700 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Scrollable Content */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-6">
          {items.length === 0 ? (
            <div className="text-center py-16 space-y-3">
              <div className="w-16 h-16 bg-stone-100 rounded-full flex items-center justify-center mx-auto text-stone-400">
                <ShoppingBag className="w-8 h-8" />
              </div>
              <h3 className="font-bold text-stone-800 text-base">Tu comanda está vacía</h3>
              <p className="text-xs text-stone-500 max-w-xs mx-auto">
                Selecciona uno de los almuerzos del día o desayunos criollos para comenzar tu pedido express.
              </p>
              <button
                onClick={onClose}
                className="mt-3 px-4 py-2 bg-amber-500 text-stone-950 text-xs font-black rounded-xl"
              >
                Ver Menú del Día
              </button>
            </div>
          ) : (
            <>
              {/* Item List */}
              <div className="space-y-3">
                <span className="text-xs font-black uppercase tracking-wider text-stone-900 block">
                  Platos en la Comanda
                </span>

                {items.map((item) => (
                  <div
                    key={item.cartItemId}
                    className="p-3.5 rounded-xl border border-stone-200 bg-stone-50/70 space-y-2"
                  >
                    <div className="flex items-start justify-between gap-2">
                      <div className="flex-1">
                        <h4 className="font-bold text-sm text-stone-900 leading-snug">
                          {item.name}
                        </h4>
                        <div className="mt-1 space-y-0.5 text-xs text-stone-600">
                          {item.selectedSide && (
                            <p className="flex items-center gap-1 text-[11px]">
                              <span className="text-amber-700 font-semibold">• Guarnición:</span> {item.selectedSide}
                            </p>
                          )}
                          {item.selectedBeverage && (
                            <p className="flex items-center gap-1 text-[11px]">
                              <span className="text-emerald-700 font-semibold">• Bebida:</span> {item.selectedBeverage}
                            </p>
                          )}
                          {item.notes && (
                            <p className="text-[11px] text-stone-500 italic">
                              Nota: "{item.notes}"
                            </p>
                          )}
                        </div>
                      </div>

                      <span className="font-black text-sm text-stone-900">
                        ${item.totalPrice.toFixed(2)}
                      </span>
                    </div>

                    {/* Quantity and delete */}
                    <div className="flex items-center justify-between pt-2 border-t border-stone-200/60">
                      <div className="flex items-center border border-stone-300 rounded-lg bg-white">
                        <button
                          type="button"
                          onClick={() => onUpdateQuantity(item.cartItemId, item.quantity - 1)}
                          className="p-1.5 text-stone-600 hover:text-stone-950 active:bg-stone-100"
                        >
                          <Minus className="w-3.5 h-3.5" />
                        </button>
                        <span className="px-2.5 text-xs font-black text-stone-900">
                          {item.quantity}
                        </span>
                        <button
                          type="button"
                          onClick={() => onUpdateQuantity(item.cartItemId, item.quantity + 1)}
                          className="p-1.5 text-stone-600 hover:text-stone-950 active:bg-stone-100"
                        >
                          <Plus className="w-3.5 h-3.5" />
                        </button>
                      </div>

                      <button
                        type="button"
                        onClick={() => onRemoveItem(item.cartItemId)}
                        className="text-stone-400 hover:text-red-500 p-1 transition-colors"
                        title="Eliminar plato"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>

              {/* Delivery Type Selector */}
              <div className="space-y-2 pt-2 border-t border-stone-200">
                <span className="text-xs font-black uppercase tracking-wider text-stone-900 block">
                  Modalidad de Entrega
                </span>
                <div className="grid grid-cols-2 gap-2">
                  <button
                    type="button"
                    onClick={() => setOrderDetails(prev => ({ ...prev, deliveryType: 'delivery' }))}
                    className={`p-3 rounded-xl border text-left transition-all ${
                      orderDetails.deliveryType === 'delivery'
                        ? 'border-amber-500 bg-amber-50 text-stone-950 font-bold'
                        : 'border-stone-200 text-stone-700 bg-white'
                    }`}
                  >
                    <div className="text-xs font-bold">Delivery a Oficina</div>
                    <div className="text-[11px] text-stone-500 mt-0.5">En 15-25 min (+$1.50)</div>
                  </button>

                  <button
                    type="button"
                    onClick={() => setOrderDetails(prev => ({ ...prev, deliveryType: 'pickup' }))}
                    className={`p-3 rounded-xl border text-left transition-all ${
                      orderDetails.deliveryType === 'pickup'
                        ? 'border-amber-500 bg-amber-50 text-stone-950 font-bold'
                        : 'border-stone-200 text-stone-700 bg-white'
                    }`}
                  >
                    <div className="text-xs font-bold">Retiro sin Fila</div>
                    <div className="text-[11px] text-stone-500 mt-0.5">Mostrador Express (Gratis)</div>
                  </button>
                </div>
              </div>

              {/* Delivery Info Form */}
              <div className="space-y-3 pt-2 border-t border-stone-200">
                <span className="text-xs font-black uppercase tracking-wider text-stone-900 block">
                  Datos de Despacho
                </span>

                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className="block text-[11px] font-bold text-stone-700 mb-1">
                      Nombre
                    </label>
                    <input
                      type="text"
                      placeholder="Tu nombre"
                      value={orderDetails.customerName}
                      onChange={(e) => setOrderDetails(p => ({ ...p, customerName: e.target.value }))}
                      className="w-full px-3 py-2 text-xs border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-amber-500"
                    />
                  </div>

                  <div>
                    <label className="block text-[11px] font-bold text-stone-700 mb-1">
                      Teléfono / WhatsApp
                    </label>
                    <input
                      type="tel"
                      placeholder="6234-5678"
                      value={orderDetails.phone}
                      onChange={(e) => setOrderDetails(p => ({ ...p, phone: e.target.value }))}
                      className="w-full px-3 py-2 text-xs border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-amber-500"
                    />
                  </div>
                </div>

                {orderDetails.deliveryType === 'delivery' && (
                  <div className="grid grid-cols-2 gap-2">
                    <div>
                      <label className="block text-[11px] font-bold text-stone-700 mb-1">
                        Edificio / Torre
                      </label>
                      <input
                        type="text"
                        placeholder="Ej: Torre Global Bank"
                        value={orderDetails.officeBuilding}
                        onChange={(e) => setOrderDetails(p => ({ ...p, officeBuilding: e.target.value }))}
                        className="w-full px-3 py-2 text-xs border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-amber-500"
                      />
                    </div>

                    <div>
                      <label className="block text-[11px] font-bold text-stone-700 mb-1">
                        Piso / Oficina
                      </label>
                      <input
                        type="text"
                        placeholder="Ej: Piso 14, Of. 1402"
                        value={orderDetails.floorOffice}
                        onChange={(e) => setOrderDetails(p => ({ ...p, floorOffice: e.target.value }))}
                        className="w-full px-3 py-2 text-xs border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-amber-500"
                      />
                    </div>
                  </div>
                )}

                <div className="grid grid-cols-2 gap-2">
                  <div>
                    <label className="block text-[11px] font-bold text-stone-700 mb-1">
                      Hora de Entrega
                    </label>
                    <select
                      value={orderDetails.deliveryTime}
                      onChange={(e) => setOrderDetails(p => ({ ...p, deliveryTime: e.target.value }))}
                      className="w-full px-3 py-2 text-xs border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-amber-500 bg-white"
                    >
                      <option value="Inmediato (15-25 min)">Inmediato (15-25 min)</option>
                      <option value="11:45 AM">11:45 AM</option>
                      <option value="12:00 MD">12:00 MD</option>
                      <option value="12:30 PM">12:30 PM</option>
                      <option value="1:00 PM">1:00 PM</option>
                      <option value="1:30 PM">1:30 PM</option>
                    </select>
                  </div>

                  <div>
                    <label className="block text-[11px] font-bold text-stone-700 mb-1">
                      Método de Pago
                    </label>
                    <select
                      value={orderDetails.paymentMethod}
                      onChange={(e) => setOrderDetails(p => ({ ...p, paymentMethod: e.target.value as PaymentMethod }))}
                      className="w-full px-3 py-2 text-xs border border-stone-300 rounded-lg focus:outline-none focus:ring-1 focus:ring-amber-500 bg-white"
                    >
                      <option value="yappy">Yappy Directo</option>
                      <option value="tarjeta">Tarjeta / Clave</option>
                      <option value="efectivo">Efectivo Exacto</option>
                    </select>
                  </div>
                </div>
              </div>

              {/* Price Breakdown */}
              <div className="bg-stone-50 p-4 rounded-xl border border-stone-200 space-y-1.5 text-xs text-stone-600">
                <div className="flex justify-between">
                  <span>Subtotal alimentos:</span>
                  <span className="font-semibold text-stone-900">${subtotal.toFixed(2)}</span>
                </div>
                <div className="flex justify-between">
                  <span className="flex items-center gap-1">
                    <span>Empaque térmico trilaminado:</span>
                    <ShieldCheck className="w-3 h-3 text-emerald-600" />
                  </span>
                  <span className="font-semibold text-stone-900">${packagingFee.toFixed(2)}</span>
                </div>
                <div className="flex justify-between">
                  <span>
                    {orderDetails.deliveryType === 'delivery' ? 'Despacho express a oficina:' : 'Retiro sin fila:'}
                  </span>
                  <span className="font-semibold text-stone-900">${deliveryFee.toFixed(2)}</span>
                </div>
                <div className="flex justify-between pt-2 border-t border-stone-200 text-sm font-black text-stone-950">
                  <span>Total a Pagar:</span>
                  <span className="text-base text-amber-700">${grandTotal.toFixed(2)}</span>
                </div>
              </div>
            </>
          )}
        </div>

        {/* Footer Actions */}
        {items.length > 0 && (
          <div className="p-4 bg-stone-100 border-t border-stone-200 space-y-2 shrink-0">
            <button
              id="dispatch-whatsapp-button"
              onClick={handleDispatchWhatsApp}
              className="w-full py-3.5 px-4 bg-emerald-500 hover:bg-emerald-400 text-stone-950 font-black text-sm rounded-xl shadow-md flex items-center justify-center gap-2.5 transition-all active:scale-[0.98]"
            >
              <Send className="w-4 h-4 fill-current" />
              <span>Despachar Comanda por WhatsApp (${grandTotal.toFixed(2)})</span>
            </button>

            <button
              onClick={handleCopySummary}
              className="w-full py-2 px-3 bg-white hover:bg-stone-50 border border-stone-300 text-stone-700 font-bold text-xs rounded-xl flex items-center justify-center gap-1.5 transition-colors"
            >
              {copied ? (
                <>
                  <Check className="w-3.5 h-3.5 text-emerald-600" />
                  <span>¡Texto de Comanda Copiado!</span>
                </>
              ) : (
                <>
                  <Copy className="w-3.5 h-3.5 text-stone-500" />
                  <span>Copiar texto de comanda</span>
                </>
              )}
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

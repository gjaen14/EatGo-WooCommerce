import React, { useState } from 'react';
import { 
  Sparkles, 
  Calendar, 
  Clock, 
  Send, 
  ShoppingBag, 
  Check, 
  Gift, 
  Award, 
  Users, 
  Building2, 
  ArrowRight,
  ShieldCheck,
  CheckCircle2,
  Lock,
  Eye,
  AlertTriangle
} from 'lucide-react';
import { CHRISTMAS_DISHES, CHRISTMAS_PACKAGES, ChristmasDish, ChristmasPackage } from '../data/christmasData';
import { CartItem } from '../types';

interface ChristmasSpecialViewProps {
  onAddToCart?: (item: Omit<CartItem, 'cartItemId'>) => void;
}

export const ChristmasSpecialView: React.FC<ChristmasSpecialViewProps> = ({ onAddToCart }) => {
  // Toggle between Draft Preview and Active mode
  const [isPublished, setIsPublished] = useState<boolean>(true);
  
  // Reservation Form State
  const [deliveryDate, setDeliveryDate] = useState<'24-dic' | '31-dic' | 'evento-corporativo'>('24-dic');
  const [deliveryTime, setDeliveryTime] = useState<string>('12:00 PM - 2:00 PM');
  const [deliveryMode, setDeliveryMode] = useState<'pick-and-go' | 'delivery-termico'>('pick-and-go');
  const [customerName, setCustomerName] = useState<string>('');
  const [customerPhone, setCustomerPhone] = useState<string>('');
  const [customerCompany, setCustomerCompany] = useState<string>('');
  const [selectedPackageId, setSelectedPackageId] = useState<string>('pack-nav-familiar');
  const [reservationSent, setReservationSent] = useState<boolean>(false);
  const [addedItemName, setAddedItemName] = useState<string | null>(null);

  const selectedPackage = CHRISTMAS_PACKAGES.find((p) => p.id === selectedPackageId) || CHRISTMAS_PACKAGES[0];

  const handleAddDishToCart = (dish: ChristmasDish) => {
    if (onAddToCart) {
      onAddToCart({
        dishId: dish.id,
        name: `🎄 ${dish.name}`,
        basePrice: dish.price,
        unitPrice: dish.price,
        quantity: 1,
        selectedSide: dish.servingsInfo,
        notes: `Especial Navideño: ${dish.unit}`,
        totalPrice: dish.price
      });
      setAddedItemName(dish.name);
      setTimeout(() => setAddedItemName(null), 2000);
    }
  };

  const handleAddPackageToCart = (pkg: ChristmasPackage) => {
    if (onAddToCart) {
      onAddToCart({
        dishId: pkg.id,
        name: `🎄 ${pkg.name}`,
        basePrice: pkg.price,
        unitPrice: pkg.price,
        quantity: 1,
        selectedSide: `${pkg.servings} comensales`,
        notes: `Paquete Navideño Completo para ${pkg.servings} personas`,
        totalPrice: pkg.price
      });
      setAddedItemName(pkg.name);
      setTimeout(() => setAddedItemName(null), 2000);
    }
  };

  const handleSendChristmasWhatsApp = (e: React.FormEvent) => {
    e.preventDefault();
    if (!customerName || !customerPhone) return;

    const dateLabels: Record<string, string> = {
      '24-dic': '24 de Diciembre (Nochebuena)',
      '31-dic': '31 de Diciembre (Víspera de Año Nuevo)',
      'evento-corporativo': 'Evento Corporativo de Fin de Año'
    };

    const modeLabels: Record<string, string> = {
      'pick-and-go': 'Retiro Pick & Go en Local (Sin Filas)',
      'delivery-termico': 'Entrega en Camión Térmico a Oficina/Residencia'
    };

    const depositAmount = (selectedPackage.price * 0.5).toFixed(2);

    const message = `*SOLICITUD DE RESERVA NAVIDEÑA - EAT & GO* 🎄🍗
--------------------------------------------
👤 *Cliente:* ${customerName}
${customerCompany ? `🏢 *Empresa:* ${customerCompany}\n` : ''}📱 *Teléfono:* ${customerPhone}

🎁 *Paquete Elegido:* ${selectedPackage.name}
👥 *Comensales:* ${selectedPackage.servings} personas
💰 *Valor Total:* $${selectedPackage.price.toFixed(2)}
💵 *Abono 50% requerido:* $${depositAmount}

📅 *Fecha de Entrega:* ${dateLabels[deliveryDate]}
⏰ *Horario Preferido:* ${deliveryTime}
🚚 *Modalidad:* ${modeLabels[deliveryMode]}

*Solicito confirmación de cupo y datos para abono vía Yappy o transferencia.*`;

    window.open(`https://wa.me/50762345678?text=${encodeURIComponent(message)}`, '_blank');
    setReservationSent(true);
  };

  return (
    <div className="space-y-8 sm:space-y-10 pb-16">
      {/* ========================================================================= */}
      {/* BANNER DE CONTROL: MÓDULO TEMPORAL (Borrador / Activación 15 de Noviembre) */}
      {/* ========================================================================= */}
      <div className="bg-stone-900 text-stone-100 rounded-2xl p-4 sm:p-5 border border-amber-600/60 shadow-lg">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div className="flex items-start sm:items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400 shrink-0">
              <Lock className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-[11px] font-black uppercase tracking-wider text-amber-400">
                  MÓDULO TEMPORAL OCULTO
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-red-950 text-red-300 border border-red-800">
                  Programado: 15 de Noviembre
                </span>
              </div>
              <p className="text-xs text-stone-300 mt-0.5">
                Plantilla para venta de cenas familiares y corporativas con reserva previa para el 24 y 31 de diciembre.
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 self-start md:self-auto">
            <button
              onClick={() => setIsPublished(!isPublished)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold flex items-center gap-1.5 transition-all border ${
                isPublished
                  ? 'bg-emerald-600/30 text-emerald-300 border-emerald-500'
                  : 'bg-stone-800 text-stone-400 border-stone-700'
              }`}
            >
              <Eye className="w-3.5 h-3.5" />
              <span>{isPublished ? 'Vista Previa Activa' : 'Simular Estado Oculto'}</span>
            </button>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* HERO FESTIVO NAVIDEÑO                                                     */}
      {/* ========================================================================= */}
      <div className="relative rounded-2xl sm:rounded-3xl overflow-hidden bg-gradient-to-r from-red-950 via-stone-900 to-emerald-950 text-white p-6 sm:p-12 border border-amber-500/30 shadow-xl">
        <div className="absolute top-0 right-0 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none" />
        
        <div className="relative z-10 max-w-2xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/40 text-amber-300 text-xs font-black uppercase tracking-wider mb-3">
            <Gift className="w-3.5 h-3.5 text-amber-400" />
            <span>Temporada Navideña & Fin de Año • Cupos Limitados</span>
          </div>

          <h1 className="text-2xl sm:text-4xl md:text-5xl font-black tracking-tight leading-tight">
            Cenas Navideñas Criollas & Banquetes de Fin de Año
          </h1>

          <p className="mt-3 text-xs sm:text-base text-stone-200 leading-relaxed font-normal">
            Jamón horneado con piña y miel de raspadura, pernil asado a la leña, pavo criollo, tamales en hoja de bijao y ron ponche artesanal. Reserva anticipadamente para el <strong>24 y 31 de Diciembre</strong> y olvídate de cocinar.
          </p>

          <div className="mt-6 flex flex-wrap items-center gap-3">
            <a
              href="#formulario-reserva-navidena"
              className="px-5 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-stone-950 font-black text-xs sm:text-sm shadow-md transition-all active:scale-95 flex items-center gap-2"
            >
              <Calendar className="w-4 h-4" />
              <span>Reservar Fecha (24 o 31 Dic)</span>
            </a>

            <a
              href="#paquetes-navidenos"
              className="px-4 py-3 rounded-xl bg-white/10 hover:bg-white/20 text-white font-bold text-xs sm:text-sm backdrop-blur-xs border border-white/20 transition-colors"
            >
              <span>Ver Paquetes Familiares y B2B</span>
            </a>
          </div>
        </div>
      </div>

      {/* FEEDBACK TOAST */}
      {addedItemName && (
        <div className="bg-emerald-600 text-white text-xs sm:text-sm font-bold p-3 rounded-xl shadow-lg flex items-center gap-2 animate-bounce">
          <CheckCircle2 className="w-4 h-4" />
          <span>¡&quot;{addedItemName}&quot; añadido a tu comanda navideña!</span>
        </div>
      )}

      {/* ========================================================================= */}
      {/* 1. PAQUETES COMPLETOS DE BANQUETES (Familiares & Corporativos)            */}
      {/* ========================================================================= */}
      <section id="paquetes-navidenos" className="scroll-mt-24">
        <div className="mb-6">
          <span className="text-[11px] font-black uppercase tracking-widest text-amber-800 block">
            CENAS COMPLETAS LISTAS PARA SERVIR
          </span>
          <h2 className="text-2xl sm:text-3xl font-black text-stone-900 tracking-tight">
            Paquetes Festivos Todo Incluido
          </h2>
          <p className="text-xs sm:text-sm text-stone-600 mt-1">
            Empacados en cajas troqueladas individuales o bandejas térmicas gastronómicas que conservan el calor a 75°C.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {CHRISTMAS_PACKAGES.map((pkg) => (
            <div
              key={pkg.id}
              className="bg-white rounded-2xl border-2 border-stone-200 hover:border-amber-400 rounded-2xl overflow-hidden shadow-xs hover:shadow-md transition-all flex flex-col justify-between"
            >
              <div>
                <div className="relative aspect-[16/10] bg-stone-100 overflow-hidden">
                  <img
                    src={pkg.image}
                    alt={pkg.name}
                    className="w-full h-full object-cover"
                    referrerPolicy="no-referrer"
                  />
                  <span className="absolute top-3 left-3 bg-red-900/90 backdrop-blur-xs text-white text-[10px] font-black uppercase px-2.5 py-1 rounded-md">
                    {pkg.badge}
                  </span>
                  <div className="absolute bottom-3 right-3 bg-stone-950/90 text-amber-400 text-sm font-black px-3 py-1 rounded-lg">
                    ${pkg.price.toFixed(2)}
                  </div>
                </div>

                <div className="p-5">
                  <div className="flex items-center gap-1.5 text-xs font-bold text-amber-800 mb-1">
                    <Users className="w-3.5 h-3.5" />
                    <span>Para {pkg.servings} Personas</span>
                  </div>

                  <h3 className="font-black text-stone-900 text-lg leading-snug">
                    {pkg.name}
                  </h3>

                  <p className="text-xs text-stone-600 mt-2 leading-relaxed">
                    {pkg.description}
                  </p>

                  <div className="mt-4 pt-3 border-t border-stone-100 space-y-1.5">
                    <span className="text-[11px] font-bold text-stone-800 block">
                      Incluye:
                    </span>
                    {pkg.includes.map((inc, i) => (
                      <div key={i} className="flex items-start gap-1.5 text-xs text-stone-600">
                        <Check className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                        <span className="leading-tight">{inc}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              <div className="p-5 pt-0 space-y-2">
                <button
                  onClick={() => handleAddPackageToCart(pkg)}
                  className="w-full py-2.5 px-4 rounded-xl bg-amber-500 hover:bg-amber-400 text-stone-950 font-black text-xs flex items-center justify-center gap-2 transition-all shadow-sm active:scale-95"
                >
                  <ShoppingBag className="w-4 h-4" />
                  <span>Agregar al Pedido (${pkg.price.toFixed(2)})</span>
                </button>

                <button
                  onClick={() => {
                    setSelectedPackageId(pkg.id);
                    const formEl = document.getElementById('formulario-reserva-navidena');
                    formEl?.scrollIntoView({ behavior: 'smooth' });
                  }}
                  className="w-full py-2 px-3 rounded-xl bg-stone-100 hover:bg-stone-200 text-stone-700 font-bold text-[11px] transition-colors"
                >
                  Seleccionar para Reserva Formal
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 2. CATÁLOGO INDIVIDUAL POR PIEZA Y BANDEJAS                                */}
      {/* ========================================================================= */}
      <section className="scroll-mt-24">
        <div className="mb-6">
          <span className="text-[11px] font-black uppercase tracking-widest text-amber-800 block">
            A LA CARTA NAVIDEÑA
          </span>
          <h2 className="text-2xl sm:text-3xl font-black text-stone-900 tracking-tight">
            Piezas Enteras, Tamales y Acompañamientos
          </h2>
          <p className="text-xs sm:text-sm text-stone-600 mt-1">
            Pide piezas de jamón o pernil enteras, tamales por docena o bandejas de arroz navideño.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          {CHRISTMAS_DISHES.map((dish) => (
            <div
              key={dish.id}
              className="bg-white rounded-2xl border border-stone-200 overflow-hidden shadow-xs hover:border-amber-400 transition-all flex flex-col justify-between"
            >
              <div>
                <div className="relative aspect-[4/3] bg-stone-100 overflow-hidden">
                  <img
                    src={dish.image}
                    alt={dish.name}
                    className="w-full h-full object-cover"
                    referrerPolicy="no-referrer"
                  />
                  <span className="absolute top-2.5 left-2.5 bg-stone-900/80 text-amber-400 text-[10px] font-black px-2 py-0.5 rounded">
                    {dish.badge}
                  </span>
                  <span className="absolute top-2.5 right-2.5 bg-white text-stone-900 text-xs font-black px-2 py-0.5 rounded shadow-sm">
                    ${dish.price.toFixed(2)}
                  </span>
                </div>

                <div className="p-4">
                  <h4 className="font-bold text-stone-900 text-sm leading-snug">
                    {dish.name}
                  </h4>
                  <span className="text-[11px] text-amber-800 font-bold block mt-1">
                    {dish.unit}
                  </span>
                  <p className="text-xs text-stone-600 mt-1 line-clamp-2 leading-relaxed">
                    {dish.description}
                  </p>
                </div>
              </div>

              <div className="p-4 pt-0">
                <button
                  onClick={() => handleAddDishToCart(dish)}
                  className="w-full py-2 px-3 rounded-xl bg-stone-900 hover:bg-stone-800 text-amber-400 font-bold text-xs flex items-center justify-center gap-1.5 transition-colors"
                >
                  <ShoppingBag className="w-3.5 h-3.5" />
                  <span>Agregar (${dish.price.toFixed(2)})</span>
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. SISTEMA DE RESERVA PREVIA CON FECHA DE ENTREGA (24 Y 31 DICIEMBRE)     */}
      {/* ========================================================================= */}
      <section
        id="formulario-reserva-navidena"
        className="bg-stone-900 text-white rounded-2xl sm:rounded-3xl p-6 sm:p-10 border border-stone-800 scroll-mt-24 shadow-xl"
      >
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div className="lg:col-span-5 space-y-4">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-950 text-red-300 border border-red-800 text-xs font-bold">
              <Calendar className="w-3.5 h-3.5 text-red-400" />
              <span>Programación con Cupo Cerrado</span>
            </div>

            <h2 className="text-2xl sm:text-3xl font-black tracking-tight">
              Sistema de Reserva Previa para Nochebuena y Fin de Año
            </h2>

            <p className="text-xs sm:text-sm text-stone-300 leading-relaxed">
              Para garantizar la calidad de los horneados y la puntualidad sin demoras, <strong>los pedidos para el 24 y 31 de Diciembre se reciben hasta el 20 de Diciembre con el 50% de anticipo</strong>.
            </p>

            <div className="space-y-3 pt-2">
              <div className="flex items-start gap-3 bg-stone-800/80 p-3.5 rounded-xl border border-stone-700">
                <ShieldCheck className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                <div className="text-xs">
                  <span className="font-bold text-stone-100 block">Horneados Artesanales Frescos</span>
                  <span className="text-stone-400">Entregas calientes el mismo 24 o 31 de Diciembre.</span>
                </div>
              </div>

              <div className="flex items-start gap-3 bg-stone-800/80 p-3.5 rounded-xl border border-stone-700">
                <Clock className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
                <div className="text-xs">
                  <span className="font-bold text-stone-100 block">Retiro Pick & Go Sin Filas</span>
                  <span className="text-stone-400">Entrega rápida en barra exclusiva para clientes con reserva.</span>
                </div>
              </div>
            </div>
          </div>

          <div className="lg:col-span-7 bg-stone-950 p-6 sm:p-8 rounded-2xl border border-stone-800">
            <h3 className="text-lg font-black text-white mb-4 flex items-center gap-2">
              <Gift className="w-5 h-5 text-amber-400" />
              <span>Formulario de Reserva Navideña</span>
            </h3>

            {reservationSent ? (
              <div className="p-6 bg-emerald-950/70 border border-emerald-700 rounded-xl text-center space-y-3">
                <CheckCircle2 className="w-10 h-10 text-emerald-400 mx-auto" />
                <h4 className="text-base font-black text-white">¡Reserva enviada a WhatsApp!</h4>
                <p className="text-xs text-stone-300">
                  Nuestro equipo de gerencia te responderá para confirmar el cupo y los datos para el abono del 50%.
                </p>
                <button
                  onClick={() => setReservationSent(false)}
                  className="text-xs text-amber-400 font-bold underline"
                >
                  Enviar otra reserva
                </button>
              </div>
            ) : (
              <form onSubmit={handleSendChristmasWhatsApp} className="space-y-4">
                {/* Selector de Fecha */}
                <div>
                  <label className="text-xs font-bold text-stone-300 block mb-1.5">
                    1. Fecha Programada de Entrega:
                  </label>
                  <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
                    <button
                      type="button"
                      onClick={() => setDeliveryDate('24-dic')}
                      className={`p-3 rounded-xl text-xs font-bold border transition-all text-left ${
                        deliveryDate === '24-dic'
                          ? 'bg-amber-500 text-stone-950 border-amber-400 font-black'
                          : 'bg-stone-900 text-stone-300 border-stone-700 hover:bg-stone-800'
                      }`}
                    >
                      <span className="block font-black">24 de Diciembre</span>
                      <span className="text-[10px] opacity-80">Nochebuena</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => setDeliveryDate('31-dic')}
                      className={`p-3 rounded-xl text-xs font-bold border transition-all text-left ${
                        deliveryDate === '31-dic'
                          ? 'bg-amber-500 text-stone-950 border-amber-400 font-black'
                          : 'bg-stone-900 text-stone-300 border-stone-700 hover:bg-stone-800'
                      }`}
                    >
                      <span className="block font-black">31 de Diciembre</span>
                      <span className="text-[10px] opacity-80">Fin de Año</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => setDeliveryDate('evento-corporativo')}
                      className={`p-3 rounded-xl text-xs font-bold border transition-all text-left ${
                        deliveryDate === 'evento-corporativo'
                          ? 'bg-amber-500 text-stone-950 border-amber-400 font-black'
                          : 'bg-stone-900 text-stone-300 border-stone-700 hover:bg-stone-800'
                      }`}
                    >
                      <span className="block font-black">Cena de Empresa</span>
                      <span className="text-[10px] opacity-80">1 al 23 de Dic</span>
                    </button>
                  </div>
                </div>

                {/* Paquete seleccionado */}
                <div>
                  <label className="text-xs font-bold text-stone-300 block mb-1">
                    2. Paquete o Banquete Principal:
                  </label>
                  <select
                    value={selectedPackageId}
                    onChange={(e) => setSelectedPackageId(e.target.value)}
                    className="w-full bg-stone-900 border border-stone-700 rounded-xl p-2.5 text-xs text-white focus:ring-1 focus:ring-amber-500"
                  >
                    {CHRISTMAS_PACKAGES.map((pkg) => (
                      <option key={pkg.id} value={pkg.id}>
                        {pkg.name} ({pkg.servings} pax) - ${pkg.price.toFixed(2)}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Horario y Modalidad */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label className="text-xs font-bold text-stone-300 block mb-1">
                      Horario de Entrega:
                    </label>
                    <select
                      value={deliveryTime}
                      onChange={(e) => setDeliveryTime(e.target.value)}
                      className="w-full bg-stone-900 border border-stone-700 rounded-xl p-2.5 text-xs text-white"
                    >
                      <option value="11:00 AM - 1:00 PM">11:00 AM - 1:00 PM</option>
                      <option value="1:00 PM - 3:00 PM">1:00 PM - 3:00 PM</option>
                      <option value="3:00 PM - 5:00 PM">3:00 PM - 5:00 PM</option>
                    </select>
                  </div>

                  <div>
                    <label className="text-xs font-bold text-stone-300 block mb-1">
                      Modalidad de Entrega:
                    </label>
                    <select
                      value={deliveryMode}
                      onChange={(e) => setDeliveryMode(e.target.value as any)}
                      className="w-full bg-stone-900 border border-stone-700 rounded-xl p-2.5 text-xs text-white"
                    >
                      <option value="pick-and-go">Pick & Go en Local (Sin Filas)</option>
                      <option value="delivery-termico">Despacho en Camión Térmico</option>
                    </select>
                  </div>
                </div>

                {/* Datos del Cliente */}
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  <div>
                    <label className="text-xs font-bold text-stone-300 block mb-1">
                      Nombre Completo: *
                    </label>
                    <input
                      type="text"
                      required
                      placeholder="Ej. Carmen Rodríguez"
                      value={customerName}
                      onChange={(e) => setCustomerName(e.target.value)}
                      className="w-full bg-stone-900 border border-stone-700 rounded-xl p-2.5 text-xs text-white placeholder-stone-500"
                    />
                  </div>

                  <div>
                    <label className="text-xs font-bold text-stone-300 block mb-1">
                      Teléfono WhatsApp: *
                    </label>
                    <input
                      type="tel"
                      required
                      placeholder="+507 6000-0000"
                      value={customerPhone}
                      onChange={(e) => setCustomerPhone(e.target.value)}
                      className="w-full bg-stone-900 border border-stone-700 rounded-xl p-2.5 text-xs text-white placeholder-stone-500"
                    />
                  </div>
                </div>

                <div>
                  <label className="text-xs font-bold text-stone-300 block mb-1">
                    Empresa / Razón Social (Opcional si requiere factura fiscal):
                  </label>
                  <input
                    type="text"
                    placeholder="Ej. Corporación Logística Panamá S.A."
                    value={customerCompany}
                    onChange={(e) => setCustomerCompany(e.target.value)}
                    className="w-full bg-stone-900 border border-stone-700 rounded-xl p-2.5 text-xs text-white placeholder-stone-500"
                  />
                </div>

                {/* Resumen de Pago */}
                <div className="bg-stone-900 p-3.5 rounded-xl border border-stone-700 flex items-center justify-between text-xs">
                  <div>
                    <span className="text-stone-400 block">Total Paquete:</span>
                    <span className="font-bold text-white">${selectedPackage.price.toFixed(2)}</span>
                  </div>
                  <div className="text-right">
                    <span className="text-amber-400 font-bold block">Abono 50% para Reservar:</span>
                    <span className="text-sm font-black text-amber-400">
                      ${(selectedPackage.price * 0.5).toFixed(2)}
                    </span>
                  </div>
                </div>

                <button
                  type="submit"
                  className="w-full py-3 px-4 rounded-xl bg-amber-500 hover:bg-amber-400 text-stone-950 font-black text-xs sm:text-sm flex items-center justify-center gap-2 shadow-lg transition-all active:scale-95"
                >
                  <Send className="w-4 h-4 fill-current" />
                  <span>Enviar Reserva Anticipada por WhatsApp</span>
                </button>
              </form>
            )}
          </div>
        </div>
      </section>
    </div>
  );
};

import React from 'react';
import { 
  ShieldCheck, 
  Flame, 
  Clock, 
  MapPin, 
  CheckCircle2, 
  Truck, 
  Sparkles, 
  HelpCircle,
  CreditCard,
  QrCode
} from 'lucide-react';
import { PACKAGING_BENEFITS } from '../data/menuData';

export const DeliveryInfoView: React.FC = () => {
  const deliveryZones = [
    { name: 'Obarrio & Calle 50', time: '15-20 min', cost: '$1.50' },
    { name: 'Marbella & Balboa', time: '15-25 min', cost: '$1.50' },
    { name: 'San Francisco & Vía Porras', time: '20-25 min', cost: '$2.00' },
    { name: 'Punta Pacífica & Paitilla', time: '20-30 min', cost: '$2.00' },
    { name: 'Costa del Este', time: 'Programado 12:00 MD', cost: '$2.50' },
    { name: 'Retiro en Local (Pick & Go)', time: 'Listo en 10 min (0 Filas)', cost: 'Gratis ($0.00)' },
  ];

  const faqs = [
    {
      q: '¿Cómo garantizan que la comida llega caliente?',
      a: 'Utilizamos empaques térmicos troquelados trilaminados diseñados con cámara de aire aislante. Mantienen la temperatura sobre los 70°C por más de 45 minutos sin humedecer las comidas crocantes.'
    },
    {
      q: '¿Las chichas pueden derramarse en mi mochila o ascensor?',
      a: 'No. Todas nuestras chichas y jugos naturales son embotellados en envases PET sellados con anillo de seguridad inviolable. Cero derrames garantizados.'
    },
    {
      q: '¿Cómo funciona el retiro sin fila (Pick & Go)?',
      a: 'Haces tu comanda en este menú digital o por WhatsApp. Cuando llegas a la sucursal, tu bolsa térmica rotulada con tu nombre está esperando en el mostrador express. Solo la tomas y te vas.'
    },
    {
      q: '¿Qué métodos de pago aceptan?',
      a: 'Aceptamos Yappy directo (@eatandgopa), tarjetas de crédito/débito y efectivo exacto al momento de la entrega.'
    }
  ];

  return (
    <div className="space-y-10 pb-12">
      {/* Packaging Deep Dive */}
      <section className="bg-stone-900 text-white rounded-2xl sm:rounded-3xl p-6 sm:p-10 border border-stone-800">
        <div className="max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-bold uppercase tracking-wider mb-3">
            <ShieldCheck className="w-3.5 h-3.5" />
            <span>Tecnología de Empaque & Aislamiento</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-black tracking-tight">
            Diseñado para la Oficina Moderna: Cero Fugas, Cero Olores Fuertes
          </h1>
          <p className="mt-2 text-stone-300 text-sm sm:text-base leading-relaxed">
            El mayor problema de pedir comida criolla a una oficina son las bolsas chorreadas de salsa y la comida tibia. Nosotros rediseñamos todo el proceso con empaque troquelado de cierre hermético.
          </p>
        </div>

        <div className="mt-8 grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-stone-800/80 rounded-2xl p-6 border border-stone-700 space-y-4">
            <div className="w-10 h-10 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center font-bold">
              <Flame className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-stone-100">
              Bandeja Compartimentada con Sello de Presión
            </h3>
            <p className="text-xs sm:text-sm text-stone-400 leading-relaxed">
              Las paredes divisorias impiden que la salsa del mondongo o el pollo moje las tajadas maduras o el arroz con guandú. Cada elemento conserva su textura crujiente y aroma individual hasta que abres la tapa en tu escritorio.
            </p>
            <ul className="space-y-2 text-xs text-stone-300 pt-2 border-t border-stone-700/60">
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>Libre de BPA y 100% reciclable</span>
              </li>
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>Apta para microondas en caso de reuniones tardías</span>
              </li>
            </ul>
          </div>

          <div className="bg-stone-800/80 rounded-2xl p-6 border border-stone-700 space-y-4">
            <div className="w-10 h-10 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center font-bold">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-stone-100">
              Botellas PET con Precinto Antiviolable
            </h3>
            <p className="text-xs sm:text-sm text-stone-400 leading-relaxed">
              Dile adiós a los vasos de foam con tape que se perforan en el viaje. Nuestras chichas artesanales (raspadura, maracuyá, nance) van en botellas cerradas de fábrica con tapón termosellado que se destapa solo al quebrar el precinto.
            </p>
            <ul className="space-y-2 text-xs text-stone-300 pt-2 border-t border-stone-700/60">
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>Mantiene la chicha fría sin derretir hielo sobre la comida</span>
              </li>
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>Transporte seguro en maletines o bolsos</span>
              </li>
            </ul>
          </div>
        </div>
      </section>

      {/* Coverage Zones */}
      <section className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200 shadow-xs">
        <div className="flex items-center gap-2 text-xs font-black uppercase tracking-wider text-amber-700 mb-1">
          <Truck className="w-4 h-4" />
          <span>Cobertura & Tiempos de Entrega</span>
        </div>
        <h2 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
          Zonas de Despacho Inmediato
        </h2>
        <p className="text-xs sm:text-sm text-stone-600 mt-1">
          Nuestros motorizados operan en radios cortos para asegurar que tu almuerzo llegue en menos de 25 minutos.
        </p>

        <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
          {deliveryZones.map((zone, idx) => (
            <div
              key={idx}
              className="p-4 rounded-xl border border-stone-200 bg-stone-50 flex items-center justify-between"
            >
              <div className="flex items-start gap-2.5">
                <MapPin className="w-4 h-4 text-amber-600 shrink-0 mt-0.5" />
                <div>
                  <h3 className="font-bold text-sm text-stone-900">{zone.name}</h3>
                  <span className="text-[11px] text-stone-500">{zone.time}</span>
                </div>
              </div>
              <span className="text-xs font-black text-stone-800 bg-white px-2 py-1 rounded border border-stone-200">
                {zone.cost}
              </span>
            </div>
          ))}
        </div>
      </section>

      {/* FAQs */}
      <section className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200 shadow-xs">
        <div className="flex items-center gap-2 text-xs font-black uppercase tracking-wider text-amber-700 mb-1">
          <HelpCircle className="w-4 h-4" />
          <span>Preguntas Frecuentes</span>
        </div>
        <h2 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight mb-6">
          Todo sobre tu Pedido & Despacho
        </h2>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {faqs.map((faq, i) => (
            <div key={i} className="p-4 rounded-xl border border-stone-200 bg-stone-50/50">
              <h3 className="font-bold text-sm text-stone-900 mb-1.5">{faq.q}</h3>
              <p className="text-xs text-stone-600 leading-relaxed">{faq.a}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

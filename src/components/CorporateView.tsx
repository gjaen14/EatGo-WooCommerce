import React, { useState } from 'react';
import { 
  Building2, 
  Users, 
  Receipt, 
  Clock, 
  CheckCircle2, 
  Send, 
  ShoppingBag, 
  Mail, 
  FileText, 
  Award, 
  ShieldCheck, 
  PackageCheck, 
  Calculator, 
  Sparkles,
  DollarSign,
  Calendar as CalendarIcon,
  Check
} from 'lucide-react';
import { CORPORATE_PACKAGES } from '../data/menuData';
import { CartItem } from '../types';

interface CorporateViewProps {
  onAddToCart: (item: Omit<CartItem, 'cartItemId'>) => void;
}

export const CorporateView: React.FC<CorporateViewProps> = ({ onAddToCart }) => {
  // Calculadora B2B state
  const [eventType, setEventType] = useState<'ejecutivo' | 'capacitacion' | 'licitacion' | 'findeano'>('licitacion');
  const [peopleRange, setPeopleRange] = useState<'50-100' | '100-300' | '500+'>('100-300');
  const [exactPax, setExactPax] = useState<number>(150);
  const [budgetPerPlate, setBudgetPerPlate] = useState<number>(8.75);
  const [serviceMode, setServiceMode] = useState<'cajas-troqueladas' | 'buffet-rechauds'>('cajas-troqueladas');
  const [eventDate, setEventDate] = useState<string>('');
  const [eventTime, setEventTime] = useState<string>('12:00 PM');
  
  // Contact details
  const [companyName, setCompanyName] = useState<string>('');
  const [ruc, setRuc] = useState<string>('');
  const [contactPerson, setContactPerson] = useState<string>('');
  const [corporateEmail, setCorporateEmail] = useState<string>('');
  const [phone, setPhone] = useState<string>('');
  const [specialNotes, setSpecialNotes] = useState<string>('');

  // Status state
  const [showMailModal, setShowMailModal] = useState<boolean>(false);
  const [alertSent, setAlertSent] = useState<boolean>(false);
  const [addedPkgId, setAddedPkgId] = useState<string | null>(null);

  // Range change handler
  const handleRangeChange = (range: '50-100' | '100-300' | '500+') => {
    setPeopleRange(range);
    if (range === '50-100') setExactPax(75);
    else if (range === '100-300') setExactPax(200);
    else setExactPax(550);
  };

  // Pricing calculations
  const subtotalPlates = exactPax * budgetPerPlate;
  const packagingFee = serviceMode === 'cajas-troqueladas' ? 0 : exactPax * 1.50; // extra for rechauds & service staff
  const volumeDiscountRate = exactPax >= 500 ? 0.10 : exactPax >= 200 ? 0.05 : 0;
  const volumeDiscount = subtotalPlates * volumeDiscountRate;
  const estimatedTotal = (subtotalPlates + packagingFee - volumeDiscount);

  const eventTypeLabels: Record<string, string> = {
    ejecutivo: 'Reunión Ejecutiva / Directorio',
    capacitacion: 'Almuerzo Corporativo / Capacitación Masiva',
    licitacion: 'Licitación Estatal (Panamá Compra)',
    findeano: 'Banquete de Fin de Año / Gala Empresarial'
  };

  const serviceModeLabels: Record<string, string> = {
    'cajas-troqueladas': 'Cajas Troqueladas Térmicas Individuales (75°C Selladas)',
    'buffet-rechauds': 'Estación de Buffet Asistido con Rechauds y Personal'
  };

  // Dual Dispatch: WhatsApp Alert
  const handleSendWhatsAppAlert = () => {
    if (!companyName || !phone) {
      alert('Por favor ingresa al menos la Empresa y el Teléfono de contacto.');
      return;
    }

    const msg = `*ALERTA B2B COTIZACIÓN PRIORITARIA - EAT & GO* 🏢
--------------------------------------------
🏛️ *Empresa/Entidad:* ${companyName}
📄 *RUC/DV:* ${ruc || 'Por confirmar'}
👤 *Contacto:* ${contactPerson || 'Encargado de Compras'}
📞 *Teléfono:* ${phone}
📧 *Email:* ${corporateEmail || 'No provisto'}

🎯 *Tipo de Evento:* ${eventTypeLabels[eventType]}
👥 *Comensales:* ${exactPax} personas (Rango: ${peopleRange})
🍽️ *Presupuesto Estimado/Plato:* $${budgetPerPlate.toFixed(2)}
📦 *Modalidad:* ${serviceModeLabels[serviceMode]}
📅 *Fecha Tentativa:* ${eventDate || 'Por coordinar'} a las ${eventTime}

💰 *Estimación Total:* $${estimatedTotal.toFixed(2)}
${specialNotes ? `📝 *Observaciones:* ${specialNotes}\n` : ''}
*Requerimos atención prioritaria y propuesta formal en PDF.*`;

    window.open(`https://wa.me/50762345678?text=${encodeURIComponent(msg)}`, '_blank');
    setAlertSent(true);
  };

  // Dual Dispatch: Email formal
  const handleSendCorporateMail = () => {
    const subject = `Solicitud de Cotización B2B - ${companyName || 'Empresa'} - ${exactPax} Platos`;
    const body = `Estimado equipo de Ventas Corporativas Eat & Go,

Por medio de la presente solicito formalmente cotización para el siguiente requerimiento:

1. DATOS DE LA EMPRESA / INSTITUCIÓN:
- Empresa: ${companyName}
- RUC / DV: ${ruc}
- Contacto: ${contactPerson}
- Teléfono: ${phone}
- Correo Electrónico: ${corporateEmail}

2. DETALLES DEL EVENTO / SERVICIO:
- Tipo de evento: ${eventTypeLabels[eventType]}
- Cantidad de comensales: ${exactPax} personas
- Presupuesto estimado por plato: $${budgetPerPlate.toFixed(2)}
- Modalidad de presentación: ${serviceModeLabels[serviceMode]}
- Fecha estimada: ${eventDate || 'A coordinar'} - Hora: ${eventTime}
- Inversión total proyectada: $${estimatedTotal.toFixed(2)}

3. REQUERIMIENTOS ESPECIALES:
${specialNotes || 'Ninguno especificado'}

Agradecemos nos remitan la propuesta con desglose de menú, tiempo de despacho y datos para orden de compra o Panamá Compra.

Atentamente,
${contactPerson || companyName}`;

    window.location.href = `mailto:cotizaciones@eatandgo.pa?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    setShowMailModal(true);
  };

  const handleAddQuickPackage = (pkg: typeof CORPORATE_PACKAGES[0]) => {
    onAddToCart({
      dishId: pkg.id,
      name: pkg.name,
      basePrice: pkg.price,
      unitPrice: pkg.price,
      quantity: 1,
      selectedSide: `${pkg.servings} personas`,
      notes: `Paquete corporativo (${pkg.servings} comensales) con entrega programada`,
      totalPrice: pkg.price,
    });
    setAddedPkgId(pkg.id);
    setTimeout(() => setAddedPkgId(null), 2500);
  };

  return (
    <div className="space-y-10 pb-16">
      {/* ========================================================================= */}
      {/* 1. HERO B2B & PROPUESTA DE VALOR CORPORATIVA                              */}
      {/* ========================================================================= */}
      <div className="bg-stone-900 text-white rounded-2xl sm:rounded-3xl p-6 sm:p-10 border border-stone-800 shadow-xl">
        <div className="max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-black uppercase tracking-wider mb-3 border border-amber-500/30">
            <Building2 className="w-3.5 h-3.5 text-amber-400" />
            <span>CATERING B2B • LICITACIONES PANAMÁ COMPRA (100 A 700+ PLATOS)</span>
          </div>
          
          <h1 className="text-2xl sm:text-4xl md:text-5xl font-black tracking-tight leading-tight">
            El Estándar Corporativo de Comida Criolla en Panamá
          </h1>
          
          <p className="mt-3 text-stone-300 text-xs sm:text-base leading-relaxed">
            Abastecemos grandes corporaciones, bancos, multinacionales y entidades del Estado con <strong>capacidad probada de 100 a 700+ platos en simultáneo</strong>. Cero regueros con nuestras nuevas cajas troqueladas térmicas a 75°C o estaciones de buffet asistido con rechauds.
          </p>

          {/* Sellos de Confianza B2B */}
          <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
            <div className="flex items-center gap-2.5 bg-stone-800/80 p-3 rounded-xl border border-stone-700">
              <Clock className="w-5 h-5 text-amber-400 shrink-0" />
              <div className="text-xs">
                <span className="font-bold text-stone-100 block">Puntualidad 100%</span>
                <span className="text-stone-400 text-[11px]">Despacho en flota térmica</span>
              </div>
            </div>

            <div className="flex items-center gap-2.5 bg-stone-800/80 p-3 rounded-xl border border-stone-700">
              <ShieldCheck className="w-5 h-5 text-emerald-400 shrink-0" />
              <div className="text-xs">
                <span className="font-bold text-stone-100 block">Higiene MINSA</span>
                <span className="text-stone-400 text-[11px]">Carné blanco y verde</span>
              </div>
            </div>

            <div className="flex items-center gap-2.5 bg-stone-800/80 p-3 rounded-xl border border-stone-700">
              <PackageCheck className="w-5 h-5 text-amber-400 shrink-0" />
              <div className="text-xs">
                <span className="font-bold text-stone-100 block">Cajas Troqueladas</span>
                <span className="text-stone-400 text-[11px]">Compartimentos a 75°C</span>
              </div>
            </div>

            <div className="flex items-center gap-2.5 bg-stone-800/80 p-3 rounded-xl border border-stone-700">
              <Receipt className="w-5 h-5 text-emerald-400 shrink-0" />
              <div className="text-xs">
                <span className="font-bold text-stone-100 block">Panamá Compra</span>
                <span className="text-stone-400 text-[11px]">RUC, DV y Paz y Salvo</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* 2. CALCULADORA INTERACTIVA / FORMULARIO DE COTIZACIÓN EXCLUSIVO B2B       */}
      {/* ========================================================================= */}
      <section className="bg-white rounded-2xl sm:rounded-3xl border border-stone-200/90 p-6 sm:p-10 shadow-xs">
        <div className="mb-8">
          <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800 mb-1">
            <Calculator className="w-4 h-4 text-amber-700" />
            <span>CALCULADORA DE VOLUMEN EN TIEMPO REAL</span>
          </div>
          <h2 className="text-2xl sm:text-3xl font-black text-stone-900 tracking-tight">
            Calcula tu Cotización Institucional (100 a 700 Platos)
          </h2>
          <p className="text-xs sm:text-sm text-stone-600 mt-1">
            Configura los parámetros de tu evento o licitación y obtén un estimado inmediato con opción de envío dual (Correo Formal + Alerta WhatsApp).
          </p>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* Columna Izquierda: Parámetros */}
          <div className="lg:col-span-7 space-y-6">
            {/* 1. Tipo de Evento */}
            <div>
              <label className="text-xs font-bold text-stone-900 uppercase tracking-wider block mb-2">
                1. Tipo de Evento o Contrato:
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                {[
                  { id: 'ejecutivo', title: 'Reunión Ejecutiva', desc: 'Directorio y comités' },
                  { id: 'capacitacion', title: 'Almuerzo Corporativo', desc: 'Capacitaciones masivas' },
                  { id: 'licitacion', title: 'Licitación Estatal', desc: 'Panamá Compra / Gob.' },
                  { id: 'findeano', title: 'Fiesta Fin de Año', desc: 'Gala y banquetes' }
                ].map((item) => (
                  <button
                    key={item.id}
                    type="button"
                    onClick={() => setEventType(item.id as any)}
                    className={`p-3 rounded-xl border text-left transition-all ${
                      eventType === item.id
                        ? 'border-amber-500 bg-amber-50/60 ring-2 ring-amber-400'
                        : 'border-stone-200 bg-white hover:bg-stone-50'
                    }`}
                  >
                    <span className="text-xs font-black text-stone-900 block">{item.title}</span>
                    <span className="text-[11px] text-stone-500">{item.desc}</span>
                  </button>
                ))}
              </div>
            </div>

            {/* 2. Rango de Personas */}
            <div>
              <div className="flex items-center justify-between mb-2">
                <label className="text-xs font-bold text-stone-900 uppercase tracking-wider">
                  2. Rango de Personas:
                </label>
                <span className="text-xs font-black text-amber-800 bg-amber-100 px-2.5 py-0.5 rounded-full">
                  {exactPax} Comensales
                </span>
              </div>

              {/* Botones de Rango Rápido */}
              <div className="grid grid-cols-3 gap-2 mb-3">
                {[
                  { id: '50-100', label: '50 – 100 pax' },
                  { id: '100-300', label: '100 – 300 pax' },
                  { id: '500+', label: '+500 pax' }
                ].map((r) => (
                  <button
                    key={r.id}
                    type="button"
                    onClick={() => handleRangeChange(r.id as any)}
                    className={`py-2 px-3 rounded-xl text-xs font-black border transition-all text-center ${
                      peopleRange === r.id
                        ? 'bg-stone-900 text-amber-400 border-stone-900 shadow-xs'
                        : 'bg-stone-50 text-stone-700 border-stone-200 hover:bg-stone-100'
                    }`}
                  >
                    {r.label}
                  </button>
                ))}
              </div>

              {/* Slider de Pax */}
              <input
                type="range"
                min="50"
                max="750"
                step="25"
                value={exactPax}
                onChange={(e) => setExactPax(Number(e.target.value))}
                className="w-full accent-amber-500 cursor-pointer"
              />
              <div className="flex justify-between text-[10px] text-stone-400 mt-1">
                <span>50 Platos</span>
                <span>350 Platos</span>
                <span>750+ Platos</span>
              </div>
            </div>

            {/* 3. Presupuesto por Plato */}
            <div>
              <label className="text-xs font-bold text-stone-900 uppercase tracking-wider block mb-2">
                3. Presupuesto Estimado por Plato:
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-2">
                {[
                  { val: 6.50, title: 'Económico Criollo', desc: '$6.50 / plato' },
                  { val: 8.75, title: 'Ejecutivo Completo', desc: '$8.75 (Con chicha y postre)' },
                  { val: 12.50, title: 'Premium Gala Buffet', desc: '$12.50 (2 proteínas)' }
                ].map((b) => (
                  <button
                    key={b.val}
                    type="button"
                    onClick={() => setBudgetPerPlate(b.val)}
                    className={`p-3 rounded-xl border text-left transition-all ${
                      budgetPerPlate === b.val
                        ? 'border-amber-500 bg-amber-50/60 ring-2 ring-amber-400'
                        : 'border-stone-200 bg-white hover:bg-stone-50'
                    }`}
                  >
                    <span className="text-xs font-black text-stone-900 block">{b.title}</span>
                    <span className="text-[11px] font-bold text-amber-700">{b.desc}</span>
                  </button>
                ))}
              </div>
            </div>

            {/* 4. Modalidad de Presentación */}
            <div>
              <label className="text-xs font-bold text-stone-900 uppercase tracking-wider block mb-2">
                4. Presentación y Servicio:
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
                <button
                  type="button"
                  onClick={() => setServiceMode('cajas-troqueladas')}
                  className={`p-3 rounded-xl border text-left transition-all flex items-start gap-2.5 ${
                    serviceMode === 'cajas-troqueladas'
                      ? 'border-amber-500 bg-amber-50/60 ring-2 ring-amber-400'
                      : 'border-stone-200 bg-white hover:bg-stone-50'
                  }`}
                >
                  <PackageCheck className="w-5 h-5 text-amber-700 shrink-0 mt-0.5" />
                  <div>
                    <span className="text-xs font-black text-stone-900 block">Cajas Troqueladas 75°C</span>
                    <span className="text-[11px] text-stone-500">Individuales, limpias y listas para comer</span>
                  </div>
                </button>

                <button
                  type="button"
                  onClick={() => setServiceMode('buffet-rechauds')}
                  className={`p-3 rounded-xl border text-left transition-all flex items-start gap-2.5 ${
                    serviceMode === 'buffet-rechauds'
                      ? 'border-amber-500 bg-amber-50/60 ring-2 ring-amber-400'
                      : 'border-stone-200 bg-white hover:bg-stone-50'
                  }`}
                >
                  <Sparkles className="w-5 h-5 text-amber-700 shrink-0 mt-0.5" />
                  <div>
                    <span className="text-xs font-black text-stone-900 block">Buffet con Rechauds</span>
                    <span className="text-[11px] text-stone-500">Acero inoxidable con personal de servicio</span>
                  </div>
                </button>
              </div>
            </div>

            {/* 5. Selector de Fecha y Hora */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
              <div>
                <label className="text-xs font-bold text-stone-900 uppercase tracking-wider block mb-1">
                  Fecha del Evento:
                </label>
                <input
                  type="date"
                  value={eventDate}
                  onChange={(e) => setEventDate(e.target.value)}
                  className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-800 font-medium"
                />
              </div>

              <div>
                <label className="text-xs font-bold text-stone-900 uppercase tracking-wider block mb-1">
                  Hora de Entrega Deseada:
                </label>
                <select
                  value={eventTime}
                  onChange={(e) => setEventTime(e.target.value)}
                  className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-800 font-medium"
                >
                  <option value="11:30 AM">11:30 AM (Turno Temprano)</option>
                  <option value="12:00 PM">12:00 PM (Almuerzo Corporativo)</option>
                  <option value="12:30 PM">12:30 PM</option>
                  <option value="1:00 PM">1:00 PM</option>
                  <option value="6:30 PM">6:30 PM (Cena o Gala)</option>
                </select>
              </div>
            </div>

            {/* Datos del Cliente y Empresa */}
            <div className="pt-4 border-t border-stone-200 space-y-3">
              <span className="text-xs font-black text-stone-900 uppercase tracking-wider block">
                Datos de la Empresa o Institución:
              </span>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                <input
                  type="text"
                  placeholder="Nombre de Empresa / Razón Social *"
                  value={companyName}
                  onChange={(e) => setCompanyName(e.target.value)}
                  className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-900 placeholder-stone-400 font-medium"
                />

                <input
                  type="text"
                  placeholder="RUC y DV (Ej: 155678-1-658890 DV 45)"
                  value={ruc}
                  onChange={(e) => setRuc(e.target.value)}
                  className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-900 placeholder-stone-400 font-medium"
                />
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                <input
                  type="text"
                  placeholder="Persona de Contacto"
                  value={contactPerson}
                  onChange={(e) => setContactPerson(e.target.value)}
                  className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-900 placeholder-stone-400"
                />

                <input
                  type="tel"
                  placeholder="Teléfono / WhatsApp *"
                  value={phone}
                  onChange={(e) => setPhone(e.target.value)}
                  className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-900 placeholder-stone-400"
                />

                <input
                  type="email"
                  placeholder="Correo Corporativo"
                  value={corporateEmail}
                  onChange={(e) => setCorporateEmail(e.target.value)}
                  className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-900 placeholder-stone-400"
                />
              </div>

              <textarea
                rows={2}
                placeholder="Notas adicionales: Alergias, ubicación del evento, requerimiento de crédito 30 días, etc."
                value={specialNotes}
                onChange={(e) => setSpecialNotes(e.target.value)}
                className="w-full bg-stone-50 border border-stone-200 rounded-xl p-2.5 text-xs text-stone-900 placeholder-stone-400"
              />
            </div>
          </div>

          {/* Columna Derecha: Resumen de Cotización & ENVÍO DUAL */}
          <div className="lg:col-span-5 bg-stone-900 text-white rounded-2xl p-6 sm:p-7 border border-stone-800 space-y-6">
            <div className="border-b border-stone-800 pb-4">
              <span className="text-[10px] font-black uppercase tracking-widest text-amber-400 block">
                PRESUPUESTO PRELIMINAR B2B
              </span>
              <h3 className="text-xl font-black text-white mt-1">
                Desglose de Cotización
              </h3>
            </div>

            <div className="space-y-3 text-xs">
              <div className="flex justify-between text-stone-300">
                <span>Comensales / Platos:</span>
                <span className="font-bold text-white">{exactPax} unidades</span>
              </div>

              <div className="flex justify-between text-stone-300">
                <span>Presupuesto por plato:</span>
                <span className="font-bold text-white">${budgetPerPlate.toFixed(2)}</span>
              </div>

              <div className="flex justify-between text-stone-300">
                <span>Subtotal Comida:</span>
                <span className="font-bold text-white">${subtotalPlates.toFixed(2)}</span>
              </div>

              {serviceMode === 'buffet-rechauds' && (
                <div className="flex justify-between text-stone-300">
                  <span>Rechauds & Personal asistido:</span>
                  <span className="font-bold text-amber-400">+${packagingFee.toFixed(2)}</span>
                </div>
              )}

              {volumeDiscountRate > 0 && (
                <div className="flex justify-between text-emerald-400 font-bold">
                  <span>Descuento por Volumen ({(volumeDiscountRate * 100)}%):</span>
                  <span>-${volumeDiscount.toFixed(2)}</span>
                </div>
              )}

              <div className="pt-3 border-t border-stone-800 flex justify-between items-baseline">
                <span className="text-sm font-black text-stone-200">Total Proyectado:</span>
                <span className="text-2xl font-black text-amber-400">
                  ${estimatedTotal.toFixed(2)}
                </span>
              </div>
              <span className="text-[10px] text-stone-400 block text-right">
                *Precios sujetos a confirmación formal de menú y factura fiscal.
              </span>
            </div>

            {/* ========================================================================= */}
            {/* ENVÍO DUAL: CORREO FORMAL + ALERTA WHATSAPP                              */}
            {/* ========================================================================= */}
            <div className="space-y-3 pt-2">
              <span className="text-[11px] font-black uppercase tracking-wider text-stone-300 block">
                Envío Dual de Propuesta:
              </span>

              {/* Canal 1: Correo Formal */}
              <button
                type="button"
                onClick={handleSendCorporateMail}
                className="w-full py-3 px-4 rounded-xl bg-stone-800 hover:bg-stone-700 text-stone-100 font-bold text-xs flex items-center justify-center gap-2 border border-stone-600 transition-all active:scale-95"
              >
                <Mail className="w-4 h-4 text-amber-400" />
                <span>1. Enviar Solicitud Formal por Correo (PDF / RUC)</span>
              </button>

              {/* Canal 2: Alerta Inmediata a WhatsApp */}
              <button
                type="button"
                onClick={handleSendWhatsAppAlert}
                className="w-full py-3 px-4 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-stone-950 font-black text-xs flex items-center justify-center gap-2 shadow-lg transition-all active:scale-95"
              >
                <Send className="w-4 h-4 fill-current" />
                <span>2. Alerta Prioritaria a WhatsApp de Gerencia B2B</span>
              </button>

              {alertSent && (
                <div className="p-3 bg-emerald-950/80 border border-emerald-600 rounded-xl text-center text-xs text-emerald-300 flex items-center justify-center gap-1.5">
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                  <span>Alerta enviada a Gerencia. Respuesta en &lt;15 mins.</span>
                </div>
              )}
            </div>

            <div className="p-3.5 bg-stone-950 rounded-xl border border-stone-800 text-[11px] text-stone-400 space-y-1">
              <span className="font-bold text-stone-200 block">¿Licitación en Panamá Compra?</span>
              <p>
                Aceptamos órdenes de compra estatales con pago a 30/60 días una vez validado el paz y salvo de DGI y CSS.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. COMBOS PRE-DISEÑADOS DE OFICINA (5 A 20 PERSONAS)                      */}
      {/* ========================================================================= */}
      <div>
        <div className="mb-6">
          <span className="text-[11px] font-black uppercase tracking-widest text-amber-800 block">
            DESPACHO RÁPIDO PARA GRUPOS PEQUEÑOS
          </span>
          <h2 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
            Combos de Oficina Listos para Agregar a la Comanda
          </h2>
          <p className="text-xs sm:text-sm text-stone-600 mt-1">
            Si tu grupo es menor de 50 personas, puedes seleccionar estos combos y agregarlos directamente al carrito de compras.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          {CORPORATE_PACKAGES.map((pkg) => (
            <div
              key={pkg.id}
              className="bg-white rounded-2xl border border-stone-200 overflow-hidden flex flex-col justify-between shadow-xs hover:border-amber-400 transition-all"
            >
              <div>
                <div className="h-44 bg-stone-100 relative">
                  <img
                    src={pkg.image}
                    alt={pkg.name}
                    className="w-full h-full object-cover"
                    referrerPolicy="no-referrer"
                  />
                  <span className="absolute bottom-2.5 right-2.5 bg-stone-950 text-amber-400 font-black text-base px-3 py-1 rounded-lg shadow-sm">
                    ${pkg.price.toFixed(2)}
                  </span>
                  <span className="absolute top-2.5 left-2.5 bg-white text-stone-950 text-xs font-black px-2.5 py-1 rounded-md shadow-xs flex items-center gap-1">
                    <Users className="w-3.5 h-3.5" />
                    {pkg.servings} {pkg.servings === 1 ? 'Persona' : 'Personas'}
                  </span>
                </div>

                <div className="p-5">
                  <h3 className="font-black text-stone-900 text-lg">{pkg.name}</h3>
                  <p className="text-xs text-stone-600 mt-1.5 leading-relaxed">{pkg.description}</p>
                  
                  <div className="mt-3.5 pt-3 border-t border-stone-100 space-y-1">
                    <span className="text-[11px] font-bold text-stone-700 block">Incluye:</span>
                    {pkg.includes.map((it, i) => (
                      <div key={i} className="flex items-center gap-1.5 text-xs text-stone-600">
                        <Check className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                        <span>{it}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              <div className="p-5 pt-0">
                <button
                  onClick={() => handleAddQuickPackage(pkg)}
                  className={`w-full py-2.5 px-4 rounded-xl font-black text-xs flex items-center justify-center gap-2 transition-all shadow-sm ${
                    addedPkgId === pkg.id
                      ? 'bg-emerald-600 text-white'
                      : 'bg-amber-500 hover:bg-amber-400 text-stone-950 active:scale-95'
                  }`}
                >
                  {addedPkgId === pkg.id ? (
                    <>
                      <CheckCircle2 className="w-4 h-4 text-white" />
                      <span>¡Agregado a la Comanda!</span>
                    </>
                  ) : (
                    <>
                      <ShoppingBag className="w-4 h-4" />
                      <span>Agregar al Pedido (${pkg.price.toFixed(2)})</span>
                    </>
                  )}
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

import React, { useState } from 'react';
import { 
  MapPin, 
  Clock, 
  PhoneCall, 
  Send, 
  Utensils, 
  PackageCheck, 
  Navigation, 
  Building2, 
  ShieldCheck, 
  CheckCircle2, 
  ExternalLink,
  Car,
  Mail,
  MessageSquare
} from 'lucide-react';

export const ContactLocationView: React.FC = () => {
  const [formData, setFormData] = useState({
    nombre: '',
    telefono: '',
    asunto: 'retiro',
    mensaje: '',
  });
  const [sentSuccess, setSentSuccess] = useState(false);

  const handleSubmitMessage = (e: React.FormEvent) => {
    e.preventDefault();
    const whatsappMsg = `*MENSAJE DESDE WEB EAT & GO*\n👤 *Nombre:* ${formData.nombre}\n📱 *Teléfono:* ${formData.telefono}\n📌 *Asunto:* ${formData.asunto}\n💬 *Mensaje:* ${formData.mensaje}`;
    window.open(`https://wa.me/50762345678?text=${encodeURIComponent(whatsappMsg)}`, '_blank');
    setSentSuccess(true);
    setTimeout(() => setSentSuccess(false), 3500);
  };

  const deliveryZones = [
    { zone: 'Obarrio & Calle 50', time: '15 - 20 min', price: '$1.50' },
    { zone: 'Marbella & Balboa', time: '15 - 25 min', price: '$1.50' },
    { zone: 'San Francisco & Vía Porras', time: '20 - 25 min', price: '$2.00' },
    { zone: 'Punta Pacífica & Paitilla', time: '20 - 30 min', price: '$2.00' },
    { zone: 'Costa del Este', time: 'Programado 12:00 MD', price: '$2.50' },
    { zone: 'Mostrador Pick & Go (Retiro)', time: 'Listo en 10 min (0 Filas)', price: 'Gratis ($0.00)' },
  ];

  return (
    <div className="space-y-10 sm:space-y-12 pb-16">
      {/* ========================================================================= */}
      {/* 1. CABECERA: DÓNDE COMER Y RETIRAR PEDIDOS                                */}
      {/* ========================================================================= */}
      <div className="bg-stone-900 text-white rounded-2xl sm:rounded-3xl p-6 sm:p-10 border border-stone-800">
        <div className="max-w-3xl">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-bold uppercase tracking-wider mb-3">
            <MapPin className="w-3.5 h-3.5" />
            <span>Sede Central • Zona Bancaria, Panamá</span>
          </div>
          <h1 className="text-2xl sm:text-4xl font-black tracking-tight">
            Dónde Comer y Retirar Tus Pedidos
          </h1>
          <p className="mt-2 text-stone-300 text-xs sm:text-base leading-relaxed">
            Disfruta de la mejor cocina criolla panameña en nuestro comedor climatizado o retira tu comida caliente en 30 segundos en nuestro mostrador express <strong>Pick & Go</strong> sin hacer filas.
          </p>
        </div>

        {/* Badges rápidos */}
        <div className="mt-6 flex flex-wrap gap-3 text-xs font-bold text-stone-200">
          <div className="flex items-center gap-1.5 bg-stone-800 px-3 py-1.5 rounded-lg border border-stone-700">
            <Utensils className="w-4 h-4 text-amber-400" />
            <span>Salón con A/C Climatizado</span>
          </div>
          <div className="flex items-center gap-1.5 bg-stone-800 px-3 py-1.5 rounded-lg border border-stone-700">
            <PackageCheck className="w-4 h-4 text-emerald-400" />
            <span>Mostrador Pick & Go Cero Filas</span>
          </div>
          <div className="flex items-center gap-1.5 bg-stone-800 px-3 py-1.5 rounded-lg border border-stone-700">
            <Car className="w-4 h-4 text-amber-400" />
            <span>Estacionamiento de Cortesía</span>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* 2. DOS MODALIDADES PRESENCIALES: COMEDOR vs RETIRO PICK & GO               */}
      {/* ========================================================================= */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Opción A: Ir a Comer al Local */}
        <div className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200 shadow-xs flex flex-col justify-between">
          <div>
            <div className="w-12 h-12 rounded-2xl bg-amber-500/15 border border-amber-500/30 text-amber-700 flex items-center justify-center mb-4">
              <Utensils className="w-6 h-6" />
            </div>

            <div className="flex items-center gap-2 mb-1">
              <span className="text-[10px] uppercase font-black px-2 py-0.5 rounded bg-amber-100 text-amber-800">
                Opción Presencial
              </span>
              <span className="text-xs text-stone-500 font-semibold">Salón Climatizado</span>
            </div>

            <h2 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
              Visítanos en Nuestro Comedor
            </h2>

            <p className="text-xs sm:text-sm text-stone-600 mt-2 leading-relaxed">
              Un espacio moderno, limpio y con aire acondicionado diseñado para que los colaboradores y ejecutivos de la Zona Bancaria almuercen cómodamente paila criolla servida al momento.
            </p>

            <ul className="mt-5 space-y-2.5 text-xs text-stone-700">
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <span><strong>Horario de Almuerzos:</strong> Lunes a Viernes 11:30 AM a 3:30 PM</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <span><strong>Horario de Desayunos:</strong> Lunes a Sábado 6:30 AM a 11:00 AM</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <span><strong>Mesas individuales y grupales</strong> con servicio rápido de paila.</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0 mt-0.5" />
                <span><strong>Wi-Fi gratuito</strong> y tomas de corriente en barra para laptop.</span>
              </li>
            </ul>
          </div>

          <div className="mt-6 pt-5 border-t border-stone-100">
            <a
              href="https://maps.google.com/?q=Calle+50+Torre+Banco+de+Panama+Obarrio"
              target="_blank"
              rel="noopener noreferrer"
              className="w-full py-2.5 px-4 bg-stone-900 hover:bg-stone-800 text-white rounded-xl text-xs font-bold flex items-center justify-center gap-2 transition-colors"
            >
              <Navigation className="w-4 h-4 text-amber-400" />
              <span>Cómo Llegar al Comedor (Google Maps)</span>
            </a>
          </div>
        </div>

        {/* Opción B: Retiro Express Pick & Go */}
        <div className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-amber-200 shadow-xs flex flex-col justify-between bg-gradient-to-b from-amber-50/40 to-white">
          <div>
            <div className="w-12 h-12 rounded-2xl bg-emerald-500/15 border border-emerald-500/30 text-emerald-700 flex items-center justify-center mb-4">
              <PackageCheck className="w-6 h-6" />
            </div>

            <div className="flex items-center gap-2 mb-1">
              <span className="text-[10px] uppercase font-black px-2 py-0.5 rounded bg-emerald-100 text-emerald-800">
                Retiro Express
              </span>
              <span className="text-xs text-stone-500 font-semibold">Listo en 10-15 min</span>
            </div>

            <h2 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
              Mostrador Pick & Go (Cero Filas)
            </h2>

            <p className="text-xs sm:text-sm text-stone-600 mt-2 leading-relaxed">
              ¿Poco tiempo de almuerzo? Pide desde tu celular antes de bajar del piso de tu oficina. Cuando llegues, tu comanda estará empacada y rotulada con tu nombre en el mostrador rápido.
            </p>

            <div className="mt-5 space-y-3">
              <div className="flex items-start gap-3 bg-white p-3 rounded-xl border border-stone-200/80">
                <span className="w-6 h-6 rounded-full bg-amber-500 text-stone-950 font-black text-xs flex items-center justify-center shrink-0">1</span>
                <p className="text-xs text-stone-700"><strong>Pides por la Web o WhatsApp:</strong> Indicas retiro Pick & Go y tu nombre.</p>
              </div>

              <div className="flex items-start gap-3 bg-white p-3 rounded-xl border border-stone-200/80">
                <span className="w-6 h-6 rounded-full bg-amber-500 text-stone-950 font-black text-xs flex items-center justify-center shrink-0">2</span>
                <p className="text-xs text-stone-700"><strong>Empacamos a 75°C:</strong> En bolsa térmica sellada para mantener el calor.</p>
              </div>

              <div className="flex items-start gap-3 bg-white p-3 rounded-xl border border-stone-200/80">
                <span className="w-6 h-6 rounded-full bg-amber-500 text-stone-950 font-black text-xs flex items-center justify-center shrink-0">3</span>
                <p className="text-xs text-stone-700"><strong>Llegas y retiras:</strong> Muestras tu confirmación, tomas tu paquete y listo.</p>
              </div>
            </div>
          </div>

          <div className="mt-6 pt-5 border-t border-amber-200/60">
            <a
              href="https://wa.me/50762345678?text=Hola%20Eat%20%26%20Go!%20Quiero%20hacer%20un%20pedido%20para%20retiro%20Pick%20%26%20Go%20en%2015%20minutos."
              target="_blank"
              rel="noopener noreferrer"
              className="w-full py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold flex items-center justify-center gap-2 transition-colors shadow-xs"
            >
              <Send className="w-4 h-4 fill-current" />
              <span>Pedir para Retiro Inmediato por WhatsApp</span>
            </a>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* 2.1 HORARIOS DETALLADOS Y MÉTODOS DE PAGO (YAPPY, CLAVE, EFECTIVO, VISA)   */}
      {/* ========================================================================= */}
      <div className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200/90 shadow-xs">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Horario Detallado */}
          <div className="space-y-4">
            <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800">
              <Clock className="w-4 h-4 text-amber-700" />
              <span>Horario de Atención y Cocina en Vivo</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
              Turnos de Servicio Diario
            </h3>
            <p className="text-xs sm:text-sm text-stone-600 leading-relaxed">
              Cocinamos en dos tandas frescas cada día para asegurar sabor y textura crujiente:
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
              <div className="p-4 rounded-xl bg-amber-50/80 border border-amber-200/80 space-y-1">
                <span className="text-[10px] font-black uppercase text-amber-900 tracking-wider block">
                  🌅 Turno Mañana
                </span>
                <span className="font-black text-stone-900 text-sm block">Desayunos Criollos</span>
                <span className="text-xs font-bold text-amber-800 block">6:30 AM – 11:00 AM</span>
                <p className="text-[11px] text-stone-600">Hojaldres, carimañolas, tortillas y bistec picado al momento.</p>
              </div>

              <div className="p-4 rounded-xl bg-stone-900 text-white border border-stone-800 space-y-1">
                <span className="text-[10px] font-black uppercase text-amber-400 tracking-wider block">
                  🍲 Turno Mediodía
                </span>
                <span className="font-black text-white text-sm block">Almuerzos de Paila</span>
                <span className="text-xs font-bold text-amber-300 block">11:30 AM – 3:00 PM</span>
                <p className="text-[11px] text-stone-300">Guisos del día, sancochos y mondongos calientes a 75°C.</p>
              </div>
            </div>
          </div>

          {/* Métodos de Pago Aceptados con Yappy destacado */}
          <div className="space-y-4">
            <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-emerald-800">
              <ShieldCheck className="w-4 h-4 text-emerald-700" />
              <span>Transacciones Rápidas y Transparentes</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
              Métodos de Pago Aceptados
            </h3>
            <p className="text-xs sm:text-sm text-stone-600 leading-relaxed">
              Aceptamos los principales métodos de pago de Panamá, tanto para retiro Pick & Go, consumo en comedor o delivery a oficinas:
            </p>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 pt-1">
              {/* Yappy */}
              <div className="p-3 rounded-xl bg-sky-50 border border-sky-200 flex flex-col items-center text-center">
                <div className="w-10 h-10 rounded-lg bg-sky-500 text-white font-black text-xs flex items-center justify-center shadow-xs mb-1.5">
                  Yappy
                </div>
                <span className="font-black text-xs text-sky-950">Yappy</span>
                <span className="text-[10px] text-sky-800">@eatandgopa</span>
              </div>

              {/* Efectivo */}
              <div className="p-3 rounded-xl bg-emerald-50 border border-emerald-200 flex flex-col items-center text-center">
                <div className="w-10 h-10 rounded-lg bg-emerald-600 text-white font-black text-sm flex items-center justify-center shadow-xs mb-1.5">
                  💵
                </div>
                <span className="font-black text-xs text-emerald-950">Efectivo</span>
                <span className="text-[10px] text-emerald-800">Dólares (USD)</span>
              </div>

              {/* Tarjeta Clave */}
              <div className="p-3 rounded-xl bg-amber-50 border border-amber-200 flex flex-col items-center text-center">
                <div className="w-10 h-10 rounded-lg bg-amber-500 text-stone-950 font-black text-xs flex items-center justify-center shadow-xs mb-1.5">
                  CLAVE
                </div>
                <span className="font-black text-xs text-amber-950">Tarjeta Clave</span>
                <span className="text-[10px] text-amber-800">Débito Local</span>
              </div>

              {/* Visa & Mastercard */}
              <div className="p-3 rounded-xl bg-stone-100 border border-stone-200 flex flex-col items-center text-center">
                <div className="w-10 h-10 rounded-lg bg-stone-900 text-white font-black text-[10px] flex items-center justify-center shadow-xs mb-1.5">
                  VISA/MC
                </div>
                <span className="font-black text-xs text-stone-900">Visa / MC</span>
                <span className="text-[10px] text-stone-600">Crédito y Débito</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200 shadow-xs">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
          {/* Datos de Dirección */}
          <div className="lg:col-span-6 space-y-4">
            <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800">
              <MapPin className="w-4 h-4 text-amber-700" />
              <span>Dirección Exacta</span>
            </div>

            <h3 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
              Torre Banco de Panamá, Planta Baja
            </h3>

            <p className="text-xs sm:text-sm text-stone-600 leading-relaxed">
              <strong>Ubicación:</strong> Calle 50 cruce con Calle 53 Este, Local 2 (Planta Baja), Obarrio, Corregimiento de Bella Vista, Ciudad de Panamá.
            </p>

            <div className="p-4 rounded-xl bg-stone-50 border border-stone-200 space-y-2 text-xs text-stone-700">
              <p className="font-bold text-stone-900">Puntos de Referencia:</p>
              <ul className="space-y-1 text-stone-600">
                <li>• Justo al frente del Banco General de Calle 50.</li>
                <li>• A 250 metros de la estación de Metro Iglesia del Carmen (Salida Calle 50).</li>
                <li>• Diagonal a Torre Credicorp Bank y Soho Mall.</li>
                <li>• Acceso fácil por Calle 50, Calle 53 Obarrio y Vía España.</li>
              </ul>
            </div>

            <div className="flex flex-wrap gap-3 pt-2">
              <a
                href="https://maps.google.com/?q=Calle+50+Torre+Banco+de+Panama+Obarrio"
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-2.5 rounded-xl bg-stone-900 hover:bg-stone-800 text-white font-bold text-xs flex items-center gap-2"
              >
                <Navigation className="w-3.5 h-3.5 text-amber-400" />
                <span>Abrir en Google Maps</span>
              </a>

              <a
                href="https://waze.com/ul?q=Calle+50+Obarrio+Panama"
                target="_blank"
                rel="noopener noreferrer"
                className="px-4 py-2.5 rounded-xl bg-sky-500 hover:bg-sky-400 text-white font-bold text-xs flex items-center gap-2"
              >
                <ExternalLink className="w-3.5 h-3.5" />
                <span>Navegar con Waze</span>
              </a>
            </div>
          </div>

          {/* Tarjeta Visual de Mapa / Croquis */}
          <div className="lg:col-span-6">
            <div className="w-full h-72 sm:h-80 rounded-2xl overflow-hidden border border-stone-200 relative shadow-inner bg-stone-100 flex items-center justify-center">
              {/* Imagen aérea de referencia de Ciudad de Panamá */}
              <img
                src="https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=1000&q=80"
                alt="Ubicación Eat and Go Calle 50"
                className="w-full h-full object-cover filter brightness-90 contrast-110"
                referrerPolicy="no-referrer"
              />

              {/* Pin flotante interactivo */}
              <div className="absolute inset-0 bg-stone-950/40 backdrop-blur-[2px] flex flex-col items-center justify-center p-6 text-center text-white">
                <div className="w-14 h-14 rounded-2xl bg-amber-500 text-stone-950 flex items-center justify-center shadow-2xl animate-bounce mb-3">
                  <MapPin className="w-8 h-8 fill-current" />
                </div>
                <span className="font-black text-lg text-white">EAT & GO Criollo Express</span>
                <span className="text-xs text-stone-200 mt-0.5">Calle 50 & Obarrio • Torre Banco de Panamá (PB)</span>
                <span className="mt-3 text-[11px] font-bold bg-stone-900/90 text-amber-400 px-3 py-1 rounded-full border border-amber-400/30">
                  Salón Climatizado & Mostrador Pick & Go
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* 4. ZONAS DE DESPACHO A OFICINAS & DELIVERY                                */}
      {/* ========================================================================= */}
      <div className="bg-stone-50 rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200">
        <div className="max-w-2xl mb-6">
          <h3 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
            Cobertura de Despacho a Oficinas (Delivery)
          </h3>
          <p className="text-xs sm:text-sm text-stone-600 mt-1">
            Si prefieres no salir de tu cubículo, nuestros motorizados llevan tu comida caliente hasta la recepción o lobby de tu edificio.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5">
          {deliveryZones.map((zone, idx) => (
            <div
              key={idx}
              className="bg-white rounded-xl p-4 border border-stone-200 flex items-center justify-between"
            >
              <div>
                <h4 className="font-bold text-xs sm:text-sm text-stone-900">{zone.zone}</h4>
                <p className="text-[11px] text-stone-500 mt-0.5 flex items-center gap-1">
                  <Clock className="w-3 h-3 text-amber-600" />
                  <span>{zone.time}</span>
                </p>
              </div>
              <span className="text-xs font-black text-amber-800 bg-amber-50 px-2 py-1 rounded-lg border border-amber-200">
                {zone.price}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* ========================================================================= */}
      {/* 5. CANALES DIRECTOS DE CONTACTO & FORMULARIO DE MENSAJE                   */}
      {/* ========================================================================= */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
        {/* Canales Directos */}
        <div className="lg:col-span-5 space-y-4">
          <h3 className="text-xl font-black text-stone-900 tracking-tight">
            Canales de Atención Directa
          </h3>
          <p className="text-xs text-stone-600 leading-relaxed">
            Respondemos de inmediato para confirmación de pedidos, dudas sobre platos de la paila o reservas de almuerzos corporativos.
          </p>

          <div className="space-y-3 pt-2">
            <a
              href="https://wa.me/50762345678"
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-3.5 p-4 rounded-xl bg-white border border-stone-200 hover:border-emerald-500 transition-colors group shadow-xs"
            >
              <div className="w-10 h-10 rounded-xl bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
                <Send className="w-5 h-5 fill-current" />
              </div>
              <div>
                <span className="text-xs font-bold text-stone-900 group-hover:text-emerald-700 transition-colors block">
                  WhatsApp Pedidos Express
                </span>
                <span className="text-xs text-stone-500">+507 6234-5678 (Respuesta &lt; 2 min)</span>
              </div>
            </a>

            <a
              href="tel:+5072645000"
              className="flex items-center gap-3.5 p-4 rounded-xl bg-white border border-stone-200 hover:border-amber-500 transition-colors group shadow-xs"
            >
              <div className="w-10 h-10 rounded-xl bg-amber-100 text-amber-800 flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
                <PhoneCall className="w-5 h-5" />
              </div>
              <div>
                <span className="text-xs font-bold text-stone-900 group-hover:text-amber-800 transition-colors block">
                  Teléfono Fijo de Cocina
                </span>
                <span className="text-xs text-stone-500">+507 264-5000 (Mostrador Local)</span>
              </div>
            </a>

            <a
              href="mailto:pedidos@eatandgopa.com"
              className="flex items-center gap-3.5 p-4 rounded-xl bg-white border border-stone-200 hover:border-amber-500 transition-colors group shadow-xs"
            >
              <div className="w-10 h-10 rounded-xl bg-stone-100 text-stone-800 flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
                <Mail className="w-5 h-5" />
              </div>
              <div>
                <span className="text-xs font-bold text-stone-900 group-hover:text-amber-800 transition-colors block">
                  Correo Corporativo
                </span>
                <span className="text-xs text-stone-500">pedidos@eatandgopa.com</span>
              </div>
            </a>
          </div>
        </div>

        {/* Formulario de Mensaje Rápido */}
        <div className="lg:col-span-7 bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200 shadow-xs">
          <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800 mb-1">
            <MessageSquare className="w-4 h-4 text-amber-700" />
            <span>Envíanos un Mensaje</span>
          </div>
          <h3 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
            ¿Tienes alguna consulta o requerimiento especial?
          </h3>
          <p className="text-xs text-stone-600 mt-1 mb-5">
            Escríbenos y te contactamos por WhatsApp o llamada en minutos.
          </p>

          <form onSubmit={handleSubmitMessage} className="space-y-4">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-xs font-bold text-stone-700 mb-1">
                  Nombre Completo *
                </label>
                <input
                  type="text"
                  required
                  placeholder="Ej: Carlos Moreno"
                  value={formData.nombre}
                  onChange={(e) => setFormData({ ...formData, nombre: e.target.value })}
                  className="w-full px-3.5 py-2.5 bg-stone-50 border border-stone-300 rounded-xl text-xs sm:text-sm text-stone-900 focus:outline-none focus:ring-2 focus:ring-amber-500"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-stone-700 mb-1">
                  Teléfono / WhatsApp *
                </label>
                <input
                  type="tel"
                  required
                  placeholder="Ej: +507 6123-4567"
                  value={formData.telefono}
                  onChange={(e) => setFormData({ ...formData, telefono: e.target.value })}
                  className="w-full px-3.5 py-2.5 bg-stone-50 border border-stone-300 rounded-xl text-xs sm:text-sm text-stone-900 focus:outline-none focus:ring-2 focus:ring-amber-500"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-bold text-stone-700 mb-1">
                Motivo de Consulta
              </label>
              <select
                value={formData.asunto}
                onChange={(e) => setFormData({ ...formData, asunto: e.target.value })}
                className="w-full px-3.5 py-2.5 bg-stone-50 border border-stone-300 rounded-xl text-xs sm:text-sm text-stone-900 focus:outline-none focus:ring-2 focus:ring-amber-500"
              >
                <option value="retiro">Retiro Pick & Go en Local</option>
                <option value="comedor">Visitar el Comedor Presencial</option>
                <option value="menu_semanal">Consultar Platos del Menú Semanal</option>
                <option value="empresa">Almuerzo de Empresa / Factura Fiscal</option>
                <option value="otro">Otra Consulta</option>
              </select>
            </div>

            <div>
              <label className="block text-xs font-bold text-stone-700 mb-1">
                Mensaje o Pedido Detallado
              </label>
              <textarea
                rows={3}
                placeholder="Indícanos platos de interés, número de personas o cualquier instrucción..."
                value={formData.mensaje}
                onChange={(e) => setFormData({ ...formData, mensaje: e.target.value })}
                className="w-full px-3.5 py-2 bg-stone-50 border border-stone-300 rounded-xl text-xs sm:text-sm text-stone-900 focus:outline-none focus:ring-2 focus:ring-amber-500"
              />
            </div>

            <button
              type="submit"
              className="w-full py-3 px-4 bg-amber-500 hover:bg-amber-400 text-stone-950 font-black text-xs sm:text-sm rounded-xl transition-all shadow-md active:scale-95 flex items-center justify-center gap-2"
            >
              <Send className="w-4 h-4 fill-current" />
              <span>Enviar Consulta Directa por WhatsApp</span>
            </button>

            {sentSuccess && (
              <p className="text-center text-xs font-bold text-emerald-700 flex items-center justify-center gap-1.5 mt-2">
                <CheckCircle2 className="w-4 h-4" />
                <span>¡Mensaje preparado! Abriendo WhatsApp...</span>
              </p>
            )}
          </form>
        </div>
      </div>
    </div>
  );
};

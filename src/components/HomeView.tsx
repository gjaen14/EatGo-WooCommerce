import React, { useState, useEffect } from 'react';
import { 
  Flame, 
  Clock, 
  ShieldCheck, 
  Send, 
  ShoppingBag, 
  CheckCircle2, 
  ArrowRight, 
  Utensils, 
  Package, 
  Users,
  MapPin,
  ChevronLeft,
  ChevronRight,
  Sparkles,
  PhoneCall,
  Check,
  Building2,
  Calendar
} from 'lucide-react';
import { Dish, CartItem, DayOfWeek } from '../types';
import { PACKAGING_BENEFITS, CORPORATE_PACKAGES } from '../data/menuData';
import { WEEKLY_MENUS } from '../data/weeklyMenuData';

interface HomeViewProps {
  todayDishes: Dish[];
  breakfastDishes: Dish[];
  onSelectDish: (dish: Dish) => void;
  onNavigateTab: (tab: string, day?: DayOfWeek) => void;
  onOpenCart: () => void;
  onAddToCart?: (item: Omit<CartItem, 'cartItemId'>) => void;
}

export const HomeView: React.FC<HomeViewProps> = ({
  todayDishes,
  breakfastDishes,
  onSelectDish,
  onNavigateTab,
  onOpenCart,
  onAddToCart,
}) => {
  // Slider state
  const [currentSlide, setCurrentSlide] = useState(0);
  const [isPaused, setIsPaused] = useState(false);

  // Section 1 featured dishes pagination state (3 visible at a time)
  const [featuredPage, setFeaturedPage] = useState(0);

  // Corporate added state
  const [addedCorpId, setAddedCorpId] = useState<string | null>(null);

  // Hero Carousel slides (Panorámico 21:9 o 16:9)
  const slides = [
    {
      id: 'slide-1',
      tag: '🔥 DESPACHO CALIENTE • ZONA BANCARIA & OBARRIO',
      title: 'Tu almuerzo criollo auténtico listo a tiempo, sin hacer 1 minuto de fila.',
      description: 'Paila panameña del día cocinada a fuego lento, empacada en bandejas térmicas a 75°C y despachada directo a la recepción de tu piso o lista para retiro Pick & Go.',
      image: 'https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=2000&q=80',
      ctaPrimaryText: 'Pide tu almuerzo de hoy sin hacer filas',
      ctaPrimaryLink: 'https://wa.me/50762345678?text=Hola%20Eat%20%26%20Go!%20Quiero%20pedir%20mi%20almuerzo%20de%20hoy%20sin%20filas.',
      ctaSecondaryText: 'Ver Menú de la Semana',
      targetTab: 'semanal',
      targetSection: 'seccion-menu-semanal'
    },
    {
      id: 'slide-2',
      tag: '🌅 DISPONIBLE DESDE LAS 6:30 AM • COCINA MATUTINA',
      title: 'Desayunos Fijos Típicos: Hojaldres Crujientes, Bistec y Tortillas.',
      description: 'Arranca tu jornada laboral con sabor auténtico de fonda: carimañolas doradas con carne mechada, café criollo y chichas artesanales selladas sin esperas.',
      image: 'https://images.unsplash.com/photo-1541544741938-0af808871cc0?auto=format&fit=crop&w=2000&q=80',
      ctaPrimaryText: 'Pedir Desayuno Express',
      ctaPrimaryLink: 'https://wa.me/50762345678?text=Hola%20Eat%20%26%20Go!%20Quiero%20pedir%20desayunos%20para%20la%20oficina.',
      ctaSecondaryText: 'Ver Desayunos Fijos',
      targetTab: null,
      targetSection: 'desayunos-fijos'
    },
    {
      id: 'slide-3',
      tag: '🏢 ALMUERZOS DE EQUIPO • ENTREGA SINCRONIZADA 12:00 MD',
      title: 'Combos Corporativos para 5 y 10 Personas con Factura Fiscal.',
      description: 'Bandejas térmicas trilaminadas compartimentadas para reuniones de trabajo y capacitaciones. Cero regueros, cero comida fría, 100% deducible con RUC.',
      image: 'https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=2000&q=80',
      ctaPrimaryText: 'Cotizar Almuerzo de Equipo',
      ctaPrimaryLink: 'https://wa.me/50762345678?text=Hola%20Eat%20%26%20Go!%20Necesito%20cotizar%20un%20paquete%20corporativo%20con%20factura.',
      ctaSecondaryText: 'Ver Opciones Empresa',
      targetTab: 'empresa',
      targetSection: 'combos-oficina'
    }
  ];

  // Auto-play for the Hero Slider
  useEffect(() => {
    if (isPaused) return;
    const timer = setInterval(() => {
      setCurrentSlide((prev) => (prev + 1) % slides.length);
    }, 6000);
    return () => clearInterval(timer);
  }, [isPaused, slides.length]);

  const handlePrevSlide = () => {
    setCurrentSlide((prev) => (prev - 1 + slides.length) % slides.length);
  };

  const handleNextSlide = () => {
    setCurrentSlide((prev) => (prev + 1) % slides.length);
  };

  // Section 1 logic: Take 3 dishes based on featuredPage
  const visibleFeaturedDishes = todayDishes.slice(featuredPage * 3, featuredPage * 3 + 3);
  const maxFeaturedPages = Math.ceil(todayDishes.length / 3);

  const handleAddCorporate = (pkg: typeof CORPORATE_PACKAGES[0]) => {
    if (onAddToCart) {
      onAddToCart({
        dishId: pkg.id,
        name: pkg.name,
        basePrice: pkg.price,
        unitPrice: pkg.price,
        quantity: 1,
        notes: `Paquete corporativo (${pkg.servings} personas) con entrega sincronizada a las 12:00 MD`,
        totalPrice: pkg.price,
      });
      setAddedCorpId(pkg.id);
      setTimeout(() => setAddedCorpId(null), 2200);
    } else {
      onNavigateTab('corporativo');
    }
  };

  const scrollTo = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth' });
    }
  };

  // Detección automática del día actual de la semana (Lunes a Sábado)
  const getTodayDayOfWeek = (): DayOfWeek => {
    const dayIndex = new Date().getDay(); // 0 = Domingo, 1 = Lunes, ..., 6 = Sábado
    switch (dayIndex) {
      case 1: return 'lunes';
      case 2: return 'martes';
      case 3: return 'miercoles';
      case 4: return 'jueves';
      case 5: return 'viernes';
      case 6: return 'sabado';
      default: return 'lunes'; // Domingo o fuera de horario apunta al lunes
    }
  };

  const todayDayId = getTodayDayOfWeek();
  const todayDayMenu = WEEKLY_MENUS.find(m => m.dayId === todayDayId) || WEEKLY_MENUS[0];

  return (
    <div className="space-y-8 sm:space-y-12 pb-16">
      {/* ========================================================================= */}
      {/* 2. HERO SECTION (Banner Principal)                                        */}
      {/* Estructura: 100% ancho, relación panorámica 21:9 o 16:9                   */}
      {/* Componente: Carrusel / Slider                                             */}
      {/* Flechas flotantes desenfocadas en los extremos + Dots parte inferior       */}
      {/* ========================================================================= */}
      <section 
        id="hero-slider"
        onMouseEnter={() => setIsPaused(true)}
        onMouseLeave={() => setIsPaused(false)}
        className="relative w-full aspect-[16/9] sm:aspect-[21/9] min-h-[380px] sm:min-h-[440px] rounded-2xl sm:rounded-3xl overflow-hidden bg-stone-950 text-white shadow-xl border border-stone-800"
      >
        {/* Slides */}
        {slides.map((slide, index) => (
          <div
            key={slide.id}
            className={`absolute inset-0 transition-opacity duration-700 ease-in-out ${
              index === currentSlide ? 'opacity-100 z-10' : 'opacity-0 z-0 pointer-events-none'
            }`}
          >
            {/* Background Image (Cover Panorámico) */}
            <img
              src={slide.image}
              alt={slide.title}
              className="w-full h-full object-cover filter contrast-110 brightness-90"
              referrerPolicy="no-referrer"
            />
            {/* Deep gradient overlay */}
            <div className="absolute inset-0 bg-gradient-to-r from-stone-950 via-stone-950/85 to-transparent" />
            <div className="absolute inset-0 bg-gradient-to-t from-stone-950/90 via-transparent to-black/30" />

            {/* Content inside the slide */}
            <div className="absolute inset-0 flex flex-col justify-center px-6 sm:px-12 md:px-16 max-w-3xl z-10">
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-500/25 border border-amber-500/40 text-amber-300 text-[11px] sm:text-xs font-black uppercase tracking-wider mb-3 w-fit">
                <span className="w-2 h-2 rounded-full bg-amber-400 animate-pulse" />
                {slide.tag}
              </span>

              <h1 className="text-2xl sm:text-4xl md:text-5xl font-black tracking-tight leading-[1.12] text-white">
                {slide.title}
              </h1>

              <p className="mt-2.5 sm:mt-3.5 text-xs sm:text-sm md:text-base text-stone-300 leading-relaxed max-w-2xl font-normal">
                {slide.description}
              </p>

              {/* Action Buttons inside Hero */}
              <div className="mt-5 sm:mt-7 flex flex-wrap items-center gap-3">
                <a
                  href={slide.ctaPrimaryLink}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-2 px-5 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-stone-950 font-black text-xs sm:text-sm shadow-md transition-transform active:scale-95"
                >
                  <Send className="w-4 h-4 fill-current" />
                  <span>{slide.ctaPrimaryText}</span>
                </a>

                <button
                  onClick={() => {
                    if (slide.targetTab) {
                      onNavigateTab(slide.targetTab);
                    } else {
                      scrollTo(slide.targetSection);
                    }
                  }}
                  className="flex items-center gap-2 px-4 py-3 rounded-xl bg-stone-900/80 hover:bg-stone-800 text-stone-200 border border-stone-700 font-bold text-xs sm:text-sm backdrop-blur-xs transition-colors"
                >
                  <Utensils className="w-4 h-4 text-amber-400" />
                  <span>{slide.ctaSecondaryText}</span>
                </button>
              </div>
            </div>
          </div>
        ))}

        {/* Flechas de navegación flotantes (position: absolute) centradas verticalmente */}
        {/* Circulares con ligero desenfoque o transparencia */}
        <button
          onClick={handlePrevSlide}
          aria-label="Slide anterior"
          className="absolute left-3 sm:left-5 top-1/2 -translate-y-1/2 w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-black/40 hover:bg-black/70 backdrop-blur-md text-white border border-white/20 flex items-center justify-center transition-all z-20 shadow-lg active:scale-95"
        >
          <ChevronLeft className="w-5 h-5 sm:w-6 sm:h-6" />
        </button>

        <button
          onClick={handleNextSlide}
          aria-label="Siguiente slide"
          className="absolute right-3 sm:right-5 top-1/2 -translate-y-1/2 w-10 h-10 sm:w-12 sm:h-12 rounded-full bg-black/40 hover:bg-black/70 backdrop-blur-md text-white border border-white/20 flex items-center justify-center transition-all z-20 shadow-lg active:scale-95"
        >
          <ChevronRight className="w-5 h-5 sm:w-6 sm:h-6" />
        </button>

        {/* Paginador de puntos (Dots) flotante en la parte inferior central */}
        <div className="absolute bottom-4 sm:bottom-6 left-1/2 -translate-x-1/2 flex items-center gap-2 z-20">
          {slides.map((_, dotIdx) => (
            <button
              key={dotIdx}
              onClick={() => setCurrentSlide(dotIdx)}
              aria-label={`Ir al slide ${dotIdx + 1}`}
              className={`h-2.5 rounded-full transition-all ${
                dotIdx === currentSlide
                  ? 'w-7 bg-amber-400 shadow-xs'
                  : 'w-2.5 bg-white/40 hover:bg-white/70'
              }`}
            />
          ))}
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 3. NOTIFICATION / ACTION BAR: BANNER DINÁMICO DEL MENÚ DE HOY             */}
      {/* Muestra dinámicamente el día actual y dirige al menú correspondiente       */}
      {/* ========================================================================= */}
      <section
        id="notification-action-bar"
        onClick={() => onNavigateTab('semanal', todayDayId)}
        role="button"
        tabIndex={0}
        onKeyDown={(e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            onNavigateTab('semanal', todayDayId);
          }
        }}
        className="w-full bg-white/80 backdrop-blur-md hover:bg-white border border-stone-200/80 hover:border-orange-500/40 rounded-[20px] p-3.5 sm:p-4 shadow-sm hover:shadow-md transition-all cursor-pointer group flex items-center justify-between gap-4"
      >
        {/* Izquierda: Icono gastronómico animado */}
        <div className="flex items-center gap-3.5 min-w-0">
          <div className="w-10 h-10 rounded-full bg-orange-500/15 border border-orange-500/30 text-orange-600 flex items-center justify-center shrink-0 group-hover:scale-105 transition-transform">
            <Flame className="w-5 h-5 text-[#FF4F00] animate-pulse" />
          </div>

          {/* Centro: Título y descripción demostrativa del Menú de Hoy */}
          <div className="min-w-0">
            <div className="flex items-center gap-2">
              <span className="text-xs sm:text-sm font-black text-[#1A1A1A] tracking-tight block truncate">
                Menú de Hoy: {todayDayMenu.dayName}
              </span>
              <span className="hidden sm:inline-flex items-center gap-1 text-[10px] uppercase font-black px-2.5 py-0.5 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-300/80">
                <span className="w-1.5 h-1.5 rounded-full bg-emerald-500 animate-pulse" />
                Despachando
              </span>
            </div>
            <p className="text-[11px] sm:text-xs text-stone-600 leading-snug mt-0.5 truncate">
              Especial de hoy: <strong className="text-[#1A1A1A] font-bold">{todayDayMenu.starDishName}</strong> (${todayDayMenu.starDishPrice.toFixed(2)}) • Toca para ver los platos de hoy y pedir sin esperas.
            </p>
          </div>
        </div>

        {/* Derecha: Botón de acción con flecha en color acento redondeado */}
        <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-full bg-[#FF4F00] group-hover:bg-[#e04500] text-white flex items-center justify-center shrink-0 shadow-md shadow-orange-500/20 transition-transform group-hover:translate-x-1">
          <ArrowRight className="w-4 h-4 stroke-[2.5]" />
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 🏗️ SECCIÓN 1: PLATOS DESTACADOS DE HOY (Top Section)                      */}
      {/* 3 cards verticales (aspect 4:5), fondo oscuro, foto protagonista y botón  */}
      {/* ========================================================================= */}
      <section id="seccion-grilla-destacada" className="scroll-mt-28">
        {/* Header de la Sección */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-3 mb-6">
          <div>
            <span className="text-[11px] font-black uppercase tracking-widest text-stone-400 block mb-1">
              MENÚ DEL DÍA
            </span>
            <h2 className="text-2xl sm:text-3xl md:text-4xl font-black text-[#1A1A1A] tracking-tight leading-none uppercase">
              PLATOS DESTACADOS DE HOY
            </h2>
          </div>

          {/* Controles a la derecha */}
          <div className="flex items-center gap-4 self-start sm:self-auto">
            <button
              onClick={() => onNavigateTab('menu')}
              className="text-xs font-bold text-orange-600 hover:text-orange-700 hover:underline flex items-center gap-1 transition-colors"
            >
              <span>Ver menú completo</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>

            <div className="flex items-center gap-1.5">
              <button
                onClick={() => setFeaturedPage((prev) => Math.max(0, prev - 1))}
                disabled={featuredPage === 0}
                aria-label="Página anterior de destacados"
                className="w-9 h-9 rounded-full bg-stone-900 hover:bg-stone-800 disabled:opacity-30 disabled:cursor-not-allowed text-white flex items-center justify-center transition-colors border border-stone-800 shadow-xs cursor-pointer"
              >
                <ChevronLeft className="w-4 h-4" />
              </button>
              <button
                onClick={() => setFeaturedPage((prev) => (prev + 1 < maxFeaturedPages ? prev + 1 : 0))}
                aria-label="Siguiente página de destacados"
                className="w-9 h-9 rounded-full bg-stone-900 hover:bg-stone-800 text-white flex items-center justify-center transition-colors border border-stone-800 shadow-xs cursor-pointer"
              >
                <ChevronRight className="w-4 h-4" />
              </button>
            </div>
          </div>
        </div>

        {/* Arquitectura del Grid: 3 columnas iguales en Desktop (repeat(3, 1fr)) con gap 24px */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {visibleFeaturedDishes.map((dish) => (
            <div
              key={dish.id}
              onClick={() => onSelectDish(dish)}
              className="group relative aspect-[4/5] rounded-[24px] bg-stone-950 border border-stone-800/80 hover:border-orange-500/50 overflow-hidden shadow-lg hover:shadow-2xl transition-all duration-300 flex flex-col justify-between p-5 sm:p-6 cursor-pointer"
            >
              {/* Fotografía recortada/sangrada ocupando gran parte de la tarjeta con efecto hover */}
              <div className="absolute inset-0 z-0">
                <img
                  src={dish.image}
                  alt={dish.name}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500 opacity-85 group-hover:opacity-95"
                  referrerPolicy="no-referrer"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-stone-950 via-stone-950/60 to-black/30" />
              </div>

              {/* Top Header dentro de la Card */}
              <div className="relative z-10 flex items-center justify-between">
                <span className="bg-stone-900/90 backdrop-blur-md text-[#FACC15] text-[11px] font-black uppercase tracking-wider px-3 py-1 rounded-full border border-amber-400/30 shadow-xs">
                  {dish.badge || '🔥 Especial de Hoy'}
                </span>
                <span className="bg-[#FF4F00] text-white font-black text-sm px-3 py-1 rounded-full shadow-md shadow-orange-600/30">
                  ${dish.price.toFixed(2)}
                </span>
              </div>

              {/* Bottom Body dentro de la Card: Tipografía Grande + Botón sutil de Agregar */}
              <div className="relative z-10 text-white pt-10">
                <h3 className="text-xl sm:text-2xl font-black tracking-tight leading-tight group-hover:text-amber-300 transition-colors">
                  {dish.name}
                </h3>
                <p className="text-xs text-stone-300 line-clamp-2 mt-1.5 leading-relaxed font-normal">
                  {dish.description}
                </p>

                <div className="mt-4 pt-3 border-t border-white/15 flex items-center justify-between gap-3">
                  <div className="text-[11px] text-stone-400 truncate font-medium">
                    Incluye guarnición criolla
                  </div>
                  <button
                    type="button"
                    id={`btn-add-featured-${dish.id}`}
                    onClick={(e) => {
                      e.stopPropagation();
                      onSelectDish(dish);
                    }}
                    className="px-4 py-2 rounded-full bg-[#FF4F00] hover:bg-[#e04500] active:bg-[#c93e00] text-white font-black text-xs transition-all shadow-md shadow-orange-600/30 active:scale-95 flex items-center gap-1.5 shrink-0 cursor-pointer"
                  >
                    <ShoppingBag className="w-3.5 h-3.5" />
                    <span>Agregar</span>
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </section>

      {/* ========================================================================= */}
      {/* 🏗️ SECCIÓN 2: EXPLORAR MENÚ SEMANAL (Bottom Section - 5 Días Lunes a Viernes)*/}
      {/* Formato Banners Horizontales: 3 en fila sup + 2 centrados en fila inf     */}
      {/* Lado izq: Bloque sólido Paleta Eat & Go + Texto grande del día           */}
      {/* Lado der: Fotografía que sangra al borde derecho                          */}
      {/* ========================================================================= */}
      <section id="seccion-menu-semanal" className="scroll-mt-28">
        <div className="mb-6">
          <h2 className="text-2xl sm:text-3xl md:text-4xl font-black text-stone-900 tracking-tight leading-none uppercase">
            EXPLORA NUESTRO MENÚ SEMANAL
          </h2>
          <p className="text-xs sm:text-sm text-stone-600 mt-1.5">
            Selecciona el día de la semana para ordenar tu almuerzo ejecutivo criollo con despacho garantizado:
          </p>
        </div>

        {/* Grid de 5 días: 3 columnas arriba (Lunes, Martes, Miércoles) y 2 centradas abajo (Jueves, Viernes) */}
        <div className="grid grid-cols-1 md:grid-cols-6 gap-6">
          {(() => {
            // Filtrar únicamente los 5 días laborales (Lunes a Viernes)
            const fiveWeekDays = WEEKLY_MENUS.filter(m => m.dayId !== 'sabado').slice(0, 5);

            // Estilos específicos de la paleta Eat & Go para cada día
            const dayStyles: Record<string, { bg: string; border: string; accent: string; category: string }> = {
              lunes: {
                bg: 'bg-stone-900',
                border: 'border-stone-800 hover:border-amber-500/60',
                accent: 'text-amber-400',
                category: 'Especial de Sopas & Paila Criolla'
              },
              martes: {
                bg: 'bg-[#9A3412]', // Naranja quemado Eat & Go
                border: 'border-orange-700 hover:border-amber-400',
                accent: 'text-amber-200',
                category: 'Guisados Campesinos & Estofados'
              },
              miercoles: {
                bg: 'bg-[#B45309]', // Amarillo quemado
                border: 'border-amber-600 hover:border-amber-300',
                accent: 'text-amber-100',
                category: 'Lechona Asada & Cerdo Criollo'
              },
              jueves: {
                bg: 'bg-[#14532D]', // Verde Criollo profundo
                border: 'border-emerald-700 hover:border-emerald-400',
                accent: 'text-emerald-300',
                category: 'Costillas, Aves & Sabor Ahumado'
              },
              viernes: {
                bg: 'bg-stone-950', // Carbón intenso con acento dorado
                border: 'border-amber-500/40 hover:border-amber-400',
                accent: 'text-amber-400',
                category: 'Mariscos de la Costa & Pescado Frito'
              }
            };

            return fiveWeekDays.map((dayMenu, idx) => {
              const style = dayStyles[dayMenu.dayId] || dayStyles.lunes;
              // Las 3 primeras ocupan 2 columnas cada una en grid de 6 (total 6 cols = 3 tarjetas)
              // Las 2 últimas ocupan 2 columnas cada una y se centran con offset (col-start-2 para la 4ta)
              const colSpanClass = idx < 3 
                ? 'md:col-span-2' 
                : idx === 3 
                  ? 'md:col-span-2 md:col-start-2' 
                  : 'md:col-span-2';

              return (
                <div
                  key={dayMenu.dayId}
                  onClick={() => onNavigateTab('semanal', dayMenu.dayId)}
                  className={`group relative h-40 sm:h-44 rounded-2xl ${style.bg} border ${style.border} overflow-hidden shadow-md hover:shadow-2xl transition-all duration-300 hover:-translate-y-1 cursor-pointer flex items-stretch justify-between ${colSpanClass}`}
                >
                  {/* Lado Izquierdo: Bloque de Texto Brandeado Eat & Go */}
                  <div className="w-[58%] sm:w-[60%] p-5 sm:p-6 z-10 flex flex-col justify-between">
                    <div>
                      <span className="text-[10px] font-black uppercase tracking-wider text-stone-300/80 block">
                        {dayMenu.badge.split(' ')[0]} • ROTACIÓN
                      </span>
                      <h3 className="text-2xl sm:text-3xl font-black text-white tracking-tight uppercase leading-none mt-1 group-hover:text-amber-300 transition-colors">
                        {dayMenu.shortName}
                      </h3>
                      <p className={`text-xs font-semibold ${style.accent} mt-1.5 leading-snug`}>
                        {style.category}
                      </p>
                    </div>

                    <div className="flex items-center gap-1.5 text-xs font-extrabold text-white group-hover:translate-x-1 transition-transform">
                      <span>Ver menú</span>
                      <ArrowRight className="w-3.5 h-3.5 text-amber-400" />
                    </div>
                  </div>

                  {/* Lado Derecho: Fotografía recortada que sangra al llegar al borde derecho */}
                  <div className="w-[42%] sm:w-[40%] relative overflow-hidden flex items-center justify-end">
                    <img
                      src={dayMenu.starDishImage}
                      alt={dayMenu.starDishName}
                      className="absolute -right-6 sm:-right-8 w-36 sm:w-44 h-36 sm:h-44 rounded-full object-cover shadow-2xl border-4 border-stone-900/40 transform group-hover:scale-110 group-hover:rotate-3 transition-all duration-500"
                      referrerPolicy="no-referrer"
                    />
                  </div>
                </div>
              );
            });
          })()}
        </div>
      </section>

      {/* SECCIÓN INTERACTIVA ANCLADA: Desayunos Fijos Criollos (6:30 AM) */}
      <section id="desayunos-fijos" className="scroll-mt-28 bg-amber-50/70 border border-amber-200/80 rounded-2xl sm:rounded-3xl p-6 sm:p-8">
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-2 mb-6">
          <div>
            <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800 mb-1">
              <Clock className="w-4 h-4 text-amber-700" />
              <span>Disponible Diario de 6:30 a.m. a 11:00 a.m.</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-black text-stone-900 tracking-tight">
              Desayunos Fijos Criollos
            </h2>
            <p className="text-stone-600 text-xs sm:text-sm mt-0.5">
              Hojaldres recién fritas, tortillas de maíz, carimañolas doradas y bistec encebollado con salsa criolla.
            </p>
          </div>

          <span className="text-xs font-bold text-stone-700 bg-white px-3 py-1.5 rounded-lg border border-amber-200 self-start sm:self-auto">
            ☕ Café criollo & Chichas frías selladas
          </span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {breakfastDishes.map((dish) => (
            <div
              key={dish.id}
              className="bg-white rounded-xl border border-amber-200/60 p-3.5 flex flex-col justify-between shadow-xs hover:shadow-sm transition-all"
            >
              <div className="flex gap-3">
                <img
                  src={dish.image}
                  alt={dish.name}
                  className="w-16 h-16 rounded-lg object-cover shrink-0"
                  referrerPolicy="no-referrer"
                />
                <div className="flex-1 min-w-0">
                  <h3 className="font-bold text-sm text-stone-900 truncate">
                    {dish.name}
                  </h3>
                  <p className="text-[11px] text-stone-500 line-clamp-2 mt-0.5">
                    {dish.description}
                  </p>
                  <p className="text-amber-700 font-black text-sm mt-1">
                    ${dish.price.toFixed(2)}
                  </p>
                </div>
              </div>

              <button
                id={`btn-add-breakfast-${dish.id}`}
                onClick={() => onSelectDish(dish)}
                className="mt-3 w-full py-1.5 px-2 bg-stone-900 hover:bg-stone-800 text-white text-xs font-bold rounded-lg transition-colors flex items-center justify-center gap-1.5"
              >
                <span>+ Agregar a Comanda</span>
              </button>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};

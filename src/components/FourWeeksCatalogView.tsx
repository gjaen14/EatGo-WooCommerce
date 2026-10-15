import React, { useState } from 'react';
import { 
  Calendar, 
  Flame, 
  Clock, 
  ShoppingBag, 
  Send, 
  CheckCircle2, 
  Coffee, 
  Sparkles, 
  ArrowRight,
  Filter,
  Check,
  PackageCheck,
  Eye
} from 'lucide-react';
import { Dish, CartItem } from '../types';
import { FOUR_WEEKS_DATA, FIXED_BREAKFAST_ITEMS, WeekDayDish, WeekSchedule } from '../data/fourWeeksData';
import { COMMON_SIDES } from '../data/menuData';

interface FourWeeksCatalogViewProps {
  onAddToCart: (item: Omit<CartItem, 'cartItemId'>) => void;
  onSelectDish: (dish: Dish) => void;
  initialWeek?: 1 | 2 | 3 | 4;
}

export const FourWeeksCatalogView: React.FC<FourWeeksCatalogViewProps> = ({
  onAddToCart,
  onSelectDish,
  initialWeek = 1
}) => {
  // Tabs: 'desayunos' | 1 | 2 | 3 | 4
  const [activeTab, setActiveTab] = useState<'desayunos' | 1 | 2 | 3 | 4>(1);
  const [selectedDayId, setSelectedDayId] = useState<'lunes' | 'martes' | 'miercoles' | 'jueves' | 'viernes' | 'sabado'>('lunes');
  
  // Track which dishes have "boxed view" toggled: { [dishId]: boolean }
  const [boxedViewMap, setBoxedViewMap] = useState<Record<string, boolean>>({});
  
  // Selected side option per dish: { [dishId]: string }
  const [selectedSidesMap, setSelectedSidesMap] = useState<Record<string, string>>({});
  
  // Added to cart feedback
  const [addedDishId, setAddedDishId] = useState<string | null>(null);

  // Toggle boxed image view
  const toggleBoxedView = (dishId: string) => {
    setBoxedViewMap((prev) => ({
      ...prev,
      [dishId]: !prev[dishId]
    }));
  };

  // Handle side selection
  const handleSelectSide = (dishId: string, sideName: string) => {
    setSelectedSidesMap((prev) => ({
      ...prev,
      [dishId]: sideName
    }));
  };

  // Add dish to order directly from card
  const handleQuickAdd = (dish: WeekDayDish, dayName?: string) => {
    const chosenSide = selectedSidesMap[dish.id] || dish.recommendedSide || 'Arroz criollo';
    onAddToCart({
      dishId: dish.id,
      name: dish.name,
      basePrice: dish.price,
      unitPrice: dish.price,
      quantity: 1,
      selectedSide: chosenSide,
      notes: dayName ? `Planificación ${dayName} con ${chosenSide}` : `Acompañamiento: ${chosenSide}`,
      totalPrice: dish.price
    });
    setAddedDishId(dish.id);
    setTimeout(() => setAddedDishId(null), 1800);
  };

  const handleWhatsAppInquiry = (dish: WeekDayDish, weekText: string, dayText: string) => {
    const msg = `*PLANIFICACIÓN DE ALMUERZO EAT & GO*\n📅 *${weekText} - ${dayText}*\n🍲 *Plato:* ${dish.name} ($${dish.price.toFixed(2)})\n🍚 *Acompañamiento:* ${selectedSidesMap[dish.id] || dish.recommendedSide}\n\n*Quiero coordinar este pedido anticipado para mi oficina.*`;
    window.open(`https://wa.me/50762345678?text=${encodeURIComponent(msg)}`, '_blank');
  };

  // Find current active week data
  const currentWeekData: WeekSchedule | undefined = typeof activeTab === 'number' 
    ? FOUR_WEEKS_DATA.find((w) => w.weekNumber === activeTab) 
    : undefined;

  // Find current day within week
  const currentDayMenu = currentWeekData?.days.find((d) => d.dayId === selectedDayId) || currentWeekData?.days[0];

  return (
    <div className="space-y-8 sm:space-y-10 pb-16">
      {/* ========================================================================= */}
      {/* 1. HEADER DEL CATÁLOGO INTERACTIVO                                         */}
      {/* ========================================================================= */}
      <div className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200/90 shadow-xs">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-5">
          <div>
            <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800 mb-1">
              <Calendar className="w-4 h-4 text-amber-700" />
              <span>PLANIFICA TUS ALMUERZOS DE OFICINA • CERO REPETICIÓN</span>
            </div>
            <h1 className="text-2xl sm:text-4xl font-black text-stone-900 tracking-tight">
              Catálogo Interactivo de las 4 Semanas
            </h1>
            <p className="mt-2 text-xs sm:text-sm text-stone-600 max-w-2xl leading-relaxed">
              Consulta el menú completo de las 4 semanas del mes o pide tus desayunos fijos diarios. Visualiza la comida servida o dentro de nuestras nuevas <strong>cajas troqueladas térmicas</strong> anti-derrames a 75°C.
            </p>
          </div>

          <div className="flex items-center gap-2 bg-amber-50/90 border border-amber-200/80 p-3 rounded-2xl shrink-0">
            <PackageCheck className="w-8 h-8 text-amber-700 shrink-0" />
            <div className="text-xs">
              <span className="font-black text-stone-900 block">Cajas Troqueladas 75°C</span>
              <span className="text-stone-600">Compartimentos separados para salsas</span>
            </div>
          </div>
        </div>

        {/* ========================================================================= */}
        {/* SELECTOR POR PESTAÑAS: Desayunos (Fijos) | Semanas 1 a 4                  */}
        {/* ========================================================================= */}
        <div className="mt-8 border-t border-stone-100 pt-6">
          <div className="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1">
            {/* Pestaña 1: Desayunos Fijos Diarios */}
            <button
              id="tab-btn-desayunos-fijos"
              onClick={() => setActiveTab('desayunos')}
              className={`px-4 py-2.5 rounded-xl font-black text-xs sm:text-sm flex items-center gap-2 whitespace-nowrap transition-all ${
                activeTab === 'desayunos'
                  ? 'bg-stone-900 text-amber-400 shadow-md ring-2 ring-amber-500/50'
                  : 'bg-stone-100 text-stone-700 hover:bg-stone-200 hover:text-stone-900'
              }`}
            >
              <Coffee className="w-4 h-4 text-amber-400" />
              <span>Pestaña 1: Desayunos (Fijos Diarios)</span>
            </button>

            {/* Pestañas 2 a 5: Semanas 1, 2, 3 y 4 */}
            {FOUR_WEEKS_DATA.map((week) => (
              <button
                key={week.weekNumber}
                id={`tab-btn-semana-${week.weekNumber}`}
                onClick={() => setActiveTab(week.weekNumber)}
                className={`px-4 py-2.5 rounded-xl font-black text-xs sm:text-sm flex items-center gap-2 whitespace-nowrap transition-all ${
                  activeTab === week.weekNumber
                    ? 'bg-amber-500 text-stone-950 shadow-md font-black ring-2 ring-amber-400'
                    : 'bg-stone-100 text-stone-700 hover:bg-stone-200 hover:text-stone-900'
                }`}
              >
                <Calendar className="w-4 h-4 text-stone-900" />
                <span>Semana {week.weekNumber}</span>
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* VISTA 1: DESAYUNOS (FIJOS DIARIOS REPETIDOS)                              */}
      {/* ========================================================================= */}
      {activeTab === 'desayunos' && (
        <div className="space-y-6">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 bg-amber-50/70 border border-amber-200/90 rounded-2xl p-4 sm:p-5">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 rounded-xl bg-amber-500 text-stone-950 flex items-center justify-center font-black">
                <Coffee className="w-5 h-5" />
              </div>
              <div>
                <h3 className="font-extrabold text-stone-900 text-sm sm:text-base">
                  Desayunos Típicos Diarios (Disponibles desde las 6:30 AM)
                </h3>
                <p className="text-xs text-stone-600 mt-0.5">
                  Confirmado: Las recetas de desayuno se preparan frescas todas las mañanas sin rotación semanal.
                </p>
              </div>
            </div>
            <span className="text-[11px] font-bold px-3 py-1 rounded-full bg-white text-amber-800 border border-amber-300 w-fit">
              Frituras al Momento
            </span>
          </div>

          {/* Grilla de Desayunos */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {FIXED_BREAKFAST_ITEMS.map((dish) => {
              const isBoxed = !!boxedViewMap[dish.id];
              return (
                <div
                  key={dish.id}
                  className="bg-white rounded-2xl border border-stone-200/90 overflow-hidden shadow-xs hover:border-amber-400 hover:shadow-md transition-all flex flex-col justify-between"
                >
                  <div>
                    {/* Visual Container with Boxed Toggle */}
                    <div className="relative aspect-[4/3] bg-stone-100 overflow-hidden group">
                      <img
                        src={isBoxed ? dish.boxedImage : dish.image}
                        alt={dish.name}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                        referrerPolicy="no-referrer"
                      />

                      {/* Badge Top Left */}
                      <span className="absolute top-3 left-3 bg-stone-950/80 backdrop-blur-xs text-amber-400 text-[10px] font-black uppercase px-2.5 py-1 rounded-md border border-stone-800">
                        {dish.badge}
                      </span>

                      {/* Price Tag Top Right */}
                      <span className="absolute top-3 right-3 bg-white text-stone-950 text-xs sm:text-sm font-black px-2.5 py-1 rounded-lg shadow-sm">
                        ${dish.price.toFixed(2)}
                      </span>

                      {/* Toggle: Ver en Caja Troquelada */}
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          toggleBoxedView(dish.id);
                        }}
                        className={`absolute bottom-3 right-3 px-2.5 py-1.5 rounded-lg text-[11px] font-bold flex items-center gap-1.5 backdrop-blur-md shadow-md transition-all ${
                          isBoxed
                            ? 'bg-amber-500 text-stone-950 ring-2 ring-stone-950'
                            : 'bg-stone-950/80 hover:bg-stone-900 text-white'
                        }`}
                      >
                        <Eye className="w-3.5 h-3.5" />
                        <span>{isBoxed ? 'Ver en Plato' : 'Ver en Caja'}</span>
                      </button>
                    </div>

                    {/* Contenido Card */}
                    <div className="p-4 sm:p-5">
                      <div className="flex items-center gap-1.5 text-[10px] font-bold text-amber-700 uppercase tracking-wider mb-1">
                        <Clock className="w-3 h-3" />
                        <span>{dish.timeAvailable || '6:30 AM a 11:00 AM'}</span>
                      </div>

                      <h4 className="font-black text-stone-900 text-base leading-snug">
                        {dish.name}
                      </h4>

                      <p className="text-xs text-stone-600 mt-1.5 line-clamp-2 leading-relaxed">
                        {dish.description}
                      </p>

                      {/* Selector de Acompañamiento */}
                      {dish.availableSides && dish.availableSides.length > 0 && (
                        <div className="mt-3.5 pt-3 border-t border-stone-100">
                          <label className="text-[11px] font-bold text-stone-700 block mb-1.5">
                            Acompañamiento incluido:
                          </label>
                          <select
                            value={selectedSidesMap[dish.id] || dish.availableSides[0].name}
                            onChange={(e) => handleSelectSide(dish.id, e.target.value)}
                            className="w-full text-xs bg-stone-50 border border-stone-200 rounded-lg p-2 font-medium text-stone-800 focus:ring-1 focus:ring-amber-500"
                          >
                            {dish.availableSides.map((s) => (
                              <option key={s.id} value={s.name}>
                                {s.name} {s.extraPrice > 0 ? `(+$${s.extraPrice.toFixed(2)})` : '(Incluido)'}
                              </option>
                            ))}
                          </select>
                        </div>
                      )}
                    </div>
                  </div>

                  {/* Actions Bottom */}
                  <div className="p-4 sm:p-5 pt-0">
                    <button
                      onClick={() => handleQuickAdd(dish, 'Desayuno')}
                      className={`w-full py-2.5 px-4 rounded-xl font-black text-xs flex items-center justify-center gap-2 transition-all shadow-sm ${
                        addedDishId === dish.id
                          ? 'bg-emerald-600 text-white'
                          : 'bg-amber-500 hover:bg-amber-400 text-stone-950 active:scale-95'
                      }`}
                    >
                      {addedDishId === dish.id ? (
                        <>
                          <Check className="w-4 h-4 text-white" />
                          <span>¡Agregado a la Comanda!</span>
                        </>
                      ) : (
                        <>
                          <ShoppingBag className="w-4 h-4" />
                          <span>+ Agregar al Pedido</span>
                        </>
                      )}
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* VISTA 2: SEMANAS 1 A 4 CON FILTRO POR DÍA (Lunes Sopa, Martes Mondongo...)*/}
      {/* ========================================================================= */}
      {typeof activeTab === 'number' && currentWeekData && (
        <div className="space-y-6">
          {/* Sub-barra de información de la semana */}
          <div className="bg-stone-900 text-white p-4 sm:p-5 rounded-2xl flex flex-col sm:flex-row sm:items-center justify-between gap-3 border border-stone-800">
            <div>
              <span className="text-[10px] font-black uppercase tracking-widest text-amber-400 block">
                {currentWeekData.datesDescription}
              </span>
              <h2 className="text-lg sm:text-xl font-black tracking-tight">
                {currentWeekData.title}
              </h2>
              <p className="text-xs text-stone-300 mt-0.5">
                {currentWeekData.subtitle}
              </p>
            </div>

            <div className="flex items-center gap-2 text-xs font-bold text-amber-300 bg-stone-800/80 px-3 py-1.5 rounded-xl border border-stone-700 shrink-0">
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
              <span>Rotación Mensual Asegurada</span>
            </div>
          </div>

          {/* FILTRO POR DÍA DE LA SEMANA (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado) */}
          <div className="flex items-center gap-2 overflow-x-auto no-scrollbar pb-1">
            {currentWeekData.days.map((day) => {
              const isSelected = day.dayId === selectedDayId;
              return (
                <button
                  key={day.dayId}
                  onClick={() => setSelectedDayId(day.dayId)}
                  className={`px-3.5 py-2 rounded-xl text-xs font-bold flex flex-col sm:flex-row sm:items-center gap-1 sm:gap-2 whitespace-nowrap transition-all border ${
                    isSelected
                      ? 'bg-amber-500 text-stone-950 border-amber-600 font-black shadow-sm'
                      : 'bg-white text-stone-700 hover:bg-stone-50 border-stone-200'
                  }`}
                >
                  <span className="uppercase text-[11px] font-black">{day.dayName}</span>
                  <span className={`text-[10px] ${isSelected ? 'text-stone-900 font-medium' : 'text-stone-500'}`}>
                    {day.theme.split('&')[0]}
                  </span>
                </button>
              );
            })}
          </div>

          {/* Info Banner del Día Seleccionado */}
          {currentDayMenu && (
            <div className="bg-amber-50/80 border border-amber-200/90 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
              <div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-black uppercase tracking-wider text-amber-900">
                    Menú del {currentDayMenu.dayName}
                  </span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded bg-amber-200/80 text-amber-950">
                    {currentDayMenu.badge}
                  </span>
                </div>
                <p className="text-xs text-stone-700 mt-1">
                  {currentDayMenu.description}
                </p>
              </div>

              <div className="text-[11px] font-bold text-stone-600 shrink-0">
                {currentDayMenu.dishes.length} especialidades preparadas hoy
              </div>
            </div>
          )}

          {/* GRILLA DE PLATOS DEL DÍA CON TARJETAS DE PRODUCTO RÁPIDO */}
          {currentDayMenu && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {currentDayMenu.dishes.map((dish) => {
                const isBoxed = !!boxedViewMap[dish.id];
                const activeSide = selectedSidesMap[dish.id] || dish.recommendedSide;

                return (
                  <div
                    key={dish.id}
                    className="bg-white rounded-2xl border border-stone-200/90 overflow-hidden shadow-xs hover:border-amber-400 hover:shadow-md transition-all flex flex-col justify-between"
                  >
                    <div>
                      {/* Imagen con Toggle "Servido / En Caja Troquelada" */}
                      <div className="relative aspect-[4/3] bg-stone-100 overflow-hidden group">
                        <img
                          src={isBoxed ? dish.boxedImage : dish.image}
                          alt={dish.name}
                          className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                          referrerPolicy="no-referrer"
                        />

                        {/* Badge */}
                        <span className="absolute top-3 left-3 bg-stone-950/80 backdrop-blur-xs text-amber-400 text-[10px] font-black uppercase px-2.5 py-1 rounded-md border border-stone-800">
                          {dish.badge || 'Criollo Auténtico'}
                        </span>

                        {/* Price Tag */}
                        <span className="absolute top-3 right-3 bg-white text-stone-950 text-sm font-black px-2.5 py-1 rounded-lg shadow-sm">
                          ${dish.price.toFixed(2)}
                        </span>

                        {/* Switch Interactivo: Servido vs Caja Troquelada */}
                        <button
                          onClick={(e) => {
                            e.stopPropagation();
                            toggleBoxedView(dish.id);
                          }}
                          className={`absolute bottom-3 right-3 px-2.5 py-1.5 rounded-lg text-[11px] font-bold flex items-center gap-1.5 backdrop-blur-md shadow-md transition-all ${
                            isBoxed
                              ? 'bg-amber-500 text-stone-950 ring-2 ring-stone-950'
                              : 'bg-stone-950/80 hover:bg-stone-900 text-white'
                          }`}
                        >
                          <PackageCheck className="w-3.5 h-3.5" />
                          <span>{isBoxed ? 'Ver en Plato' : 'Ver en Caja 75°C'}</span>
                        </button>
                      </div>

                      {/* Info del Plato */}
                      <div className="p-4 sm:p-5">
                        <h4 className="font-black text-stone-900 text-base leading-snug group-hover:text-amber-700 transition-colors">
                          {dish.name}
                        </h4>

                        <p className="text-xs text-stone-600 mt-1.5 line-clamp-2 leading-relaxed">
                          {dish.description}
                        </p>

                        {/* Selector de Acompañamiento en la propia tarjeta */}
                        <div className="mt-4 pt-3 border-t border-stone-100 space-y-1.5">
                          <label className="text-[11px] font-bold text-stone-700 block">
                            Acompañamiento a tu gusto:
                          </label>
                          <select
                            value={activeSide}
                            onChange={(e) => handleSelectSide(dish.id, e.target.value)}
                            className="w-full text-xs bg-stone-50 border border-stone-200 rounded-lg p-2 font-semibold text-stone-800 focus:ring-1 focus:ring-amber-500"
                          >
                            <option value="Arroz Blanco Criollo">Arroz Blanco Criollo</option>
                            <option value="Arroz con Guandú Oloroso">Arroz con Guandú Oloroso</option>
                            <option value="Patacones Crocantes">Patacones Crocantes con Sal</option>
                            <option value="Tajadas de Plátano Maduro">Tajadas de Plátano Maduro</option>
                            <option value="Ensalada de Feria de Remolacha">Ensalada de Feria (Remolacha & Papa)</option>
                            <option value="Yuca al Vapor con Mojo">Yuca al Vapor con Mojo Criollo</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    {/* Botón de Agregar y Botón de Encargar */}
                    <div className="p-4 sm:p-5 pt-0 space-y-2">
                      <button
                        onClick={() => handleQuickAdd(dish, `${currentWeekData.title} - ${currentDayMenu.dayName}`)}
                        className={`w-full py-2.5 px-4 rounded-xl font-black text-xs flex items-center justify-center gap-2 transition-all shadow-sm ${
                          addedDishId === dish.id
                            ? 'bg-emerald-600 text-white'
                            : 'bg-amber-500 hover:bg-amber-400 text-stone-950 active:scale-95'
                        }`}
                      >
                        {addedDishId === dish.id ? (
                          <>
                            <Check className="w-4 h-4 text-white" />
                            <span>¡Agregado a la Comanda!</span>
                          </>
                        ) : (
                          <>
                            <ShoppingBag className="w-4 h-4" />
                            <span>+ Agregar al Pedido</span>
                          </>
                        )}
                      </button>

                      <button
                        onClick={() => handleWhatsAppInquiry(dish, currentWeekData.title, currentDayMenu.dayName)}
                        className="w-full py-2 px-3 rounded-xl font-bold text-[11px] text-stone-700 hover:text-stone-900 bg-stone-100 hover:bg-stone-200 flex items-center justify-center gap-1.5 transition-colors"
                      >
                        <Send className="w-3.5 h-3.5 text-emerald-600" />
                        <span>Planificar para este día por WhatsApp</span>
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

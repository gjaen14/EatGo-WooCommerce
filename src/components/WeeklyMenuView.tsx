import React, { useState } from 'react';
import { 
  Calendar, 
  Flame, 
  Clock, 
  ShoppingBag, 
  Send, 
  CheckCircle2, 
  Search, 
  Sparkles, 
  ArrowRight,
  Filter,
  Check,
  Utensils
} from 'lucide-react';
import { Dish, DayOfWeek, CartItem } from '../types';
import { WEEKLY_MENUS, DayMenu } from '../data/weeklyMenuData';
import { DISHES } from '../data/menuData';

interface WeeklyMenuViewProps {
  onSelectDish: (dish: Dish) => void;
  onAddToCart?: (item: Omit<CartItem, 'cartItemId'>) => void;
  initialDay?: DayOfWeek;
}

export const WeeklyMenuView: React.FC<WeeklyMenuViewProps> = ({
  onSelectDish,
  onAddToCart,
  initialDay = 'lunes',
}) => {
  const [selectedDay, setSelectedDay] = useState<DayOfWeek>(initialDay);
  const [viewMode, setViewMode] = useState<'single' | 'all'>('single');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [addedDishId, setAddedDishId] = useState<string | null>(null);

  // Identify today's current day in Panama time (0 = Sunday, 1 = Monday, ..., 6 = Saturday)
  const currentDayIndex = new Date().getDay();
  const dayIndexMap: Record<number, DayOfWeek> = {
    1: 'lunes',
    2: 'martes',
    3: 'miercoles',
    4: 'jueves',
    5: 'viernes',
    6: 'sabado',
    0: 'lunes', // Sunday falls back to lunes for menu preview
  };
  const todayDayOfWeek = dayIndexMap[currentDayIndex];

  const activeMenu = WEEKLY_MENUS.find((m) => m.dayId === selectedDay) || WEEKLY_MENUS[0];

  const handleQuickAdd = (dish: Dish, dayName: string) => {
    if (onAddToCart) {
      const sideName = dish.availableSides && dish.availableSides.length > 0
        ? dish.availableSides[0].name
        : 'Arroz criollo';
      onAddToCart({
        dishId: dish.id,
        name: dish.name,
        basePrice: dish.price,
        unitPrice: dish.price,
        quantity: 1,
        selectedSide: sideName,
        notes: `Menú del ${dayName} con ${sideName}`,
        totalPrice: dish.price,
      });
      setAddedDishId(dish.id);
      setTimeout(() => setAddedDishId(null), 1800);
    } else {
      onSelectDish(dish);
    }
  };

  const handleWhatsAppOrderForDay = (dish: Dish, dayName: string) => {
    const text = `Hola Eat & Go! Quiero encargar para el *${dayName}*:\n🍲 *${dish.name}* ($${dish.price.toFixed(2)})\n¿Me confirman disponibilidad y despacho?`;
    window.open(`https://wa.me/50762345678?text=${encodeURIComponent(text)}`, '_blank');
  };

  return (
    <div className="space-y-8 sm:space-y-10 pb-16">
      {/* ========================================================================= */}
      {/* 1. CABECERA DE LA PÁGINA: MENÚ SEMANAL                                     */}
      {/* ========================================================================= */}
      <div className="bg-white rounded-2xl sm:rounded-3xl p-6 sm:p-8 border border-stone-200/90 shadow-xs">
        <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
          <div className="max-w-2xl">
            <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800 mb-1">
              <Calendar className="w-4 h-4 text-amber-700" />
              <span>Programación Gastronómica de Lunes a Sábado</span>
            </div>
            <h1 className="text-2xl sm:text-4xl font-black text-stone-900 tracking-tight">
              Menú Semanal Criollo
            </h1>
            <p className="mt-2 text-xs sm:text-sm text-stone-600 leading-relaxed">
              Cada día de la semana encendemos la paila con una especialidad criolla distinta. Puedes ordenar el menú del día o encargar con anticipación los almuerzos de tu equipo para toda la semana.
            </p>
          </div>

          {/* Quick controls: Mode Toggle + Search */}
          <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
            <div className="relative">
              <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-stone-400" />
              <input
                type="text"
                placeholder="Buscar plato semanal..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full sm:w-56 pl-9 pr-3 py-2 bg-stone-50 border border-stone-300 rounded-xl text-xs sm:text-sm text-stone-800 focus:outline-none focus:ring-2 focus:ring-amber-500"
              />
            </div>

            <div className="flex items-center bg-stone-100 p-1 rounded-xl border border-stone-200 text-xs font-bold self-start sm:self-auto">
              <button
                onClick={() => setViewMode('single')}
                className={`px-3 py-1.5 rounded-lg transition-all ${
                  viewMode === 'single'
                    ? 'bg-white text-stone-950 shadow-xs font-black'
                    : 'text-stone-600 hover:text-stone-900'
                }`}
              >
                Día por Día
              </button>
              <button
                onClick={() => setViewMode('all')}
                className={`px-3 py-1.5 rounded-lg transition-all ${
                  viewMode === 'all'
                    ? 'bg-white text-stone-950 shadow-xs font-black'
                    : 'text-stone-600 hover:text-stone-900'
                }`}
              >
                Semana Completa
              </button>
            </div>
          </div>
        </div>

        {/* ========================================================================= */}
        {/* SELECTOR INTERACTIVO DE DÍAS (LUNES A SÁBADO)                            */}
        {/* ========================================================================= */}
        <div className="mt-6 pt-5 border-t border-stone-100">
          <p className="text-[11px] uppercase font-bold tracking-wider text-stone-600 mb-3">
            Selecciona el día para ver platos y ordenar:
          </p>

          <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2.5">
            {WEEKLY_MENUS.map((menu) => {
              const isSelected = selectedDay === menu.dayId && viewMode === 'single';
              const isToday = todayDayOfWeek === menu.dayId;

              return (
                <button
                  key={menu.dayId}
                  onClick={() => {
                    setSelectedDay(menu.dayId);
                    setViewMode('single');
                  }}
                  className={`p-3 rounded-xl sm:rounded-2xl text-left border transition-all relative flex flex-col justify-between min-h-[96px] ${
                    isSelected
                      ? 'bg-stone-950 text-white border-stone-900 shadow-md ring-2 ring-amber-400'
                      : 'bg-white hover:bg-amber-50/50 text-stone-800 border-stone-200'
                  }`}
                >
                  <div className="flex items-center justify-between w-full">
                    <span className={`text-xs sm:text-sm font-black tracking-tight ${isSelected ? 'text-amber-400' : 'text-stone-900'}`}>
                      {menu.shortName}
                    </span>
                    {isToday && (
                      <span className="text-[9px] font-black uppercase px-1.5 py-0.5 rounded bg-emerald-500 text-white leading-none">
                        HOY
                      </span>
                    )}
                  </div>

                  <div className="mt-1">
                    <p className={`text-[10px] sm:text-[11px] font-semibold truncate ${isSelected ? 'text-stone-300' : 'text-stone-600'}`}>
                      {menu.starDishName.split(' ')[0]} {menu.starDishName.split(' ')[1]}
                    </p>
                    <span className={`text-xs font-black block mt-0.5 ${isSelected ? 'text-amber-300' : 'text-amber-800'}`}>
                      ${menu.starDishPrice.toFixed(2)}
                    </span>
                  </div>
                </button>
              );
            })}
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* VISTA 1: DÍA SELECCIONADO INDIVIDUAL (ENFOQUE COMPLETO)                   */}
      {/* ========================================================================= */}
      {viewMode === 'single' && (
        <div className="space-y-6">
          {/* Banner del Día Seleccionado */}
          <div className="rounded-2xl sm:rounded-3xl bg-stone-900 text-white p-6 sm:p-8 border border-stone-800 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
            <div className="max-w-xl">
              <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 text-xs font-bold uppercase tracking-wider mb-2">
                <Flame className="w-3.5 h-3.5" />
                <span>{activeMenu.badge}</span>
              </div>
              <h2 className="text-2xl sm:text-3xl font-black text-white tracking-tight">
                Menú del {activeMenu.dayName}
              </h2>
              <p className="text-xs sm:text-sm text-stone-300 mt-1">
                {activeMenu.subtitle}. Despacho caliente desde las 11:30 a.m. hasta las 3:30 p.m.
              </p>
            </div>

            <div className="bg-stone-800/90 rounded-2xl p-4 border border-stone-700/80 flex items-center gap-4 self-stretch sm:self-auto shrink-0">
              <img
                src={activeMenu.starDishImage}
                alt={activeMenu.starDishName}
                className="w-16 h-16 rounded-xl object-cover"
                referrerPolicy="no-referrer"
              />
              <div>
                <span className="text-[10px] font-black uppercase tracking-wider text-amber-400 block">
                  Plato Recomendado
                </span>
                <p className="text-xs sm:text-sm font-bold text-white max-w-[180px] truncate">
                  {activeMenu.starDishName}
                </p>
                <span className="text-base font-black text-amber-400">
                  ${activeMenu.starDishPrice.toFixed(2)}
                </span>
              </div>
            </div>
          </div>

          {/* Grilla de Platos del Día */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {activeMenu.dishes
              .filter(d => 
                !searchQuery || 
                d.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
                d.description.toLowerCase().includes(searchQuery.toLowerCase())
              )
              .map((dish) => (
                <div
                  key={dish.id}
                  className="bg-white rounded-2xl border border-stone-200/90 overflow-hidden shadow-xs hover:border-amber-400 transition-all flex flex-col justify-between group"
                >
                  <div className="flex flex-col sm:flex-row">
                    <div className="sm:w-2/5 h-44 sm:h-auto relative overflow-hidden bg-stone-100">
                      <img
                        src={dish.image}
                        alt={dish.name}
                        className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                        referrerPolicy="no-referrer"
                      />
                      <span className="absolute top-2.5 left-2.5 bg-stone-950/80 backdrop-blur-xs text-amber-400 text-[10px] font-black uppercase px-2 py-0.5 rounded shadow-sm">
                        {dish.badge || activeMenu.shortName}
                      </span>
                    </div>

                    <div className="sm:w-3/5 p-5 flex flex-col justify-between">
                      <div>
                        <div className="flex items-baseline justify-between gap-2">
                          <h3 className="text-base sm:text-lg font-black text-stone-900 leading-snug group-hover:text-amber-800 transition-colors">
                            {dish.name}
                          </h3>
                        </div>

                        <p className="text-xs text-stone-600 mt-1.5 leading-relaxed line-clamp-3">
                          {dish.description}
                        </p>

                        <div className="mt-3 text-[11px] text-stone-600 bg-stone-50 rounded-lg p-2 border border-stone-100">
                          <span className="font-bold text-stone-800">Guarniciones a elegir: </span>
                          <span>Arroz con guandú, arroz blanco, tajadas o patacones.</span>
                        </div>
                      </div>

                      <div className="mt-4 flex items-center justify-between pt-3 border-t border-stone-100">
                        <span className="text-lg sm:text-xl font-black text-stone-900">
                          ${dish.price.toFixed(2)}
                        </span>

                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => handleWhatsAppOrderForDay(dish, activeMenu.shortName)}
                            title="Pedir por WhatsApp para este día"
                            className="p-2.5 rounded-xl bg-emerald-50 text-emerald-700 hover:bg-emerald-100 border border-emerald-200 transition-colors"
                          >
                            <Send className="w-4 h-4 fill-current" />
                          </button>

                          <button
                            onClick={() => onSelectDish(dish)}
                            className="px-3.5 py-2 rounded-xl bg-amber-500 hover:bg-amber-400 text-stone-950 font-black text-xs shadow-xs transition-all flex items-center gap-1.5 active:scale-95"
                          >
                            <ShoppingBag className="w-3.5 h-3.5" />
                            <span>Comandar</span>
                          </button>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              ))}
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* VISTA 2: SEMANA COMPLETA (LUNES A SÁBADO EN CORRIDO)                      */}
      {/* ========================================================================= */}
      {viewMode === 'all' && (
        <div className="space-y-12">
          {WEEKLY_MENUS.map((menu) => {
            const filteredMenuDishes = menu.dishes.filter(d => 
              !searchQuery || 
              d.name.toLowerCase().includes(searchQuery.toLowerCase()) || 
              d.description.toLowerCase().includes(searchQuery.toLowerCase())
            );

            if (filteredMenuDishes.length === 0) return null;

            return (
              <div key={menu.dayId} className="space-y-4">
                <div className="flex items-center justify-between border-b border-stone-200 pb-3">
                  <div className="flex items-center gap-3">
                    <span className="w-8 h-8 rounded-lg bg-amber-500 text-stone-950 font-black text-xs flex items-center justify-center">
                      {menu.shortName.slice(0, 2).toUpperCase()}
                    </span>
                    <div>
                      <h2 className="text-xl sm:text-2xl font-black text-stone-900 tracking-tight">
                        {menu.dayName}
                      </h2>
                      <p className="text-xs text-stone-600">
                        {menu.subtitle}
                      </p>
                    </div>
                  </div>

                  <button
                    onClick={() => {
                      setSelectedDay(menu.dayId);
                      setViewMode('single');
                    }}
                    className="text-xs font-bold text-amber-700 hover:underline flex items-center gap-1"
                  >
                    <span>Ver solo {menu.shortName}</span>
                    <ArrowRight className="w-3.5 h-3.5" />
                  </button>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                  {filteredMenuDishes.map((dish) => (
                    <div
                      key={dish.id}
                      onClick={() => onSelectDish(dish)}
                      className="bg-white rounded-xl border border-stone-200/90 overflow-hidden p-3.5 flex flex-col justify-between shadow-xs hover:border-amber-400 transition-all cursor-pointer group"
                    >
                      <div>
                        <div className="h-32 rounded-lg overflow-hidden relative bg-stone-100">
                          <img
                            src={dish.image}
                            alt={dish.name}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform"
                            referrerPolicy="no-referrer"
                          />
                          <span className="absolute bottom-2 right-2 bg-stone-950/90 text-amber-400 font-black text-xs px-2 py-0.5 rounded">
                            ${dish.price.toFixed(2)}
                          </span>
                        </div>

                        <h3 className="font-bold text-sm text-stone-900 mt-2.5 line-clamp-1 group-hover:text-amber-800 transition-colors">
                          {dish.name}
                        </h3>
                        <p className="text-[11px] text-stone-500 mt-1 line-clamp-2 leading-relaxed">
                          {dish.description}
                        </p>
                      </div>

                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          onSelectDish(dish);
                        }}
                        className="mt-3 w-full py-1.5 bg-stone-100 hover:bg-amber-500 hover:text-stone-950 text-stone-800 text-xs font-bold rounded-lg transition-colors flex items-center justify-center gap-1.5"
                      >
                        <ShoppingBag className="w-3.5 h-3.5" />
                        <span>Comandar</span>
                      </button>
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      )}

      {/* ========================================================================= */}
      {/* SECCIÓN FIJA COMPLEMENTARIA: DESAYUNOS DE LUNES A SÁBADO                  */}
      {/* ========================================================================= */}
      <div className="bg-amber-50/70 border border-amber-200/80 rounded-2xl sm:rounded-3xl p-6 sm:p-8">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-5">
          <div>
            <div className="flex items-center gap-2 text-xs font-black uppercase tracking-widest text-amber-800 mb-1">
              <Clock className="w-4 h-4 text-amber-700" />
              <span>Disponible Diario de Lunes a Sábado • 6:30 a.m. a 11:00 a.m.</span>
            </div>
            <h3 className="text-xl sm:text-2xl font-black text-stone-900">
              Desayunos Típicos Fijos (Todos los Días)
            </h3>
            <p className="text-xs text-stone-600 mt-0.5">
              Hojaldres crujientes, bistec encebollado, tortillas, carimañolas y café criollo.
            </p>
          </div>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
          {DISHES.filter(d => d.category === 'desayunos').slice(0, 4).map((dish) => (
            <div
              key={dish.id}
              onClick={() => onSelectDish(dish)}
              className="bg-white rounded-xl border border-amber-200/60 p-3 flex flex-col justify-between cursor-pointer hover:border-amber-400 transition-all"
            >
              <div>
                <img
                  src={dish.image}
                  alt={dish.name}
                  className="w-full h-24 rounded-lg object-cover mb-2"
                  referrerPolicy="no-referrer"
                />
                <h4 className="font-bold text-xs text-stone-900 line-clamp-1">{dish.name}</h4>
                <p className="text-amber-800 font-black text-xs mt-1">${dish.price.toFixed(2)}</p>
              </div>

              <button
                onClick={(e) => {
                  e.stopPropagation();
                  onSelectDish(dish);
                }}
                className="mt-2.5 w-full py-1 bg-stone-900 hover:bg-stone-800 text-white text-[11px] font-bold rounded-md"
              >
                + Comandar
              </button>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

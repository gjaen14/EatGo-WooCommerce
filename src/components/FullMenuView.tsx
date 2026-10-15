import React, { useState, useMemo } from 'react';
import { Search, SlidersHorizontal, Plus, Sparkles, Clock, Check } from 'lucide-react';
import { Dish, Category } from '../types';

interface FullMenuViewProps {
  dishes: Dish[];
  onSelectDish: (dish: Dish) => void;
}

export const FullMenuView: React.FC<FullMenuViewProps> = ({
  dishes,
  onSelectDish,
}) => {
  const [selectedCategory, setSelectedCategory] = useState<string>('todos');
  const [searchQuery, setSearchQuery] = useState<string>('');

  const filteredDishes = useMemo(() => {
    return dishes.filter((dish) => {
      const matchesCategory =
        selectedCategory === 'todos' ||
        (selectedCategory === 'hoy' && dish.isDailySpecial) ||
        dish.category === selectedCategory;

      const matchesSearch =
        dish.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        dish.description.toLowerCase().includes(searchQuery.toLowerCase());

      return matchesCategory && matchesSearch;
    });
  }, [dishes, selectedCategory, searchQuery]);

  const categories = [
    { id: 'todos', label: 'Todos los Platos' },
    { id: 'hoy', label: '🔥 Menú de Hoy' },
    { id: 'desayunos', label: '🌅 Desayunos (Desde 6:30 AM)' },
    { id: 'almuerzos', label: '🍲 Almuerzos Criollos' },
    { id: 'guarniciones', label: '🍚 Guarniciones' },
    { id: 'bebidas', label: '🥤 Bebidas Selladas' },
    { id: 'postres', label: '🍯 Postres' },
  ];

  return (
    <div className="space-y-6 pb-12">
      {/* Header */}
      <div className="bg-white rounded-2xl p-6 sm:p-8 border border-stone-200 shadow-xs">
        <div className="max-w-2xl">
          <span className="text-xs font-black uppercase tracking-wider text-amber-700">
            Carta Digital Eat & Go
          </span>
          <h1 className="text-2xl sm:text-3xl font-black text-stone-900 tracking-tight mt-1">
            Catálogo Criollo Completo
          </h1>
          <p className="text-sm text-stone-600 mt-1">
            Platos preparados a diario con ingredientes locales frescos. Agrega a tu comanda y despacha en minutos.
          </p>
        </div>

        {/* Search Bar */}
        <div className="mt-5 relative max-w-md">
          <Search className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-stone-400" />
          <input
            type="text"
            placeholder="Buscar mondongo, sancocho, hojaldre, raspadura..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-2.5 bg-stone-50 text-sm border border-stone-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-amber-500 focus:bg-white"
          />
        </div>
      </div>

      {/* Category Pills */}
      <div className="flex items-center gap-1.5 overflow-x-auto no-scrollbar py-1">
        {categories.map((cat) => {
          const isActive = selectedCategory === cat.id;
          return (
            <button
              key={cat.id}
              onClick={() => setSelectedCategory(cat.id)}
              className={`whitespace-nowrap px-4 py-2 rounded-xl text-xs font-bold transition-all ${
                isActive
                  ? 'bg-amber-500 text-stone-950 shadow-xs'
                  : 'bg-white text-stone-700 hover:bg-stone-100 border border-stone-200'
              }`}
            >
              {cat.label}
            </button>
          );
        })}
      </div>

      {/* Dishes Grid */}
      {filteredDishes.length === 0 ? (
        <div className="text-center py-16 bg-white rounded-2xl border border-stone-200 p-6">
          <p className="text-stone-500 font-semibold text-sm">No encontramos platos que coincidan con tu búsqueda.</p>
          <button
            onClick={() => {
              setSearchQuery('');
              setSelectedCategory('todos');
            }}
            className="mt-3 text-xs font-bold text-amber-700 hover:underline"
          >
            Restablecer filtros
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
          {filteredDishes.map((dish) => (
            <div
              key={dish.id}
              className="bg-white rounded-2xl border border-stone-200 overflow-hidden flex flex-col justify-between hover:border-amber-400 hover:shadow-md transition-all group"
            >
              <div className="relative h-40 bg-stone-100 overflow-hidden">
                <img
                  src={dish.image}
                  alt={dish.name}
                  className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  referrerPolicy="no-referrer"
                />
                {dish.badge && (
                  <span className="absolute top-2.5 left-2.5 bg-stone-900/90 text-amber-400 text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded-md backdrop-blur-xs">
                    {dish.badge}
                  </span>
                )}
                {dish.timeAvailable && (
                  <span className="absolute bottom-2.5 left-2.5 bg-stone-900/80 text-white text-[10px] font-semibold px-2 py-0.5 rounded flex items-center gap-1">
                    <Clock className="w-3 h-3 text-amber-400" />
                    {dish.timeAvailable}
                  </span>
                )}
                <span className="absolute bottom-2.5 right-2.5 bg-white/95 text-stone-950 font-black text-sm px-2 py-0.5 rounded-md shadow-xs">
                  ${dish.price.toFixed(2)}
                </span>
              </div>

              <div className="p-4 flex-1 flex flex-col justify-between">
                <div>
                  <h3 className="font-bold text-sm text-stone-900 group-hover:text-amber-700 transition-colors">
                    {dish.name}
                  </h3>
                  <p className="text-xs text-stone-500 mt-1 line-clamp-2 leading-relaxed">
                    {dish.description}
                  </p>
                </div>

                <div className="mt-4 pt-3 border-t border-stone-100 flex items-center justify-between gap-2">
                  <div className="text-xs">
                    {dish.availableSides && (
                      <span className="text-[11px] text-stone-500">
                        {dish.availableSides.length} guarniciones
                      </span>
                    )}
                  </div>

                  <button
                    id={`btn-menu-add-${dish.id}`}
                    onClick={() => onSelectDish(dish)}
                    className="flex items-center gap-1.5 px-3 py-1.5 bg-stone-900 hover:bg-stone-800 text-white text-xs font-bold rounded-lg transition-colors active:scale-95"
                  >
                    <Plus className="w-3.5 h-3.5" />
                    <span>Agregar</span>
                  </button>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

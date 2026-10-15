import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { HomeView } from './components/HomeView';
import { WeeklyMenuView } from './components/WeeklyMenuView';
import { FourWeeksCatalogView } from './components/FourWeeksCatalogView';
import { ChristmasSpecialView } from './components/ChristmasSpecialView';
import { FullMenuView } from './components/FullMenuView';
import { CorporateView } from './components/CorporateView';
import { ContactLocationView } from './components/ContactLocationView';
import { DeliveryInfoView } from './components/DeliveryInfoView';
import { DishConfigModal } from './components/DishConfigModal';
import { CartDrawer } from './components/CartDrawer';
import { StickyComandaBar } from './components/StickyComandaBar';
import { FatFooter } from './components/FatFooter';
import { DISHES } from './data/menuData';
import { Dish, CartItem, DayOfWeek } from './types';
import { Utensils, Phone, Clock, MapPin, ShieldCheck, Heart, Sparkles, CalendarDays } from 'lucide-react';

export default function App() {
  const [currentTab, setCurrentTab] = useState<string>('home');
  const [selectedWeeklyDay, setSelectedWeeklyDay] = useState<DayOfWeek>('lunes');
  const [menuDisplayMode, setMenuDisplayMode] = useState<'4weeks' | 'singleWeek'>('4weeks');
  const [selectedDishForModal, setSelectedDishForModal] = useState<Dish | null>(null);
  const [isCartOpen, setIsCartOpen] = useState<boolean>(false);

  // Cart state initialized from localStorage
  const [cartItems, setCartItems] = useState<CartItem[]>(() => {
    try {
      const saved = localStorage.getItem('eat_and_go_cart');
      return saved ? JSON.parse(saved) : [];
    } catch {
      return [];
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('eat_and_go_cart', JSON.stringify(cartItems));
    } catch (e) {
      console.error('Error saving cart to local storage', e);
    }
  }, [cartItems]);

  const handleAddToCart = (item: Omit<CartItem, 'cartItemId'>) => {
    const newItem: CartItem = {
      ...item,
      cartItemId: `${item.dishId}-${Date.now()}-${Math.random().toString(36).substr(2, 4)}`,
    };
    setCartItems(prev => [...prev, newItem]);
  };

  const handleUpdateQuantity = (cartItemId: string, newQuantity: number) => {
    if (newQuantity <= 0) {
      handleRemoveItem(cartItemId);
      return;
    }
    setCartItems(prev =>
      prev.map(item => {
        if (item.cartItemId === cartItemId) {
          return {
            ...item,
            quantity: newQuantity,
            totalPrice: item.unitPrice * newQuantity,
          };
        }
        return item;
      })
    );
  };

  const handleRemoveItem = (cartItemId: string) => {
    setCartItems(prev => prev.filter(item => item.cartItemId !== cartItemId));
  };

  const handleClearCart = () => {
    setCartItems([]);
  };

  const cartTotal = cartItems.reduce((sum, item) => sum + item.totalPrice, 0);
  const cartCount = cartItems.reduce((sum, item) => sum + item.quantity, 0);

  const todayDishes = DISHES.filter(d => d.isDailySpecial);
  const breakfastDishes = DISHES.filter(d => d.category === 'desayunos');

  return (
    <div className="min-h-screen flex flex-col bg-[#FDFBF7] text-[#1A1A1A] selection:bg-[#FF4F00] selection:text-white relative overflow-x-hidden">
      {/* Blobs orgánicos decorativos de fondo (Fast Food Moderno) */}
      <div className="fixed -top-40 -right-40 w-96 h-96 bg-orange-200/20 rounded-full blur-3xl pointer-events-none -z-10" />
      <div className="fixed top-1/2 -left-40 w-96 h-96 bg-yellow-200/20 rounded-full blur-3xl pointer-events-none -z-10" />
      
      {/* Top Navbar */}
      <Navbar
        currentTab={currentTab}
        onSelectTab={(tab) => {
          setCurrentTab(tab);
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }}
        cartCount={cartCount}
        cartTotal={cartTotal}
        onOpenCart={() => setIsCartOpen(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1 max-w-[1300px] w-full mx-auto px-4 sm:px-6 pt-6 sm:pt-8">
        {/* PÁGINA 1: HOME / INICIO */}
        {(currentTab === 'home' || currentTab === 'hoy') && (
          <HomeView
            todayDishes={todayDishes}
            breakfastDishes={breakfastDishes}
            onSelectDish={(dish) => setSelectedDishForModal(dish)}
            onNavigateTab={(tab, day) => {
              if (day) {
                setSelectedWeeklyDay(day);
                setMenuDisplayMode('singleWeek');
              }
              setCurrentTab(tab);
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
            onOpenCart={() => setIsCartOpen(true)}
            onAddToCart={handleAddToCart}
          />
        )}

        {/* PÁGINA 2: MENÚ SEMANAL Y CATÁLOGO DE 4 SEMANAS (LUNES A SÁBADO) */}
        {currentTab === 'semanal' && (
          <div className="space-y-6">
            {/* Selector de modo de visualización: Catálogo 4 Semanas vs Semana Actual */}
            <div className="bg-white border border-stone-200/90 rounded-2xl p-3 sm:p-4 shadow-xs flex flex-col sm:flex-row items-center justify-between gap-3">
              <div className="flex items-center gap-2.5">
                <div className="w-9 h-9 rounded-xl bg-amber-500/15 border border-amber-500/30 text-amber-800 flex items-center justify-center shrink-0">
                  <CalendarDays className="w-5 h-5" />
                </div>
                <div>
                  <h2 className="text-xs sm:text-sm font-black text-stone-900 leading-tight">
                    Programación Menú Ejecutivo & Paila
                  </h2>
                  <p className="text-[11px] text-stone-500">
                    4 semanas completas de rotación criolla panameña sin repetir platos
                  </p>
                </div>
              </div>

              <div className="flex items-center bg-stone-100 p-1 rounded-xl border border-stone-200 w-full sm:w-auto justify-center">
                <button
                  type="button"
                  onClick={() => setMenuDisplayMode('4weeks')}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                    menuDisplayMode === '4weeks'
                      ? 'bg-amber-500 text-stone-950 shadow-xs'
                      : 'text-stone-600 hover:text-stone-950'
                  }`}
                >
                  Catálogo 4 Semanas
                </button>
                <button
                  type="button"
                  onClick={() => setMenuDisplayMode('singleWeek')}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                    menuDisplayMode === 'singleWeek'
                      ? 'bg-amber-500 text-stone-950 shadow-xs'
                      : 'text-stone-600 hover:text-stone-950'
                  }`}
                >
                  Vista Día por Día
                </button>
              </div>
            </div>

            {menuDisplayMode === '4weeks' ? (
              <FourWeeksCatalogView
                onAddToCart={handleAddToCart}
                onSelectDish={(dish) => setSelectedDishForModal(dish)}
              />
            ) : (
              <WeeklyMenuView
                onSelectDish={(dish) => setSelectedDishForModal(dish)}
                onAddToCart={handleAddToCart}
                initialDay={selectedWeeklyDay}
              />
            )}
          </div>
        )}

        {/* PÁGINA 3: EMPRESAS & COMBOS */}
        {(currentTab === 'empresa' || currentTab === 'corporativo') && (
          <CorporateView onAddToCart={handleAddToCart} />
        )}

        {/* PÁGINA 4: DÓNDE COMER Y RETIRAR PEDIDOS */}
        {(currentTab === 'contacto' || currentTab === 'despacho') && (
          <ContactLocationView />
        )}

        {/* MÓDULO ESPECIAL: TEMPORADA NAVIDEÑA (CENAS EMPRESARIALES & FAMILIARES) */}
        {currentTab === 'navidad' && (
          <ChristmasSpecialView onAddToCart={handleAddToCart} />
        )}

        {/* CARTA COMPLETA (MODO CATÁLOGO GENERAL) */}
        {currentTab === 'menu' && (
          <FullMenuView
            dishes={DISHES}
            onSelectDish={(dish) => setSelectedDishForModal(dish)}
          />
        )}
      </main>

      {/* Dish Configuration Modal (Side & drink customization) */}
      <DishConfigModal
        dish={selectedDishForModal}
        onClose={() => setSelectedDishForModal(null)}
        onAddToCart={handleAddToCart}
      />

      {/* Cart & Checkout Drawer */}
      <CartDrawer
        isOpen={isCartOpen}
        onClose={() => setIsCartOpen(false)}
        items={cartItems}
        onUpdateQuantity={handleUpdateQuantity}
        onRemoveItem={handleRemoveItem}
        onClearCart={handleClearCart}
      />

      {/* Floating Sticky Comanda Bar */}
      <StickyComandaBar
        items={cartItems}
        onOpenCart={() => setIsCartOpen(true)}
      />

      {/* 7. FAT FOOTER (Pie de Página Robusto) */}
      <FatFooter onNavigateTab={setCurrentTab} />
    </div>
  );
}

import React, { useState } from 'react';
import { 
  ShoppingBag, 
  Clock, 
  MapPin, 
  PhoneCall, 
  Building2, 
  ChevronDown, 
  Check 
} from 'lucide-react';

interface NavbarProps {
  currentTab: string;
  onSelectTab: (tab: string) => void;
  cartCount: number;
  cartTotal: number;
  onOpenCart: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentTab,
  onSelectTab,
  cartCount,
  cartTotal,
  onOpenCart,
}) => {
  const [deliveryContext, setDeliveryContext] = useState<'oficina' | 'pickgo'>('oficina');
  const [showLocationDropdown, setShowLocationDropdown] = useState(false);

  const handleCategoryClick = (sectionIdOrTab: string) => {
    if (
      sectionIdOrTab === 'home' ||
      sectionIdOrTab === 'semanal' ||
      sectionIdOrTab === 'empresa' ||
      sectionIdOrTab === 'contacto' ||
      sectionIdOrTab === 'navidad' ||
      sectionIdOrTab === 'menu'
    ) {
      onSelectTab(sectionIdOrTab);
      window.scrollTo({ top: 0, behavior: 'smooth' });
      return;
    }

    // If currently not on 'home', switch to 'home' first then scroll
    if (currentTab !== 'home') {
      onSelectTab('home');
      setTimeout(() => {
        const el = document.getElementById(sectionIdOrTab);
        if (el) {
          el.scrollIntoView({ behavior: 'smooth' });
        }
      }, 100);
    } else {
      const el = document.getElementById(sectionIdOrTab);
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      }
    }
  };

  return (
    <header className="w-full shadow-md">
      {/* ========================================================================= */}
      {/* NIVEL 1: TOP BAR (Light Theme Puro - Estilo Papa John's)                  */}
      {/* Fondo #FFFFFF, padding 20px, logo libre y utilidades en gris #333333      */}
      {/* ========================================================================= */}
      <div className="w-full bg-white border-b border-[#EAEAEA]">
        <div className="max-w-[1300px] mx-auto px-4 sm:px-6 py-4 sm:py-5 flex items-center justify-between gap-6">
          {/* Lado Izquierdo: Logo Libre + Tagline & Badge */}
          <button
            onClick={() => {
              onSelectTab('home');
              window.scrollTo({ top: 0, behavior: 'smooth' });
            }}
            className="flex items-center gap-4 text-left group focus:outline-none shrink-0"
          >
            {/* Logo Transparente Libre Directo sobre el Blanco */}
            <div className="h-11 sm:h-13 flex items-center justify-center group-hover:scale-105 transition-transform shrink-0">
              <img 
                src="/images/logo.png" 
                alt="Eat & Go" 
                className="h-10 sm:h-12 w-auto object-contain block"
              />
            </div>

            {/* Bloque de Texto Derecho en Columna */}
            <div className="flex flex-col justify-center gap-1">
              {/* Fila superior: Badge */}
              <div>
                <span className="inline-block text-[10px] uppercase font-black tracking-wider px-2 py-0.5 rounded-full bg-[#FF4F00] text-white shadow-xs">
                  CRIOLLO EXPRESS
                </span>
              </div>
              {/* Fila inferior: Tagline en gris oscuro (#4A4A4A) */}
              <p className="text-xs text-[#4A4A4A] font-medium leading-none tracking-wide">
                Sabor de Paila Auténtico • Despacho Sin Filas
              </p>
            </div>
          </button>

          {/* Lado Derecho: Menú de Utilidades (Gris Oscuro #333333, gap: 32px) */}
          <div className="hidden lg:flex items-center justify-end gap-8 text-xs">
            {/* Ítem 1: [Icono Pin] Dónde Comer */}
            <button 
              onClick={() => {
                onSelectTab('contacto');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="flex items-center gap-2 cursor-pointer group transition-colors"
            >
              <MapPin className="w-4 h-4 text-[#333333] group-hover:text-[#FF4F00] shrink-0 transition-colors" />
              <span className="font-semibold text-[#333333] group-hover:text-[#FF4F00] transition-colors">
                Dónde Comer
              </span>
            </button>

            {/* Ítem 2: [Icono Reloj] 6:30 AM - 3:30 PM */}
            <div className="flex items-center gap-2">
              <Clock className="w-4 h-4 text-[#333333] shrink-0" />
              <span className="font-semibold text-[#333333]">
                6:30 AM - 3:30 PM
              </span>
            </div>

            {/* Ítem 3: [Icono Teléfono] +507 6234-5678 */}
            <a
              href="https://wa.me/50762345678?text=Hola%20Eat%20%26%20Go!%20Quiero%20hacer%20un%20pedido%20o%20consultar%20el%20menú."
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-2 group transition-colors"
            >
              <PhoneCall className="w-4 h-4 text-[#333333] group-hover:text-emerald-600 shrink-0 transition-colors" />
              <span className="font-semibold text-[#333333] group-hover:text-emerald-600 transition-colors">
                +507 6234-5678
              </span>
            </a>

            {/* Ítem 4: [Icono Edificio] Empresas (Factura con RUC) */}
            <button
              onClick={() => {
                onSelectTab('empresa');
                window.scrollTo({ top: 0, behavior: 'smooth' });
              }}
              className="flex items-center gap-2 group transition-colors"
            >
              <Building2 className="w-4 h-4 text-[#333333] group-hover:text-[#FF4F00] shrink-0 transition-colors" />
              <span className="font-semibold text-[#333333] group-hover:text-[#FF4F00] transition-colors">
                Empresas (Factura con RUC)
              </span>
            </button>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* NIVEL 2: BOTTOM NAV (Minimalista Papa John's Style)                       */}
      {/* 3 enlaces esenciales con gap 40px, activo píldora y Carrito solo a la der */}
      {/* ========================================================================= */}
      <nav 
        aria-label="Navegación principal y carrito"
        className="w-full sticky top-0 z-40 bg-stone-900/98 backdrop-blur-md border-b border-stone-800"
      >
        <div className="max-w-[1300px] mx-auto px-4 sm:px-6 h-14 flex items-center justify-between gap-4">
          {/* Lado Izquierdo: 3 enlaces con espaciado generoso (gap: 40px) */}
          <div className="flex items-center gap-10 overflow-x-auto no-scrollbar py-1 text-xs">
            {/* INICIO */}
            <button
              id="nav-btn-home"
              onClick={() => handleCategoryClick('home')}
              className={`whitespace-nowrap tracking-wide transition-all ${
                currentTab === 'home' || currentTab === 'hoy'
                  ? 'bg-[#FF4F00] text-white px-6 py-2 rounded-full font-black shadow-md shadow-orange-600/30'
                  : 'text-stone-300 hover:text-white font-semibold'
              }`}
            >
              INICIO
            </button>

            {/* MENÚ SEMANAL */}
            <button
              id="nav-btn-semanal"
              onClick={() => handleCategoryClick('semanal')}
              className={`whitespace-nowrap tracking-wide transition-all ${
                currentTab === 'semanal'
                  ? 'bg-[#FF4F00] text-white px-6 py-2 rounded-full font-black shadow-md shadow-orange-600/30'
                  : 'text-stone-300 hover:text-white font-semibold'
              }`}
            >
              MENÚ SEMANAL
            </button>

            {/* DÓNDE COMER & RETIRAR */}
            <button
              id="nav-btn-contacto"
              onClick={() => handleCategoryClick('contacto')}
              className={`whitespace-nowrap tracking-wide transition-all ${
                currentTab === 'contacto'
                  ? 'bg-[#FF4F00] text-white px-6 py-2 rounded-full font-black shadow-md shadow-orange-600/30'
                  : 'text-stone-300 hover:text-white font-semibold'
              }`}
            >
              DÓNDE COMER & RETIRAR
            </button>
          </div>

          {/* Lado Derecho: Carrito SOLO anclado al margen derecho */}
          <div className="flex items-center shrink-0">
            <button
              id="open-cart-button"
              onClick={onOpenCart}
              className="flex items-center gap-2 sm:gap-2.5 px-5 py-2.5 bg-[#FF4F00] hover:bg-[#e04500] active:scale-95 text-white font-black text-xs sm:text-sm rounded-full shadow-lg shadow-orange-600/30 transition-all border border-orange-400/40 tracking-tight cursor-pointer"
            >
              <ShoppingBag className="w-4 h-4 text-white fill-white/20 shrink-0" />
              <span className="hidden sm:inline font-extrabold uppercase tracking-wider">
                Carrito
              </span>
              
              <span className="flex items-center gap-1.5 pl-2 border-l border-white/30">
                <span className="bg-stone-950 text-[#FACC15] font-black text-[11px] px-2 py-0.5 rounded-full">
                  {cartCount}
                </span>
                <span className="font-black text-white">
                  ${cartTotal.toFixed(2)}
                </span>
              </span>
            </button>
          </div>
        </div>
      </nav>
    </header>
  );
};

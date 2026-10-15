import React from 'react';
import { 
  Instagram, 
  Facebook, 
  Linkedin, 
  PhoneCall, 
  ShieldCheck, 
  Clock, 
  MapPin, 
  Utensils 
} from 'lucide-react';

interface FatFooterProps {
  onNavigateTab?: (tab: string) => void;
}

export const FatFooter: React.FC<FatFooterProps> = ({ onNavigateTab }) => {
  const handleNav = (tab: string, elementId?: string) => {
    if (onNavigateTab) {
      onNavigateTab(tab);
    }
    if (elementId) {
      setTimeout(() => {
        const el = document.getElementById(elementId);
        if (el) el.scrollIntoView({ behavior: 'smooth' });
      }, 100);
    }
  };

  return (
    <footer className="w-full bg-stone-200/90 text-stone-800 border-t border-stone-300">
      {/* Contenedor Centrado */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-12 sm:py-16">
        {/* Layout en 6 Columnas (Columna 1 más ancha) */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-8 sm:gap-6">
          {/* Columna 1: Más ancha (Logo + Redes Sociales en línea) */}
          <div className="lg:col-span-2 pr-0 lg:pr-6">
            <div className="flex items-center gap-3 mb-3">
              <div className="h-10 px-2.5 py-1 rounded-lg bg-white border border-stone-200 shadow-2xs flex items-center justify-center shrink-0">
                <img 
                  src="/images/logo.png" 
                  alt="Eat & Go" 
                  className="h-full w-auto object-contain block" 
                />
              </div>
              <div>
                <span className="text-[11px] text-stone-700 font-extrabold uppercase tracking-wider block">
                  CRIOLLO EXPRESS
                </span>
                <p className="text-[11px] text-stone-500 font-normal leading-tight">
                  Sabor de Paila Auténtico
                </p>
              </div>
            </div>

            <p className="text-xs text-stone-600 leading-relaxed max-w-sm mb-5">
              La paila auténtica panameña adaptada al ritmo de oficina. Almuerzos calientes y desayunos criollos empacados en bandejas térmicas troqueladas a 75°C, con factura fiscal y cero filas.
            </p>

            {/* Redes Sociales (Iconos en línea) */}
            <div>
              <span className="block text-[11px] font-bold uppercase tracking-wider text-stone-700 mb-2">
                Conecta con nosotros:
              </span>
              <div className="flex items-center gap-2.5">
                <a
                  href="https://instagram.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Instagram de Eat and Go"
                  className="w-9 h-9 rounded-lg bg-stone-300/80 hover:bg-amber-500 hover:text-stone-950 text-stone-700 flex items-center justify-center transition-colors shadow-2xs"
                >
                  <Instagram className="w-4 h-4" />
                </a>

                <a
                  href="https://wa.me/50762345678"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="WhatsApp de Eat and Go"
                  className="w-9 h-9 rounded-lg bg-stone-300/80 hover:bg-emerald-600 hover:text-white text-stone-700 flex items-center justify-center transition-colors shadow-2xs"
                >
                  <PhoneCall className="w-4 h-4" />
                </a>

                <a
                  href="https://facebook.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="Facebook de Eat and Go"
                  className="w-9 h-9 rounded-lg bg-stone-300/80 hover:bg-blue-600 hover:text-white text-stone-700 flex items-center justify-center transition-colors shadow-2xs"
                >
                  <Facebook className="w-4 h-4" />
                </a>

                <a
                  href="https://linkedin.com"
                  target="_blank"
                  rel="noopener noreferrer"
                  aria-label="LinkedIn de Eat and Go"
                  className="w-9 h-9 rounded-lg bg-stone-300/80 hover:bg-sky-700 hover:text-white text-stone-700 flex items-center justify-center transition-colors shadow-2xs"
                >
                  <Linkedin className="w-4 h-4" />
                </a>
              </div>
            </div>
          </div>

          {/* Columna 2: Menú Criollo (Lista de enlaces verticales) */}
          <div>
            <h3 className="font-extrabold text-xs uppercase tracking-wider text-stone-900 mb-3.5">
              Navegación
            </h3>
            <div className="flex flex-col gap-2 text-xs text-stone-600">
              <button 
                onClick={() => handleNav('home')}
                className="text-left hover:text-amber-700 hover:underline transition-colors font-medium"
              >
                🏠 Inicio & Resumen
              </button>
              <button 
                onClick={() => handleNav('semanal')}
                className="text-left hover:text-amber-700 hover:underline transition-colors font-medium"
              >
                📅 Menú Semanal (Lun-Sáb)
              </button>
              <button 
                onClick={() => handleNav('navidad')}
                className="text-left text-emerald-800 hover:text-emerald-950 hover:underline transition-colors font-semibold"
              >
                🎄 Especial Navideño (15 Nov)
              </button>
              <button 
                onClick={() => handleNav('home', 'seccion-grilla-destacada')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                🔥 Platos del Día
              </button>
              <button 
                onClick={() => handleNav('home', 'desayunos-fijos')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                🌅 Desayunos (6:30 AM)
              </button>
              <button 
                onClick={() => handleNav('menu')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                📜 Carta Completa
              </button>
            </div>
          </div>

          {/* Columna 3: Servicios Corporativos (Lista de enlaces verticales) */}
          <div>
            <h3 className="font-extrabold text-xs uppercase tracking-wider text-stone-900 mb-3.5">
              Para Empresas
            </h3>
            <div className="flex flex-col gap-2 text-xs text-stone-600">
              <button 
                onClick={() => handleNav('empresa')}
                className="text-left hover:text-amber-700 hover:underline transition-colors font-medium text-stone-900"
              >
                🏢 Página Empresa & Combos
              </button>
              <button 
                onClick={() => handleNav('empresa')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                Bandejas para Reuniones de Oficina
              </button>
              <button 
                onClick={() => handleNav('empresa')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                Combos para 5 & 10 Personas
              </button>
              <button 
                onClick={() => handleNav('empresa')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                Factura Fiscal con RUC (DGI)
              </button>
              <button 
                onClick={() => handleNav('empresa')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                Entrega Garantizada a las 12:00 MD
              </button>
            </div>
          </div>

          {/* Columna 4: Dónde Comer y Retirar (Lista de enlaces verticales) */}
          <div>
            <h3 className="font-extrabold text-xs uppercase tracking-wider text-stone-900 mb-3.5">
              Ubicación & Retiro
            </h3>
            <div className="flex flex-col gap-2 text-xs text-stone-600">
              <button 
                onClick={() => handleNav('contacto')}
                className="text-left hover:text-amber-700 hover:underline transition-colors font-medium text-stone-900"
              >
                📍 Dónde Comer & Retirar
              </button>
              <button 
                onClick={() => handleNav('contacto')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                Calle 50, Obarrio
              </button>
              <button 
                onClick={() => handleNav('contacto')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                Pick & Go Express (10 min)
              </button>
              <button 
                onClick={() => handleNav('contacto')}
                className="text-left hover:text-amber-700 hover:underline transition-colors"
              >
                Horarios: 6:30 AM - 3:30 PM
              </button>
              <button 
                onClick={() => handleNav('contacto')}
                className="text-left hover:text-amber-700 hover:underline transition-colors font-medium text-amber-800"
              >
                Enviar Consulta Directa
              </button>
            </div>
          </div>

          {/* Columna 5: Horarios y Seguridad (Lista de enlaces verticales) */}
          <div>
            <h3 className="font-extrabold text-xs uppercase tracking-wider text-stone-900 mb-3.5">
              Horario & Calidad
            </h3>
            <div className="flex flex-col gap-2 text-xs text-stone-600">
              <div className="flex items-center gap-1.5 text-stone-700">
                <Clock className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                <span>Desayunos: 6:30 - 11 AM</span>
              </div>
              <div className="flex items-center gap-1.5 text-stone-700">
                <Utensils className="w-3.5 h-3.5 text-amber-600 shrink-0" />
                <span>Almuerzos: 11:30 - 3:30 PM</span>
              </div>
              <button 
                onClick={() => handleNav('empresa')}
                className="text-left hover:text-amber-700 hover:underline transition-colors flex items-center gap-1.5"
              >
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
                <span>Garantía Térmica (75°C) & Empaques</span>
              </button>
              <button 
                onClick={() => handleNav('contacto')}
                className="text-left hover:text-amber-700 hover:underline transition-colors text-[11px]"
              >
                Gastronomía Criolla Panameña
              </button>
              <a 
                href="https://wa.me/50762345678"
                target="_blank"
                rel="noopener noreferrer"
                className="hover:text-emerald-700 hover:underline transition-colors font-semibold text-emerald-800 pt-1"
              >
                WhatsApp: +507 6234-5678
              </a>
            </div>
          </div>
        </div>

        {/* Sub-Footer (Cierre): Franja final inferior separada por línea sutil, texto centrado con Copyright y legales */}
        <div className="mt-12 pt-6 border-t border-stone-300 flex flex-col sm:flex-row items-center justify-between gap-3 text-center sm:text-left text-xs text-stone-600">
          <p className="mx-auto sm:mx-0">
            © {new Date().getFullYear()} Eat & Go S.A. — Menú Digital Criollo Express. Todos los derechos reservados.
          </p>
          <div className="flex items-center justify-center gap-4 text-[11px] text-stone-500">
            <span>R.U.C. 1557890-1-859472 DV 45</span>
            <span>•</span>
            <span className="hover:underline cursor-pointer">Términos de Servicio</span>
            <span>•</span>
            <span className="hover:underline cursor-pointer">Aviso de Privacidad</span>
          </div>
        </div>
      </div>
    </footer>
  );
};

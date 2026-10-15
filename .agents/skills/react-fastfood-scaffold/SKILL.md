---
name: react-fastfood-scaffold
description: Inicializa y estructura aplicaciones React (Vite + TSX) para negocios de comida rápida utilizando TailwindCSS v4, Lucide React y Motion, siguiendo la paleta y design system de Eat&Go. Usa este skill cuando el usuario pida crear una app de comida rápida, scaffold de fast food o estructura React Eat&Go.
---

# 🍔 React Fast-Food App Scaffolding (Eat&Go Style)

Este skill define la receta para inicializar aplicaciones React orientadas a restaurantes, food trucks y delivery con el sistema de diseño Eat&Go.

## 🛠️ Stack Tecnológico
- **Build Tool:** Vite (React + TypeScript).
- **Styling:** Tailwind CSS v4 (`@tailwindcss/vite`).
- **Iconos:** Lucide React.
- **Animaciones:** Framer Motion (`motion`).
- **Routing/State:** SPA con `React.useState` o `React Router Dom`.

---

## 🎨 Sistema de Diseño & Tokens
- **Brand Primary (Naranja):** `#FF4F00` (`bg-orange-600` / `text-orange-600`)
- **Brand Secondary (Amarillo):** `#FCE694` / `#FACC15` (`bg-yellow-400`)
- **Text Dark:** `#1A1A1A` (`text-zinc-900`)
- **Background:** `#FDFBF7` / `#F9F5F1` (Fondo global neutro)
- **Card BG:** Glassmorphic `#FFFFFF` (`bg-white/40 backdrop-blur-md`)
- **CTA WhatsApp:** `#059669` (`bg-emerald-600`)

---

## 📐 Patrones de UI (Correcto vs. Incorrecto)
- **❌ Incorrecto:** Usar cajas blancas sólidas rectangulares y sombras oscuras pesadas.
- **✅ Correcto:** Implementar glassmorphism (`backdrop-blur-lg bg-white/40 border border-white/50 rounded-[32px]`).
- **❌ Incorrecto:** Botones cuadrados con bordes rígidos.
- **✅ Correcto:** Botones totalmente redondeados (`rounded-full`) con sombras del mismo tono de la marca.

---

## 📁 Estructura del Proyecto
```text
src/
├── App.tsx             # Layout principal con blobs decorativos de fondo
├── main.tsx            # Punto de entrada
├── data.ts             # Mock data (consultar resources/mock-data.ts)
├── index.css           # Import de fuente Outfit y tema Tailwind
├── context/
│   └── CartContext.tsx # Lógica de carrito y envío a WhatsApp
├── components/         # Navbar, Footer, ProductCard
└── pages/              # Home, Menu, Cart, Checkout
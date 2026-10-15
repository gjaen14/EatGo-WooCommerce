# 📦 Plantillas de Elementor - Eat&Go

Este directorio contiene las plantillas exportadas en formato nativo JSON de **Elementor** listas para ser importadas en WordPress.

---

## 📁 Archivos Disponibles

1. **`header_duotone.json`**  
   - **Tipo:** Plantilla de Cabecera (Header / Theme Builder).  
   - **Estructura:**  
     - **Top Bar (Blanco puro `#FFFFFF`):** Logo Eat&Go libre sin cajas, badge `[CRIOLLO EXPRESS]`, lema *"Sabor de Paila Auténtico"* y enlaces de utilidad a la derecha (Día/Horarios, WhatsApp directo, Conoce Eat&Go).  
     - **Bottom Bar (Oscuro carbón `#18181B`):** Navegación minimalista de 3 enlaces (`INICIO`, `MENÚ SEMANAL`, `DÓNDE COMER & RETIRAR`) con botón píldora activo en naranja `#FF4F00`, y botón Carrito flotante en el extremo derecho.

2. **`home_body.json`**  
   - **Tipo:** Plantilla de Página (Page).  
   - **Estructura:**  
     - **Hero Section:** Banner de impacto criollo con CTAs directos a WhatsApp y ancla a menú.  
     - **Barra Menú de Hoy:** Franja naranja destacando platos recién salidos de la paila.  
     - **3 Platos Destacados (Grid 4:5):** Tarjetas con fondo oscuro `#1C1917`, foto de plato, descripción y botón píldora *"Agregar"*.  
     - **Explorar Menú Semanal:** Cabecera y distribución de los días de la semana laboral.

---

## 🚀 Pasos para Importar en WordPress

1. Ingresa a tu panel de administración de WordPress (`/wp-admin`).
2. En el menú lateral, ve a **Plantillas** → **Plantillas guardadas**.
3. Haz clic en el botón superior **Importar plantillas**.
4. Selecciona el archivo JSON deseado (ej. `header_duotone.json` o `home_body.json`) y presiona **Importar ahora**.
5. **Para el Header:**  
   - Si usas Elementor Pro: Ve a **Theme Builder** → **Header** y publícalo con la condición *"Entire Site"* (Todo el sitio).
6. **Para el Home:**  
   - Crea o edita tu página de Inicio con Elementor.  
   - Haz clic en el icono de carpeta (Añadir plantilla) → pestaña **Mis Plantillas** → Insertar `Eat&Go - Home Page Body`.
7. **Reemplazo de Imágenes:**  
   - Cada plantilla cuenta con etiquetas de imagen como `[IMG_LOGO_URL]`, `[IMG_HERO_BANNER_URL]`, `[IMG_PLATO_1_URL]`. Simplemente haz clic en el widget de imagen en Elementor y selecciona tu archivo desde la Biblioteca de Medios.

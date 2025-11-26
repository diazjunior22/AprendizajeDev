🏷️ Guía Completa de Estudio — Tailwind CSS
📌 1. Introducción
1.1 ¿Qué es Tailwind CSS?

Filosofía Utility-First

Diferencias con Bootstrap / CSS tradicional

Cuándo usar Tailwind

1.2 Setup / Instalación

Instalación vía CDN (modo prueba)

Instalación vía NPM

Configuración inicial (tailwind.config.js)

Estructura del proyecto recomendada

📌 2. Fundamentos Base

Aquí se aprende lo esencial para empezar a usar Tailwind.

2.1 Espaciado

Margin (m, mt, mx, etc.)

Padding (p, py, px)

Gap

2.2 Tamaños

Width (w-*, max-w-*)

Height (h-*, max-h-*)

2.3 Tipografía

Tamaño (text-*)

Peso (font-*)

Alineación (text-center, text-left, etc.)

Line-height (leading-*)

Tracking (tracking-*)

2.4 Colores

Texto: text-*

Fondo: bg-*

Bordes: border-*

Gradientes (bg-gradient-to-*)

2.5 Bordes y Sombras

border, border-*

rounded-*

shadow-*

📌 3. Responsive Design
3.1 Breakpoints

sm:, md:, lg:, xl:, 2xl:

3.2 Mobile First

Estilo base → mejoras en desktop

3.3 Responsive Utilities

Columnas

Tipografía

Ocultar/mostrar (hidden, block, md:hidden)

📌 4. Layouts Modernos
4.1 Flexbox

flex, flex-col, flex-row

justify-*, items-*

basis-*, grow, shrink

4.2 Grid System

grid-cols-*

gap-*

Responsive grids

auto-fit y minmax()

4.3 Positioning

relative, absolute, fixed, sticky

z-*

Offsets (top-*, left-*)

📌 5. Interactividad & Animaciones
5.1 Pseudo Estados

hover:

focus:

active:

disabled:

5.2 Transiciones

transition, duration-*, ease-*

5.3 Animaciones

animate-bounce, animate-spin

Personalizar animaciones en config

📌 6. Formularios & Componentes Básicos
6.1 Inputs

Estilos base

Focus rings

Errores y validación visual

6.2 Botones

Variantes: primario, secundario, peligro

Hover + transición

6.3 Cards

Imagen + título + descripción + CTA

6.4 Modals

Overlay + positioning

6.5 Navbars

Sticky, responsive toggle

📌 7. Dark Mode
7.1 Configuración (darkMode: "class")
7.2 Uso de clases dark:*
7.3 Toggle Manual con JavaScript
📌 8. Reutilización y Escalabilidad
8.1 @apply en CSS

Crear componentes reutilizables

8.2 Tailwind Config avanzado

Extender colores

Fuentes personalizadas

Espaciados, sombras, animaciones personalizadas

8.3 Naming System (Pattern UI)
📌 9. Ecosistema UI (Opcional)
9.1 DaisyUI
9.2 Flowbite
9.3 Headless UI
9.4 Preline UI
9.5 Shadcn + Tailwind (React)
📌 10. Proyectos Prácticos

Esta sección es clave para tu repo.

Proyecto	Categoría	Qué Practicas
Mini Card UI	Basicos	Tipografía + Spacing
Landing Page	Responsive	Hero + layout + CTA
Login UI	Componentes	Formularios + validación
Dashboard	Avanzado	Grid + sidebar + modales
App UI Clone (Netflix / Spotify)	Diseño real	Dark mode + responsive UX
Portfolio Pro	Final	Todo + Deployment
📌 11. Optimización y Deploy
11.1 PurgeCSS (Optimizar tamaño)
11.2 Minify Build
11.3 Deploy en:

Netlify

Vercel

GitHub Pages
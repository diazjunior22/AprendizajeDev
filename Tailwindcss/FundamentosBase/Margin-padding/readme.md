# 📌 Tailwind Spacing — Margin, Padding & Gap

El espaciado controla separación interna o externa de los elementos.

---

## 🧱 1️⃣ Margin (`m-*`)

👉 Espacio **externo** del elemento.

| Clase | Descripción |
|-------|-------------|
| `m-4` | Margen en todos los lados |
| `mx-4` | Horizontal (izquierda/derecha) |
| `my-4` | Vertical (arriba/abajo) |
| `mt-4` / `mb-4` | Arriba / Abajo |
| `ml-4` / `mr-4` | Izquierda / Derecha |
| `m-auto` | Centrado horizontal automático |

Ejemplo:

```html
<div class="mt-6 ml-4">Caja con margen</div>
🎯 2️⃣ Padding (p-*)
👉 Espacio interno, dentro del elemento.

Clase	Descripción
p-4	Todos los lados
px-4	Horizontal
py-4	Vertical
pt-4, pb-4, pl-4, pr-4	Lados específicos

Ejemplo:

html
Copy code
<button class="px-6 py-3 bg-blue-600 text-white rounded">Botón</button>
🧩 3️⃣ Gap (solo en flex y grid)
👉 Controla espacio entre elementos hijos.

Ejemplo:

html
Copy code
<div class="flex gap-4">
  <div class="bg-red-400 w-16 h-16"></div>
  <div class="bg-red-500 w-16 h-16"></div>
</div>
📐 4️⃣ Width & Height
👉 Tamaños responsivos y escalas útiles.

Ejemplos:

w-full   → 100% ancho
w-1/2    → mitad del contenedor
w-64     → tamaño fijo (16rem)

h-16     → altura fija
h-screen → altura de toda la pantalla
Ejemplo real:


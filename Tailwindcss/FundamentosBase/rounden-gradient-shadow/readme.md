# 🎨 Bordes, Redondeado, Sombras & Gradientes en Tailwind CSS

---

## 1️⃣ Bordes (`border-*`)

Controla visibilidad, grosor y estilo del borde.

| Clase | Uso |
|-------|-----|
| `border` | 1px border |
| `border-2`, `border-4`, `border-8` | grosor |
| `border-gray-500`, `border-blue-600` | color |
| `border-dashed`, `border-dotted`, `border-double` | estilo |

Ejemplo:

```html
<div class="border-2 border-blue-600 rounded-lg p-4">Caja con borde</div>
2️⃣ Bordes Redondeados (rounded-*)
Clase	Forma
rounded-none	Sin esquinas
rounded-sm, rounded-md, rounded-xl	Radio progresivo
rounded-full	Total (círculo si es cuadrado)

Ejemplo:

html
Copy code
<button class="bg-green-600 text-white px-4 py-2 rounded-full">
  Continuar
</button>
3️⃣ Sombras (shadow-*)
Añaden profundidad al diseño.

Clase	Intensidad
shadow-sm	Muy ligera
shadow	normal
shadow-md	media
shadow-lg	fuerte
shadow-xl	muy fuerte
shadow-2xl	extrema
shadow-none	sin sombra

Ejemplo:

html
Copy code
<div class="shadow-lg rounded-xl p-6 bg-white">Card con sombra</div>
4️⃣ Gradientes (bg-gradient-to-*)
Direcciones disponibles:

Clase	Dirección
bg-gradient-to-r	Izquierda → derecha
bg-gradient-to-l	Derecha → izquierda
bg-gradient-to-b	Arriba → abajo
bg-gradient-to-t	Abajo → arriba
bg-gradient-to-bl / to-br / to-tr	diagonales


⭐ Tips Profesionales

✔ Usa shadow-sm para UI minimalista
✔ Usa gradientes en CTA, headers, backgrounds
✔ Usa rounded-lg y shadow-md para componentes modernos
✔ Combina border + hover + transition para mejores efectos

🧪 Ejemplo final limpio:
<button class="bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-6 py-3 rounded-lg shadow-lg hover:scale-105 transition">
  Empezar ahora
</button>
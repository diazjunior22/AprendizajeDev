# 🎨 Colors & Design System en Tailwind

Tailwind tiene una paleta de colores lista basada en tonos y niveles:

gray, slate, zinc, neutral, red, green, blue, indigo, violet...

php-template
Copy code

Cada color tiene niveles del `50` al `900`.

Ejemplo:

```html
<p class="text-blue-600">Texto azul</p>
<div class="bg-red-500 text-white p-4">Fondo rojo</div>
1️⃣ Texto (text-color)
html
Copy code
<p class="text-gray-500">Texto gris</p>
<p class="text-green-600">Texto verde</p>
<p class="text-indigo-700">Texto indigo</p>
2️⃣ Fondos (bg-color)
html
Copy code
<div class="bg-blue-500 text-white p-3 rounded">Botón azul</div>
3️⃣ Bordes (border-color)
html
Copy code
<input class="border border-gray-300 p-2 rounded" />
4️⃣ Hover, Focus, Active
html
Copy code
<button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
  Guardar
</button>
5️⃣ Design System Real (⚠️ Importante)
En proyectos reales NO usas colores random.

En lugar de bg-blue-600, crearás tu propio sistema:

📁 tailwind.config.js:

js
Copy code
extend: {
  colors: {
    primary: "#4F46E5",
    danger: "#DC2626",
    success: "#22C55E",
  }
}
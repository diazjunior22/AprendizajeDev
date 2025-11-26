🔧 1.5 Formas de usar Tailwind
Método	Uso recomendado
CDN (sin instalación)	Para aprender y pruebas rápidas
NPM (instalación real)	Proyectos reales y escalables
Frameworks (Next.js, React, Vue, Laravel, Django)	Desarrollo profesional



📦 1.7 Instalar Tailwind (2 opciones)
🔹 Método rápido — CDN (solo para practicar)
<script src="https://cdn.tailwindcss.com"></script>

Ejemplo mínimo:

<h1 class="text-3xl font-bold text-blue-500">Hola Tailwind 🚀</h1>

🔹 Método profesional — Instalación con Node
npm install -D tailwindcss
npx tailwindcss init

Luego crea input.css:
@tailwind base;
@tailwind components;
@tailwind utilities;


Y compila:

npx tailwindcss -i ./input.css -o ./output.css --watch

🌑 1.8 Tailwind en Modo Producción

Tailwind elimina clases no usadas, dejando el CSS final muy liviano:

Desarrollo → ~3MB

Producción → ~20–50 KB

Eso lo hace ideal para:

✔ Web apps
✔ SaaS
✔ Dashboards
✔ UI moderna
✔ Mobile-first websites
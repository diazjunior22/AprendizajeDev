🧩 1.1 ¿Qué es Tailwind CSS?

Tailwind CSS es un framework CSS basado en utilidades (utility-first).
Esto significa que, en lugar de escribir estilos en un archivo CSS, usas clases pequeñas y reutilizables directamente en tu HTML para construir tus diseños.

Ejemplo:

<button class="px-4 py-2 bg-blue-600 text-white rounded-md">
  Enviar
</button>


No necesitas escribir esto en CSS:

button {
  padding: 10px 20px;
  background-color: #2563eb;
  color: #fff;
  border-radius: 6px;
}


Tailwind te da clases listas, rápidas y responsivas.


🎯 1.2 ¿Por qué usar Tailwind?
✔ Ventajas principales
Ventaja	Explicación
🚀 Crear interfaces rápido	No vuelves a pensar en nombres de clases CSS como .btn-primary
🎨 Consistencia visual	El sistema de diseño (tipografías, espacios, colores) está definido
📱 Responsive fácil	Las clases responsive se agregan con prefijos (sm:, md:, lg:)
⚡ Optimizado	Tailwind elimina clase no usada → el CSS final es muy ligero
🧩 Escalable	Puedes crear temas, componentes, dark mode y UI profesional

❌ Desventajas (al inicio)
Desventaja	Cómo se supera
HTML parece "lleno de clases"	Con práctica y @apply se vuelve legible
Hay que aprender muchas utilidades	VSCode autocompleta → se aprende rápido






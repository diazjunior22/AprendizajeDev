# ✨ Tipografía en Tailwind CSS

La tipografía define tamaño, peso, color, alineación y espaciado de letras en una interfaz.

Tailwind ofrece clases utilitarias para controlar cada aspecto **sin escribir CSS**.

---

## 1️⃣ Tamaños (`text-size`)

Basado en una escala real utilizada en diseño moderno.

| Clase | Tamaño |
|-------|--------|
| `text-xs` | Muy pequeño |
| `text-sm` | Pequeño |
| `text-base` | Default |
| `text-lg` | Grande |
| `text-xl`, `text-2xl`, `text-4xl` | Títulos |

Ejemplo:

```html
<h1 class="text-4xl font-bold">Título</h1>


2️⃣ Peso de Fuente (font-weight)
Clase	Peso
font-light	Delgado
font-normal	Normal
font-medium	Medio
font-semibold	Semibold
font-bold	Negrita

3️⃣ Alineación (text-left, text-center...)
<p class="text-center">Texto centrado</p>
<p class="text-justify">Texto justificado</p>

4️⃣ Colores (text-{color})
<p class="text-gray-600">Texto gris</p>
<p class="text-blue-600">Texto azul</p>


Los colores se basan en paletas predeterminadas que luego puedes personalizar.

5️⃣ Altura de línea (leading) y espaciado entre letras (tracking)
<p class="leading-relaxed tracking-wide">
  Este texto tiene buena lectura.
</p>

Leading	Uso
leading-tight	Títulos
leading-normal	Párrafos
leading-relaxed	Lectura cómoda
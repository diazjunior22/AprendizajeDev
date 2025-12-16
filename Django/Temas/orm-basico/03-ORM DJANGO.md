# Django ORM — CRUD Completo (Crear, Leer, Actualizar y Borrar)

Este documento es una guía práctica para aprender cómo manejar datos usando el ORM de Django. Aquí encontrarás ejemplos reales de cómo insertar, consultar, modificar y eliminar datos desde Django sin escribir SQL.

---

## 📌 ¿Qué es el ORM?

El **ORM (Object Relational Mapping)** permite trabajar con bases de datos usando Python en lugar de SQL.

📍 Ejemplo: en lugar de escribir:

```sql
SELECT * FROM tareas;
```

En Django escribes:

```python
Tarea.objects.all()
```

---

## 🧱 Modelo base para los ejemplos

Usaremos este modelo:

```python
from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True, blank=True)
    estado = models.CharField(max_length=50, default="pendiente")

    def __str__(self):
        return self.titulo
```

---

# 1️⃣ CREAR REGISTROS (INSERT)

### ✔️ Forma estándar

```python
tarea = Tarea(titulo="Aprender Django", descripcion="Repasar ORM")
tarea.save()
```

### ✔️ Forma directa (más usada)

```python
Tarea.objects.create(
    titulo="Ir al gimnasio",
    descripcion="Entrenamiento pesado",
    estado="en progreso"
)
```

### ✔️ Crear múltiples registros (bulk)

```python
Tarea.objects.bulk_create([
    Tarea(titulo="Leer 10 páginas"),
    Tarea(titulo="Estudiar inglés"),
])
```

---

# 2️⃣ LEER REGISTROS (SELECT)

### ✔️ Obtener todos los registros

```python
Tarea.objects.all()
```

### ✔️ Filtrar resultados

```python
Tarea.objects.filter(estado="pendiente")
```

### ✔️ Obtener un solo objeto

```python
tarea = Tarea.objects.get(id=1)
```

⚠️ Si no existe: error.

### ✔️ Obtener con seguridad (`.first()`)

```python
tarea = Tarea.objects.filter(id=1).first()
```

### ✔️ Ordenar resultados

```python
Tarea.objects.order_by("titulo")     # ascendente
Tarea.objects.order_by("-titulo")    # descendente
```

### ✔️ Búsquedas con coincidencias (LIKE)

```python
Tarea.objects.filter(titulo__icontains="django")   # sin distinguir mayúsculas
```

📍 Otros filtros útiles:

| Filtro         | Uso                                  |
| -------------- | ------------------------------------ |
| `__contains`   | Contiene texto (sensible mayúsculas) |
| `__startswith` | Empieza con                          |
| `__endswith`   | Termina con                          |

---

# 3️⃣ ACTUALIZAR REGISTROS (UPDATE)

### ✔️ Editar un registro

```python
tarea = Tarea.objects.get(id=1)
tarea.estado = "completada"
tarea.save()
```

### ✔️ Actualizar múltiples registros

```python
Tarea.objects.filter(estado="pendiente").update(estado="en progreso")
```

---

# 4️⃣ ELIMINAR REGISTROS (DELETE)

### ✔️ Eliminar uno

```python
tarea = Tarea.objects.get(id=1)
tarea.delete()
```

### ✔️ Eliminar varios

```python
Tarea.objects.filter(estado="completada").delete()
```

---

## 🔧 Métodos útiles del ORM

### ✔️ Contar registros

```python
Tarea.objects.count()
```

### ✔️ Verificar si existe un registro

```python
Tarea.objects.filter(titulo="Ir al gimnasio").exists()
```

### ✔️ Obtener solo columnas específicas (optimizado)

```python
Tarea.objects.values("titulo", "estado")
```

---

## ⚡ Consultas avanzadas

### OR lógico (Q objects)

```python
from django.db.models import Q

Tarea.objects.filter(
    Q(estado="pendiente") | Q(estado="en progreso")
)
```
🧠 ¿Qué es un Q object en Django?

Normalmente, cuando haces filtros con .filter(), Django usa AND entre condiciones.

Ejemplo:

Tarea.objects.filter(estado="pendiente", prioridad="alta")


Esto significa:

Solo trae tareas donde estado sea pendiente y además la prioridad sea alta.

Pero… ¿qué pasa si necesitas un OR? 🤔
Ejemplo: buscar tareas que estén pendientes o en progreso.

Ahí entra en acción Q().

🔥 Uso del OR con Q
from django.db.models import Q

Tarea.objects.filter(
    Q(estado="pendiente") | Q(estado="en progreso")
)

Traducción mental:

Dame tareas donde el estado sea pendiente O el estado sea en progreso.

📌 ¿Por qué usar Q()?

Porque .filter() por defecto no sabe usar OR.
Q() permite:

✔ mezclar condiciones con | (OR)
✔ mezclar condiciones con & (AND)
✔ negar condiciones con ~ (NOT)

🧪 Ejemplos útiles
👉 Buscar por OR
Tarea.objects.filter(Q(prioridad="alta") | Q(prioridad="media"))

👉 Mezclar AND + OR
Tarea.objects.filter(
    (Q(estado="pendiente") | Q(estado="en progreso")) &
    Q(prioridad="alta")
)


Traducción:

Dame tareas que estén pendientes o en progreso pero también tengan prioridad alta.

👉 Usar NOT
Tarea.objects.filter(~Q(estado="completada"))


Significa:

Todas las tareas excepto las completadas.

🧠 Resumen en una tabla
Operador	Django	Significado
`	`	OR
&	AND	Ambas condiciones
~	NOT	Negación

























### Comparar valores del mismo modelo (F objects)

```python
from django.db.models import F

Tarea.objects.update(descripcion=F("titulo"))
```

---

# 🚀 Resumen rápido CRUD

| Acción     | Django ORM                      | Equivalente SQL |
| ---------- | ------------------------------- | --------------- |
| Crear      | `.create()` o `.save()`         | `INSERT`        |
| Leer       | `.filter()`, `.all()`, `.get()` | `SELECT`        |
| Actualizar | `.update()` o `.save()`         | `UPDATE`        |
| Borrar     | `.delete()`                     | `DELETE`        |

---

# 📝 Ejercicio recomendado

1. Crear 3 tareas
2. Listarlas ordenadas por nombre
3. Cambiar el estado de una
4. Buscar solo las que están pendientes
5. Eliminar una

---

### ✔️ Fin del documento

Continúa con consultas optimizadas: `select_related()` y `prefetch_related()` cuando trabajes con relaciones.
⚡ 4. Consultas optimizadas: select_related() y prefetch_related()

Cuando trabajamos con relaciones entre modelos en Django, es importante optimizar las consultas a la base de datos.

¿Por qué? Porque si accedes a datos relacionados sin optimización, Django hará múltiples consultas extra (problema llamado N+1 queries).

📌 select_related() — Para relaciones ForeignKey o **OneToOne`

Optimiza trayendo los datos relacionados en una sola consulta SQL usando JOIN.

Ejemplo:

# Sin optimización: hace una consulta por cada post al acceder al autor
posts = Post.objects.all()
for p in posts:
    print(p.autor.nombre)

Esto puede generar muchas consultas.

Optimizado:

posts = Post.objects.select_related('autor')
for p in posts:
    print(p.autor.nombre)

✔ Ahora todo se hace en una sola consulta.

📌 Úsalo cuando la relación sea:

ForeignKey

OneToOneField

📌 prefetch_related() — Para ManyToMany o relación inversa

Este método hace dos consultas pero Django las combina en memoria para evitar repeticiones.

Ejemplo:

# Tareas con etiquetas (muchos a muchos)
tareas = Tarea.objects.prefetch_related('etiquetas')
for t in tareas:
    print(t.etiquetas.all())

Sin prefetch_related(), Django haría una consulta extra por cada tarea.

✔ Con prefetch_related() solo hace:
1 consulta para tareas
1 consulta para etiquetas relacionadas

📊 Comparación rápida
Caso	Usa
Relaciones 1→1 o 1→N	select_related()
Relaciones N↔N o reverse FK (ej: post.comentarios)	prefetch_related()
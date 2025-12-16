# Relaciones en Django (ForeignKey, ManyToMany, OneToOne)

Este documento explica cómo funcionan las relaciones entre modelos en Django. Es una guía clara para entender cómo conectar tablas en la base de datos utilizando Django ORM.

---

## 📌 ¿Qué son las relaciones en Django?

En Django, los modelos pueden conectarse entre sí usando tipos especiales de campos. Estos campos permiten replicar relaciones como las de una base de datos relacional.

Los tres tipos principales son:

| Relación     | Django            | Ejemplo del mundo real       |
| ------------ | ----------------- | ---------------------------- |
| One to One   | `OneToOneField`   | Un usuario → un único perfil |
| One to Many  | `ForeignKey`      | Un autor → muchos libros     |
| Many to Many | `ManyToManyField` | Estudiantes ↔ Cursos         |

---

## 🧩 1. ForeignKey (One-To-Many)

Esta relación significa:

> *Un registro pertenece a uno, pero ese uno puede tener muchos registros relacionados.*

Ejemplo: un **autor puede tener muchos libros**, pero cada libro tiene **solo un autor**.

```python
from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
```

### 🔧 Opciones de `on_delete`

| Modo          | Comportamiento                                  |
| ------------- | ----------------------------------------------- |
| `CASCADE`     | Borra los libros si el autor desaparece.        |
| `SET_NULL`    | Pone el campo en `NULL` (requiere `null=True`). |
| `PROTECT`     | Evita borrar si hay relaciones.                 |
| `SET_DEFAULT` | Pone un valor por defecto.                      |

### 🔄 Acceso inverso

```python
autor.libro_set.all()
```

Puedes renombrar esto usando `related_name`:

```python
autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
```

Ahora se consulta así:

```python
autor.libros.all()
```

---

## 🔗 2. ManyToMany (Muchos a Muchos)

Usada cuando **ambos lados pueden tener múltiples relaciones**.

Ejemplo: estudiantes y cursos.

```python
class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    estudiantes = models.ManyToManyField(Estudiante)
```

### 🛠️ Uso

```python
juan = Estudiante.objects.create(nombre="Juan")
python = Curso.objects.create(nombre="Python")
python.estudiantes.add(juan)
```

### 🔄 Consultas

```python
python.estudiantes.all()  # Estudiantes inscritos
juan.curso_set.all()      # Cursos del estudiante
```

### 🧱 ManyToMany con tabla intermedia

Si necesitas añadir datos extra a la relación (como calificación), usa `through=`:

```python
class Curso(models.Model):
    nombre = models.CharField(max_length=100)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, through="Inscripcion")

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.FloatField(null=True)
```

---

## 🧍‍♂️ 3. OneToOne (Uno a Uno)

Ejemplo clásico: usuario y perfil.

```python
from django.contrib.auth.models import User

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"
```

Esto asegura que **cada usuario tenga solo un perfil**.

---

## 🚀 Resumen rápido

| Relación   | Campo Django      | Cuándo usar                                       |
| ---------- | ----------------- | ------------------------------------------------- |
| OneToOne   | `OneToOneField`   | Información extendida de un usuario, config extra |
| OneToMany  | `ForeignKey`      | Blog → posts, categoría → productos               |
| ManyToMany | `ManyToManyField` | Roles, etiquetas, cursos, habilidades             |

---

## 📚 ¿Qué sigue?

Opciones sugeridas para avanzar:

* Formularios con relaciones
* Administración de relaciones en Django Admin
* Consultas avanzadas (`select_related`, `prefetch_related`)

---

### ✔️ Fin del documento.

# 📌 Django: Migraciones, Admin y ORM

Guía resumida para aprender y recordar.

---

## 🧱 1. Modelos en Django

Los **modelos** representan tablas en la base de datos. Cada modelo es una clase en Python dentro del archivo `models.py`.

Django convierte estas clases en tablas usando migraciones.

---

### 📌 1.1 ¿Qué es un modelo?

Un modelo es una estructura que define cómo serán los datos: qué campos tienen, qué tipo de datos guardan y cómo se relacionan con otros modelos.

Ejemplo básico:

```python
from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creado = models.DateTimeField(auto_now_add=True)
```

En este ejemplo:

* Django creará una tabla llamada `app_producto`.
* Cada instancia es un registro en la base de datos.

---

### 🧱 1.2 Tipos comunes de campos

| Tipo              | Uso                                 |
| ----------------- | ----------------------------------- |
| `CharField`       | Texto corto (nombres, títulos)      |
| `TextField`       | Texto grande (descripciones largas) |
| `IntegerField`    | Números enteros                     |
| `DecimalField`    | Números con decimales (precios)     |
| `BooleanField`    | Verdadero/Falso                     |
| `DateTimeField`   | Fecha y hora                        |
| `ForeignKey`      | Relación uno a muchos               |
| `ManyToManyField` | Relación muchos a muchos            |
| `EmailField`      | Emails con validación integrada     |

Ejemplo con varios campos:

```python
class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    activo = models.BooleanField(default=True)
    registrado = models.DateTimeField(auto_now_add=True)
```

---

### 🏷️ 1.3 Opciones avanzadas dentro de modelos (`Meta`)

Podemos personalizar nombre de tabla, ordenamiento y otros detalles.

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
```

---

### ⭐ 1.4 Métodos útiles en modelos

Puedes personalizar la forma en que se muestra el objeto:

```python
class Producto(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
```

Esto hace que al mostrar el objeto en admin, salga el nombre y no: `Producto object(3)`.

También puedes crear métodos personalizados:

```python
class Producto(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.IntegerField(default=0)

    def precio_final(self):
        return self.precio - (self.precio * self.descuento / 100)
```

---

## 🧱 2. Migraciones en Django

Las migraciones son la forma en que Django sincroniza los modelos con la base de datos.

### 🔨 Crear migraciones

```bash
python manage.py makemigrations
```

Esto detecta cambios en los modelos.

### 💾 Aplicar migraciones

```bash
python manage.py migrate
```

Esto aplica los cambios a la base de datos.

### 📋 Ver estado

```bash
python manage.py showmigrations
```

---

## 🛠️ 2. Django Admin

El admin permite gestionar datos desde el navegador.

### 🔑 Crear usuario administrador

```bash
python manage.py createsuperuser
```

### 📁 Registrar modelos en admin

En `app/admin.py`:

```python
from django.contrib import admin
from .models import Producto
admin.site.register(Producto)
```

### ✨ Personalización básica

```python
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'fecha_creado')
    search_fields = ('nombre',)
    list_filter = ('categoria',)
```

---

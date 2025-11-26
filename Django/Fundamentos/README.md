# 🧠 Django Study Project
Repositorio creado con el objetivo de aprender Django paso a paso, documentando cada tema con ejemplos y buenas prácticas.
---
## 📌 Tema 1: Entorno, Proyecto Django, App, Modelos y Admi
### 🏗️ 1. Crear entorno virtual

```bash
# Windows
python -m venv venv
# Activar
venv\Scripts\activate

# Instalar Django
pip install django

#Crear Proyecto
django-admin startproject core .


--------------------------------------------------------------
#ESTUTURA DEL PROYECTO INICIAL
Fundamentos/
    manage.py
    core/
        settings.py
        urls.py
        asgi.py
        wsgi.py

#EJECUTAR EL SERVIDOR
python manage.py runserver



#🧩 5. Crear una app
python manage.py startapp blog

#ESTRUCTURA DE LA APP
Notas/
    models.py
    views.py
    admin.py
    apps.py

#📌 6.                                  Registrar la app en settings.py
#Debos registrar cada app para 
Editar myproject/settings.py en INSTALLED_APPS:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'blog',
]

#🏗️ 7. Crear modelo (base de datos)
# Modelo = diseño de los datos (estructura)
# Django usa ese modelo para crear tablas automáticas en la base de datos.

Archivo: notas/models.py

from django.db import models
class Nota(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

#🛠️ 8. Migraciones (crear tablas)
python manage.py makemigrations
python manage.py migrate

#🏛️ 9. Registrar modelo en admin
Archivo: notas/admin.py
from django.contrib import admin
from .models import Post
admin.site.register(Post)

#🔐 10. Crear usuario administrador
python manage.py createsuperuser

#🖥️ 11. Acceder al panel Admin
http://127.0.0.1:8000/admin/


#Podrás crear objetos del modelo desde el panel.

#🎯 Ejercicio: Añadir categorías

Modificar models.py:

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


Ejecutar migraciones:

python manage.py makemigrations
python manage.py migrate


Registrar en admin.py:

from .models import Category
admin.site.register(Category)

#📂 Estructura final del proyecto
myproject/
│── manage.py
│── venv/
│── db.sqlite3
│
└── notas/
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── apps.py
    └── migrations/

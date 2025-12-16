Día 15 — Instalar DRF + Configurar Endpoints
API básica creada con Django Rest Framework

Este documento explica paso por paso cómo instalar Django Rest Framework (DRF) y cómo crear una API básica funcional usando serializers, viewsets y routers.
Todo está explicado corto, claro y acompañado de código.

✅ 1. Instalar Django Rest Framework

Asegúrate de tener tu proyecto Django ya creado.

📦 Instalar DRF:
pip install djangorestframework

🧩 Agregar DRF a INSTALLED_APPS

En config/settings.py:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'core',       # tu app principal
]

✅ 2. Crear modelo simple para exponer como API

En core/models.py:

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre


Migraciones:

python manage.py makemigrations
python manage.py migrate

✅ 3. Crear un Serializer (convierte el modelo a JSON)

En core/serializers.py:

from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']

✅ 4. Crear un ViewSet (controlador de API)

En core/views.py:

from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


Este ViewSet te da automáticamente:

GET (lista)

GET (detalle)

POST (crear)

PUT/PATCH (editar)

DELETE (borrar)

✅ 5. Crear Router para generar endpoints automáticamente

En core/urls.py:

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

✅ 6. Conectar las rutas de la app al proyecto

En config/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),   # ← IMPORTANTE
]

🚀 7. Probar la API

Ejecutar el servidor:

python manage.py runserver


Visita:

👉 http://127.0.0.1:8000/api/productos/

Y verás tu API funcionando con interfaz visual gracias a DRF.

📌 Endpoints disponibles automáticamente
Método	URL	Acción
GET	/api/productos/	Listar productos
POST	/api/productos/	Crear producto
GET	/api/productos/<id>/	Ver detalle
PUT	/api/productos/<id>/	Actualizar
PATCH	/api/productos/<id>/	Actualizar parcial
DELETE	/api/productos/<id>/	Eliminar
✅ README.md — Permisos + Autenticación JWT (Día 18)
# Día 18 — Permisos + Autenticación JWT en Django REST Framework

En este día aprenderás a proteger tu API usando **JWT (JSON Web Token)**, permitiendo que los usuarios inicien sesión y obtengan un **token de acceso** y un **refresh token**.

---

# 🎯 Objetivo del día

- Instalar y configurar JWT  
- Crear endpoints de login y refresh  
- Proteger endpoints usando permisos  
- Probar autenticación con cliente REST (Insomnia / Postman)

---

# 📌 1. Instalación de JWT

Instala la librería oficial recomendada para DRF:

```bash
pip install djangorestframework-simplejwt


Agrega en settings.py:

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
]

📌 2. Configurar JWT en Django

En config/settings.py añade:

from datetime import timedelta

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}


✔️ Esto hace que todas las vistas requieran autenticación por defecto (a menos que lo sobrescribas).

📌 3. Endpoints para login y refresh

En config/urls.py:

from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

urlpatterns = [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('core.urls')),
]

🔥 ¿Qué hace cada endpoint?
Endpoint	Función
/api/auth/token/	Usuario envía email/username + password y recibe access token + refresh token
/api/auth/token/refresh/	Envía refresh token y obtiene uno nuevo para seguir autenticado
📌 4. Cómo funciona el login con JWT

Enviar POST a:

POST /api/auth/token/


Body:

{
  "username": "admin",
  "password": "123456"
}


Respuesta:

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
  "access": "eyJhbGciOiJIUzI1..."
}


access token → dura poco (ej: 5 min)

refresh token → dura más (ej: 24h)

🔐 5. Proteger endpoints usando permisos

Ejemplo de vista con permiso:

from rest_framework import permissions, viewsets
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios logueados

Otros permisos comunes:
Permiso	Descripción
AllowAny	Cualquiera puede entrar
IsAuthenticated	Solo usuarios logueados
IsAdminUser	Solo admin
IsAuthenticatedOrReadOnly	Lectura pública, escritura protegida
📌 6. Cómo enviar el token en los request

En POSTMAN / INSOMNIA:

Header:

Authorization: Bearer <ACCESS_TOKEN>


Ejemplo:

Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

📌 7. Probar Refresh Token

Enviar POST a:

POST /api/auth/token/refresh/


Body:

{
  "refresh": "<refresh_token>"
}


Respuesta:

{
  "access": "nuevo_token"
}

📌 8. Crear usuario para pruebas
python manage.py createsuperuser
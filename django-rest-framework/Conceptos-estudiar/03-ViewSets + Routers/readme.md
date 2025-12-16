Día 17 — ViewSets + Routers

Endpoints limpios y mantenibles en Django REST Framework

Los ViewSets permiten agrupar en una sola clase todas las operaciones CRUD (listar, crear, editar, borrar).
Los Routers generan automáticamente las URLs necesarias.

🧠 1. ¿Qué es un ViewSet?

Un ViewSet combina varias vistas en una sola clase.

👉 Antes:
Necesitabas crear una vista para cada acción:

ListView

CreateView

RetrieveView

UpdateView

DeleteView

👉 Con ViewSet:
Una sola clase controla todo.

Ejemplo básico:

from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


ModelViewSet incluye:

list

retrieve

create

update

partial_update

destroy

🔌 2. ¿Qué es un Router?

Un router genera automáticamente todas las rutas CRUD para tus ViewSets.

Ejemplo:

from rest_framework import routers
from .views import ProductoViewSet

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)


Esto crea automáticamente:

Método	URL	Acción
GET	/api/productos/	listar
POST	/api/productos/	crear
GET	/api/productos/<id>/	obtener uno
PUT	/api/productos/<id>/	actualizar
PATCH	/api/productos/<id>/	actualizar parcial
DELETE	/api/productos/<id>/	eliminar

🔥 Tú no escribes esas URL manualmente.

🛣️ 3. core/urls.py completo
from rest_framework import routers
from django.urls import path, include
from .views import ProductoViewSet, ClienteViewSet, PedidoViewSet

router = routers.DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

📥 4. Conectar el router al proyecto principal

En config/urls.py:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # Aquí montas tu API completa
]

🔍 5. Ejemplo completo de ViewSet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    # Permite leer sin login, crear/editar solo con login
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtros integrados (búsqueda, ordenar)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre']
    ordering_fields = ['precio', 'nombre']

🧪 6. Probar los endpoints

Después de correr:

python manage.py runserver


Ir a:

👉 http://127.0.0.1:8000/api/productos/

👉 http://127.0.0.1:8000/api/productos/1/

Verás una interfaz automática donde puedes:

Crear productos

Listarlos

Editarlos

Borrarlos

Gracias al ViewSet + Router.

📦 7. Beneficios
Sin ViewSet	Con ViewSet
Más código	Menos código
Rutas manuales	Rutas automáticas
Mantenimiento difícil	Mantenimiento fácil
Código repetido	Código limpio
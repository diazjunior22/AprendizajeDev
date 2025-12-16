¿Qué es un Serializer?

En Django REST Framework, un serializer:

Convierte modelos → JSON (para enviar datos a clientes).

Convierte JSON → modelos (para crear o actualizar datos).

Valida datos automáticamente.

Controla qué campos se exponen.

Es similar a un ModelForm, pero para APIs.

🧩 ¿Qué es un ModelSerializer?

ModelSerializer crea automáticamente:

Campos basados en el modelo

Validaciones por tipo de dato

Validación de required, unique, etc.

Métodos .create() y .update() por defecto

Es la forma más usada en proyectos reales.

📦 Ejemplo base (Modelo)

Usaremos este modelo simple:

# core/models.py
class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

🛠️ Crear un ModelSerializer
# core/serializers.py
from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto                     # modelo a convertir
        fields = ['id', 'nombre', 'precio']  # campos expuestos en JSON


Con esto DRF:

Convierte instancias en JSON

Valida que precio sea número

Valida que nombre no esté vacío

Crea y actualiza automáticamente

📤 Cómo se ve el JSON generado
{
  "id": 1,
  "nombre": "Cuaderno",
  "precio": "12000.00"
}

📥 Cómo se usa en una Vista
# core/views.py
from rest_framework import viewsets
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

🧪 Crear un Producto vía API
POST → /api/productos/
{
  "nombre": "Lapicero",
  "precio": 2500
}


Respuesta:

{
  "id": 5,
  "nombre": "Lapicero",
  "precio": "2500.00"
}

🎛️ Personalizar campos

Ejemplo: campo solo lectura:

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio']
        read_only_fields = ['id']

🧰 Validaciones personalizadas
Validar precio mínimo:
def validate_precio(self, value):
    if value <= 0:
        raise serializers.ValidationError("El precio debe ser mayor a 0")
    return value
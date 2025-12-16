# Validaciones + Signals en Django — Guía completa

Este README está pensado para que **documentes** y **aprendas** cómo implementar validaciones y signals en Django, con explicaciones detalladas, ejemplos prácticos y buenas prácticas. Incluye código de ejemplo, casos de uso comunes y recomendaciones para pruebas y despliegue.

---

## Índice

1. Introducción
2. Validaciones en Django

   * Validators a nivel de campo
   * `clean_<fieldname>()`, `clean()` y `full_clean()`
   * Validación en forms y ModelForms
   * Validación en serializers (DRF)
   * Validadores reutilizables y configuración internacionalizada
   * Errores comunes y cómo mostrarlos en el frontend
3. Signals en Django

   * ¿Qué son y cuándo usarlos?
   * Signals incorporadas: `pre_save`, `post_save`, `pre_delete`, `post_delete`, `m2m_changed`, `post_migrate`, etc.
   * Cómo crear y usar signals personalizadas
   * `@receiver` y `dispatch_uid`
   * Dónde conectar signals (módulo `signals.py` y `apps.py`)
   * Pautas para evitar problemas comunes (doble registro, orden, side effects)
4. Patrón: lógica automática (dónde poner la lógica: signals vs model methods vs managers)
5. Manejo de transacciones y signals (`transaction.on_commit`)
6. Buenas prácticas y rendimiento
7. Testing de validaciones y signals
8. Ejemplos prácticos completos

   * Validador personalizado: verificador de identificación
   * Signal: enviar email tras creación de usuario
   * Signal: actualizar cache y contador en post_save
   * Signal m2m: reaccionar a cambios en relación many-to-many
9. Checklist para producción
10. Referencias rápidas: snippets útiles

---

## 1. Introducción

Las **validaciones** garantizan que los datos cumplan reglas antes de guardarse o procesarse. Los **signals** permiten reaccionar a eventos del ciclo de vida de los modelos (guardado, borrado, cambios en relaciones, migraciones, etc.). Ambos son poderosas herramientas para mantener integridad y lógica automática en tu aplicación.

> Tip: Antes de crear una signal, pregúntate si no sería más claro implementar la lógica dentro de un método del modelo, un `Manager`, o en la vista/servicio. Las signals son útiles para desacoplar comportamientos que deben ejecutarse en respuesta a eventos y cuando varias apps necesitan reaccionar al mismo evento.

---

## 2. Validaciones en Django

### 2.1 Validators a nivel de campo

Django permite pasar validadores a los campos del modelo:

```python
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=120, validators=[MinLengthValidator(3)])
    sku = models.CharField(
        max_length=20,
        validators=[RegexValidator(r'^SKU-[A-Z0-9]+$', 'Formato inválido: debe comenzar con "SKU-"')]
    )
```

Los validadores se ejecutan cuando llamas a `full_clean()` o cuando usas ModelForms.

### 2.2 `clean_<fieldname>()`, `clean()` y `full_clean()`

* `clean_<fieldname>(self)` — define un método en el `ModelForm` o en el `Model` para validar un campo concreto.
* `clean(self)` — valida campos en conjunto; ideal para reglas que dependen de múltiples campos.
* `full_clean()` — ejecuta validadores de campos, `clean_fields()`, `clean()` y validación de uniqueness. No se llama automáticamente en `Model.save()` por defecto.

**Ejemplo en modelo:**

```python
from django.core.exceptions import ValidationError

class Reserva(models.Model):
    inicio = models.DateTimeField()
    fin = models.DateTimeField()

    def clean(self):
        if self.fin <= self.inicio:
            raise ValidationError({'fin': 'La fecha de fin debe ser posterior a la fecha de inicio.'})
```

**Nota:** Si quieres forzar validación antes de guardar, puedes llamar a `self.full_clean()` dentro de `save()` — pero piensa en el rendimiento y en duplicidades (a veces es preferible validar en forms o serializers):

```python
def save(self, *args, **kwargs):
    self.full_clean()
    super().save(*args, **kwargs)
```

### 2.3 Validación en forms y ModelForms

Las `Form` y `ModelForm` ejecutan validaciones automáticamente en `is_valid()`.

```python
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['inicio', 'fin']

    def clean(self):
        cleaned = super().clean()
        if cleaned.get('fin') <= cleaned.get('inicio'):
            raise forms.ValidationError('Fecha fin debe ser posterior a inicio')
        return cleaned
```

### 2.4 Validación en DRF (serializers)

Si usas Django REST Framework, implementa `validate_<fieldname>()` y `validate(self, attrs)` en serializers.

```python
class ReservaSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['fin'] <= attrs['inicio']:
            raise serializers.ValidationError('La fecha fin debe ser posterior')
        return attrs
```

### 2.5 Validadores reutilizables y localización

Crea funciones o clases validadoras reutilizables:

```python
from django.core.exceptions import ValidationError

def validar_codigo_identificacion(value):
    if len(value) != 10:
        raise ValidationError('La identificación debe tener 10 caracteres')
```

Inclúyelos en `validators=[validar_codigo_identificacion]`.

Para mensajes traducibles: usa `from django.utils.translation import gettext_lazy as _`.

### 2.6 Mostrar errores en el frontend

* En templates, usa `{{ form.non_field_errors }}` y `{{ form.field.errors }}`.
* En API, DRF devuelve un JSON con errores por campo.

---

## 3. Signals en Django

### 3.1 ¿Qué son y cuándo usarlos?

Signals permiten que partes del código "escuchen" eventos. Úsalas para:

* Enviar emails cuando se crea un usuario.
* Actualizar caches o índices de búsqueda.
* Registrar auditoría (logs) cuando se cambian registros.

Evítalas si la lógica hace la aplicación difícil de seguir o si crea acoplamientos inesperados.

### 3.2 Signals integradas principales

* `pre_save` / `post_save`
* `pre_delete` / `post_delete`
* `m2m_changed` (para relaciones many-to-many)
* `pre_migrate` / `post_migrate` / `post_migrate` (útil para tareas después de migraciones)

Ejemplo de uso básico:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # crea un perfil automáticamente
        Perfil.objects.create(user=instance)
```

### 3.3 Signals personalizadas

Puedes definir nuevas señales:

```python
from django.dispatch import Signal

pedido_realizado = Signal(providing_args=['pedido_id', 'usuario'])

# emitir
pedido_realizado.send(sender=Pedido, pedido_id=pedido.id, usuario=pedido.usuario)

# escuchar
@receiver(pedido_realizado)
def handler_pedido(sender, **kwargs):
    # kwargs['pedido_id']
    pass
```

> Nota: `providing_args` está deprecado en versiones recientes de Django; ya no es obligatorio, pero puedes documentar los kwargs esperados.

### 3.4 `@receiver` y `dispatch_uid`

Usa `dispatch_uid` para evitar que un receptor se registre varias veces (útil en tests o cuando `ready()` se ejecuta varias veces):

```python
@receiver(post_save, sender=Model, dispatch_uid='actualizar_cache_modelo')
def actualizar_cache(sender, instance, **kwargs):
    pass
```

### 3.5 Dónde conectar las signals

* Crea un archivo `signals.py` dentro de tu app.
* Importa y conecta en `apps.py` dentro del método `ready()` de la `AppConfig` para registrar señales solo cuando Django arranca la app:

```python
# myapp/apps.py
from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # importa late signals
        from . import signals  # noqa
```

* No conectes signals en `models.py` si eso causa import cycles; `apps.py` es el lugar más seguro.

### 3.6 Pautas para evitar problemas

* Evita efectos secundarios pesados dentro de handlers (bloqueo, llamadas externas) — considera delegar a tareas en background (Celery, Dramatiq).
* Usa `transaction.on_commit()` si la acción debe ejecutarse solo después de que la transacción sea exitosa.
* Añade `dispatch_uid` para evitar conexiones dobles.
* Documenta claramente qué hace cada signal.

---

## 4. Lógica automática: Signals vs Model methods vs Managers vs Services

* **Model methods**: buena opción cuando la lógica es parte del dominio del modelo (p. ej. `order.calculate_total()`).
* **Managers / QuerySets**: para lógica relacionada con consultas (filtros, agregaciones).
* **Signals**: para reacciones a eventos que deben estar desacopladas o cuando múltiples apps/receptores necesitan reaccionar.
* **Services (módulos independientes)**: para lógica compleja, fácilmente testeable y reutilizable.

En general, preferir: `Model methods` / `Managers` / `Services` para lógica de negocio; usar `signals` para side-effects que deben ser reactivos y desacoplados.

---

## 5. Manejo de transacciones y signals

Problema: `post_save` puede dispararse antes de que la transacción que contiene el `save()` sea confirmada (commit). Para acciones que dependen de datos visibles para otros procesos (p. ej. indexar en búsqueda externa), usa `transaction.on_commit`:

```python
from django.db import transaction

@receiver(post_save, sender=Pedido)
def indexar_pedido(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: indexar_en_busqueda(instance.id))
```

---

## 6. Buenas prácticas y rendimiento

* No hagas consultas pesadas en signals; si necesitas, mueve a tareas asíncronas.
* Maneja excepciones dentro del handler: no dejar que un fallo silencie o interrumpa procesos críticos.
* Usa logs para auditar ejecución de handlers.
* Si una acción es crítica (p. ej. crear registros dependientes), considera hacerlo en el mismo flujo de la transacción en vez de usar signal.

---

## 7. Testing de validaciones y signals

* Para validaciones: crea tests que llamen a `full_clean()` y verifiquen `ValidationError`.
* Para forms: prueba `form.is_valid()` y `form.errors`.
* Para signals: puedes usar `django.test.override_settings` o `mock` para interceptar llamadas. Asegúrate de desconectar o usar `dispatch_uid` si ejecutas tests que importen `apps.ready()` varias veces.

**Ejemplo test validación**:

```python
from django.test import TestCase
from django.core.exceptions import ValidationError

class ReservaTest(TestCase):
    def test_fecha_fin_menor_inicio(self):
        r = Reserva(inicio=..., fin=...)
        with self.assertRaises(ValidationError):
            r.full_clean()
```

**Ejemplo test signal**:

```python
from django.test import TestCase
from django.dispatch import receiver
from django.db.models.signals import post_save

class SignalTest(TestCase):
    def test_post_save_dispara(self):
        calls = []

        @receiver(post_save, sender=MiModelo)
        def tmp(sender, **kwargs):
            calls.append(True)

        MiModelo.objects.create(...)
        self.assertTrue(calls)
```

---

## 8. Ejemplos prácticos completos

### 8.1 Validador personalizado (identificación)

```python
# myapp/validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validar_identificacion(value):
    if not value.isdigit() or len(value) not in (8, 10):
        raise ValidationError(_('Identificación inválida'))

# myapp/models.py
from django.db import models
from .validators import validar_identificacion

class Cliente(models.Model):
    nombre = models.CharField(max_length=120)
    identificacion = models.CharField(max_length=20, validators=[validar_identificacion])
```

### 8.2 Signal: crear perfil al crear usuario

```python
# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Perfil

User = get_user_model()

@receiver(post_save, sender=User, dispatch_uid='crear_perfil_usuario')
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
```

Y en `apps.py`:

```python
class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        from . import signals  # noqa
```

### 8.3 Usar `transaction.on_commit` para tareas que dependen del commit

```python
from django.db import transaction

@receiver(post_save, sender=Pedido)
def enviar_confirmacion(sender, instance, created, **kwargs):
    if created:
        transaction.on_commit(lambda: enviar_email_confirmacion(instance.id))
```

### 8.4 Signal m2m_changed ejemplo

```python
from django.db.models.signals import m2m_changed

@receiver(m2m_changed, sender=Articulo.tags.through)
def tags_cambiaron(sender, instance, action, pk_set, **kwargs):
    if action in ('post_add', 'post_remove', 'post_clear'):
        # actualizar contador, cache, etc.
        instance.actualizar_contadores()
```

````

---

## 9. Checklist para producción

- [ ] Documentar claramente cada signal y su propósito.
- [ ] Evitar trabajo pesado dentro de handlers; usar tareas asíncronas.
- [ ] Usar `transaction.on_commit` para acciones dependientes del commit.
- [ ] Añadir `dispatch_uid` cuando sea necesario.
- [ ] Revisar y probar efectos colaterales en staging.
- [ ] Añadir logging y métricas (instrumentar handlers importantes).

---

## 10. Referencias rápidas: snippets útiles

- Validar y guardar en `save()`:

```python
def save(self, *args, **kwargs):
    self.full_clean()
    super().save(*args, **kwargs)
````

* Signal con `dispatch_uid`:

```python
@receiver(post_save, sender=MiModelo, dispatch_uid='mi_modelo_post_save')
def mi_handler(sender, instance, **kwargs):
    pass
```

* Crear signal personalizada y dispararla:

```python
from django.dispatch import Signal
mi_evento = Signal()
mi_evento.send(sender=MiModelo, info='algo')
```

---

## ¿Qué debería agregar en tu repositorio?

* `myapp/validators.py` — validadores reutilizables.
* `myapp/signals.py` — handlers.
* `myapp/tests/test_validators.py` — tests de validación.
* `myapp/tests/test_signals.py` — tests de signals.
* `myapp/apps.py` — import de signals en `ready()`.
* `docs/` — documentación breve en markdown con ejemplos y decisiones de diseño.

---

## Conclusión

Esta guía te da una base sólida para implementar validaciones y lógica automática con signals en Django. Si quieres, puedo:

* Generar los archivos de ejemplo (`validators.py`, `signals.py`, `apps.py`, tests) listos para copiar y pegar.
* Ajustar la guía a la versión exacta de Django que usas.
* Crear tests unitarios completos y un ejemplo real en un proyecto minimal.

Dime cuál de estas opciones prefieres y lo genero inmediatamente.

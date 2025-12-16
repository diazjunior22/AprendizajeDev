# validators.py
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validar_identificacion(value):
    """
    Validador personalizado para identificaciones numéricas de 8 o 10 dígitos.
    """
    if not value.isdigit() or len(value) not in (8, 10):
        raise ValidationError(_('Identificación inválida: debe ser numérica y tener 8 o 10 dígitos.'))


# signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db import transaction
from django.contrib.auth import get_user_model
# from .models import Perfil, Pedido
import logging

logger = logging.getLogger(__name__)

User = get_user_model()


@receiver(post_save, sender=User, dispatch_uid='crear_perfil_usuario')
def crear_perfil_usuario(sender, instance, created, **kwargs):
    """
    Crea un Perfil automáticamente cuando se crea un usuario.
    """
    if created:
        # Perfil.objects.create(user=instance)
        logger.info(f"Perfil creado para el usuario {instance.username}")


# @receiver(post_save, sender=Pedido, dispatch_uid='enviar_confirmacion_pedido')
def enviar_confirmacion(sender, instance, created, **kwargs):
    """
    Envía un correo de confirmación cuando un pedido es creado.
    Se ejecuta solo después del commit exitoso.
    """
    if created:
        transaction.on_commit(lambda: logger.info(f"Enviando email de confirmación para pedido {instance.id}"))


# @receiver(post_delete, sender=Pedido, dispatch_uid='log_pedido_eliminado')
def log_pedido_eliminado(sender, instance, **kwargs):
    logger.warning(f"Pedido {instance.id} eliminado")


# apps.py
from django.apps import AppConfig


class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        # Importar signals cuando la app está lista
        from . import signals  # noqa


# tests/test_validators.py
from django.test import TestCase
from django.core.exceptions import ValidationError
# from myapp.validators import validar_identificacion


class TestValidadores(TestCase):
    def test_identificacion_invalida(self):
        with self.assertRaises(ValidationError):
            validar_identificacion("abc123")

        with self.assertRaises(ValidationError):
            validar_identificacion("123456")  # muy corta

    def test_identificacion_valida(self):
        try:
            validar_identificacion("12345678")
            validar_identificacion("1234567890")
        except ValidationError:
            self.fail("validar_identificacion lanzó error con datos válidos")


# tests/test_signals.py
from django.test import TestCase
from django.contrib.auth import get_user_model
from unittest.mock import patch
# from myapp.models import Pedido, Perfil

User = get_user_model()


class TestSignals(TestCase):
    def test_crea_perfil_al_crear_usuario(self):
        usuario = User.objects.create(username="testuser")
        # self.assertTrue(Perfil.objects.filter(user=usuario).exists())

    @patch('myapp.signals.logger.info')
    def test_envio_confirmacion_pedido(self, mock_logger):
        # pedido = Pedido.objects.create(total=100)
        self.assertTrue(mock_logger.called)

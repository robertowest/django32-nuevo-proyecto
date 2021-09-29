from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core.usuarios'
    label = 'usuarios'
    verbose_name = _('Usuarios')

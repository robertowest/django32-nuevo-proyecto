from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DiccionarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.diccionario'
    label = 'diccionario'
    verbose_name = _('Diccionario')

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PersonasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.personas'
    # label = 'personas'
    # verbose_name = _('Personas')

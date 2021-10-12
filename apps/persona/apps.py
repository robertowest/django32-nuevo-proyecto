from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PersonaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.persona'
    label = 'persona'
    verbose_name = _('Persona')

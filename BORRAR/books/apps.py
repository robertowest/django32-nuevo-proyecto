from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'
    label = 'books'
    verbose_name = _('Books')

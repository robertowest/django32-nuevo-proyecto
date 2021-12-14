import django_tables2 as tables

from django.utils.translation import gettext_lazy as _

from core.comunes.utils import acciones_en_tabla

from .models import Contacto


class ContactoTable(tables.Table):
    ACTIONS = acciones_en_tabla('contactos')

    # id = tables.Column(orderable=False)     # (linkify=True)
    persona = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name=_('Acciones'), orderable=False)

    class Meta:
        model = Contacto
        empty_text = _("No hay datos para el criterio de búsqueda.")
        template_name = "django_tables2/bootstrap4.html"    # bootstrap-responsive.html
        per_page = 25
        attrs = {
            "class": "table table-hover table-sm", 
            "thead" : {"class": "thead-light"},
        }
        fields = ['persona', 'active']
        sequence = []

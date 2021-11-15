import django_tables2 as tables

from django.utils.translation import gettext_lazy as _

from core.comunes.utils import acciones_en_tabla

from .models import Telefono


class TelefonoTable(tables.Table):
    ACTIONS = acciones_en_tabla('telefono')

    tipo = tables.Column(orderable=False)
    texto = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)
    
    class Meta:
        model = Telefono
        empty_text = _("No hay datos para el criterio de búsqueda.")
        template_name = "django_tables2/bootstrap4.html"
        per_page = 25
        attrs = {
            "class": "table table-hover table-sm", 
            "thead" : {"class": "thead-light"},
        }
        fields = ['tipo', 'texto', 'active']

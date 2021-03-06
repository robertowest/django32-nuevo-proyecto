import django_tables2 as tables

from django.utils.translation import gettext_lazy as _

from core.comunes.utils import acciones_en_tabla

from .models import Diccionario


class DiccionarioTable(tables.Table):
    ACTIONS = acciones_en_tabla('diccionario')

    # id = tables.Column(orderable=False)     # (linkify=True)
    tabla = tables.Column(orderable=True, order_by=('tabla', 'texto'))
    texto = tables.Column(orderable=False)
    texto_corto = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)
    
    class Meta:
        model = Diccionario
        empty_text = _("No hay datos para el criterio de búsqueda.")
        template_name = "django_tables2/bootstrap4.html"    # bootstrap-responsive.html
        per_page = 25
        attrs = {
            "class": "table table-hover table-sm", 
            "thead" : {"class": "thead-light"},
        }
        fields = ['texto', 'tabla', 'active']
        sequence = ['tabla', 'texto', 'texto_corto', 'active']

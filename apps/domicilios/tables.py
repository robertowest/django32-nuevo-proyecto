import django_tables2 as tables
from django.utils.translation import gettext_lazy as _
from core.comunes.utils import acciones_en_tabla
from .models import Domicilio


class DomicilioTable(tables.Table):
    ACTIONS = acciones_en_tabla('domicilio')

    tipo_domicilio = tables.Column(orderable=False)
    tipo_calle = tables.Column(orderable=False)
    domicilio_corto = tables.Column(verbose_name='Domicilio', orderable=False)
    # domicilio_corto = tables.Column(verbose_name='Domicilio', orderable=False, linkify=True)
    # domicilio_corto = tables.Column(verbose_name='Domicilio', orderable=False, 
    #     linkify=("domicilios:update", {"pk": tables.A("pk")}) )  # ?next={{request.get_full_path|urlencode}}
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)
    
    class Meta:
        model = Domicilio
        empty_text = _("No hay datos para el criterio de búsqueda.")
        template_name = "django_tables2/bootstrap4.html"    # bootstrap-responsive.html
        per_page = 25
        attrs = {
            "class": "table table-hover table-sm", 
            "thead" : {"class": "thead-light"},
        }
        fields = ['tipo_domicilio', 'tipo_calle', 'domicilio_corto', 'active']

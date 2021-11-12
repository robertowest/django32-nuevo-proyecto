import django_tables2 as tables

from django.utils.translation import gettext_lazy as _

from core.comunes.utils import acciones_en_tabla

from .models import Persona


class PersonaTable(tables.Table):
    ACTIONS = acciones_en_tabla('diccionario')

    # id = tables.Column(orderable=False)     # (linkify=True)
    apellido_nombre = tables.Column(verbose_name=_('Nombre'), order_by=('nombre'))
    documento = tables.Column(orderable=False)
    fecha_nacimiento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name=_('Acciones'), orderable=False)

    class Meta:
        model = Persona
        empty_text = _("No hay datos para el criterio de búsqueda.")
        template_name = "django_tables2/bootstrap4.html"    # bootstrap-responsive.html
        per_page = 25
        attrs = {
            "class": "table table-hover table-sm", 
            "thead" : {"class": "thead-light"},
        }
        fields = ['apellido_nombre', 'documento', 'fecha_nacimiento', 'edad', 'active']
        sequence = []


    def render_documento(self, value):
        return '{:0,.0f}'.format(int(value)).replace(',', '.')

    def render_fecha_nacimiento(self, value):
        return value.strftime('%d/%m/%Y')

    def render_genero(self, value, column):
        if value == 'Femenino':
            column.attrs = {'td': {'bgcolor': 'red'}}
        elif value == 'Masculino':
            column.attrs = {'td': {'bgcolor': 'lightgreen'}}        
        return value[:1]

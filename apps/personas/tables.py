import django_tables2 as tables

from django.db.models import Q
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from .models import Persona


class PersonaTable(tables.Table):
    # view sin ventana modal
    # <a href="{{record.get_read_url}}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    # view con ventana modal
    # <a href="{{record.get_read_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    ACTIONS = '''
    {% if perms.persona.view_persona %}
    <a href="{{record.get_read_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.persona.change_persona %} 
    <a href="{{record.get_update_url}}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.persona.delete_persona %} 
    <a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" title="Eliminar" data-toggle="modal" data-target="#confirmDeleteModal" data-object="{{record}}" id="deleteButton{{record.id}}"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''

    # id = tables.Column(orderable=False)     # (linkify=True)
    apellido_nombre = tables.Column(verbose_name=_('Nombre'), order_by=('nombre'))
    tipo_documento = tables.Column(orderable=False)
    documento = tables.Column(orderable=False)
    fecha_nacimiento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name=_('Acciones'), orderable=False)

    class Meta:
        model = Persona
        template_name = "django_tables2/bootstrap-responsive.html"
        attrs = {
            "class": "table table-hover table-sm", 
            "thead" : {"class": "thead-light"},
        }
        fields = ['apellido_nombre', 'tipo_documento', 'documento', 
                  'fecha_nacimiento', 'edad', 'active']
        sequence = []

    def render_tipo_documento(self, value):
        return value.codigo

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

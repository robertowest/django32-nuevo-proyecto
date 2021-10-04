import django_tables2 as tables

from django.db.models import Q
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from .models import Persona


class PersonaTable(tables.Table):
    # view: con ventana modal
    # <a href="{{record.get_detail_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    # delete: sin confirmación
    # <a href="{{record.get_detail_url}}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    ACTIONS = '''
    {% if perms.personas.view_personas %}
    <a href="{{record.get_detail_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.personas.change_personas %} 
    <a href="{{record.get_update_url}}?next={{request.get_full_path|urlencode}}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.personas.delete_personas %} 
    <a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" title="Eliminar" data-toggle="modal" data-target="#confirmDeleteModal" data-object="{{record}}" id="deleteButton{{record.id}}"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    
    id = tables.Column(orderable=False)     # (linkify=True)
    apellido_nombre = tables.Column(verbose_name='Nombre', order_by=('nombre'))
    tipo_documento = tables.Column(orderable=False)
    documento = tables.Column(orderable=False)
    fecha_nacimiento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    # genero = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)

    class Meta:
        model = Persona
        template_name = "django_tables2/bootstrap4.html"
        fields = ['id', 'apellido_nombre', 'tipo_documento', 'documento', 
                  'fecha_nacimiento', 'edad', 'active']
        attrs = {"class": "table table-hover"}

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


class PersonaTableModal(tables.Table):
    nombre_apellido = tables.LinkColumn('personas:detail', args=[A('pk')], 
                                        verbose_name='Nombre', orderable=False, 
                                        order_by=('nombre_apellido'))
    documento = tables.Column(orderable=False)
    edad = tables.Column(orderable=False)
    active = tables.BooleanColumn(orderable=False)

    class Meta:
        model = Persona
        fields = ['nombre_apellido', 'documento', 'edad', 'active']
        attrs = {"class": "table table-hover"}  # table-striped 
        empty_text = _("No hay datos para los criterios de búsqueda.")
        template_name = "django_tables2/bootstrap4.html"
        per_page = 20

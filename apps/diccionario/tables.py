import django_tables2 as tables

from .models import Diccionario


class DiccionarioTable(tables.Table):
    ACTIONS = '''
    {% if perms.diccionario.view_diccionario %}
    <a href="{{record.get_read_url}}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.diccionario.change_diccionario %} 
    <a href="{{record.get_update_url}}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.diccionario.delete_diccionario %} 
    <a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" title="Eliminar" data-toggle="modal" data-target="#confirmDeleteModal" data-object="{{record}}" id="deleteButton{{record.id}}"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''
    # sin ventana modal
    # <a href="{{record.get_read_url}}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    # sin confirmación
    # <a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" data-toggle="tooltip" data-original-title="Eliminar"><i class="fa fa-trash">&nbsp;</i></a>

    # id = tables.Column(orderable=False)     # (linkify=True)
    texto = tables.Column(order_by=('texto'), orderable=True)
    tabla = tables.Column(orderable=True)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)
    
    class Meta:
        model = Diccionario
        template_name = "django_tables2/bootstrap4.html"
        fields = ['texto', 'tabla', 'active']
        sequence = ['tabla', 'texto', 'active']
        attrs = {"class": "table table-hover"}

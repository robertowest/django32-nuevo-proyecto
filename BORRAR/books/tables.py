import django_tables2 as tables

from django.db.models import Q
from django_tables2.utils import A
from django.utils.translation import gettext_lazy as _

from .models import Book


class BookTable(tables.Table):
    # view: con ventana modal
    # <a href="{{record.get_detail_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    # delete: sin confirmación
    # <a href="{{record.get_detail_url}}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>
    ACTIONS = '''
    {% if perms.books.view_book %}
    <a href="{{record.get_read_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    {% endif %}

    {% if perms.books.change_book %} 
    <a href="{{record.get_update_url}}?next={{request.get_full_path|urlencode}}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>
    {% endif %}

    {% if perms.books.delete_book %} 
    <a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" title="Eliminar" data-toggle="modal" data-target="#confirmDeleteModal" data-object="{{record}}" id="deleteButton{{record.id}}"><i class="fa fa-trash">&nbsp;</i></a>
    {% endif %}
    '''

    id = tables.Column(orderable=False)     # (linkify=True)
    title = tables.Column(verbose_name='Título', order_by=('title'))
    author = tables.Column(verbose_name='Autor', orderable=False)
    active = tables.BooleanColumn(orderable=False)
    actions = tables.TemplateColumn(template_code=ACTIONS, verbose_name='Acciones', orderable=False)

    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap4.html"
        fields = ['id', 'title', 'author', 'active']
        attrs = {"class": "table table-hover"}

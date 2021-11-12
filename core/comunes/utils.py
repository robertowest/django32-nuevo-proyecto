import os

from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

from django_tables2 import SingleTableView

# How to use
# obj = [User].objects.create()
# get_app_name(obj)
# get_model_name(obj)

# __package__.split('.')[1]
# self._meta.verbose_name.lower()

def dictfetchall(cursor):
    "Devuelve todas las filas de un cursor como un diccionario"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def get_app_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.app_label


def get_model_name(model):
    obj_content_type = ContentType.objects.get_for_model(model)
    return obj_content_type.model


def get_template_path(appname, template):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = "{path}/{app}/templates/{app}/{html}".format(path=path, app=appname, html=template)
    if os.path.exists(file):
        template_name = "{app}/{html}".format(app=appname, html=template)
    else:
        template_name = "comunes/{html}".format(html=template)
    return template_name


def where_are_we_going(self, response):
    # terminamos, ¿hacia dónde vamos?
    if self.request.GET.get('next'):
        return HttpResponseRedirect(self.request.GET.get('next'))
    elif 'previous_url' in self.request._post:
        return HttpResponseRedirect(self.request._post['previous_url'])
    elif self.success_url:
        return HttpResponseRedirect(self.success_url)
    else:
        return response


class FilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = "filter"

    def get_table_data(self):
        self.filter = self.filter_class(
            self.request.GET, queryset=super().get_table_data()
        )
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(FilteredTableView, self).get_context_data(**kwargs)
        context[self.context_filter_name] = self.filter
        return context


def acciones_en_tabla(nombre_modelo):
    # view con ventana modal
    # <a href="{{record.get_read_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>
    # view sin ventana modal
    # <a href="{{record.get_read_url}}" class="text-info" data-toggle="tooltip" data-original-title="Ver"><i class="fa fa-eye">&nbsp;</i></a>

    btnView = '{% if perms.{0}.view_{0} %}' + \
              '<a href="{{record.get_read_url}}" class="text-info" title="Ver" data-toggle="modal" data-target="#viewModal" id="viewButton{{record.id}}"><i class="fa fa-eye">&nbsp;</i></a>' + \
              '{% endif %} '
    btnEdit = '{% if perms.{0}.change_{0} %}' + \
              '<a href="{{record.get_update_url}}?next={{request.get_full_path|urlencode}}" class="text-primary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>' + \
              '{% endif %} '
    btnDele = '{% if perms.{0}.delete_{0} %}' + \
              '<a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-danger" title="Eliminar" data-toggle="modal" data-target="#confirmDeleteModal" data-object="{{record}}" id="deleteButton{{record.id}}"><i class="fa fa-trash">&nbsp;</i></a>' + \
              '{% endif %} '

    btnView = ''
    btnEdit = '{% if perms.{0}.change_{0} %}' + \
              '<a href="{{record.get_update_url}}?next={{request.get_full_path|urlencode}}" class="text-secondary" data-toggle="tooltip" data-original-title="Editar"><i class="fa fa-edit">&nbsp;</i></a>' + \
              '{% endif %} '
    btnDele = '{% if perms.{0}.delete_{0} %}' + \
              '<a href="{{record.get_delete_url}}?next={{request.get_full_path|urlencode}}" class="text-secondary" title="Eliminar" data-toggle="modal" data-target="#confirmDeleteModal" data-object="{{record}}" id="deleteButton{{record.id}}"><i class="fa fa-trash-alt">&nbsp;</i></a>' + \
              '{% endif %} '
    return (btnView + btnEdit + btnDele).replace("{0}", nombre_modelo)

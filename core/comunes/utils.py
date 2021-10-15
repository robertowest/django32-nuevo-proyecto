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

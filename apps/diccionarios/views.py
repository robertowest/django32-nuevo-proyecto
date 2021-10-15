from django.urls import reverse
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  CreateView, 
                                  DetailView as ReadView, 
                                  UpdateView, 
                                  DeleteView)

from django_tables2 import SingleTableView

from core.comunes.utils import FilteredTableView

from .models import Diccionario
from .tables import DiccionarioTable
from .filters import DiccionarioFilter, DiccionarioFilterForm


PERMISSION = '{label}.view_{model}'.format(label='diccionarios', model='diccionario')


class MyTemplateView(TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return MyListView.as_view()(request)
    # reverse('diccionarios:list')
    # def get(self, request, *args, **kwargs):
    #     from django.http import HttpResponseRedirect
    #     return HttpResponseRedirect('/diccionarios/listado/')


class MyListView(SingleTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = PERMISSION
    model = Diccionario
    table_class = DiccionarioTable              # SingleTableView
    template_name = 'diccionarios/tabla.html'

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class MyFilterView(MyListView, FilteredTableView):
    """FilterView se utiliza para la presentación de una tabla con filtro"""
    filter_class = DiccionarioFilter            # FilteredTableView (filterset_class)
    formhelper_class = DiccionarioFilterForm    # FilteredTableView
    template_name = 'diccionarios/tabla_filtro.html'


class MyCreateView(CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    pass


class MyReadView(ReadView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    pass


class MyUpdateView(UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    pass


class MyDeleteView(DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    pass

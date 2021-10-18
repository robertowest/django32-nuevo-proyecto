from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (TemplateView, 
                                  ListView, 
                                  CreateView, 
                                  DetailView as ReadView, 
                                  UpdateView, 
                                  DeleteView)

from django_tables2 import SingleTableView

from core.audit.models import AuditableMixin
from core.comunes.utils import FilteredTableView, where_are_we_going

from .models import Diccionario
from .tables import DiccionarioTable
from .filters import DiccionarioFilter, DiccionarioFilterForm
from .forms import DiccionarioForm


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


class MyListView(PermissionRequiredMixin, SingleTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = PERMISSION
    model = Diccionario
    table_class = DiccionarioTable              # SingleTableView
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class MyFilterView(MyListView, FilteredTableView):
    """FilterView se utiliza para la presentación de una tabla con filtro"""
    filter_class = DiccionarioFilter            # FilteredTableView (filterset_class)
    formhelper_class = DiccionarioFilterForm    # FilteredTableView
    template_name = 'comunes/tabla_filtro.html'


class MyCreateView(AuditableMixin, PermissionRequiredMixin, CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    permission_required = PERMISSION.replace("view_", "add_")
    model = Diccionario
    form_class = DiccionarioForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = "col-4"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class MyReadView(PermissionRequiredMixin, ReadView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    permission_required = PERMISSION
    model = Diccionario
    # template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())
    template_name = 'comunes/detalle_modal.html'


class MyUpdateView(AuditableMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    permission_required = PERMISSION.replace("view_", "change_")
    model = Diccionario
    form_class = DiccionarioForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = "col-4"
        return context

    def get_success_message(self, cleaned_data):
        # return super().get_success_message(cleaned_data)
        return self.success_message

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class MyDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    permission_required = PERMISSION.replace('view_', 'del_')
    model = Diccionario
    # success_delete_message
    success_message = _('Registro eliminado correctamente')

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_message(self, cleaned_data):
        # return super().get_success_message(cleaned_data)
        return self.success_message

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('{}:list'.format(self.model._meta.verbose_name.lower()))

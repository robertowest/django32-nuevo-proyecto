from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import (TemplateView, 
                                  CreateView, 
                                  DetailView as ReadView, 
                                  UpdateView, 
                                  DeleteView)

from django_tables2 import SingleTableView

from core.audit.models import AuditableMixin
from core.comunes.utils import FilteredTableView, where_are_we_going

from .models import Domicilio
from .tables import DomicilioTable
from .filters import DomicilioFilter, DomicilioFilterForm
from .forms import DomicilioForm


PERMISSION = '{label}.view_{model}'.format(label='domicilios', model='domicilio')


class MyTemplateView(TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        url = '{}:list'.format(__package__.split('.')[1])
        return HttpResponseRedirect(reverse_lazy(url))


class MyListView(PermissionRequiredMixin, SingleTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = PERMISSION
    model = Domicilio
    table_class = DomicilioTable              # SingleTableView
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class MyFilterView(MyListView, FilteredTableView):
    """FilterView se utiliza para la presentación de una tabla con filtro"""
    filter_class = DomicilioFilter            # FilteredTableView (filterset_class)
    formhelper_class = DomicilioFilterForm    # FilteredTableView
    template_name = 'comunes/tabla.html'


class MyCreateView(AuditableMixin, PermissionRequiredMixin, CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    permission_required = PERMISSION.replace("view_", "add_")
    model = Domicilio
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = "col-8"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class MyReadView(PermissionRequiredMixin, ReadView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    permission_required = PERMISSION
    model = Domicilio
    # template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())
    template_name = 'comunes/detalle_modal.html'


class MyUpdateView(AuditableMixin, PermissionRequiredMixin, UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    permission_required = PERMISSION.replace("view_", "change_")
    model = Domicilio
    form_class = DomicilioForm
    template_name = 'comunes/formulario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['columns'] = "col-8"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class MyDeleteView(PermissionRequiredMixin, DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    permission_required = PERMISSION.replace('view_', 'del_')
    model = Domicilio

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        return reverse_lazy('{}:list'.format(self.model._meta.verbose_name.lower()))

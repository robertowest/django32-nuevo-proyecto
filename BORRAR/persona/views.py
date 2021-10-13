from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from core.audit.models import AuditableMixin
from core.comunes.utils import PagedFilteredTableView, where_are_we_going

from .models import Persona
from .tables import PersonaTable
from .filters import PersonaFilter, PersonaFilterForm
from .forms import PersonaForm

# from apps.domicilio.models import Domicilio
PERMISSION = '{domain}.view_{app}'.format(domain='persona', app='persona')


class PersonaTemplateView(generic.TemplateView):
    """
    TemplateView se utiliza para la página de presentación del módulo.
    Si no existe página de presentación, se llamará a la función ListView
    """
    def get(self, request, *args, **kwargs):
        return PersonaListView.as_view()(request)


class PersonaListView(PermissionRequiredMixin, PagedFilteredTableView):
    """ListView se utiliza para la presentación de una tabla de contenido"""
    permission_required = PERMISSION
    model = Persona
    table_class = PersonaTable              # SingleTableView
    filter_class = PersonaFilter            # PagedFilteredTableView
    formhelper_class = PersonaFilterForm    # PagedFilteredTableView
    template_name = 'comunes/tabla.html'

    def get_context_data(self, **kwargs):
        context = super(PersonaListView, self).get_context_data(**kwargs)
        context['add_permission'] = self.request.user.has_perm(self.permission_required.replace("view_", "add_"))
        return context


class PersonaCreateView(AuditableMixin, PermissionRequiredMixin, generic.CreateView):
    """CreateView formulario para la creación de un registro en la tabla"""
    model = Persona
    permission_required = PERMISSION.replace('view_', 'add_')
    form_class = PersonaForm
    template_name = 'comunes/formulario.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class PersonaReadView(PermissionRequiredMixin, generic.DetailView):
    """DetailView se utiliza para la presentación de un registro de la tabla"""
    permission_required = PERMISSION
    model = Persona
    # template_name = '{app}/detalle.html'.format(app=model._meta.verbose_name.lower())
    template_name = 'comunes/detalle_modal.html'


class PersonaUpdateView(AuditableMixin, PermissionRequiredMixin, generic.UpdateView):
    """UpdateView formulario para la modificación de un registro en la tabla"""
    model = Persona
    permission_required = PERMISSION.replace('view_', 'change_')
    form_class = PersonaForm
    template_name = 'comunes/formulario.html'

    # def has_permission(self, request):
    #     return request.user.is_active and request.user.is_staff
    def form_valid(self, form):
        response = super().form_valid(form)
        return where_are_we_going(self, response)


class PersonaDeleteView(PermissionRequiredMixin, generic.DeleteView):
    """DeleteView confirmación de eliminación de un registro en la tabla"""
    model = Persona
    permission_required = PERMISSION.replace('view_', 'del_')
    success_message = "Registro eliminado correctamente"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        redirect = self.request.GET.get('next')
        if redirect:
            return redirect
        #reverse_lazy('persona:read', args=(self.object.pk,))
        return reverse_lazy('persona:list')





from .tables import PersonaTableModal
from .filters import PersonaFilterModal, PersonaFilterFormModal

class DomicilioModal(PagedFilteredTableView):
    model = Persona
    table_class = PersonaTableModal
    filter_class = PersonaFilterModal
    formhelper_class = PersonaFilterFormModal
    template_name = 'persona/includes/detail_domicilio_modal3.html'


def DomicilioFiltroModal(request):
    # relacion = models.EmpresaActividadDomicilios.objects.get(id=eadId)
    # relacion.empresa_actividad_id = eaId
    # relacion.save()
    # url = reverse('empresa_actividad:read', args=(), kwargs={'pk': eaId})
    # return HttpResponseRedirect(url)
    html = "<h1>Después de pulsar el filtro</h1>"
    return HttpResponse(html)

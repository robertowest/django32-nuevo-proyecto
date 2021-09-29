from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Persona
from .forms import PersonaForm


class PersonaList(ListView): 
    model = Persona


class PersonaDetail(DetailView): 
    model = Persona


class PersonaCreate(SuccessMessageMixin, CreateView): 
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('persona:list')
    success_message = "Persona creada con éxito!"


class PersonaUpdate(SuccessMessageMixin, UpdateView): 
    model = Persona
    form_class = PersonaForm
    success_url = reverse_lazy('persona:list')
    success_message = "Persona modificada con éxito!"


class PersonaDelete(SuccessMessageMixin, DeleteView):
    model = Persona
    success_url = reverse_lazy('persona:list')
    success_message = "Persona eliminada con éxito!"

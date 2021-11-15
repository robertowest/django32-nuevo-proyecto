# departamentos / localidades
# https://www.colesctuc.com/index.php/es/publicaciones-de-interes/8-informativo/85-departamentos-y-municipios-de-tucuman

from django.contrib import admin

from .models import Telefono


@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ['id', 'texto', 'active']
    list_display_links = ['texto']
    list_filter = ['tipo']
    search_fields = ['texto']
    ordering = ['texto']

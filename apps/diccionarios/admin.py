from django.contrib import admin

from .models import Diccionario


@admin.register(Diccionario)
class DiccionarioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Diccionario._meta.get_fields()]
    # list_display = ['id', 'texto', 'codigo']
    list_display_links = ['texto']
    list_filter = ['tabla']
    search_fields = ['texto']
    ordering = ['texto']

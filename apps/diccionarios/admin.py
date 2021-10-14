from django.contrib import admin

from .models import Diccionario


@admin.register(Diccionario)
class DiccionariosAdmin(admin.ModelAdmin):
    # list_display = ['id', 'texto', 'texto_corto']
    # include_fields = [f.name for f in Diccionario._meta.get_fields()]
    # list_display = [f for f in include_fields if f not in Diccionario.exclude_fields]

    list_display = [f.name for f in Diccionario._meta.get_fields() 
                    if f.name not in Diccionario.exclude_fields]
    list_display_links = ['texto']
    list_filter = ['tabla']
    search_fields = ['texto']
    ordering = ['texto']

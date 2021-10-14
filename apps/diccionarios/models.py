from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.audit.models import Auditable


class Diccionario(Auditable):
    TABLA = (
        ('comunicacion', _('Comunicaciones')),
        ('tipo_domicilio', _('Tipo de Domicilio')),
        ('tipo_calle', _('Tipo de Calle')),
        ('tipo_documento', _('Tipo de Documento')),
    )

    tabla = models.CharField(max_length=25, choices=TABLA, default='comunicacion')
    texto = models.CharField(max_length=150)
    texto_corto = models.CharField(max_length=5, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'diccionario'
        unique_together = ('tabla', 'texto',)
        verbose_name = _('Diccionario')
        verbose_name_plural = _('Diccionarios')

    def __str__(self):
        return self.texto

    @property
    def descripcion(self):
        return "{0} ({1})".format(self.texto, self.get_tabla_display())

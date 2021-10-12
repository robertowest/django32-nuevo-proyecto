from datetime import date

from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.audit.models import Auditable
from apps.diccionario.models import Diccionario


class Persona(Auditable):
    # tipo_documento
    GENERO = (('F', 'Femenino'), ('M', 'Masculino'))

    nombre = models.CharField(max_length=40, db_index=True)
    apellido = models.CharField(max_length=40, db_index=True)
    tipo_documento = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                                       null=True, blank=True, default=12, 
                                       verbose_name=_('Tipo Doc'),
                                       limit_choices_to={'tabla': 'tipo_documento', 'active': True})
    documento = models.CharField('Número', max_length=12, null=True, blank=True, unique=True)
    fecha_nacimiento = models.DateField(_('Fec. Nac.'), blank=True, null=True)
    genero = models.CharField(_('Sexo'), max_length=1, choices=GENERO, default='F')

    class Meta:
        db_table = 'personas'
        verbose_name = _('Persona')
        verbose_name_plural = _('Personas')

    def __str__(self):
        return self.apellido_nombre

    @property
    def edad(self):
        if self.fecha_nacimiento is None:
            return 0            
        else:
            age = date.today().year - self.fecha_nacimiento.year - ((date.today().month, date.today().day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)) 
            return age

    @property
    def nombre_apellido(self):
        return '{0} {1}'.format(self.nombre, self.apellido)

    @property
    def apellido_nombre(self):
        return '{0}, {1}'.format(self.apellido, self.nombre)

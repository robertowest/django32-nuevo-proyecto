from datetime import date 

from django.db import models

from core.audit.models import Auditable


class Persona(Auditable):
    DOCUMENTO = (('DNI', 'D.N.I.'), ('PASS', 'Pasaporte'))
    GENERO = (('M', 'Masculino'), ('F', 'Femenino'))

    nombre = models.CharField(max_length=40, db_index=True)
    apellido = models.CharField(max_length=40, db_index=True)
    tipo_documento = models.CharField('Tipo Doc.', max_length=4, choices=DOCUMENTO, default='DNI')
    documento = models.CharField('Número', max_length=12, null=True, blank=True, unique=True)
    fecha_nacimiento = models.DateField('Fec. Nac.', blank=True, null=True)
    genero = models.CharField('Sexo', max_length=1, choices=GENERO, default='M')
    # campos de auditoría
    f_creacion = models.DateTimeField(auto_now_add=True)
    f_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

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

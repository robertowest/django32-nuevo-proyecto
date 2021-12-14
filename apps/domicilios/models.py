from django.db import models
from django.utils.translation import ugettext_lazy as _

from core.audit.models import Auditable
from apps.diccionarios.models import Diccionario

class Pais(Auditable):
    nombre = models.CharField(max_length=40)
    cod_area_tel = models.CharField(_('Cód. Area Telef.'), max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'paises'
        verbose_name = _('País')
        verbose_name_plural = _('Paises')

    def __str__(self):
        return self.nombre


class Provincia(Auditable):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=60)

    class Meta:
        db_table = 'provincias'
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'

    def __str__(self):
        return self.nombre


class Departamento(Auditable):
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=60)

    class Meta:
        db_table = 'departamentos'
        verbose_name = _('Departamento')
        verbose_name_plural = _('Departamentos')

    def __str__(self):
        return self.nombre


class Localidad(Auditable):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name='Dpto.', default=2)
    nombre = models.CharField(max_length=150)
    cod_postal = models.CharField(_('Cód. Postal'), max_length=12, null=True, blank=True)
    cod_area_tel = models.CharField(_('Cód. Area Telef.'), max_length=4, null=True, blank=True)

    class Meta:
        db_table = 'localidades'
        verbose_name = _('Localidad')
        verbose_name_plural = _('Localidades')

    def __str__(self):
        return self.nombre


class Domicilio(Auditable):
    tipo_domicilio = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                                       null=True, blank=True, default=5, related_name='tipo_domicilio',
                                       limit_choices_to={'tabla': 'tipo_domicilio', 'active': True})
    tipo_calle = models.ForeignKey(Diccionario, on_delete=models.CASCADE,
                                   null=True, blank=True, default=9, related_name='tipo_calle',
                                   limit_choices_to={'tabla': 'tipo_calle', 'active': True})
    nombre = models.CharField(max_length=80, null=True, blank=True)
    numero = models.IntegerField('Número', null=True, blank=True)
    piso = models.CharField(max_length=2, null=True, blank=True)
    puerta = models.CharField(max_length=2, null=True, blank=True)
    barrio = models.CharField(max_length=40, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE,
                                  null=True, blank=True, 
                                  limit_choices_to={'active': True}, default=1)
    departamento = models.ForeignKey(Departamento, related_name="departamentos", 
                                     on_delete=models.CASCADE, null=True, blank=True, 
                                     verbose_name='Dpto.')
    localidad = models.ForeignKey(Localidad, related_name="localidades", 
                                  on_delete=models.CASCADE, null=True, blank=True)
    observacion = models.TextField('Nota', null=True, blank=True)

    class Meta:
        db_table = 'domicilios'
        verbose_name = _('Domicilio')
        verbose_name_plural = _('Domicilios')

    def __str__(self):
        return self.domicilio_largo

    @property
    def domicilio_corto(self):
        texto = self.nombre
        if self.numero:
            texto += " " + str(self.numero)
        return texto

    @property
    def domicilio_largo(self):
        texto = "%s %s" % (self.tipo_calle.texto, self.nombre)
        if self.numero:
            texto += " " + str(self.numero)
        if self.piso:
            texto += " - %s piso, puerta %s" % (self.piso, self.puerta)
        return texto

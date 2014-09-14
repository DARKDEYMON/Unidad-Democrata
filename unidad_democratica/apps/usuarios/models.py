from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here

a=(('C33','C33'),('C34','C34'),('C35','C35'),('C36','C36'),('C37','C37'),('C38','C38'),('C39','C39'))
b=(('Urbano','Urbano'),('Rural','Rural'))
class control_electoral(models.Model):
	nombre = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=100)
	apellido_materno = models.CharField(max_length=100)
	fecha = models.DateField(auto_now=True)
	ci = models.IntegerField()
	telefono = models.IntegerField(null=False)#ver si funsiona
	sircunscripcion = models.CharField(max_length=100, choices=a)
	municipio = models.CharField(max_length=100)
	recinto = models.CharField(max_length=100)
	mesa = models.CharField(max_length=100)
	class Meta:
		verbose_name = _('Control Electoral')
		verbose_name_plural = _('Control Electoral')
class nivel_2(models.Model):
	nombre = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=100)
	apellido_materno = models.CharField(max_length=100)
	fecha = models.DateField(auto_now=True)
	ci = models.IntegerField()
	sircunscripcion = models.CharField(max_length=100, choices=a)
	telefono = models.IntegerField()
	class Meta:
		verbose_name = _('Nivel 2')
		verbose_name_plural = _('Nivel 2')
class nivel_3(models.Model):
	nombre = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=100)
	apellido_materno = models.CharField(max_length=100)
	fecha = models.DateField(auto_now=True)
	ci = models.IntegerField()
	sircunscripcion = models.CharField(max_length=100, choices=a)
	telefono = models.IntegerField()
	lugar = models.CharField(max_length=100, choices=b)
	municio_recinto = models.CharField(max_length=100)
	class Meta:
		verbose_name = _('Nivel 3')
		verbose_name_plural = _('Nivel 3')
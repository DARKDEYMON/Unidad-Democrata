from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here

class control_electoral(models.Model):
	nombre = models.CharField(max_length=100)
	apellido_paterno = models.CharField(max_length=100)
	apellido_materno = models.CharField(max_length=100)
	fecha = models.DateField(auto_now=True)
	ci = models.IntegerField()
	sircunscripcion = models.CharField(max_length=100)
	municipio = models.CharField(max_length=100)
	recinto = models.CharField(max_length=100)
	mesa = models.CharField(max_length=100)
	class Meta:
		verbose_name = _('Control Electoral')
		verbose_name_plural = _('Control Electoral')
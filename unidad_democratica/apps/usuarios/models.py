from django.db import models

# Create your models here.
class control_electoral(models.Model):
	nombre=models.CharField(max_length=100)
	apellido_paterno=models.CharField(max_length=100)
	apellido_materno=models.CharField(max_length=100)
	fecha=models.DateField(auto_now=True)
	ci=models.IntegerField()
	sircunscripcion=models.CharField(max_length=100)
	municipio=models.CharField(max_length=100)
	recinto=models.CharField(max_length=100)
	mesa=models.CharField(max_length=100)
from django.contrib import admin
from models import control_electoral
# Register your models here.
class control_electoral_vista(admin.ModelAdmin):
	
	list_display = ('nombre','apellido_paterno','apellido_materno','ci','sircunscripcion','municipio','recinto','mesa','ci','fecha')
admin.site.register(control_electoral,control_electoral_vista)
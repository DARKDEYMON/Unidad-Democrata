from django.contrib import admin
from models import *

# Register your models here.
class control_electoral_vista(admin.ModelAdmin):
	list_display = ('nombre','apellido_paterno','apellido_materno','ci','sircunscripcion','municipio','recinto','mesa','ci','fecha')
	#list_filter = ('sircunscripcion','nombre')

admin.site.register(control_electoral,control_electoral_vista)
admin.site.register(nivel_2)
admin.site.register(nivel_3)
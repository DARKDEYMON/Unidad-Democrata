from django.contrib import admin
from models import *

# Register your models here.
class control_electoral_vista(admin.ModelAdmin):
	list_display = ('id','nombre','apellido_paterno','apellido_materno','ci','sircunscripcion','municipio','recinto','mesa','ci','fecha')
	#list_filter = ('sircunscripcion','nombre')
	search_fields = ('nombre','apellido_paterno')
class nivel_2_vista(admin.ModelAdmin):
	#list_display = ('id','nombre','apellido_paterno','apellido_materno','ci','sircunscripcion','municipio','recinto','mesa','ci','fecha')
	#list_filter = ('sircunscripcion','nombre')
	search_fields = ('nombre','apellido_paterno')
class nivel_3_vista(admin.ModelAdmin):
	#list_display = ('id','nombre','apellido_paterno','apellido_materno','ci','sircunscripcion','municipio','recinto','mesa','ci','fecha')
	#list_filter = ('sircunscripcion','nombre')
	search_fields = ('nombre','apellido_paterno')
admin.site.register(control_electoral,control_electoral_vista)
admin.site.register(nivel_2,nivel_2_vista)
admin.site.register(nivel_3,nivel_3_vista)
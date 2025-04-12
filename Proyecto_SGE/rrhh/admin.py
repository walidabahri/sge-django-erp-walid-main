from django.contrib import admin
from .models import Departamento, Puesto, Empleado

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'responsable')
    search_fields = ('nombre', 'responsable')

@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'departamento')
    search_fields = ('titulo',)
    list_filter = ('departamento',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'departamento', 'puesto', 'email')
    search_fields = ('nombre', 'apellidos', 'email')
    list_filter = ('departamento', 'puesto')

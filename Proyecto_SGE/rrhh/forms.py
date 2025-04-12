from django import forms
from .models import Departamento, Puesto, Empleado

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'responsable']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = ['titulo', 'departamento']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellidos', 'direccion', 'departamento', 'puesto', 'email', 'foto']

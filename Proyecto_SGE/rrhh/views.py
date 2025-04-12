from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Departamento, Puesto, Empleado
from .forms import DepartmentForm, PositionForm, EmpleadoForm

class DepartamentoListView(ListView):
    model = Departamento
    context_object_name = 'departamentos'
    template_name = 'rrhh/departamento_listar.html'

class DepartamentoDetailView(DetailView):
    model = Departamento
    context_object_name = 'departamento'
    template_name = 'rrhh/departamento_detalle.html'

class DepartamentoCreateView(CreateView):
    model = Departamento
    form_class = DepartmentForm
    context_object_name = 'departamento'
    template_name = 'rrhh/departamento_crear.html'
    success_url = reverse_lazy('listar_departamentos')

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    form_class = DepartmentForm
    context_object_name = 'departamento'
    template_name = 'rrhh/departamento_editar.html'
    success_url = reverse_lazy('listar_departamentos')

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    context_object_name = 'departamento'
    template_name = 'rrhh/departamento_eliminar.html'
    success_url = reverse_lazy('listar_departamentos')


class PuestoListView(ListView):
    model = Puesto
    context_object_name = 'puestos'
    template_name = 'rrhh/puesto_listar.html'

class PuestoDetailView(DetailView):
    model = Puesto
    context_object_name = 'puesto'
    template_name = 'rrhh/puesto_detalle.html'

class PuestoCreateView(CreateView):
    model = Puesto
    form_class = PositionForm
    context_object_name = 'puesto'
    template_name = 'rrhh/puesto_crear.html'
    success_url = reverse_lazy('listar_puestos')

class PuestoUpdateView(UpdateView):
    model = Puesto
    form_class = PositionForm
    context_object_name = 'puesto'
    template_name = 'rrhh/puesto_editar.html'
    success_url = reverse_lazy('listar_puestos')

class PuestoDeleteView(DeleteView):
    model = Puesto
    context_object_name = 'puesto'
    template_name = 'rrhh/puesto_eliminar.html'
    success_url = reverse_lazy('listar_puestos')


class EmpleadoListView(ListView):
    model = Empleado
    context_object_name = 'empleados'
    template_name = 'rrhh/empleado_listar.html'

class EmpleadoDetailView(DetailView):
    model = Empleado
    context_object_name = 'empleado'
    template_name = 'rrhh/empleado_detalle.html'

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    context_object_name = 'empleado'
    template_name = 'rrhh/empleado_crear.html'
    success_url = reverse_lazy('listar_empleados')

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    context_object_name = 'empleado'
    template_name = 'rrhh/empleado_editar.html'
    success_url = reverse_lazy('listar_empleados')

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    context_object_name = 'empleado'
    template_name = 'rrhh/empleado_eliminar.html'
    success_url = reverse_lazy('listar_empleados')

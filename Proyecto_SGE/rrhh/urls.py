"""
URL configuration for Proyecto_SGE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    # Departamento URLs
    path('departamentos/', views.DepartamentoListView.as_view(), name='listar_departamentos'),
    path('departamentos/<int:pk>/', views.DepartamentoDetailView.as_view(), name='ver_departamento'),
    path('departamentos/crear/', views.DepartamentoCreateView.as_view(), name='crear_departamento'),
    path('departamentos/editar/<int:pk>/', views.DepartamentoUpdateView.as_view(), name='editar_departamento'),
    path('departamentos/eliminar/<int:pk>/', views.DepartamentoDeleteView.as_view(), name='eliminar_departamento'),
    # Puesto URLs
    path('puestos/', views.PuestoListView.as_view(), name='listar_puestos'),
    path('puestos/<int:pk>/', views.PuestoDetailView.as_view(), name='ver_puesto'),
    path('puestos/crear/', views.PuestoCreateView.as_view(), name='crear_puesto'),
    path('puestos/editar/<int:pk>/', views.PuestoUpdateView.as_view(), name='editar_puesto'),
    path('puestos/eliminar/<int:pk>/', views.PuestoDeleteView.as_view(), name='eliminar_puesto'),
    # Empleado URLs
    path('empleados/', views.EmpleadoListView.as_view(), name='listar_empleados'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='ver_empleado'),
    path('empleados/crear/', views.EmpleadoCreateView.as_view(), name='crear_empleado'),
    path('empleados/editar/<int:pk>/', views.EmpleadoUpdateView.as_view(), name='editar_empleado'),
    path('empleados/eliminar/<int:pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar_empleado'),
]

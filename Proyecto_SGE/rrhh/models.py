# rrhh/models.py
from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    responsable = models.CharField(max_length=100, verbose_name="Responsable")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.nombre

class Puesto(models.Model):
    titulo = models.CharField(max_length=100, verbose_name="Título")
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):
        return self.titulo

class Empleado(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    direccion = models.TextField(verbose_name="Dirección")
    email = models.EmailField(verbose_name="Email")
    foto = models.ImageField(upload_to='fotos', null=True, blank=True, verbose_name="Fotografía")
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento")
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, verbose_name="Puesto")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    def __str__(self):

        return f"{self.nombre} {self.apellidos}"

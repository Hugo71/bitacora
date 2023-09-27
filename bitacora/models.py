from django.db import models
from django.contrib.auth.models import User  # Asegúrate de importar User si aún no lo has hecho
from django.contrib import admin



class Actividad(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.CASCADE)  # Asociar actividad a un empleado
    fecha = models.DateField(null=True)
    area = models.CharField(max_length=100)  # Agrega el campo "Área"
    usuario = models.CharField(max_length=100)  # Agrega el campo "Usuario"
    tema = models.CharField(max_length=100)  # Agrega el campo "Tema"
    descripcion = models.TextField()
    
    
    class Meta:
        verbose_name_plural = "Actividades"

    def __str__(self):
        return f"{self.fecha} - {self.empleado.username}"

# Create your models here.

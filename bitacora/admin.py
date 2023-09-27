from .models import Actividad
from django.contrib import admin


# Register your models here.
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'fecha', 'area', 'usuario', 'tema', 'descripcion')
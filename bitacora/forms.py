from django import forms
from .models import Actividad
from django.forms.widgets import DateInput

class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ['fecha', 'area', 'usuario', 'tema', 'descripcion']
        widgets = {
            'fecha': DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'fecha': 'Fecha',
            'area': 'Area',
            'usuario': 'Usuario',
            'tema': 'Tema',
            'descripcion': 'Descripción',
        }

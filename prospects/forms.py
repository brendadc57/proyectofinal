from django import forms
from .models import Prospect, Seguimiento

class ProspectForm(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = ['nombre', 'correo', 'telefono', 'estatus']

class SeguimientoForm(forms.ModelForm):
    class Meta:
        model = Seguimiento
        fields = ['nota', 'creado_por', 'nuevo_estatus']

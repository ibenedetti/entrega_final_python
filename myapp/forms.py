from django import forms
from .models import Estudiante, Profesor, Examen

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email']


class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['asignatura', 'fecha', 'hora']
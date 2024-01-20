from django import forms
from .models import Genero, Alumno
from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model  = Genero
        fields = "__all__"

class AlumnoForm(ModelForm):
    class Meta:
        model  = Alumno
        fields = "__all__"
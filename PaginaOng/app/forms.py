from django import forms
from django.forms import ModelForm
from .models import Organizacion

class OrganizacionForm(ModelForm):
    
    class Meta:
        model = Organizacion
        fields = ['idOng','nombreOng', 'fechaOng', 'descripcionOng', 'fotoOng']
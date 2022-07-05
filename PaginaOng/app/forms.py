from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Organizacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrganizacionForm(ModelForm):
    
    class Meta:
        model = Organizacion
        fields = ['idOng','nombreOng', 'fechaOng', 'descripcionOng', 'fotoOng']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]
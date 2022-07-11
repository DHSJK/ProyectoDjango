from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Organizacion, Donacion, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class OrganizacionForm(forms.ModelForm):
    
    class Meta:
        model = Organizacion
        #fields = ['idOng','nombreOng', 'fechaOng', 'descripcionOng', 'fotoOng']
        fields = '__all__'
        widgets = {
            "fechaOng": forms.SelectDateWidget()
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]


class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['usuarioDonador', 'nombreDonador', 'correoDonador', 'ong', 'monto']
        #fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


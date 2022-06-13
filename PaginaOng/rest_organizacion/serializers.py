from dataclasses import fields
from rest_framework import serializers
from app.models import Organizacion

class OrganizacionSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Organizacion
        fields = ['nombreOng', 'fechaOng', 'descripcionOng', 'fotoOng']
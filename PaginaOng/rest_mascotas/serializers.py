from dataclasses import fields
from rest_framework import serializers
from app.models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    sexo_mascota = serializers.CharField(source="sexoMascota")
    
    raza_mascota = serializers.CharField(source="razaMascota")
    
    class Meta:
        model = Mascota
        fields = ['nombreMascota', 'edadAnioMascota', 'edadMesesMascota', 'sexo_mascota', 'estEstirizadoMascota', 'raza_mascota', 'fotoMascota']
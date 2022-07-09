from dataclasses import fields
from .models import Donacion
from rest_framework import serializers

class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = '__all__'
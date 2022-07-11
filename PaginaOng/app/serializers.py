from dataclasses import fields
from .models import Donacion, Producto, Marca, Organizacion
from rest_framework import serializers

class DonacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donacion
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'



class ProductoSerializer(serializers.ModelSerializer):
    #personalizar visualizador informacion de campos de la base de datos
    nombre_marca = serializers.CharField(read_only=True, source="marcaProducto.nombreMarca")
    marcaProducto = MarcaSerializer(read_only=True)
    idMarca = serializers.PrimaryKeyRelatedField(queryset=Marca.objects.all(), source="marcaProducto")
    #caracteres minimos para nombre
    nombreProducto = serializers.CharField(required=True, min_length=3)
    

    #Validacion si exite nombre de producto
    #def validate_nombreProducto(self, value):
     #   existe = Producto.objects.filter(nombreProducto__iexact=value).exists()
#
#        if existe:
 #           raise serializers.ValidationError("Este Nombre de producto ya existe")

  #      return value


    class Meta:
        model = Producto
        fields = '__all__'

class OrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizacion
        fields = ['idOng','nombreOng', 'fechaOng', 'descripcionOng', 'fotoOng']
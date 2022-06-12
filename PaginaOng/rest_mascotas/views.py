from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Mascota
from .serializers import MascotaSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_mascotas(request):
    """
    GET = Lista todas las mascotas
    POST = Agrega Registro
    """
    if request.method == 'GET':
        mascota = Mascota.objects.all()
        serializer = MascotaSerializer(mascota, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MascotaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
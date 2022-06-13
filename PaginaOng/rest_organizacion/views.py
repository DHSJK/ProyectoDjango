from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Organizacion
from .serializers import OrganizacionSerializer

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_organizacion(request):
    """
    GET = Lista todas las Organizaciones
    POST = Agrega Registro
    """
    if request.method == 'GET':
        organizacion = Organizacion.objects.all()
        serializer = OrganizacionSerializer(organizacion, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrganizacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.

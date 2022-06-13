from django.shortcuts import render
import requests,json
from .models import Mascota

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def tienda(request):
    return render(request, 'app/inc/tienda.html')

def nosotros(request):
    return render(request, 'app/inc/nosotros.html')

def donaciones(request):
    return render(request, 'app/inc/donaciones.html')

def contacto(request):
    return render(request, 'app/inc/contacto.html')

def carrito(request):
    return render(request, 'app/inc/carrito.html')

def tabla(request):
    # mascotas = Mascota.objects.all
    mascotas = requests.get('http://127.0.0.1:8000/api/lista-mascotas')
    
    datos = mascotas.json()
    data = {
        'mascotas': datos
    } 
    
    return render(request, 'app/tabla.html', data)


def tablaproducto(request):
 
    productos = requests.get('http://127.0.0.1:8000/api/lista-productos')
    
    datos = productos.json()
    data = {
        'productos': datos
    } 
    
    return render(request, 'app/tablaproducto.html', data)




def organizacion(request):
 
    organizacion = requests.get('http://127.0.0.1:8000/api/lista-organizacion')
    
    datos = organizacion.json()
    data = {
        'organizacion': datos
    } 
    
    return render(request, 'app/organizacion.html', data)

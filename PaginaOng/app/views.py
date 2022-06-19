from django.shortcuts import render, redirect
import requests,json
from app.forms import OrganizacionForm
from .models import Mascota, Organizacion
from django.contrib import messages



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

def ong(request):
 
    organizacion = requests.get('http://127.0.0.1:8000/api/lista-organizacion')
    
    datos = organizacion.json()
    data = {
        'organizacion': datos
    } 
    
    return render(request, 'app/organizacion.html', data)




def form_organizacion(request):

    organizacion = requests.get('http://127.0.0.1:8000/api/lista-organizacion')

    datos = {
        'form': OrganizacionForm
    }
    
    if request.method == 'POST':
        formulario = OrganizacionForm(request.POST)
        
        print(request.POST)
        print(request.POST['nombreOng'])
        if formulario.is_valid:
            
            Org = Organizacion()
            Org.nombreOng = request.POST['nombreOng']
            Org.fechaOng = request.POST['fechaOng']
            Org.descripcionOng = request.POST['descripcionOng']
            if len(request.FILES) != 0:
                Org.fotoOng = request.FILES['fotoOng']
                Org.save()

            datos['mensaje'] = 'Guardado Correctamente'
            
    return render(request, 'app/form_organizacion.html', datos)




def form_mod_organizacion(request, id):

    organizacion = Organizacion.objects.get(idOng = id)
    
    datos = {
        'form': OrganizacionForm(instance = organizacion)
    }
    
    if request.method == 'POST':
        formulario = OrganizacionForm(data=request.POST, instance = organizacion)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Modificado Correctamente'
            
    return render(request, 'app/form_organizacion.html', datos)

def form_del_organizacion(request, id):
    organizacion = Organizacion.objects.get(idOng = id)
    
    organizacion.delete()
    
    return redirect(to=ong)




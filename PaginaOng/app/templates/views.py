from django.shortcuts import render, redirect
import requests,json
from app.forms import OrganizacionForm, CustomUserCreationForm, DonacionForm, ProductoForm
from .models import Organizacion, Donacion, Producto
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from rest_framework import viewsets
from .serializers import DonacionSerializer, ProductoSerializer


# Create your views here.

class DonacionViewset(viewsets.ModelViewSet):
    queryset = Donacion.objects.all()
    serializer_class = DonacionSerializer

def index(request):
    return render(request, 'app/index.html')

def tienda(request):
    productos = requests.get('http://127.0.0.1:8000/api/producto')
        
    datos = productos.json()
    data = {
        'productos': datos
    } 
    
    return render(request, 'app/inc/tienda.html', data)


def nosotros(request):
    return render(request, 'app/inc/nosotros.html')

def donaciones(request):
    data = {
        'form': DonacionForm()
    }

    if request.method == 'POST':
        formulario = DonacionForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Donación registrada a su cuenta"
        else:
            data["form"] = formulario

    return render(request, 'app/inc/donaciones.html', data)

def contacto(request):
    return render(request, 'app/inc/contacto.html')

def carrito(request):
    return render(request, 'app/inc/carrito.html')


def registro(request):
    return render(request, 'app/inc/registro.html')

def login(request):
    return render(request, 'app/inc/login.html')


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
        formulario = OrganizacionForm(data=request.POST, instance = organizacion, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Modificado Correctamente'
        datos['form'] = OrganizacionForm (instance=Organizacion.objects.get(idOng=id))
            
    return render(request, 'app/form_organizacion.html', datos)

def form_del_organizacion(request, id):
    organizacion = Organizacion.objects.get(idOng = id)
    
    organizacion.delete()
    
    return redirect(to=ong)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            auth_login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #redirigir al home
            return redirect(to="/")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)



class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    #Filtro nombre de los productos
    def get_queryset(self):
        productos = Producto.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombreProducto__contains=nombre)
        
        return productos

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

@api_view(['GET', 'PUT', 'DELETE'])
def detalle_organizacion(request, id):
    """
    GET = Muestra 1 organización en particular
    PUT = Actualiza 1 organización en particular
    DELETE = Elimina 1 organización en particular
    """
    try:
        organizacion = Organizacion.objects.get(idOng=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = OrganizacionSerializer(organizacion)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrganizacionSerializer(organizacion, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        organizacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


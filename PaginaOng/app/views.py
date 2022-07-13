from django.shortcuts import render, redirect, get_object_or_404
import requests,json
from app.forms import OrganizacionForm, CustomUserCreationForm, DonacionForm, ProductoForm
from .models import Organizacion, Donacion, Producto
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from rest_framework import viewsets
from .serializers import DonacionSerializer, ProductoSerializer, OrganizacionSerializer
from app.carrito import Carrito


# ORGANIZACIONES
class OrganizacionViewset(viewsets.ModelViewSet):
    queryset = Organizacion.objects.all()
    serializer_class = OrganizacionSerializer

    def get_queryset(self):
        organizaciones = Organizacion.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            organizaciones = organizaciones.filter(nombreOng__contains=nombre)
        
        return organizaciones

def agregar_ong(request):
    data = {
        'form' : OrganizacionForm()
    }

    if request.method == 'POST':
        formulario = OrganizacionForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "ONG agregada correctamente")
        else:
            data["form"] = formulario

    return render(request, 'app/organizacion/agregar.html', data)

def listar_ong(request):
    ong = requests.get('http://127.0.0.1:8000/api/organizacion/')
    
    datos = ong.json()
    data = {
        'ong': datos
    } 
    
    return render(request, 'app/organizacion/listar.html', data)

def modificar_ong(request, id):
    
    ong = Organizacion.objects.get(idOng = id)
        
    data = {
        'form': OrganizacionForm(instance = ong)
    }
    if request.method == 'POST':
        formulario = OrganizacionForm(data=request.POST, instance = ong, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_ong")
        datos['form'] = formulario
            
    return render(request, 'app/organizacion/modificar.html', data)

def eliminar_ong(request, id):
    
    ong = Organizacion.objects.get(idOng = id)
    ong.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_ong")

# FIN ORGANIZACIONES

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

def agregar_producto(request, producto_idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_idProducto)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_idProducto)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_idProducto):
    carrito = Carrito(request)
    producto = Producto.objects.get(idProducto=producto_idProducto)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")

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
            messages.success(request, "Donación registrada.")
        else:
            data["form"] = formulario

    return render(request, 'app/inc/donaciones.html', data)

def contacto(request):
    return render(request, 'app/inc/contacto.html')



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



# PRODUCTOS
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





def agregar_producto_tienda(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")
        else:
            data["form"] = formulario

    return render(request, 'app/productos/agregar_prod.html', data)

def listar_producto_tienda(request):
    productos = requests.get('http://127.0.0.1:8000/api/producto/')
    
    datos = productos.json()
    data = {
        'productos': datos
    } 
    
    return render(request, 'app/productos/listar_prod.html', data)

def modificar_producto_tienda(request, id):
    
    productos = Producto.objects.get(idProducto = id)
        
    data = {
        'form': ProductoForm(instance = productos)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance = productos, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar_producto_tienda")
        datos['form'] = formulario
            
    return render(request, 'app/productos/modificar_prod.html', data)

def eliminar_producto_tienda(request, id):
    
    productos = Producto.objects.get(idProducto = id)
    productos.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="listar_producto_tienda")

# FIN PRODUCTOS


from django.shortcuts import render

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



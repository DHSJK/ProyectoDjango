from django.urls import path
from .views import index, tienda, nosotros, donaciones, contacto, carrito, tabla, tablaproducto, organizacion

urlpatterns = [
    path('', index, name="index"),
    path('tienda/', tienda, name="tienda"),
    path('nosotros/', nosotros, name="nosotros"),
    path('donaciones/', donaciones, name="donaciones"),
    path('contacto/', contacto, name="contacto"),
    path('carrito/', carrito, name="carrito"),
    path('tabla/', tabla, name="tabla"),
    path('tablaproducto/', tablaproducto, name="tablaproducto"),
    path('organizacion/', organizacion, name="organizacion"),
    

    
]

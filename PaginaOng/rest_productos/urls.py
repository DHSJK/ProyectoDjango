from django.urls import path
from .views import lista_productos

urlpatterns = [
    path('lista-productos', lista_productos, name='lista_productos'),
]
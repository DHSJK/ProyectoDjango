from django.urls import path
from .views import lista_mascotas

urlpatterns = [
    path('lista-mascotas', lista_mascotas, name='lista_mascotas'),
]
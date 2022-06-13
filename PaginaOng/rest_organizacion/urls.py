from django.urls import path
from .views import lista_organizacion

urlpatterns = [
    path('lista-organizacion', lista_organizacion, name='lista_organizacion'),
]
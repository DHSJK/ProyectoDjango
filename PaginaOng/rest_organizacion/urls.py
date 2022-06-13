from django.urls import path
from .views import lista_organizacion, detalle_organizacion

urlpatterns = [
    path('lista-organizacion', lista_organizacion, name='lista_organizacion'),
    path('detalle-organizacion/<id>', detalle_organizacion, name='detalle_organizacion'),
]
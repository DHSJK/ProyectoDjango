from django.contrib import admin
from .models import *
# Register your models here.

# productos
admin.site.register(TipoMascotaPRO)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)

# ONG
admin.site.register(Organizacion)

# DONACIONES
admin.site.register(Donacion)


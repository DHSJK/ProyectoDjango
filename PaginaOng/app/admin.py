from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Raza)
admin.site.register(Sexo)
admin.site.register(TipoMascota)
admin.site.register(Mascota)


# productos
admin.site.register(TipoMascotaPRO)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)

# ONG
admin.site.register(Organizacion)


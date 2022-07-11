from django.urls import path, include
from .views import index, tienda, nosotros, donaciones, contacto, tablaproducto, ProductoViewset,\
    registro, login, DonacionViewset, OrganizacionViewset, agregar_ong, listar_ong, modificar_ong, eliminar_ong, \
    agregar_producto, eliminar_producto, restar_producto, limpiar_carrito
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('donacion', DonacionViewset),
router.register('producto', ProductoViewset),
router.register('organizacion', OrganizacionViewset)


urlpatterns = [
    path('', index, name="index"),
    path('tienda/', tienda, name="tienda"),
    path('agregar-ong/', agregar_ong, name="agregar_ong"),
    path('listar-ong/', listar_ong, name="listar_ong"),
    path('modificar-ong/<id>/', modificar_ong, name='modificar_ong'),
    path('eliminar-ong/<id>/', eliminar_ong, name='eliminar_ong'),
    
    path('agregar/<int:producto_idProducto>/', agregar_producto, name='Add'),
    path('eliminar/<int:producto_idProducto>/', eliminar_producto, name='Del'),
    path('restar/<int:producto_idProducto>/', restar_producto, name='Sub'),
    path('limpiar/', limpiar_carrito, name='CLS'),
    

    path('nosotros/', nosotros, name="nosotros"),
    path('donaciones/', donaciones, name="donaciones"),
    path('contacto/', contacto, name="contacto"),
   
    path('tablaproducto/', tablaproducto, name="tablaproducto"),
    path('registro/', registro, name="registro"),
    path('login/', login, name="login"),
    path('api/', include(router.urls)),   

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
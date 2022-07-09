from django.urls import path, include
from .views import index, ong, tienda, nosotros, donaciones, contacto, carrito, tabla, tablaproducto,\
     organizacion,form_organizacion, form_mod_organizacion, form_del_organizacion, registro, login, DonacionViewset
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('donacion', DonacionViewset)

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
    path('form-organizacion/', form_organizacion, name='form_organizacion'),
    path('ong/', ong, name='ong'),
    path('form-mod-organizacion/<id>', form_mod_organizacion, name='form_mod_organizacion'),
    path('form-del-organizacion/<id>', form_del_organizacion, name='form_del_organizacion'),
    path('registro/', registro, name="registro"),
    path('login/', login, name="login"),
    path('api/', include(router.urls)),
    

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
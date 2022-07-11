from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tkinter.tix import INCREASING
from django.db import models

# Create your models here.
#**************************BASE DE DATOS PRODUCTOS*********************


class TipoMascotaPRO(models.Model):
    idTipoProducto = models.AutoField(primary_key=True, verbose_name='Id de Mascota')
    descTipoMascota = models.CharField(max_length=30, verbose_name='Descripción de Mascota')
    
    def __str__(self):
        return self.descTipoMascota

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='Id de Categoria')
    descCategoria = models.CharField(max_length=50)
    tipoMascota = models.ForeignKey(TipoMascotaPRO, default=1, on_delete=models.CASCADE)
       
    def __str__(self):
        return self.descCategoria

class Marca(models.Model):
    idMarca = models.AutoField(primary_key=True, verbose_name='Id de marca')
    nombreMarca = models.CharField(max_length=200)
    
       
    def __str__(self):
        return self.nombreMarca


class Producto(models.Model):
    idProducto = models.AutoField (primary_key=True, verbose_name='Id del Producto')
    nombreProducto = models.CharField(max_length=40, verbose_name='Nombre del Producto')
    precioProducto = models.IntegerField(verbose_name='Precio del Producto')
    descripcionProducto = models.TextField(verbose_name='Descripcion del Producto')
    marcaProducto = models.ForeignKey(Marca, on_delete=models.PROTECT)
    stockProducto = models.IntegerField(verbose_name='Cantidad Stock')
    categoriaProducto = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fotoProducto = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombreProducto

#**************************FIN BASE DE DATOS PRODUCTOS*********************


#****************************BASE DE DATOS ORGANIZACION***********************
    


class Organizacion(models.Model):
    idOng = models.AutoField (primary_key=True, verbose_name='Id de la Ong')
    nombreOng = models.CharField(max_length=40, verbose_name='Nombre de la Ong')
    fechaOng = models.DateField(verbose_name='Fecha de Ingreso Ong')
    descripcionOng = models.TextField(verbose_name='Descripcion de la Ong')
    fotoOng = models.ImageField(upload_to="Organizacion", null=True, blank=True)

    
    def __str__(self):
        return str(self.nombreOng)


#****************************FIN BASE DE DATOS ORGANIZACION***********************

#****************************BASE DE DATOS DONACIONES***********************
opciones_donaciones = [
    [0, 1000],
    [1, 2000],
    [2, 5000],
    [3, 10000],
    [4, 20000]

]
class Donacion(models.Model):
    usuarioDonador = models.CharField(max_length=50, verbose_name='Usuario')
    nombreDonador = models.CharField(max_length=50, verbose_name='Nombre y Apellido')
    ong = models.ForeignKey(Organizacion, null=True, blank=True, on_delete=models.CASCADE, verbose_name='ONG')
    correoDonador = models.EmailField(verbose_name='Correo')
    fechaDonacion = models.DateTimeField(auto_now_add=True)
    monto = models.IntegerField(choices=opciones_donaciones, verbose_name='Monto a donar')

    def __str__(self):
        return str(self.usuarioDonador)



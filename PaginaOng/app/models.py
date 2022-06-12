from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tkinter.tix import INCREASING
from django.db import models

# Create your models here.

class TipoMascota(models.Model):
    idTipoMascota = models.AutoField(primary_key=True, verbose_name='Id de Mascota')
    descTipoMascota = models.CharField(max_length=15, verbose_name='Descripción de Mascota')
    
    def __str__(self):
        return self.descTipoMascota
    
class Raza(models.Model):
    idRaza = models.AutoField(primary_key=True, verbose_name='Id de Raza')
    descRaza = models.CharField(max_length=40, verbose_name='Descripción Raza')
    tipoMascota = models.ForeignKey(TipoMascota, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descRaza

class Sexo(models.Model):
    idSexo = models.AutoField(primary_key=True)
    descSexo = models.CharField(max_length=15)
    
    def __str__(self):
        return self.descSexo

class Mascota(models.Model):
    idMascota = models.AutoField(primary_key=True, verbose_name='Id de Mascota')
    nombreMascota = models.CharField(max_length=40, verbose_name='Nombre de Mascota')
    edadAnioMascota = models.IntegerField(verbose_name='Edad en Años de Mascota')
    edadMesesMascota = models.IntegerField(verbose_name='Edad en Meses de Mascota')
    sexoMascota = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    estEstirizadoMascota = models.BooleanField(verbose_name='Estado Estirilización de Mascota')
    razaMascota = models.ForeignKey(Raza, on_delete=models.CASCADE)
    fotoMascota = models.ImageField(upload_to='static/img/')
    
    def __str__(self):
        return self.nombreMascota
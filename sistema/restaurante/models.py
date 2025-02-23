from django.db import models

# Create your models here.
class restaurante(models.Model):
    id = models.AutoField(primary_key=True)
    platillo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción",null=True)
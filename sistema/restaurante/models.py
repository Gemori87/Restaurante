from django.db import models

# Create your models here.
class Platillos(models.Model):
    id = models.AutoField(primary_key=True)
    platillo = models.CharField(max_length=100, verbose_name='Título')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    descripcion = models.TextField(verbose_name="Descripción",null=True)

    def __str__(self):
        fila = "Título: " + self.platillo + " - " + "Descripción" + self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
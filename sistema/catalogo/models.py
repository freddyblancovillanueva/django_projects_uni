from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True , verbose_name="Id")
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", null=True, blank=True)
    imagen = models.ImageField(upload_to='MEDIA/', verbose_name="IMG", null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True, verbose_name="Descripción")

    def __str__(self):
        return self.nombre

class PDF(models.Model):
    id_pdf = models.AutoField(primary_key=True , verbose_name="Id")
    archivo = models.FileField(upload_to='pdfs/')
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario", null=True, blank=True)



# agregar formularios
#agregar usuario 
#link para compartir 
#id y pdf tabla unica class pdf
# PAGINA INICIO filtrada con usuario 
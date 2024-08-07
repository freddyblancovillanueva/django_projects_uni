from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class PDF(models.Model):
    archivo = models.FileField(upload_to='pdfs/')



# agregar formularios
#agregar usuario 
#link para compartir 
#id y pdf tabla unica class pdf
# PAGINA INICIO filtrada con usuario 
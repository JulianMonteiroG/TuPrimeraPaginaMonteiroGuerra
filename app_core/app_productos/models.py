from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=40)
    descripcion_producto = models.CharField(max_length=9999, default="Sin descripción")
    precio_producto = models.IntegerField()
    
    def __str__(self):
        return (f"{self.nombre_producto} - {self.precio_producto}")


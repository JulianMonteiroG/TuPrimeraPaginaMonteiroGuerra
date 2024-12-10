from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.CharField(max_length=40)
    nombre_de_usuario = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def __str__(self):
        return (f"{self.nombre} - {self.apellidos} - {self.edad} - {self.email} - {self.nombre_de_usuario} - {self.password}")


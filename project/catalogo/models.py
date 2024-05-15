from django.db import models

class NuevoProducto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=50, unique=True)
    año =  models.CharField(max_length=50, unique=True)


    def __str__(self) -> str:
        return  f"{self.nombre} {self.marca} {self.año}"
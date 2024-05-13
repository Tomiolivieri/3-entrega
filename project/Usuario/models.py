from django.db import models

class Provincia(models.Model):
    nombre = models.CharField(max_length=35)

    def __str__(self) -> str:
        return self.nombre

class Usuario(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=30)
    telefono =  models.CharField(max_length=12)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True, blank=True, verbose_name= "Provincia en la que reside")

    def __str__(self) -> str:
        return self.dni


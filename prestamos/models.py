from django.db import models

# Create your models here.

class Genero(models.Model):
    genero = models.CharField(max_length=10, default='M')

    def __str__(self):
        return self.genero

class Prestamo(models.Model):
    dni = models.IntegerField(default=1)
    nombre_apellido = models.CharField(max_length=200, default='Juan Roman Riquelme')
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    email = models.EmailField(max_length=200, default='roman@moni.com.ar')
    monto = models.IntegerField(default=1, blank = True, null = True)

    def __str__(self):
        return self.nombre_apellido
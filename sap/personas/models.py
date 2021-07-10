from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    noCalle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domilio {self.id}: {self.calle} {self.noCalle} {self.pais}'

class Persona(models.Model):
    nombre = models.CharField(max_length=255) #siempre se le debe de poner el maxLength
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True) #relacion de tablas
    #on_delete puede ser models.CASCADE por si elimino el docmilio que se elimine la persona alv

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'
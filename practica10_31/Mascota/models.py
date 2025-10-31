from django.db import models
from ..usuarios.models import Cliente

# Create your models here.

class Mascota(models.model):
    nombre_mascota = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
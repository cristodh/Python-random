from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=100) # CharField = VARCHAR
    correo_cliente = models.EmailField(unique=True) 
    telefono_cliente = models.CharField(max_length=20)
    direccion_cliente = models.CharField(max_length=200)
    fecha_registro = models.DateField(auto_now_add=True)


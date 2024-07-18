from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: Eliminar el producto
    # PROTECT: Lanza un error
    # RESTRICT: Solo elimina si no existen productos
    # SET_NULL: Actualiza a valor null
    # SET_DEFAULT: Actualiza a valor por defecto
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)

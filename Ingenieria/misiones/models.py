from django.db import models

# Create your models here.

class misiones(models.Model):
    nombre = models.CharField(max_length=99)
    puntos = models.IntegerField()

class usuario(models.Model):
    usuario = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=30)
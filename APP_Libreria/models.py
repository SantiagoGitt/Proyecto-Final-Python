from django.db import models

# Create your models here.

class Clientes(models.Modeld):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    cumpleanios = models.DateField()

class Empleados(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    cumpleanios = models.DateField()
    horario = models.IntegerField()
    legajo = models.IntegerField()

class Stock(models.Model):
    nombre = models.CharField()
    autor = models.CharField()
    genero = models.CharField()
    cantidad = models.IntegerField()

class Resenia(models.Model):
    nombre_libro = models.CharField()
    puntaje = models.IntegerField(max_length=10)
    resenia = models.TextField(max_length=280)
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    nacimiento = models.DateField()

class Empleados(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    cumpleanios = models.DateField()
    horario = models.IntegerField()
    legajo = models.IntegerField()

class Stock(models.Model):
    nombre = models.CharField(max_length=64)
    autor = models.CharField(max_length=64)
    genero = models.CharField(max_length=64)
    cantidad = models.IntegerField()

class Resenia(models.Model):
    nombre_libro = models.CharField(max_length=64)
    puntaje = models.IntegerField()
    resenia = models.TextField(max_length=280)
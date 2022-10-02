from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    nacimiento = models.DateField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Correo:{self.correo} - Nacimiento:{self.nacimiento}"

class Empleados(models.Model):
    nombre = models.CharField(max_length=64)
    correo = models.EmailField()
    cumpleanios = models.DateField()
    horario = models.IntegerField()
    legajo = models.IntegerField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Correo:{self.correo} - Cumpleaños:{self.cumpleanios} - Horario:{self.horario} - Legajo:{self.legajo}"

class Stock(models.Model):
    nombre = models.CharField(max_length=64)
    autor = models.CharField(max_length=64)
    genero = models.CharField(max_length=64)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Nombre:{self.nombre} - Autor:{self.autor} - Genero:{self.genero} - Cantidad:{self.cantidad}"

class Resenia(models.Model):
    nombre_libro = models.CharField(max_length=64)
    puntaje = models.IntegerField()
    resenia = models.TextField(max_length=280)

    def __str__(self):
        return f"Nombre:{self.nombre_libro} - Puntaje:{self.puntaje} - Reseña:{self.resenia}"
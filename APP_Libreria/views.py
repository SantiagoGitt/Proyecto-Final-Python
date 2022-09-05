from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from APP_Libreria.models import *
from APP_Libreria.forms import *


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def clientes(request):
    return render(request, "clientes.html")

def empleados(request):
    return render(request, "empleados.html")

def stock(request):
    return render(request, "stock.html")

def resenia(request):
    return render(request, "resenia.html")

def clienteFormulario(request):
        if request.method=="POST":
            form= clienteFormulario(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            mail= info["correo"]
            fechadenacimiento= info["YYYY-MM-DD"]
            clientes= Clientes(nombre=nombre, correo=correo, fecha_de_nacimiento=fechadenacimiento)
            clientes.save()
            return render (request, "templates/inicio.html", {"mensaje":"Cliente creado"})
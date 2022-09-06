from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from APP_Libreria.models import *
from APP_Libreria.forms import ClienteForm


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def empleados(request):
    return render(request, "empleados.html")

def resenia(request):
    return render(request, "resenia.html")

def stock(request):
    return render(request, "stock.html")

def clientes(request):
    if request.method == 'POST':
        formulario=ClienteForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            nombre=informacion["nombre"]
            correo=informacion["correo"]
            nacimiento=informacion["nacimiento"]
            cliente=Clientes(nombre=nombre, correo=correo, nacimiento=nacimiento)
            cliente.save()
            return render(request, "stock.html")
        else:
            return render(request, "empleados.html")

    else:
        formulario=ClienteForm()
        return render(request, "clientes.html", {"formulario":formulario})


def busquedaStock(request):
    return render(request, "busquedaStock.html")

def buscar(request):
    nombre=request.GET["autor"]
    stock=Stock.objects.filter(autor=nombre)
    return render(request, "busquedaStock.html", {"autor":stock})
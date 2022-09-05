from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from APP_Libreria.models import *
from APP_Libreria.forms import ClienteForm


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def clientes(request):
    if request.method == 'POST':
        formulario=ClienteForm(request.POST)
        print("------------11111----------------")
        print(formulario)
        print("------------11111----------------")
        if formulario.is_valid():
            print("----------------2222-----------------")
            print(formulario)
            print("----------------2222-----------------")
            informacion=formulario.cleaned_data
            print(informacion)
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

def empleados(request):
    return render(request, "empleados.html")

def stock(request):
    return render(request, "stock.html")

def resenia(request):
    return render(request, "resenia.html")

def clienteFormulario(request):
    return render (request, "cursos.html")
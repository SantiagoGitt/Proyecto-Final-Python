from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from APP_Libreria.models import *
from APP_Libreria.forms import *


# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def clientes(request):
    if request.method == 'POST':
        form=ClienteForm()
        print("--------------------------------------")
        print(form)
        print("--------------------------------------")
        if form.is_valid():
            informacion=form.cleande_data
            print(informacion)
            nombre=informacion["nombre"]
            correo=informacion["correo"]
            cumpleanios=informacion["cumpleanios"]
            cliente=Clientes(nombre=nombre, correo=correo, cumpleanios=cumpleanios)
            cliente.save()
            return render(request, "stock.html")

    else:
        formulario=ClienteForm()
        return render(request, "clientes.html", {"formulario":formulario})
    return render(request, "clientes.html")

def empleados(request):
    return render(request, "empleados.html")

def stock(request):
    return render(request, "stock.html")

def resenia(request):
    return render(request, "resenia.html")

def clienteFormulario(request):
    return render (request, "cursos.html")
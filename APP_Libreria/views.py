from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from APP_Libreria.models import *

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
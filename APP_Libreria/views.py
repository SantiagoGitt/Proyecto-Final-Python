from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from APP_Libreria.models import *

# Create your views here.

def clientes(request):
    return HttpResponse("Clientes")

def empleados(request):
    return HttpResponse("Empleados")

def stock(request):
    return HttpResponse("Stock")

def resenia(request):
    return HttpResponse("Resenia")
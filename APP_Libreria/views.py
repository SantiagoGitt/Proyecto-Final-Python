from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from APP_Libreria.models import *
from APP_Libreria.forms import ClienteForm
from APP_Libreria.forms import EmpleadosForm
from APP_Libreria.forms import ReseniaForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def empleados(request):
    return render(request, "empleados.html")
    
class Empleadoslist(ListView):
    model= Empleados
    template_name= "Empleados_List.html"

class Empleadodetalle(DetailView):
    model= Empleados
    template_name= "Empleados_Detalle.html"

class Empleadouppdate(UpdateView):
    model= Empleados
    success_url= "empleados/empleados/list"
    fields = ["nombre", "correo", "horario", "legajo"]

class Empleadoelimina(DeleteView):
    model= Empleados
    success_url= "empleados/empleados/list"

def EmpleadoNuevo(request):
    if request.method == 'POST':
        formulario=EmpleadosForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            nombre=informacion["nombre"]
            correo=informacion["correo"]
            cumpleanios=informacion["cumpleanios"]
            horario=informacion["horario"]
            legajo=informacion["legajo"]
            empleados=Empleados(nombre=nombre, correo=correo, cumpleanios=cumpleanios,horario=horario, legajo=legajo)
            empleados.save()
            return render(request, "empleados.html")
        else:
            return render(request, "empleado_nuevo.html")
    else:
        formulario=EmpleadosForm()
    return render(request, "empleado_nuevo.html", {"formulario":formulario})


def resenias(request):
    if request.method == 'POST':
        formulario=ReseniaForm(request.POST)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            nombre_libro=informacion["nombre_libro"]
            puntaje=informacion["puntaje"]
            resenia=informacion["resenia"]
            resenias=Resenia(nombre_libro=nombre_libro, puntaje=puntaje, resenia=resenia)
            resenias.save()
            return render(request, "inicio.html")
        else:
            return render(request, "resenia.html")
    else:
        formulario=ReseniaForm()
    return render(request, "resenia.html", {"formulario":formulario})

def ReseniaList(request):
    nombre_libro=Resenia.objects.all()
    contexto={"libro":nombre_libro}
    return render (request, "listarResenia.html", contexto)

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
            return render(request, "inicio.html")
        else:
            return render(request, "clientes.html")

    else:
        formulario=ClienteForm()
    return render(request, "clientes.html", {"formulario":formulario})

def stock(request):
    return render(request, "stock.html")


def busquedaStock(request):
    return render(request, "busquedaStock.html")

def buscar(request):
    if request.GET["autor"]:

        autor=request.GET['autor']
        nombre=Stock.objects.filter(autor__icontains=autor)
        

        return render(request, "busquedaStock.html", {"autor":autor, "nombre":nombre})

    else:
        respuesta = "No corresponden los datos"
        return HttpResponse(respuesta)

def buscarlibro(request):
    if request.GET["nombre"]:

        nombre=request.GET['nombre']
        autor=Stock.objects.filter(nombre__icontains=nombre)
        genero=Stock.objects.filter(nombre__icontains=nombre)
        
        return render(request, "busquedaStock.html", {"Autor":autor, "Nombre":nombre, "Genero":genero})
    else:
        respuesta = "No corresponden los datos"
        return HttpResponse(respuesta)

def buscargenero(request):
    if request.GET["genero"]:

        genero=request.GET['genero']
        nombre=Stock.objects.filter(genero__icontains=genero)
        autor=Stock.objects.filter(genero__icontains=genero)
        
        return render(request, "busquedaStock.html", {"Autor":autor, "Nombre":nombre, "Genero":genero})
    else:
        respuesta = "No corresponden los datos"
        return HttpResponse(respuesta)
   
class listStock(ListView):
    model= Stock
    template_name= "Stock_list.html"

class detalleStock(DetailView):
    model= Stock
    template_name= "Stock_detalle.html"

class nuevoStock(CreateView):
    model= Stock
    success_url= "stock/list"
    fields = ["nombre", "autor", "genero", "cantidad"]

class uppdateStock(UpdateView):
    model= Stock
    success_url= "stock/list"
    fields = ["genero", "cantidad"]

class eliminaStock(DeleteView):
    model= Stock
    success_url= "stock/list"
    
#def login_request (request):
#    if request.method=="POST":
#        form = AuthenticationForm(request, data=request.POST)

#        if form.is_valid():
#            usuario=form.cleaned_data.get("username")
#            contraseña=form.cleaned_data.get("password")
#
#            user= authenticate(username=usuario,password=contraseña)

#            if user is not None:
#                login(request, user)

#                return render (request, "inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            
#            else:
#                return render (request, "inicio.html", {"mensaje":f"Error - Datos Incorectos"})

#        else:
#                return render (request, "inicio.html", {"mensaje":f"Error - Formulario Erroneo"})

#    form = AuthenticationForm()
#    return render (request, "login.html", {"form":form})

#def registracion (request):
#    if request.method=="POST":
#       form = UserCreationForm (request, data=request.POST)

#       if form.is_valid():
#            usuario=form.cleaned_data["usuario"]
#            form.save()

#            return render (request, "inicio.html", {"mensaje":f"Usuario Creado {usuario}"})

#    else:
#        form=UserCreationForm
            
#    return render (request, "registroUsuario.html", {"form":form})


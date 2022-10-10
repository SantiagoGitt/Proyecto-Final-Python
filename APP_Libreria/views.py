from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from APP_Libreria.models import *
from APP_Libreria.forms import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def empleados(request):
    return render(request, "empleados.html")
    
class Empleadoslist(LoginRequiredMixin,ListView):
    model= Empleado
    template_name= "empleados.html"

class Empleadodetalle(LoginRequiredMixin,DetailView):
    model= Empleado
    template_name= "empleados_detalle.html"     

class Empleadouppdate(LoginRequiredMixin,UpdateView):
    model= Empleado
    success_url= reverse_lazy("empleados")
    fields = ['nombre', 'correo', 'cumpleaños', 'horario', 'legajo']
    template_name="empleados_form.html"

class Empleadoelimina(LoginRequiredMixin,DeleteView):
    model= Empleado
    success_url= reverse_lazy("empleados")
    template_name="empleados_confirm_delete.html"

class Empleadonuevo(LoginRequiredMixin,CreateView):
    model= Empleado
    success_url= reverse_lazy("empleados")
    fields = ['nombre', 'correo', 'cumpleaños', 'horario', 'legajo']
    template_name="empleados_form.html"


def resenias(request):
    return render(request, "inicio.html")
 
class ReseniaList(ListView):
    model= Resenia
    template_name= "resenia.html"

class Reseniaelimina(LoginRequiredMixin,DeleteView):
    model= Resenia
    success_url= reverse_lazy("resenia")
    template_name="resenia_confirm_delete.html"

class Reseniauppdate(LoginRequiredMixin,UpdateView):
    model= Resenia
    success_url= reverse_lazy("resenia")
    fields = ['nombre_libro', 'puntaje', 'reseña']
    template_name="resenia_form.html"

class Resenianueva(LoginRequiredMixin,CreateView):
    model= Resenia
    success_url= reverse_lazy("resenia")
    fields = ['nombre_libro', 'puntaje', 'reseña']
    template_name="resenia_form.html"
    def form_valid(self,form):
        Resenia.objects.create(nombre_libro= self.request.POST['nombre_libro'], user= user)
        return redirect(self.success_url)

def about(request):
    return render(request, "about.html")

def stock(request):
    return render(request, "stock.html")


def busquedaStock(request):
    return render(request, "busquedaStock.html")

def buscarautor(request):
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
        nombre=Stock.objects.filter(nombre__icontains=nombre)
                
        return render(request, "busquedaStock.html", {"nombre":nombre})
    else:
        respuesta = "No corresponden los datos"
        return HttpResponse(respuesta)

def buscargenero(request):
    if request.GET["genero"]:

        genero=request.GET['genero']
        nombre=Stock.objects.filter(genero__icontains=genero)
        
        return render(request, "busquedaStock.html", {"genero":genero, "nombre":nombre})
    else:
        respuesta = "No corresponden los datos"
        return HttpResponse(respuesta)
   
class Stocklist(ListView):
    model= Stock
    template_name= "stock_lista.html"

class Stockdetalle(DetailView):
    model= Stock
    template_name= "stock_detalle.html"

class Stocknuevo(LoginRequiredMixin,CreateView):
    model= Stock
    success_url= reverse_lazy("stock_lista")
    fields = ["nombre", "autor", "genero", "cantidad","pequeña_reseña"]
    template_name= "stock_form.html"

class Stockuppdate(LoginRequiredMixin,UpdateView):
    model= Stock
    success_url= reverse_lazy("stock_lista")
    fields = ['nombre', 'autor', 'genero', 'cantidad',"pequeña_reseña"]
    template_name= "stock_form.html"

class Stockelimina(LoginRequiredMixin,DeleteView):
    model= Stock
    success_url= reverse_lazy("stock_lista")
    template_name= "stock_confirm_delete.html"
    
def login_request(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password') 
            user= authenticate(username=usuario,password=contraseña)
            if user is not None:
                login(request, user)
                return render (request, "inicio.html")       
            else:
                return render (request, "loginerror.html", {"mensaje":"Error - Datos Erroneos"})
        else:
            return render (request, "loginerror.html", {"mensaje":"Error - Datos Erroneos"})
    form = AuthenticationForm()
    return render (request, "login.html", {'form':form})

def registracion(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, "registrocorrecto.html", {"mensaje":f"Usuario Creado {username}"})
        else:
            return render (request, "registroerror.html", {"mensaje":f"Datos Erroneos"})    
    else:
        form=UserRegistrationForm
        return render(request, "registrousuario.html", {"form":form})


@login_required
def EditarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.first_name=informacion['first_name']
            usuario.last_name=informacion['last_name']
            usuario.email=informacion['email']
            usuario.save()
            return render (request, "editarperfilCorrecto.html", {"mensaje":f"Usuario Modificado Correctamente"})
        else:
            return render (request, "editarperfilError.html", {"mensaje":f"Formularios Erroneo"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarperfil.html", {"form":form,"usuario":usuario})

@login_required
def inicio(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    if len(avatares)!=0:
            avatar=avatares[0].imagen.url
    else:
        avatar=""
    return render (request, "inicio.html",{"avatar":avatar})

@login_required
def cargaravatar(request):
    if request.method == 'POST':
        form= AvatarForm(request.POST, request.FILES)
        if form.is_valid:
            u=User.objects.get(username=request.user)
            avatar=Avatar (user=u,imagen=form.cleaned.data['imagen'])
            avatar.save()
            return render(request,"inicio.html")
    else:
        form=AvatarForm()
    return render(request,"agregaravatar.html",{"form":form})


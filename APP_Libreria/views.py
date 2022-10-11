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
    return render(request, "empleados.html",{"avatar":ObtenerAvatar(request)})
    
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
 
def ReseniaList(request):
    lista= Resenia.objects.all()
    return render(request,"resenia.html",{"lista":lista})



@login_required
def Resenianueva(request):
    if request.method=='POST':
        form=ReseniaForm(request.POST)
        if form.is_valid():             
            resenia=Resenia (user=request.user,nombre_libro=form.cleaned_data['nombre_libro'],puntaje=form.cleaned_data['puntaje'],reseña=form.cleaned_data['reseña'])
            resenia.save()  
            return render(request,"resenia_cargadaok.html", {"mensaje":f"Reseña Cargada","avatar":ObtenerAvatar(request)})
    else:
        form=ReseniaForm()
    return render(request,"resenia_nueva.html",{"form":form,"avatar":ObtenerAvatar(request)})

@login_required
def MisResenias(request):
    lista= Resenia.objects.filter(user=request.user)
    return render(request,"mis_resenias.html",{"lista":lista,"avatar":ObtenerAvatar(request)})


@login_required
def Reseniauppdate(request,id):
    resenia=Resenia.objects.filter(id=id)
    if request.method=='POST':
        form=ReseniaForm(request.POST)
        if form.is_valid():
            informacion:form.cleaned_data
            resenia.nombre_libro=informacion['nombre_libro']
            resenia.puntaje=informacion['puntaje']
            resenia.reseña=informacion['reseña']
            resenia.save()
            return render(request,"mis_resenias.html",{"avatar":ObtenerAvatar(request)})
    else:
        form=ReseniaForm(initial={'nombre_libro':resenia.nombre_libro,'puntaje':resenia.puntaje,'reseña':resenia.reseña})
        return render(request,"resenia_editar.html",{"form":form,"id":id,"avatar":ObtenerAvatar(request)})


@login_required
def Reseniaelimina(request,id):
    resenia=Resenia.objects.filter(id=id)
    resenia.delete()
    lista= Resenia.objects.filter(user=request.user)
    return render(request,"mis_resenias.html",{"lista":lista,"avatar":ObtenerAvatar(request)})

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
                return render (request, "inicio.html",{"avatar":ObtenerAvatar(request)})       
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
            return render(request, "registrocorrecto.html", {"mensaje":f"Usuario Creado {username}","avatar":ObtenerAvatar(request)})
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
            return render (request, "editarperfilCorrecto.html", {"mensaje":f"Usuario Modificado Correctamente","avatar":ObtenerAvatar(request)})
        else:
            return render (request, "editarperfilError.html", {"mensaje":f"Formularios Erroneo","avatar":ObtenerAvatar(request)})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "editarperfil.html", {"form":form,"usuario":usuario,"avatar":ObtenerAvatar(request)})

@login_required
def inicio(request):
    return render (request, "inicio.html",{"avatar":ObtenerAvatar(request)})

@login_required
def cargaravatar(request):
    if request.method == 'POST':
        form= AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avataractual=Avatar.objects.filter(user=request.user)
            if(len(avataractual)>0):
                avataractual[0].delete()
            avatar=Avatar (user=request.user,imagen=form.cleaned_data['imagen'])
            avatar.save()
            return render(request,"AvatarCargaCorrecta.html",{'usuario':request.user,'mensaje': 'IMAGEN AGREGADA CORRECTAMENTE',"imagen":avatar.imagen.url,"avatar":ObtenerAvatar(request)})
    else:
        form=AvatarForm()
    return render(request,"cargaravatar.html",{"form":form,"avatar":ObtenerAvatar(request)})

@login_required
def eiiminaavatar(request):
    avataractual=Avatar.objects.filter(user=request.user)
    if(len(avataractual)>0):
        avataractual[0].delete()
    return render(request,"AvatarCargaCorrecta.html",{'usuario':request.user,'mensaje': 'IMAGEN ELIMINADA'})

def ObtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if(len(lista)!=0):
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen



@login_required
def LibrosFavoritos(request):
    lista= Imagen.objects.filter(user=request.user)
    return render(request,"LibrosFavoritos.html",{"lista":lista,"avatar":ObtenerAvatar(request)})

@login_required
def SubirLibroFavorito(request):
    if request.method == 'POST':
        form= ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen=Imagen (user=request.user,nombre_libro=form.cleaned_data['nombre_libro'],imagen=form.cleaned_data['imagen'])
            imagen.save()
            return render(request,"LibroFavoritoCargaCorrecta.html",{'usuario':request.user,'mensaje': 'IMAGEN AGREGADA CORRECTAMENTE',"imagen":imagen.imagen.url,"avatar":ObtenerAvatar(request)})
    else:
        form=ImagenForm()
    return render(request,"LibroFavoritoCarga.html",{"form":form,"avatar":ObtenerAvatar(request)})


@login_required
def LibroFavoritoUppdate(request,id):
    librofavorito=Imagen.objects.filter(id=id)
    if request.method=='POST':
        form=ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            informacion:form.cleaned_data
            librofavorito.nombre_libro=informacion['nombre_libro']
            librofavorito.imagen=informacion['imagen']
            librofavorito.save()
            return render(request,"LibrosFavoritos.html",{"avatar":ObtenerAvatar(request)})
    else:
        form=ImagenForm(initial={'nombre_libro':librofavorito.nombre_libro,'imagen':librofavorito.imagen})
        return render(request,"LibroFavoritoEditar.html",{"form":form,"id":id,"avatar":ObtenerAvatar(request)})


@login_required
def LibroFavoritoElimina(request,id):
    librofavorito=Imagen.objects.get(id=id)
    librofavorito.delete()
    lista= Imagen.objects.filter(user=request.user)
    return render(request,"LibroFavoritoEliminado.html",{"lista":lista,"avatar":ObtenerAvatar(request)})

from dataclasses import fields
from django import forms
#from django.contrib.auth.forms import UserCreationForm, User


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=64)
    correo = forms.EmailField()
    nacimiento = forms.DateField()

class StockForm(forms.Form):
    nombre = forms.CharField(max_length=64)
    autor = forms.CharField(max_length=64)
    genero = forms.CharField(max_length=64)
    cantidad = forms.IntegerField()

class EmpleadosForm(forms.Form):
    nombre = forms.CharField(max_length=64)
    correo = forms.EmailField()
    cumpleanios = forms.DateField()
    horario = forms.IntegerField()
    legajo = forms.IntegerField()

class ReseniaForm(forms.Form):
    nombre_libro = forms.CharField(max_length=64)
    puntaje = forms.IntegerField()
    resenia = forms.CharField(max_length=280)

#class UserRegistrationForm(UserCreationForm):
#    email=forms.EmailField()
#    password1 =forms.CharField(label='Constraseña',widget=forms.PasswordInput)
#    password1 =forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    
#    class Meta:
#        model = User
#        field = ['username','email','password1','password2']
#        help_text = {k:"" for k in fields}

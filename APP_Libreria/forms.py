from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=64)
    correo = forms.EmailField()
    nacimiento = forms.DateField()

class Stock(forms.Form):
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

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
from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=64)
    correo = forms.EmailField()
    cumpleanios = forms.DateField()
from django import forms

class ClientesFormulario(forms.Form):
    nombre: forms.CharField(max_length=64)
    correo: forms.EmailField()
    fecha_de_nacimiento: forms.DateField()
from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, User


class UserRegistrationForm(UserCreationForm):
     email=forms.EmailField()
     password1 =forms.CharField(label='Constraseña',widget=forms.PasswordInput)
     password2 =forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    
class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    last_name =forms.CharField(label='Apellido')
    first_name=forms.CharField(label='Nombre')
    email=forms.EmailField()
    
    class Meta:
        model = User
        fields = ['last_name','first_name','email']
        help_text = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen= forms.ImageField()

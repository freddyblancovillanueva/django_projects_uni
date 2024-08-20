from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Producto, PDF

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']
        labels = {
            'nombre': 'Nombre del producto',
            'precio': 'Precio del producto'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'})
        }

class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['archivo']
        labels = {
            'archivo': 'Archivo PDF'
        }
        widgets = {
            'archivo': forms.FileInput(attrs={'class': 'form-control'})
        }

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Correo electrónico',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }

class LoginUsuarioForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})
        }
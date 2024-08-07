from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Producto, PDF

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', ['usuario']]

class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = [ 'archivo']

class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginUsuarioForm(AuthenticationForm):
    pass
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Producto, PDF
from .forms import ProductoForm, PDFForm, RegistroUsuarioForm, LoginUsuarioForm

@login_required
def listar_productos(request):
    productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'catalogo/listar_productos.html', {'productos': productos})
@login_required

@login_required
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'catalogo/agregar_producto.html', {'form': form})
@login_required

@login_required
def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'catalogo/editar_producto.html', {'form': form, 'producto': producto})
@login_required

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, usuario=request.user)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'catalogo/eliminar_producto.html', {'producto': producto})

def agregar_pdf(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = PDFForm()
    return render(request, 'catalogo/agregar_pdf.html', {'form': form})

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('listar_productos')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'catalogo/registrar_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginUsuarioForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listar_productos')
    else:
        form = LoginUsuarioForm()
    return render(request, 'catalogo/login_usuario.html', {'form': form})

def logout_usuario(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('login_usuario')

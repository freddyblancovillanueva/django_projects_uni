from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Producto, PDF
from .forms import ProductoForm, PDFForm, RegistroUsuarioForm, LoginUsuarioForm
from django.shortcuts import redirect
from .models import Producto
from .forms import ProductoForm
from django.http import HttpResponseForbidden

def listar_productos(request):
    productos = Producto.objects.filter(id_usuario=request.user.id)
    return render(request, 'paginas/inicio.html', {'productos': productos})

@login_required
def agregar_producto(request):
    form = ProductoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
            producto = form.save(commit=False)
            producto.usuario = request.user
            producto.save()
            return redirect('/admin/')
    return render(request, 'FRM_PRODUCTOS/agregar.html', {'form': form})

@login_required
def editar_producto(request, ):
    if request.method == 'POST':
        form = ProductoForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        form = ProductoForm()
    return render(request, 'FRM_PRODUCTOS/editar.html', {'form': form,})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        if not request.user.is_authenticated or not request.user.is_superuser:
            return HttpResponseForbidden("No tienes permisos para realizar esta acción.")
        producto.delete()
        return redirect('listar_productos')  # Cambia 'listar_productos' por el nombre correcto de tu vista de lista

    return render(request, 'FRM_PRODUCTOS/eliminar.html', {'producto': producto})

@login_required
def agregar_pdf(request):
    if request.method == 'POST':
        form = PDFForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('inicio.html')
    else:
        form = PDFForm()
    return render(request, 'FRM_PDF/cargarpdf.html', {'form': form})

@login_required
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio.html')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'FRM_USUARIOS/registro_usuario.html', {'form': form})


def login_usuario(request):
    if request.method == 'POST':
        form = LoginUsuarioForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('listar_productos')
    else:
        form = LoginUsuarioForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_usuario(request):
    from django.contrib.auth import logout
    logout(request)
    return redirect('listar_productos')

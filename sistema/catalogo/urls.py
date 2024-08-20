from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listar_productos, name='listar_productos'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('agregar_pdf/', views.agregar_pdf, name='agregar_pdf'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('login/', views.login_usuario, name='login_usuario'),
    path('salir/', views.logout_usuario, name='logout_usuario'),
    path('admin/', admin.site.urls),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

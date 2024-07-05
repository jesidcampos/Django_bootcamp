from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar/', views.agregar_usuario, name='agregar_usuario'),
    path('lista/', views.listar_usuarios, name='lista_usuario'),
]
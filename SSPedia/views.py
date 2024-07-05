from django.shortcuts import render,  redirect
from SSPedia.forms.forms import UsuarioForm
from SSPedia.Models.models import Usuario

def agregar_usuario(request):
    form = UsuarioForm()

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'agregarUsuario.html', {'form': form})

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'ListaUsuarios.html', {'usuarios': usuarios})

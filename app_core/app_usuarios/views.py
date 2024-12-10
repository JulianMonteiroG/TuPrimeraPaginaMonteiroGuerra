from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios":usuarios}
    return render(request,"app_usuarios/usuario_list.html",contexto)

def create_usuarios(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_usuarios:listar_usuarios")
    else:
        form = UsuarioForm()
        contexto = {"form":form}
    return render(request,"app_usuarios/usuario_create.html",contexto)

def delete_usuarios(request, pk):
    usuario = get_object_or_404(Usuario,pk=pk)
    if request.method == "POST":
        usuario.delete()
        return redirect("app_usuarios:listar_usuarios")
    contexto = {"usuario":usuario}
    return render(request, "app_usuarios/usuario_delete.html", contexto)


from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductoForm
from .models import Producto
# Create your views here.
def listar_productos(request):
    productos = Producto.objects.all()
    contexto = {"productos":productos}
    return render(request,"app_productos/producto_list.html",contexto)

def create_productos(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app_productos:listar_productos")
    else:
        form = ProductoForm()
        contexto = {"form":form}
    return render(request,"app_productos/producto_create.html",contexto)

def update_productos(request, pk):
    producto = get_object_or_404(Producto,pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("app_productos:listar_productos")
    else:
        form = ProductoForm(instance=producto)
        contexto = {"form":form}
    return render(request,"app_productos/producto_update.html",contexto)

def delete_productos(request, pk):
    producto = get_object_or_404(Producto,pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("app_productos:listar_productos")
    contexto = {"producto":producto}
    return render(request, "app_productos/producto_delete.html", contexto)
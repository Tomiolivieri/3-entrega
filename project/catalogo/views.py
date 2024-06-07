from django.shortcuts import render, redirect, get_object_or_404
from .models import NuevoProducto
from catalogo.forms import NuevoProductoForm

def home(request):
    return render(request, "catalogo/index.html")

def lista_catalogo(request):
    lista = NuevoProducto.objects.all()
    contexto = {"catalogo" : lista}
    return render(request, "catalogo/lista_catalogo.html", contexto)

def lista_create(request):
    if request.method == "POST":
        form = NuevoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "catalogo/lista_catalogo.html")
    else:
        form = NuevoProductoForm()
    return render(request, "catalogo/lista_create.html", {"form": form})

"""def buscar(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        consulta = NuevoProducto.objects.filter(nombre__icontains=busqueda)
    else:
        consulta = NuevoProducto.objects.all()
    contexto = {"NuevoProducto" : consulta}
    return render(request, "catalogo/lista_catalogo", contexto)"""

def catalogo_update(request,pk):
    consulta = NuevoProducto.objects.get(id=pk)
    if request.method == "POST":
        form = NuevoProductoForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("catalogo:lista_create")
    else:
        form = NuevoProductoForm(instance=consulta)
    return render(request, "catalogo/lista_create.html", {"form": form})

def catalogo_delete(request, pk):
    consulta = get_object_or_404(NuevoProducto, id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("catalogo:lista_catalogo")
    return render(request, "catalogo/catalogo_delete.html", {"object": consulta})
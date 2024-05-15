from django.shortcuts import render
from .models import NuevoProducto
from catalogo.forms import NuevoProductoForm

def home(request):
    return render(request, "catalogo/index.html")

def lista_catalogo(request):
    lista = NuevoProducto.objects.all()
    contexto = {"catalogo" : lista}
    return render(request, "catalogo/lista_catalogo.html", contexto)

def lista_create(request):
    if request.method == "post":
        form = NuevoProductoForm()
    else:
        form = NuevoProductoForm()
    return render(request, "catalogo/lista_create.html", {"form": form})
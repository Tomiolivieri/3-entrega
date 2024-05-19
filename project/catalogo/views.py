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
    if request.method == "POST":
        form = NuevoProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "catalogo/lista_catalogo.html")
    else:
        form = NuevoProductoForm()
    return render(request, "catalogo/lista_create.html", {"form": form})

#def buscar_producto():
    #busqueda = request#(#"buscar")
    #productos = NuevoProducto.objects.all()
    #if busqueda:
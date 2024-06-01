from django.shortcuts import render
from .models import Usuario
from Usuario.forms import NuevoUsuarioForm

def home(request):
    return render(request, "Usuario/index.html")

def lista_usuarios(request):
    lista = Usuario.objects.all()
    contexto = {"Usuarios" : lista}
    return render(request, "Usuario/lista_usuarios.html", contexto)

def create_usuario(request):
    if request.method == "POST":
        formulario = NuevoUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request, "Usuario/lista_usuarios.html")
    else:
        formulario = NuevoUsuarioForm()
    return render(request, "Usuario/agregar_usuarios.html", {"formulario": formulario})

def acerca_de(request):
    return render(request, "Usuario/acerca_de.html")
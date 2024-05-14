from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, "Usuario/index.html")

def lista_usuarios(request):
    lista = Usuario.objects.all()
    contexto = {"Usuarios" : lista}
    return render(request, "Usuario/lista_usuarios.html", contexto)
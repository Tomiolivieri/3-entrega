from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
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

def usuario_update(request,pk):
    consulta = Usuario.objects.get(id=pk)
    if request.method == "POST":
        form = NuevoUsuarioForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect("http://127.0.0.1:8000/Usuario/lista")
    else:
        form =  NuevoUsuarioForm(instance=consulta)
    return render(request, "Usuario/usuario_update.html", {"form": form})

def usuario_delete(request, pk):
    consulta = get_object_or_404(Usuario, id=pk)
    if request.method == "POST":
        consulta.delete()
        return redirect("http://127.0.0.1:8000/Usuario/lista")
    return render(request, "Usuario/usuario_delete.html", {"object": consulta})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    else:
        form = UserCreationForm()
    return render(request, 'Usuario/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('http://127.0.0.1:8000/') 
    else:
        form = AuthenticationForm()
    return render(request, 'Usuario/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('http://127.0.0.1:8000/')

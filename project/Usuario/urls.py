from django.urls import path
from .views import home, lista_usuarios 


app = "Usuario"

urlpatterns = [
    path("", home, name="home"),
    path("Usuario/lista", lista_usuarios, name="lista")
]
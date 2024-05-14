from django.urls import path
from .views import home, lista_usuarios 


app_name = "Usuario"

urlpatterns = [
    path("", home, name="home"),
    path("Usuario/lista", lista_usuarios, name="lista")
]
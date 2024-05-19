from django.urls import path
from .views import home, lista_usuarios, create_usuario 


app_name = "Usuario"

urlpatterns = [
    path("", home, name="home"),
    path("lista", lista_usuarios, name="lista"),
    path("create", create_usuario, name="agregar_usuarios")
]
from django.urls import path
from .views import home, lista_catalogo, lista_create


app_name = "catalogo"

urlpatterns = [
    path("", home, name="home"),
    path("lista/catalogo", lista_catalogo, name="lista_catalogo"),
    path("lista/create", lista_create, name="lista_create")
]
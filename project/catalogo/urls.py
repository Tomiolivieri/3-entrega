from django.urls import path
from .views import home, lista_catalogo, lista_create, catalogo_delete, catalogo_update


app_name = "catalogo"

urlpatterns = [
    path("", home, name="home"),
    path("lista", lista_catalogo, name="lista_catalogo"),
    path("lista/create", lista_create, name="lista_create"),
    path("update/<int:pk>", catalogo_update, name="catalogo_update"),
    path("catalogo/catalogo_delete/<int:pk>/", catalogo_delete, name="catalogo_delete")
]
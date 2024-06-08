from django.urls import path
from .views import home, lista_usuarios, create_usuario, acerca_de, usuario_delete, usuario_update, register, user_login, user_logout



app_name = "Usuario"

urlpatterns = [
    path("", home, name="home"),
    path("lista", lista_usuarios, name="lista"),
    path("create", create_usuario, name="agregar_usuarios"),
    path("acerca_de", acerca_de, name="acerca_de"),
    path("modificar/<int:pk>", usuario_update, name="usuario_update"),
    path("borrar/<int:pk>", usuario_delete, name="usuario_delete"),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
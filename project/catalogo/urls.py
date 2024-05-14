from django.urls import path
from .views import home


app = "catalogo"

urlpatterns = [
    path("", home, name="home")
]
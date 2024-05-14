from django.urls import path
from core.views import home

app = "core"
urlpatterns = [
    path("", home, name="home")
]
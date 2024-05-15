from django import forms
from . import models

class NuevoProductoForm(forms.ModelForm):
    class Meta:
        model = models.NuevoProducto
        fields = ["nombre", "marca", "año"]
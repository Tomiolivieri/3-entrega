from django import forms
from . import models

class NuevoUsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ["nombre", "dni", "telefono", "provincia"]
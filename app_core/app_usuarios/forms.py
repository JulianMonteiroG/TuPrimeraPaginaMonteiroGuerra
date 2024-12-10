from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","apellidos","edad","email","nombre_de_usuario","password"]
        widgets = {}


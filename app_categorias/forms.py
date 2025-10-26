from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['id_categoria', 'nombre_categoria', 'descripcion', 'foto_categoria']  # Incluimos id y foto

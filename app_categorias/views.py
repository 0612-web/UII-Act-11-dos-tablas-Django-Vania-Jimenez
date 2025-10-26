from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm

def listar_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'app_categorias/listar_categoria.html', {'categorias': categorias})

def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    return render(request, 'app_categorias/detalle_categoria.html', {'categoria': categoria})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_categorias:listar_categoria')
    else:
        form = CategoriaForm()
    return render(request, 'app_categorias/formulario_categoria.html', {'form': form, 'titulo': 'Crear categoria'})
def detalle_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    return render(request, 'app_categorias/detalle_categoria.html', {'categoria': categoria})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('app_categorias:listar_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'app_categorias/formulario_categoria.html', {'form': form, 'titulo': 'Editar Categoría'})

def borrar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('app_categorias:listar_categoria')
    return render(request, 'app_categorias/confirmar_borrado.html', {'categoria': categoria})

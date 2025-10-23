from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria, Producto

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'app_categorias/listar_categorias.html', {'categorias': categorias})

def detalle_categorias(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    return render(request, 'app_categorias/detalle_categorias.html', {'categoria': categoria})

def crear_categorias(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        Categoria.objects.create(nombre=nombre, descripcion=descripcion)
        return redirect('app_categorias:listar_categorias')
    return render(request, 'app_categorias/formulario_categorias.html', {'titulo': 'Crear Categoría'})

def editar_categorias(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    if request.method == 'POST':
        categoria.nombre = request.POST.get('nombre')
        categoria.descripcion = request.POST.get('descripcion')
        categoria.save()
        return redirect('app_categorias:listar_categorias')
    return render(request, 'app_categorias/formulario_categorias.html', {'categoria': categoria, 'titulo': 'Editar Categoría'})

def borrar_categorias(request, categoria_id):
    categoria = get_object_or_404(Categoria, id_categoria=categoria_id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('app_categorias:listar_categorias')
    return render(request, 'app_categorias/confirmar_borrar.html', {'categoria': categoria})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'app_categorias/listar_productos.html', {'productos': productos})

def crear_productos(request):
    categorias = Categoria.objects.all()  # NECESARIO para el select
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        id_categoria_id = request.POST.get('id_categoria')
        id_proveedor = request.POST.get('id_proveedor')
        foto = request.FILES.get('foto')
        
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            id_categoria_id=id_categoria_id,
            id_proveedor=id_proveedor,
            foto=foto
        )
        return redirect('app_categorias:listar_productos')
    
    return render(request, 'app_categorias/formulario_productos.html', {
        'titulo': 'Crear Producto',
        'categorias': categorias
    })

def editar_productos(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    categorias = Categoria.objects.all()  # NECESARIO para el select
    
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.id_categoria_id = request.POST.get('id_categoria')
        producto.id_proveedor = request.POST.get('id_proveedor')
        
        if 'foto' in request.FILES:
            producto.foto = request.FILES['foto']
        
        producto.save()
        return redirect('app_categorias:listar_productos')
    
    return render(request, 'app_categorias/formulario_productos.html', {
        'producto': producto,
        'titulo': 'Editar Producto',
        'categorias': categorias
    })

def borrar_productos(request, producto_id):
    producto = get_object_or_404(Producto, id_producto=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('app_categorias:listar_productos')
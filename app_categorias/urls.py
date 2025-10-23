from django.urls import path
from . import views

app_name = 'app_categorias'

urlpatterns = [
    path('', views.listar_categorias, name='listar_categorias'),
    path('<int:categoria_id>/', views.detalle_categorias, name='detalle_categorias'),
    path('crear/', views.crear_categorias, name='crear_categorias'),
    path('editar_categoria/<int:categoria_id>/', views.editar_categorias, name='editar_categorias'),
    path('borrar_categoria/<int:categoria_id>/', views.borrar_categorias, name='borrar_categorias'),
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_productos, name='crear_productos'),
    path('productos/editar/<int:producto_id>/', views.editar_productos, name='editar_productos'),
    path('productos/borrar/<int:producto_id>/', views.borrar_productos, name='borrar_productos'),
]
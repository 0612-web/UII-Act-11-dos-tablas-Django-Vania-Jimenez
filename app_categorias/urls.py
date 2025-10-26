from django.urls import path
from . import views

app_name = 'app_categorias'

urlpatterns = [
    path('', views.listar_categoria, name='listar_categoria'),
    path('artista/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('crear/', views.crear_categoria, name='crear_categoria'),
    path('editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('borrar/<int:categoria_id>/', views.borrar_categoria, name='borrar_categoria'),

]

from django.db import models

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True) 
    nombre_categoria = models.CharField(max_length=100, help_text="Nombre de la categoria")
    descripcion = models.CharField(max_length=100)
    foto_categoria = models.ImageField(upload_to='categorias/', blank=True, null=True) 

    def __str__(self):
        return f"{self.id_categoria} - {self.nombre_categoria}"

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    detalle = models.CharField(max_length=100)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    id_proveedor = models.IntegerField(primary_key=True) 
    foto =  models.ImageField(upload_to='img_categorias/', blank=True, null=True)

    def __str__(self):
        return f"{self.id_categoria.nombre_categoria}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
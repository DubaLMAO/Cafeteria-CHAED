from django.db import models

#Menu de la cafeteria
class Producto(models.Model):
    CATEGORIAS = [
        ('CAFE', 'Cafés Especiales'),
        ('SNACK', 'Pasteles & Snacks'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='CAFE', db_index=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    
    def __str__(self):
        return self.nombre
    

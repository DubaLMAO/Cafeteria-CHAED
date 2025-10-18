from django.contrib import admin
from .models import Producto

#Modelo del Menú

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)

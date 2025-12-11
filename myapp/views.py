from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Producto
from django.core.paginator import Paginator



@cache_page(60 * 15)  
def home(request):
    cafes = Producto.objects.filter(categoria='CAFE')
    snacks = Producto.objects.filter(categoria='SNACK')
    return render(request, 'core/home.html', {'cafes': cafes, 'snacks': snacks})

@cache_page(60 * 15)  
def privacy_policy(request):
    return render(request, 'core/paginas/privacy_policy.html')


def terms_conditions(request):
    return render(request, 'core/paginas/terms_conditions.html')
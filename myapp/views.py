from django.shortcuts import render
from .models import Producto


# Create your views here.
def home(request):
    cafes = Producto.objects.filter(categoria='CAFE')
    snacks = Producto.objects.filter(categoria='SNACK')
    return render(request, 'core/home.html', {'cafes': cafes, 'snacks': snacks})


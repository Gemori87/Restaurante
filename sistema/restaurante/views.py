from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def platillos(request):
    return render(request, 'platillos/index.html')
def crear(request):
    return render(request, 'platillos/crear.html')

def editar(request):
    return render(request, 'platillos/editar.html')

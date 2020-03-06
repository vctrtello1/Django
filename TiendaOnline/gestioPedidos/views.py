from django.shortcuts import render
from django.http import HttpResponse
from gestioPedidos.models import articulos

# Create your views here.


def busquedaProductos(request):
    return render(request, "busquedaProductos.html")


def buscar(request):
    if request.GET['producto']:
        # mensaje = 'Articulo buscado: %r' % request.GET['producto']
        producto = request.GET['producto']
        productos = articulos.objects.filter(
            nombre__icontains=producto)
        return render(request, 'resultadosBusqueda.html', {
            'articulos': productos, 'query': producto})
    else:
        mensaje = 'No has introducido nada'
    return HttpResponse(mensaje)

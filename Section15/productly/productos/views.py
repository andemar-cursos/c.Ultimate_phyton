from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from productos.models import Producto


# Create your views here.
def index(request):
    productos = Producto.objects.all().values()

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    return HttpResponse(producto_id)


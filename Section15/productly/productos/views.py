from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404

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
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'detalle.html', context={'producto': producto})


# Si no se quiere usar except
# try:
# except Producto.DoesNotExist:
# raise Http404()
from django.http import HttpResponse, JsonResponse

from productos.models import Producto


# Create your views here.
def index(request):
    productos = Producto.objects.all().values()
    return JsonResponse(list(productos), safe=False)


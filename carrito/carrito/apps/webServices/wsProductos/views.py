# Create your views here.
from django.http import HttpResponse
from carrito.apps.ventas.models import producto
#integramos la serializacion de los objetos
from django.core import serializers

def wsProductos_view(request):
	data = serializers.serialize("json",producto.objects.filter(status=True).order_by('-id'))
	#retorna la informacion json para obtener en formato xml solo se cambia el formato de json a xml
	return HttpResponse(data,mimetype='application/json')
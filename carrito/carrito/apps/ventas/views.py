from django.shortcuts import render_to_response
from django.template import RequestContext
from carrito.apps.ventas.forms import addProductForm
from carrito.apps.ventas.models import producto

def add_product_view(request):
	if request.method == "POST":
			form = addProductForm(request.POST)
			info = "Inicializando"
			if form.is_valid():
					nombre = form.cleaned_data['nombre']
					descripcion = form.cleaned_data['descripcion']
					p = producto()
					p.nombre = nombre
					p.descripcion = descripcion
					p.status = True
					p.save()
					info = "Datos guardados con exito :)"
			else:
				info = "Innformacion con datos incorrectos :("
			form = addProductForm()
			ctx = {'form':form, 'informacion':info}
			return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))

	else:
		form = addProductForm()
    	ctx = {'form':form}
    	return render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))

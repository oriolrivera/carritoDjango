#importamos la loibrerias de aceso de django
from django.shortcuts import render_to_response
from django.template import RequestContext
#impostamos la libreria models y traemos la clase productos para crear nuestra vista dinamica desde la db
from carrito.apps.ventas.models import producto
#importar el formulario creado
from carrito.apps.home.forms import ContactForm

#creamos nuestra vistas
def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje = 'Mensaje enviado desde mi vista'
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def productos_view(request):
	prod = producto.objects.filter(status=True)
	ctx = {'productos':prod}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def contacto_view(request):
	info_enviado = False
	email  = ""
	titulo = ""
	texto  = ""
	if request.method == "POST":
		formulario = ContactForm(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['Email']
			titulo = formulario.cleaned_data['Titulo']
			texto = formulario.cleaned_data['Texto']
	else:
		formulario = ContactForm()
	ctx = {'form':formulario, 'email':email,'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))
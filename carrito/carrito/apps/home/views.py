#importamos la loibrerias de aceso de django
from django.shortcuts import render_to_response
from django.template import RequestContext
#impostamos la libreria models y traemos la clase productos para crear nuestra vista dinamica desde la db
from carrito.apps.ventas.models import producto
#importar el formulario creado
from carrito.apps.home.forms import ContactForm, LoginForm
#libreria para enviar correo con estilo html
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
#libreria de paginacion django
from django.core.paginator import Paginator,EmptyPage,InvalidPage

#creamos nuestra vistas
def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje = 'Mensaje enviado desde mi vista'
	ctx = {'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))

def productos_view(request,pagina):
	#select * from ventas_productos where status = True ORDER BY id DESC
	lista_prod = producto.objects.filter(status=True).order_by('-id')
	paginator = Paginator(lista_prod,10)
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)
	ctx = {'productos':productos}
	return render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def singleProduct_view(request,id_prod):
	prod = producto.objects.get(id=id_prod)
	ctx = {'producto':prod}
	return render_to_response('home/singleProducto.html',ctx,context_instance=RequestContext(request))

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

			#configuracion de enviar correo
			to_admin = 'tucorrreo@gmail.com'
			html_content = "Imformacion recibida de %s<br><br><br>***Mensaje***<br><br>%s"%(email,texto)
			msg = EmailMultiAlternatives('Correo de contacto', html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') #define el content html
			msg.send() #enviar

	else:
		formulario = ContactForm()
	ctx = {'form':formulario, 'email':email,'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		     return HttpResponseRedirect('/')
	else:
     	     if request.method == "POST":
     	     	form = LoginForm(request.POST)
     	     	if form.is_valid():
     	     		username = form.cleaned_data['username']
     	     		password = form.cleaned_data['password']
     	     		usuario = authenticate(username=username,password=password)
     	     		if usuario is not None and usuario.is_active:
     	     			login(request,usuario)
     	     			return HttpResponseRedirect('/')
     	     		else:
     	     			mensaje = "Usuario y/o password icorrecto :("
             form = LoginForm()
             ctx = {'form':form, 'mensaje':mensaje}
             return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

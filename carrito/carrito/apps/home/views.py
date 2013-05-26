#importamos la loibrerias de aceso de django
from django.shortcuts import render_to_response
from django.template import RequestContext

#creamos nuestra vistas
def index_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
	return render_to_response('home/about.html',context_instance=RequestContext(request))
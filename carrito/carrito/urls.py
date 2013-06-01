from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrito.views.home', name='home'),
    # url(r'^carrito/', include('carrito.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #mis urls apps
    url(r'^', include('carrito.apps.home.urls')),
    url(r'^', include('carrito.apps.ventas.urls')),
    url(r'^', include('carrito.apps.webServices.wsProductos.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     #mi url de server de medias
     url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)

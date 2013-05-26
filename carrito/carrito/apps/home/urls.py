from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('carrito.apps.home.views',
        url(r'^$','index_view',name="vista_principal"),
        url(r'^about/$', 'about_view', name='vista_about'),
        url(r'^productos/$', 'productos_view', name='vista_productos'),

)
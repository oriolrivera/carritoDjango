from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('carrito.apps.ventas.views',
        url(r'^add/producto/$','add_product_view',name= "vista_agregar_producto"),
)
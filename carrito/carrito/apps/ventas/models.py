from django.db import models

# Create your models here.
class cliente(models.Model):
	       nombre         = models.CharField(max_length=50)
	       apellidos      = models.CharField(max_length=50)
	       status         = models.BooleanField(default=True)

	       def __unicode__(self):
	       	      nombreCompleto = "%s %s"%(self.nombre,self.apellidos)
	       	      return nombreCompleto
	       	      #retorna la concatenacion del nombre y el apellido para mostrar mas la descripcion del cliente en el panel

class producto(models.Model):
	def url(self,filename):
		ruta = "MultimediaData/producto/%s/%s"%(self.nombre,str(filename))
		return ruta

	nombre      = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=300)
	status      = models.BooleanField(default=True)
	imagen      = models.ImageField(upload_to=url,null=True,blank=True)
	precio      = models.DecimalField(max_digits=6,decimal_places=2)
	stock       = models.IntegerField()

	def __unicode__(self):
		return self.nombre
    	#retornar nombre del producto para presentar una descripcion en el panel
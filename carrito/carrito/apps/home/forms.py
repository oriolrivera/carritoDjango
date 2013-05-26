from django import forms
#importamos la libreria de formulario de django

class ContactForm(forms.Form):
	Email  = forms.EmailField(widget=forms.TextInput())
	Titulo = forms.CharField(widget=forms.TextInput())
	texto  = forms.CharField(widget=forms.Textarea())
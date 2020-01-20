from django import forms
from .models import Noticia, Area
from django.forms import ModelForm

class PostNoticia(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ('author', 'area', 'photo', 'title', 'text')


class PostArea(forms.ModelForm):
	class Meta:
		model = Area
		fields = ('descricao', 'cor', 'status')
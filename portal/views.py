from django.shortcuts import render, get_object_or_404, redirect
from .models import Noticia, Area
from django.utils import timezone
from . forms import PostNoticia, PostArea
# Create your views here.


def post_list(request):
	post = Area.objects.order_by('descricao')
	return render(request, 'portal/post_list.html', {'posts':post})


def post_detail(request,pk):	
	post = get_object_or_404(Area, pk=pk)
	return render(request, 'portal/post_detail.html', {'post':post})

def post_new(request):
	if request.method == "POST":
		form = PostArea(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			#post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostArea()
	return render(request, 'portal/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Area, pk=pk)
	if request.method == "POST":
		form = PostArea(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostArea(instance=post)
	return render(request, 'portal/post_edit.html', {'form': form})

def post_remove(requeste, pk):
	post = get_object_or_404(Area, pk=pk)
	post.delete()
	return redirect('post_list')
	
#aqui é a parte da noticia

def post_noticia(request):
	if request.method == "POST":
		form = PostNoticia(request.POST, request.FILES)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('post_detail_noticia', pk=post.pk)
	else:
		form = PostNoticia()
	return render(request, 'portal/post_edit_noticia.html', {'form': form})

def post_edit_noticia(request, pk):
	post = get_object_or_404(Noticia, pk=pk)
	if request.method == "POST":
		form = PostNoticia(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail_noticia', pk=post.pk)
	else:
		form = PostNoticia(instance=post)
	return render(request, 'portal/post_edit_noticia.html', {'form': form})

def post_remove_noticia(requeste, pk):
	post = get_object_or_404(Noticia, pk=pk)
	post.delete()
	return redirect('post_list_noticia')

def post_list_noticia(request):
	post = Noticia.objects.order_by('published_date')
	return render(request, 'portal/post_list_noticia.html', {'posts':post})

def post_detail_noticia(request, pk):
	post = get_object_or_404(Noticia, pk=pk)
	return render(request, 'portal/post_detail_noticia.html', {'post':post})

def post_publicar_noticia(request, pk):
	post = get_object_or_404(Noticia, pk=pk)
	if request.method=="POST":
		form = PostNoticia(request.POST, request.FILES, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail_noticia', pk=post.pk)
	else:
		form = PostNoticia(instance=post)
	return render(request, 'portal/post_edit_noticia.html', {'form': form})

def post_visitante(request):
	posts = Noticia.objects.all()
	areas = Area.objects.all()
	
	return render(request, 'portal/post_visitante.html', {'posts': posts, 'areas': areas}) 




'''def post_visitante(request):
	try:
		noticia_esporte = Noticia.objects.filter(area=area_verde)
		area_verde = Area.objects.get(cor="verde", status=True)	
	except:
		noticia_esporte = []

	try:
		noticia_politica = Noticia.objects.filter(area=area_vermelha)
		area_vermelha = Area.objects.get(cor="vermelha", status=True)	
	except:
		noticia_politica = []

	return render(request, 'portal/post_visitante.html', {'noticia_politica': noticia_politica, 'noticia_esporte': noticia_esporte})

'''
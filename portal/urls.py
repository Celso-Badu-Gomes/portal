from django.urls import path
from . import views

urlpatterns = [
	#path da area
	path('post_list/', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
	path('post/new', views.post_new, name='post_new'),
	path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/<pk>/remove/', views.post_remove, name='post_remove'),
	#patch da noticia
	path('', views.post_list_noticia, name='post_list_noticia'),
	path('post/noticia', views.post_noticia, name='post_noticia'),
	path('post/<int:pk>/detail_noticia', views.post_detail_noticia, name='post_detail_noticia'),
	path('post/<int:pk>/edit_noticia/', views.post_edit_noticia, name='post_edit_noticia'),
	path('post/<pk>/remove_noticia/', views.post_remove_noticia, name='post_remove_noticia'),
	path('post/<int:pk>/publicar_noticia/', views.post_publicar_noticia, name='post_publicar_noticia'),
	#path do visitante
	path('post_visitante', views.post_visitante, name='post_visitante'),
]
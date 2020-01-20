from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone


class Noticia(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    area = models.ForeignKey('Area', on_delete=models.SET_NULL, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Area(models.Model):
    descricao = models.CharField(max_length=200)
    cor = models.CharField(max_length=200)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.descricao

    def ativar(self):
        self.status=True
        self.save()

    def desativar(self):
        self.status=False
        self.save()
  
	

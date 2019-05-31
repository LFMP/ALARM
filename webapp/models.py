from django.db import models
from django.conf import settings

class Post(models.Model):
    ip = models.CharField(max_length=50)
    idUser = models.CharField(max_length=250)
    idClick = models.CharField(max_length=250, primary_key=True)
    classe = models.CharField(max_length=50)
    texto = models.TextField(max_length=250)
    current = models.CharField(max_length=250)
    href = models.CharField(max_length=250)
    timestamp = models.FloatField()
    dateTimestamp = models.IntegerField()
    dateR =  models.DateTimeField(auto_now = False, auto_now_add=True)

class Adapters(models.Model):
    rid = models.CharField(max_length=250,primary_key=True)
    ativo = models.IntegerField(default=0, choices={(1,0)})

class RecomendacaoAcessada(models.Model):
    rid = models.ForeignKey(Adapters,max_length=250, on_delete=models.CASCADE)
    idClick = models.ForeignKey(Post,max_length=250,on_delete=models.CASCADE)
    idRows = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
class RecomendacaoGerada(models.Model):
    rid = models.ForeignKey(Adapters,on_delete=models.CASCADE)
    idClick = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    idFileira = models.AutoField(primary_key=True)

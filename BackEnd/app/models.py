from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models

class Local(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    descricao = models.TextField()
    def __str__(self):
        return self.descricao

class Missao(models.Model):
    titulo = models.CharField(max_length=100)
    missao = models.TextField()
    descricao = models.TextField()
    respostaCorreta = models.CharField(max_length=150)
    figura = models.ImageField()
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
class Perfil(AbstractUser):
    
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True )
    dataNascimento = models.DateField()
    CEP = models.CharField(max_length=8)
    numero = models.CharField(max_length=10)
    endereco = models.CharField(max_length=400)
    telefone = models.CharField(max_length=11)
    foto = models.ImageField()


    def __str__(self):
        return self.username

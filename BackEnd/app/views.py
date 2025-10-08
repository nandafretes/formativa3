from django.shortcuts import render
from rest_framework import generics
from .serializers import PerfilSerializers, MissaoSerializers,LocalSerializers
from django.contrib.auth import get_user_model
from .models import Missao, Local
# Create your views here.

Perfil = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializers
class MissaoListCreateView(generics.ListCreateAPIView):
    queryset = Missao.objects.all()
    serializer_class = MissaoSerializers
class MissaoRetrUpdDes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Missao.objects.all()
    serializer_class = MissaoSerializers

class LocalListCreateView(generics.ListCreateAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializers
class LocalRetrUpdDes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Local.objects.all()
    serializer_class = LocalSerializers
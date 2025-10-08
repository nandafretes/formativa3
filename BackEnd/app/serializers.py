from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Missao, Local
Perfil = get_user_model()

class PerfilSerializers(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}  # <- isso oculta no HTML
    )

    class Meta:
        model = Perfil
        fields = ('id', 'username','nome','email',
                  'dataNascimento', 'password', 'foto', 'CEP', 
                  'numero','endereco','telefone')

    def create(self, validated_data):
        user = Perfil.objects.create(
            username=validated_data['username'],
            nome=validated_data['nome'],
            email=validated_data['email'],
            dataNascimento=validated_data['dataNascimento'],
            foto=validated_data['foto'],
            CEP=validated_data['CEP'],
            numero=validated_data['numero'],
            endereco=validated_data['endereco'],
            telefone=validated_data['telefone'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class MissaoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Missao
        fields = ('id','titulo','missao','descricao','respostaCorreta','figura', 'local')

class LocalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Local
        fields = ('id','latitude', 'longitude', 'descricao')
    


        
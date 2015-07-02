#-*- coding: utf-8 -*-
import json
from core.models import UnidadeFederativa, Cidade, Cinema, RegistroFilme
from rest_framework import serializers

class UfSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UnidadeFederativa
        fields = (u'nome', u'sigla')

class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        fields = (u'nome', u'uf')

class CinemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cinema
        fields = (u'nome', u'slug', u'cidade')

class RegistroFilmeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegistroFilme
        fields = (u'sala', u'filme', u'segunda', u'terca', u'quarta', u'quinta',
                  u'sexta', u'sabado', u'domingo', u'tres_d',)

    def to_representation(self, obj):
        retorno = super(RegistroFilmeSerializer, self).to_representation(obj)
        for i in (u'segunda', u'terca', u'quarta', u'quinta', u'sexta',
                  u'sabado', u'domingo'):
            retorno[i] = json.loads(retorno[i])

        return retorno

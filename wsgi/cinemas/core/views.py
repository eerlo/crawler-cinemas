#-*- coding: utf-8 -*-
from core.models import UnidadeFederativa, Cidade, Cinema, RegistroFilme
from core.serializers import UfSerializer, CidadeSerializer, CinemaSerializer, \
                             RegistroFilmeSerializer
from rest_framework import viewsets, filters
# Create your views here.

class UfViewSet(viewsets.ModelViewSet):
    queryset = UnidadeFederativa.objects.all()
    serializer_class = UfSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (u'slug', u'uf')

class CinemaViewSet(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
    filter_backends = (filters.DjangoFilterBackend,)

class RegistroFilmeViewSet(viewsets.ModelViewSet):
    queryset = RegistroFilme.objects.all()
    serializer_class = RegistroFilmeSerializer
    filter_backends = (filters.DjangoFilterBackend,)


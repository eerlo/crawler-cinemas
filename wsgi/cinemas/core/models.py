#-*- coding: utf-8 -*-
from django.db import models

class UnidadeFederativa(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome

class Cidade(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.ForeignKey(UnidadeFederativa, related_name=u'cidades')

    def __unicode__(self):
        return self.nome

class Cinema(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome

class RegistroFilme(models.Model):
    data = models.DateField()
    sala = models.CharField(max_length=50)
    filme = models.CharField(max_length=100)
    horarios = models.CharField(max_length=200)
    tres_d = models.BooleanField(default=False)
    cinema = models.ForeignKey(Cinema)

    def __unicode__(self):
        return u'%s - %s' % (self.cinema, self.filme)

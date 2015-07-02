#-*- coding: utf-8 -*-
from django.db import models
from django.db.models import signals
from django.template.defaultfilters import slugify

def slug_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)
def slug_filme_post_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(
          u'%s-%s-%s' % (slugify(instance.filme), slugify(instance.cinema.nome),
                        instance.pk))

class UnidadeFederativa(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    nome = models.CharField(max_length=200)
    sigla = models.CharField(max_length=2)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __unicode__(self):
        return self.nome
signals.pre_save.connect(slug_pre_save, sender=UnidadeFederativa)

class Cidade(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    nome = models.CharField(max_length=200)
    uf = models.ForeignKey(UnidadeFederativa, related_name=u'cidades')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __unicode__(self):
        return self.nome
signals.pre_save.connect(slug_pre_save, sender=Cidade)

class Cinema(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    nome = models.CharField(max_length=200)
    cidade = models.ForeignKey(Cidade, related_name=u'cinemas')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __unicode__(self):
        return self.nome
signals.pre_save.connect(slug_pre_save, sender=Cinema)

class RegistroFilme(models.Model):
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    sala = models.CharField(max_length=50)
    filme = models.CharField(max_length=100)
    tres_d = models.BooleanField(default=False)
    dub_leg = models.CharField(max_length=3)
    cinema = models.ForeignKey(Cinema, related_name=u'filmes')
    slug = models.SlugField(unique=True, blank=True, null=True)
    segunda = models.CharField(max_length=500)
    terca = models.CharField(max_length=500)
    quarta = models.CharField(max_length=500)
    quinta = models.CharField(max_length=500)
    sexta = models.CharField(max_length=500)
    sabado = models.CharField(max_length=500)
    domingo = models.CharField(max_length=500)

    def __unicode__(self):
        return u'%s - %s' % (self.cinema, self.filme)
signals.post_save.connect(slug_filme_post_save, sender=RegistroFilme)


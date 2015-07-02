# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('cidade', models.ForeignKey(related_name='cinemas', to='core.Cidade')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroFilme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('sala', models.CharField(max_length=50)),
                ('filme', models.CharField(max_length=100)),
                ('tres_d', models.BooleanField(default=False)),
                ('dub_leg', models.CharField(max_length=3)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
                ('segunda', models.CharField(max_length=500)),
                ('terca', models.CharField(max_length=500)),
                ('quarta', models.CharField(max_length=500)),
                ('quinta', models.CharField(max_length=500)),
                ('sexta', models.CharField(max_length=500)),
                ('sabado', models.CharField(max_length=500)),
                ('domingo', models.CharField(max_length=500)),
                ('cinema', models.ForeignKey(related_name='filmes', to='core.Cinema')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeFederativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
                ('nome', models.CharField(max_length=200)),
                ('sigla', models.CharField(max_length=2)),
                ('slug', models.SlugField(unique=True, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(related_name='cidades', to='core.UnidadeFederativa'),
        ),
    ]

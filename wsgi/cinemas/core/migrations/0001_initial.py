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
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroFilme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateField()),
                ('sala', models.CharField(max_length=50)),
                ('filme', models.CharField(max_length=100)),
                ('horarios', models.CharField(max_length=200)),
                ('tres_d', models.BooleanField(default=False)),
                ('cinema', models.ForeignKey(to='core.Cinema')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeFederativa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='cidade',
            name='uf',
            field=models.ForeignKey(related_name='cidades', to='core.UnidadeFederativa'),
        ),
    ]

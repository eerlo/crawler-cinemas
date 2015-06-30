#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from core.models import UnidadeFederativa
import logging

logger = logging.getLogger(u'atualizacao_dados')

class Command(BaseCommand):
    help = 'Atualiza todos os dados'

    def handle(self, *args, **options):
        logger.debug(u'Iniciando processo...')
        UnidadeFederativa.objects.create(nome=u'uf de teste')
        logger.debug(u'Processo Finalizado!')

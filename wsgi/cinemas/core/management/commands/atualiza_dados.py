#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from core.models import UnidadeFederativa
import logging
from core.crawlers import cinepolis, gnc

CRAWLERS = [cinepolis.CinepolisCaxiasDoSulCrawler,
            gnc.GNCCaxiasDoSulCrawler,]

logger = logging.getLogger(u'atualizacao_dados')
logger_erro = logging.getLogger(u'atualizacao_dados_erros')

class Command(BaseCommand):
    help = 'Atualiza todos os dados'

    def handle(self, *args, **options):
        logger.debug(u'Iniciando processo...')
        for crawler in CRAWLERS:
            logger.debug(u'Rodando processo %s' % crawler.slug_cinema)
            try:
                novos = crawler().processar()
            except Exception, exc:
                logger.error(exc)
                logger_erro.error(exc)
            else:
                if novos:
                    logger.debug('Resultado: %s' % str(novos))
                else:
                    logger.error('Problema ao processar dados do cinema')
                    logger_erro.error('Problema ao processar dados do cinema')
        logger.debug(u'Processo Finalizado!')


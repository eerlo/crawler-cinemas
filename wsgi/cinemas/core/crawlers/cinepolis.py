#-*- coding: utf-8 -*-
import json
from base import BaseCrawler


class CinepolisCrawler(BaseCrawler):
    css_lines = 'table.imprimir tr:not(:first-child):not(:last-child)'

    def _get_horario(self, string):
         if '-' in string:
            return string.split('-')[1].strip()
         else:
            return string.strip()

    def _get_horarios(self, string):
        horarios = []
        for i in string.split(','):
            horarios.append(self._get_horario(i))

        dias = {'segunda': [],
                'terca': [],
                'quarta': [],
                'quinta': [],
                'sexta': [],
                'sabado': [],
                'domingo': []}
        for i in horarios:
            if len(i) > 5:
                letra = i[-1]
                if letra.upper() == 'A':
                    dias['sabado'].append(i[:-1])
                    dias['domingo'].append(i[:-1])
                if letra.upper() == 'B':
                    for k in dias.keys():
                        if k <> 'quarta':
                            dias[k].append(i[:-1])
                if letra.upper() == 'C':
                    dias['quarta'].append(i[:-1])

            else:
                for k in dias.keys():
                    dias[k].append(i)
        return dias

    def get_data_dict(self, line):
        data = {}
        data['sala'] = line.cssselect('td:nth-child(1)')[0].text_content().strip()
        data['filme'] = line.cssselect('td:nth-child(2)')[0].text_content().replace('(3D)', '').strip()
        data['3d'] = '3D' in line.cssselect('td:nth-child(2)')[0].text_content().strip()
        data['classif'] = line.cssselect('td:nth-child(3)')[0].text_content().strip()
        data['dub_leg'] = 'DUB' if 'Dub' \
                  in line.cssselect('td:nth-child(4)')[0].text_content() else 'LEG'
        data[u'horarios'] = self._get_horarios(
                line.cssselect('td:nth-child(4)')[0].text_content())

        return data


class CinepolisCaxiasDoSulCrawler(CinepolisCrawler):
    url = 'http://www.cinepolis.com.br/programacao/imprimir.php?cc=12'
    slug_cinema = 'cinepolis-caxias-do-sul'

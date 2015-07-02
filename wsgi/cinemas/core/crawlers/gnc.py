#-*- coding: utf-8 -*-
import requests
from base import BaseCrawler
from datetime import datetime


class GNCCrawler(BaseCrawler):
    css_lines = 'table tr.programacao'


    def tira_espacos_duplos(self, string):
        while '  ' in string:
            string = string.replace('  ', ' ')
        return string

    def get_html(self):
        if not hasattr(self, 'html'):
            self.html = requests.post(self.url,
                                data={'cinema_id': self.cinema_id_post}).content
        return self.html

    def _get_horarios(self, string):
        horarios = [i.replace(':', 'h') for i in string.split(' ')]

        dias = {'segunda': [],
                'terca': [],
                'quarta': [],
                'quinta': [],
                'sexta': [],
                'sabado': [],
                'domingo': []}
        dias[dias.keys()[datetime.now().weekday()]] = horarios
        return dias

    def get_data_dict(self, line):
        data = {}
        tds = line.cssselect('td')
        data['sala'] = tds[0].text_content().strip().lower()\
                        .replace('sala', '').strip()
        data['filme'] = self.tira_espacos_duplos(tds[1].text_content().strip())
        data['3d'] = '3D' in tds[3].text_content().strip().upper()
        data['classif'] = \
            dict(tds[4].cssselect('img')[0].items())\
                ['src'].split('-anos')[0].split('/')[-1]
        dub_leg = tds[3].text_content().strip().upper()
        data['dub_leg'] = 'DUB' if 'DUB' in dub_leg or 'NAC' in dub_leg \
                          else 'LEG'
        data[u'horarios'] = self._get_horarios(tds[2].text_content().strip())

        return data


class GNCCaxiasDoSulCrawler(GNCCrawler):
    url = 'http://www.gnccinemas.com.br/index.php/home'
    cinema_id_post = '4'
    slug_cinema = 'gnc-caxias-do-sul'

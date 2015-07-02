#-*- coding: utf-8 -*-
import json
import requests
from lxml import html
from core.models import Cinema


class BaseCrawler(object):

    def __init__(self):
        super(BaseCrawler, self).__init__()
        self.cinema = Cinema.objects.get(slug=self.slug_cinema)

    def get_html(self):
        if not hasattr(self, 'html'):
            self.html = requests.get(self.url).content
        return self.html

    def get_parsed_html(self):
        if not hasattr(self, 'parsed_html'):
            self.parsed_html = html.fromstring(self.get_html())
        return self.parsed_html

    def get_lines(self):
        if not hasattr(self, 'lines'):
            self.lines = self.get_parsed_html().cssselect(self.css_lines)
        return self.lines

    def get_data_list(self):
        data = []
        for line in self.get_lines():
            data.append(self.get_data_dict(line))
        return data

    def processar(self):
        lista = self.get_data_list()
        if not lista:
            return None
        self.cinema.filmes.all().delete()
        criados = []
        for filme in lista:
            novo = self.cinema.filmes.create(
                sala=filme['sala'],
                filme=filme['filme'],
                tres_d=filme['3d'],
                dub_leg=filme[u'dub_leg'],
                segunda=json.dumps(filme['horarios']['segunda']),
                terca=json.dumps(filme['horarios']['terca']),
                quarta=json.dumps(filme['horarios']['quarta']),
                quinta=json.dumps(filme['horarios']['quinta']),
                sexta=json.dumps(filme['horarios']['sexta']),
                sabado=json.dumps(filme['horarios']['sabado']),
                domingo=json.dumps(filme['horarios']['domingo']),
            )
            criados.append(novo.pk)
        return criados

#-*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from core.views import UfViewSet, CidadeViewSet, CinemaViewSet, \
                       RegistroFilmeViewSet

router = routers.DefaultRouter()
router.register(r'ufs', UfViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'cinemas', CinemaViewSet)
router.register(r'filmes', RegistroFilmeViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]

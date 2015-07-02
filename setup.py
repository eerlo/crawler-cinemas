#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='cinemas',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='API de Horarios de cinemas',
    # GETTING-STARTED: set author name (your name):
    author='Eduardo Erlo',
    # GETTING-STARTED: set author email (your email):
    author_email='eduardo.erlo@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='https://pypi.python.org/pypi/',
    # GETTING-STARTED: define required django version:
    install_requires=['Django<=1.8', 'ipython', 'djangorestframework==3.1.3',
                      'requests==2.7.0', 'lxml==3.4.4', 'cssselect==0.9.1',
                      'django-filter==0.10.0'],
)

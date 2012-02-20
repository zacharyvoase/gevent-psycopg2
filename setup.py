#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages


setup(
    name='gevent-psycopg2',
    version='0.0.3',
    description='pip-installable package for patching psycopg2 to use gevent',
    author='Zachary Voase',
    author_email='z@dvxhouse.com',
    url='http://github.com/zacharyvoase/gevent-psycopg2',
    packages=find_packages(where='lib'),
    py_modules=['gevent_psycopg2'],
    package_dir={'': 'lib'},
    install_requires=[
        'gevent',
        'psycopg2>=2.2.0',
    ],
)

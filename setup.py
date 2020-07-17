#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import open
from setuptools import setup

"""
:authors: Duzive
:license: Apache License, Version 2.0, see LICENSE file
:copyright: (c) 2020 Duzive
"""


version = '1.0.0'

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'ccwrapper',
    version = version,

    author = 'Duzive',

    description=(
        u'ccwrapper - это python модуль для упрощённой работы с CatCoin API'
    ),
    
    long_description=  long_description,
    long_description_content_type = 'text/markdown',

    url = 'https://github.com/duzive/ccwrapper',
    download_url = f'https://github.com/duzive/ccwrapper/archive/v{version}.zip',

    license = 'Apache License, Version 2.0, see LICENSE file',

    packages = ['ccwrapper'],
    install_requires = ['requests'],

    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython',
    ]
)

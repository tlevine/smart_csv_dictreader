#!/usr/bin/env python3
from distutils.core import setup

import smart_csv_dictreader as s

setup(name='smart_csv_dictreader',
    author = 'Thomas Levine',
    author_email = '_@thomaslevine.com',
    description = 'Find the unique indices for a dataset',
    url = 'https://github.com/tlevine/special_snwoflake.git',
    classifiers = [
        'Intended Audience :: Developers',
    ],
    py_modules = ['smart_csv_dictreader'],
    install_requires = [],
    tests_require = ['nose'],
    version = s.__version__,
    license = 'AGPL',
)

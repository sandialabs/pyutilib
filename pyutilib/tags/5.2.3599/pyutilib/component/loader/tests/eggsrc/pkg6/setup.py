#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-

from setuptools import setup

setup(
    name = 'Package6',
    version = '0.1',
    packages = ['package6'],
    package_data = { 'package6': [ ] },

    author = 'Jane Doe',
    author_email = 'jdoe@dev.null',
    description = 'Package6 description.',
    license = 'BSD',
    keywords = 'package6 plugin',
    classifiers = [
        'Framework :: Package6',
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    #install_requires = ['PyUtilib==100.0'],

    entry_points = {
        'project1.plugins': [
            'package6.main = package6.unknown',
        ]
    }
)

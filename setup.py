#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import os.path
import sys

sys.path.insert(0, os.path.abspath('.'))
from i3py.version import __version__

setup(
    name='pyvisa-i3py-sim',
    description='Backend simulation for Pyvisa (inspired by i3py)',
    version=__version__,
    long_description='',
    author='Pyvisa-i3py-sim Developers (see AUTHORS)',
    author_email='m.dartiailh@gmail.com',
    url='http://github.com/MatthieuDartiailh/pyvisa-i3py-sim',
    download_url='http://github.com/MatthieuDartiailh/pyvisa-i3py-sim/tarball/master',
    keywords='instrument testing Python',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        ],
    zip_safe=False,
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_data={'': ['*.yaml']},
    requires=['future', 'pyvisa', 'funcsigs', 'stringparser'],
    install_requires=['future', 'funcsigs', 'stringparser'],
)

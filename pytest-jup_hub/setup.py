#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-jup_hub',
    version='0.1.0',
    author='Sheila Kahwai',
    author_email='sheilankw@gmail.com',
    maintainer='Sheila Kahwai',
    maintainer_email='sheilankw@gmail.com',
    license='BSD-3',
    url='https://github.com/Sheila-nk/pytest-jup_hub',
    description='"Simle re-usable JupyterHub pytest plugin"',
    long_description=read('README.rst'),
    py_modules=['pytest_jup_hub'],
    python_requires='>=3.5',
    install_requires=['pytest>=3.5.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'pytest11': [
            'jup_hub = pytest_jup_hub',
        ],
    },
    classifiers=["Framework :: Pytest"]
)

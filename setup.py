#!/usr/bin/env python
from setuptools import setup

requires = [
    'pelican>=3.1.1',
    'Markdown>=2.2.1'
]

setup(
    name='reinbach-pelican',
    version='1.0',
    description='Reinbach blog',
    author='Greg Reinbach',
    author_email='greg@reinbach.com',
    url='https://github.com/reinbach/reinbach-pelican',
    install_requires=requires,
)
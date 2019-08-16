# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in testing_module/__init__.py
from testing_module import __version__ as version

setup(
	name='testing_module',
	version=version,
	description='module of testing',
	author='Frappe',
	author_email='gerson.caballero@grintsys.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

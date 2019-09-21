#!/usr/bin/python3
# coding: utf-8

from setuptools import setup, find_packages, Extension

setup(name='pybynd',
      version='2.0.0',
      description='Python Beyondcoin library',
      keywords='bitcoin',
      url='https://github.com/Tech1k/pybynd',
      author='Alexsei Karpov',
      author_email='admin@bitaps.com',
      license='GPL-3.0',
      packages=find_packages(),
      install_requires=['pybtc'],
      include_package_data=True,
      package_data={
          'pybynd': ['bip39_word_list/*.txt', 'test/*.txt'],
      },
      test_suite='tests',
      ext_modules=[Extension("_scrypt",
                             ["pybynd/_scrypt/_scrypt.c", "pybynd/_scrypt/_scryptmodule.c"],
                             include_dirs=["pybynd/_scrypt/"])],
      zip_safe=False)

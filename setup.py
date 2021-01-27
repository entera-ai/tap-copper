#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-copper',
      version='0.0.1',
      description='Singer.io tap for extracting data from the Copper API',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_copper'],
      install_requires=[
          'tap-framework==0.0.4',
      ],
      extras_require={
        'dev': [
            'pylint',
            'ipdb',
            'nose'
        ]
      },
      entry_points='''
          [console_scripts]
          tap-copper=tap_copper:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_copper': [
              'schemas/*.json'
          ]
      })

# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

version = '0.1'
changes = open(join("docs", "HISTORY.txt")).read()
readme = open(
    join("src", "menhir", "contenttype", "rstdocument", "README.txt")).read()

tests_require = [
    'zope.component',
    'zope.publisher',
    ]

setup(name='menhir.contenttype.rstdocument',
      version=version,
      description="",
      long_description=readme + "\n" + changes,
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['menhir', 'menhir.contenttype'],
      include_package_data=True,
      zip_safe=False,
      tests_require = tests_require,
      extras_require = {'test': tests_require},
      install_requires=[
          'docutils',
          'dolmen.app.layout',
          'dolmen.app.security',
          'dolmen.content',
          'dolmen.file',
          'grokcore.view',
          'setuptools',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='menhir.contenttype.rstdocument',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
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
      install_requires=[
          'setuptools',
          'docutils',
          'dolmen.content',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
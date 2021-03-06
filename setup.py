from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='wb-project',
      version=version,
      description="WhereBee: Django project",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      maintainer='ElevenCraft Inc.',
      maintainer_email='matt@11craft.com',
      url='https://github.com/wherebee/wb-project/',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'South >= 0.7.3',
          # commented out because wb-inventory won't yet have been installed
          # if packages are being installed in parallel, as is the case with
          # some hosting providers such as ep.io
          ## 'wb-inventory',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

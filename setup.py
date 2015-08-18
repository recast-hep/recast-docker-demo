from setuptools import setup, find_packages

setup(
  name = 'recast-docker-demo',
  version = '0.0.1',
  description = 'recast-docker-demo',
  url = '',
  author = 'Lukas Heinrich',
  author_email = 'lukas.heinrich@cern.ch',
  packages = find_packages(),
  include_package_data = True,
  install_requires = [
    'Flask',
    'adage',
    'click',
    'pyyaml',
  ],
  dependency_links = [
  ]
)

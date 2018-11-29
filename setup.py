import re
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
for line in open(os.path.join(here, 'emu', '__init__.py')):
    if line.startswith('__version__'):
        version = re.match('__version__ ?= ?(.+)', line).group(1)
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

reqs = [line.strip() for line in open('requirements.txt')]
extra_reqs = [line.strip() for line in open('requirements_dev.txt')]

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
]

setup(name='emu',
      version=version,
      description='WPS processes for testing and demo',
      long_description=README + '\n\n' + CHANGES,
      classifiers=classifiers,
      author='Birdhouse',
      author_email='wps@dkrz.de',
      url='https://github.com/bird-house/emu',
      license="Apache License v2.0",
      keywords='wps pywps emu birdhouse',
      packages=find_packages(),
      include_package_data=True,
      install_requires=reqs,
      extra_requires=extra_reqs,
      entry_points={
          'console_scripts': [
             'emu=emu.cli:cli'
          ]
      },
      )

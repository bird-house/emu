import re
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

reqs = [line.strip() for line in open('requirements.txt')]
extra_reqs = [line.strip() for line in open('requirements_dev.txt')]

# copied from `requests`
about = {}
with open(os.path.join(here, 'emu', '__version__.py'), 'r') as f:
    exec(f.read(), about)

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
]

setup(name='emu',
      version=about['__version__'],
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

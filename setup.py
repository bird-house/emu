import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

reqs = [line.strip() for line in open('requirements/deploy.txt')]

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
]

setup(name='emu',
      version='0.5.0',
      description='WPS processes for testing and demo',
      long_description=README + '\n\n' + CHANGES,
      classifiers=classifiers,
      author='Birdhouse',
      author_email='',
      url='https://github.com/bird-house/emu',
      license="Apache License v2.0",
      keywords='wps pywps malleefowl emu conda birdhouse',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='emu',
      install_requires=reqs,
      entry_points={
          'console_scripts': []
      },
      )

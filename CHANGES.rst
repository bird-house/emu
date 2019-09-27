Changes
*******

0.11.0 (2019-09-27)
===================

This is the Bucharest release.

Changes:

* Skipped conda handling in Makefile (#91).
* Support WKT as input format in poly_centroid process (#49).
* Added input with multiple values (max_occurs > 1) (#89).

0.10.0 (2019-04-17)
===================

This is the San Francisco release.

Changes:

* Added example for Metalink as process output response (#84).
* Updated `inout` process with examples for AllowedValue, AnyValue and ValuesReference (#88, #85, #82).
* Using pywps `ProcessError` exception (#86)
* Added example process for *dry-run* usage (#83).
* Updated to latest cookiecutter template (#87).

0.9.1 (2018-12-04)
==================

This is the Washington release.

Changes:

* Using `emu.__version__.py` in `setup.py` (#67 and #68).
* Added Angle data type (#65).
* Added test for wps_multiple_outputs (#60).

0.9.0 (2018-09-06)
==================

This is the release for FOSS4G in Dar Es Salaam.

Changes:

* Enabled Conda support on ReadTheDocs (#40).
* Added ``ncmeta`` process with PyWPS OpenDAP support (#54).
* Added ``output_formats`` process to test NetCDF and JSON output formats (#42).
* Numerous fixes.

0.8.0 (2018-06-06)
==================

This is the first release without Buildout.
Is has a command-line interface ``emu`` to start/stop the PyWPS service using Werkzeug.

Changes:

* Removed Buildout configuration and relying only on Conda and Werkzeug.
* Support for Python 2.7/3.x (#6).
* Added templates for issues, PRs and contribution guide (#15).
* Use bumpversion (#36).
* Makefile with clean, install, start, stop and status targets (#35).
* Use staticmethod for PyWPS handler (#33).
* Using Click CLI to start/stop PyWPS service (#31).
* Using jinja template for pywps configuration (#29)

0.7.0 (2018-05-17)
==================

This is the last release using Buildout for deployment.
This release will be maintained on the 0.7.x branch.

Issues solved:

* Fix async mode in demo service (#26)
* Fix WSGI app initialisation (#17)
* Use six for Python 2/3 compatibility (#20)
* Reference Readme in Sphinx docs (#22)
* Move ``tests/`` folder to top-level directory (#21)
* Updated gunicorn 19.x (#19)

0.6.3 (2018-04-04)
==================

Issues solved:

* Clean up directory structure and files (#13)
* clean up of buildout and docker (#14)

Others:

* Updated buildout conda recipe 0.4.0.

0.6.2 (2018-02-07)
==================

* using pywps autodoc extension for Sphinx.
* added badges for chat, docs and license.
* fixed pywps output format.

0.6.1 (2018-01-10)
==================

* hello process: using keywords in metadata for description.
* updated dependencies.
* updated demo service.

0.6.0 (2017-08-16)
==================

* added esgf_demo process.
* added psycopg2 conda package for postgres
* added dill and drmaa package for scheduler.
* updated pywps recipe 0.9.2.
* added demo module.


0.5.3 (2017-05-18)
==================

* updated pywps recipe 0.9.0.
* added wsgi application.


0.5.2 (2017-05-08)
==================

* updated pywps recipe 0.8.8.
* updated supervisor recipe 0.3.6.
* updated zc.buildout 2.7.1
* update Makefile.
* enabled bbox parameter.
* using Metadata role attribute.
* updated say_hello process.
* added multiple_outputs process.
* updated conda recipe 0.3.6.


0.5.1 (2017-01-04)
==================

* added processes: nap, binaryoperator, show_error.
* updated pywps recipe 0.8.2.
* updated pywps 4.0.0.
* fixed wps_caps test.
* using __version__ constant.
* fixed install on ubuntu 16.04: updated conda env (lxml, icu).

0.5.0 (2016-12-07)
==================

* using pywps-4.
* updated all processes to pywps-4.
* updated Dockerfile.
* using docker-compose with environment from .env.

0.4.1 (2016-10-20)
==================

* fixed docs and comments.
* updated recipes, using conda-offline.

0.4.0 (2016-07-11)
==================

* using new buildout recipes.
* using conda environment.yml

0.3.2 (2016-07-11)
==================

* using pytest.

0.3.1 (2016-03-23)
==================

* added bbox process.

0.3.0 (2016-01-21)
==================

* removed malleefowl dependency.

0.2.2 (2016-01-07)
==================

* using pywps WPSProcess class.
* zonal-mean process added.
* docker-compose added.
* updated Dockerfile.
* updated pywps, supervisor and docker recipe.
* log to stderr/supervisor.

0.2.1 (2015-02-25)
==================

* updated docs and makefile.

0.2.0 (2015-02-24)
==================

* Now possible to use shared anaconda for installation.

0.1.2 (2014-11-24)
==================

* Using buildout 2.x.

0.1.1 (2014-11-11)
==================

* Using Makefile from birdhousebuilder.bootstrap to install and start application.


0.1.0 (2014-09-04)
==================

Initial Paris Release

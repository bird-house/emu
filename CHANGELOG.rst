=========
Changelog
=========

..
    `Unreleased <https://github.com/bird-house/emu>`_ (latest)
    ----------------------------------------------------------

    Contributors:

    Changes
    ^^^^^^^
    * No change.

    Fixes
    ^^^^^
    * No change.

.. _changes_1.0.0:

`v1.0.0 <https://github.com/bird-house/emu/tree/v1.0.0>`_ (2026-08-11)
----------------------------------------------------------------------

Contributors: Trevor James Smith

Changes
^^^^^^^
* `emu` now supports Python versions from 3.11 to 3.14. Older Python support has been dropped.
* For indexing reasons, the project has been named `birdhouse-emu`.
* Updated cookiecutter template version:
    * Dockerfile has been updated to use new base (`condaforge/miniforge3`) and `gunicorn` as well as use modern metadata conventions.
    * Project now uses `src` layout with `pyproject.toml` and `flit_core` as backend.
    * `emu` development and docs dependencies are now managed via `dependency-groups`.
    * `bump-my-version` is now configured to run build bumps on changes to `master`.
    * Linting now uses `ruff`, `codespell`, `vulture`, `zizmor` and other tools via `pre-commit`-compatible `prek`.
    * `CODE_OF_CONDUCT.md` is now present in project.
    * GitHub Workflows for automated deployment to PyPI deployment, docker testing, and labelling have been added.
    * `tox.toml` is now available for local testing purposes.
* Added a workflow for automatically accepting non-breaking changes originating from `Dependabot`.
* Moved all CI dependencies into `.github` to help de-clutter the top-level.
* Added a Docker Hub publishing workflow.

.. _changes_0.13.0:

`v0.13.0 <https://github.com/bird-house/emu/tree/v0.13.0>`_ (2023-11-30)
------------------------------------------------------------------------

Changes
^^^^^^^

* Fixed RTD docs build.
* Updated via cruft from cookiecutter.
* Updated PyWPS >=4.5.2,<4.7
* Added GitHub CI (#110).
* Added Geospatial process.
* Added a new recipe for installing Emu with GIS libraries (`pip install eum[gis]`).
* Added example geospatial data (raster image courtesy of USGS: `Mars MGS MOLA DEM 463m v2`).
* Refined Ultimate Question process to be truer to the source literature.

.. _changes_0.12.0:

0.12.0 (2020-10-07)
-------------------

Changes
^^^^^^^

* Updated from cookiecutter template (#103, #105, #106).
* Added Translation process (#102).
* Added thredds to docker-compose as DAP server (#99).
* Added process creating NcML file aggregating netCDF files (#97).

.. _changes_0.11.1:

0.11.1 (2020-01-03)
-------------------

Changes
^^^^^^^

* pin PyWPS 4.2.x (#94).

.. _changes_0.11.0:

0.11.0 (2019-09-27)
-------------------

This is the Bucharest release.

Changes
^^^^^^^

* Skipped conda handling in Makefile (#91).
* Support WKT as input format in poly_centroid process (#49).
* Added input with multiple values (max_occurs > 1) (#89).

.. _changes_0.10.0:

0.10.0 (2019-04-17)
-------------------

This is the San Francisco release.

Changes
^^^^^^^

* Added example for Metalink as process output response (#84).
* Updated `inout` process with examples for AllowedValue, AnyValue and ValuesReference (#88, #85, #82).
* Using pywps `ProcessError` exception (#86)
* Added example process for *dry-run* usage (#83).
* Updated to latest cookiecutter template (#87).

.. _changes_0.9.1:

0.9.1 (2018-12-04)
-------------------

This is the Washington release.

Changes
^^^^^^^

* Using `emu.__version__.py` in `setup.py` (#67 and #68).
* Added Angle data type (#65).
* Added test for wps_multiple_outputs (#60).

.. _changes_0.9.0:

0.9.0 (2018-09-06)
------------------

This is the release for FOSS4G in Dar Es Salaam.

Changes
^^^^^^^

* Enabled Conda support on ReadTheDocs (#40).
* Added ``ncmeta`` process with PyWPS OpenDAP support (#54).
* Added ``output_formats`` process to test NetCDF and JSON output formats (#42).
* Numerous fixes.

.. _changes_0.8.0:

0.8.0 (2018-06-06)
------------------

This is the first release without Buildout.
Is has a command-line interface ``emu`` to start/stop the PyWPS service using Werkzeug.

Changes
^^^^^^^

* Removed Buildout configuration and relying only on Conda and Werkzeug.
* Support for Python 2.7/3.x (#6).
* Added templates for issues, PRs and contribution guide (#15).
* Use bumpversion (#36).
* Makefile with clean, install, start, stop and status targets (#35).
* Use staticmethod for PyWPS handler (#33).
* Using Click CLI to start/stop PyWPS service (#31).
* Using jinja template for pywps configuration (#29)

.. _changes_0.7.0:

0.7.0 (2018-05-17)
------------------

This is the last release using Buildout for deployment.
This release will be maintained on the 0.7.x branch.

Issues solved
^^^^^^^^^^^^^

* Fix async mode in demo service (#26)
* Fix WSGI app initialisation (#17)
* Use six for Python 2/3 compatibility (#20)
* Reference Readme in Sphinx docs (#22)
* Move ``tests/`` folder to top-level directory (#21)
* Updated gunicorn 19.x (#19)

.. _changes_0.6.3:

0.6.3 (2018-04-04)
------------------

Issues solved
^^^^^^^^^^^^^

* Clean up directory structure and files (#13)
* clean up of buildout and docker (#14)

Others
^^^^^^

* Updated buildout conda recipe 0.4.0.

.. _changes_0.6.2:

0.6.2 (2018-02-07)
------------------

Changes
^^^^^^^

* using pywps autodoc extension for Sphinx.
* added badges for chat, docs and license.
* fixed pywps output format.

.. _changes_0.6.1:

0.6.1 (2018-01-10)
------------------

Changes
^^^^^^^

* hello process: using keywords in metadata for description.
* updated dependencies.
* updated demo service.

.. _changes_0.6.0:

0.6.0 (2017-08-16)
------------------

Changes
^^^^^^^

* added esgf_demo process.
* added psycopg2 conda package for postgres
* added dill and drmaa package for scheduler.
* updated pywps recipe 0.9.2.
* added demo module.

.. _changes_0.5.3:

0.5.3 (2017-05-18)
------------------

Changes
^^^^^^^

* updated pywps recipe 0.9.0.
* added wsgi application.

.. _changes_0.5.2:

0.5.2 (2017-05-08)
------------------

Changes
^^^^^^^

* updated pywps recipe 0.8.8.
* updated supervisor recipe 0.3.6.
* updated zc.buildout 2.7.1
* update Makefile.
* enabled bbox parameter.
* using Metadata role attribute.
* updated say_hello process.
* added multiple_outputs process.
* updated conda recipe 0.3.6.

.. _changes_0.5.1:

0.5.1 (2017-01-04)
------------------

Changes
^^^^^^^

* added processes: nap, binaryoperator, show_error.
* updated pywps recipe 0.8.2.
* updated pywps 4.0.0.
* fixed wps_caps test.
* using __version__ constant.
* fixed install on ubuntu 16.04: updated conda env (lxml, icu).

.. _changes_0.5.0:

0.5.0 (2016-12-07)
------------------

Changes
^^^^^^^

* using pywps-4.
* updated all processes to pywps-4.
* updated Dockerfile.
* using docker-compose with environment from .env.

.. _changes_0.4.1:

0.4.1 (2016-10-20)
------------------

Changes
^^^^^^^

* fixed docs and comments.
* updated recipes, using conda-offline.

.. _changes_0.4.0:

0.4.0 (2016-07-11)
------------------

Changes
^^^^^^^

* using new buildout recipes.
* using conda environment.yml

.. _changes_0.3.2:

0.3.2 (2016-07-11)
------------------

Changes
^^^^^^^

* using pytest.

.. _changes_0.3.1:

0.3.1 (2016-03-23)
------------------

Changes
^^^^^^^

* added bbox process.

.. _changes_0.3.0:

0.3.0 (2016-01-21)
------------------

Changes
^^^^^^^

* removed malleefowl dependency.

.. _changes_0.2.2:

0.2.2 (2016-01-07)
------------------

Changes
^^^^^^^

* using pywps WPSProcess class.
* zonal-mean process added.
* docker-compose added.
* updated Dockerfile.
* updated pywps, supervisor and docker recipe.
* log to stderr/supervisor.

.. _changes_0.2.1:

0.2.1 (2015-02-25)
------------------

Changes
^^^^^^^

* updated docs and makefile.

.. _changes_0.2.0:

0.2.0 (2015-02-24)
------------------

Changes
^^^^^^^

* Now possible to use shared anaconda for installation.

.. _changes_0.1.2:

0.1.2 (2014-11-24)
------------------

Changes
^^^^^^^

* Using buildout 2.x.

.. _changes_0.1.1:

0.1.1 (2014-11-11)
------------------

Changes
^^^^^^^

* Using Makefile from birdhousebuilder.bootstrap to install and start application.

.. _changes_0.1.0:

0.1.0 (2014-09-04)
------------------

Initial Paris Release

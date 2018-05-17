.. _devguide:

Developer Guide
===============

.. contents::
    :local:
    :depth: 1

.. _testing:

Running tests
-------------

Run tests using `pytest`_.

First activate the ``emu`` Conda environment and install ``pytest``.

.. code-block:: sh

   $ cd emu
   $ source activate emu
   $ conda install pytest flake8  # if not already installed

Run quick tests (skip slow and online):

.. code-block:: sh

    $ pytest -m 'not slow and not online'"

Run all tests:

.. code-block:: sh

    $ pytest

Check pep8:

.. code-block:: sh

    $ flake8

Run tests the lazy way
----------------------

Do the same as above using the ``Makefile``.

.. code-block:: sh

    $ make test
    $ make testall
    $ make pep8


.. _pytest: https://docs.pytest.org/en/latest/

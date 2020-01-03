.. _installation:

Installation
============

Install from Conda
------------------

.. image:: http://anaconda.org/birdhouse/emu/badges/installer/conda.svg
   :target: http://anaconda.org/birdhouse/emu
   :alt: Ananconda Install

.. image:: http://anaconda.org/birdhouse/emu/badges/build.svg
   :target: http://anaconda.org/birdhouse/emu
   :alt: Anaconda Build

.. image:: http://anaconda.org/birdhouse/emu/badges/version.svg
   :target: http://anaconda.org/birdhouse/emu
   :alt: Anaconda Version

.. image:: http://anaconda.org/birdhouse/emu/badges/downloads.svg
   :target: http://anaconda.org/birdhouse/emu
   :alt: Anaconda Downloads

Install the ``emu`` Conda package:

.. code-block:: console

    $ conda install -c birdhouse -c conda-forge emu
    $ emu --help


Install from GitHub
-------------------

Check out code from the Emu GitHub repo and start the installation:

.. code-block:: console

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu

Create Conda environment named `emu`:

.. code-block:: console

   $ conda env create -f environment.yml
   $ source activate emu

Install `emu` app:

.. code-block:: console

  $ pip install -e .
  OR
  make install

For development you can use this command:

.. code-block:: console

  $ pip install -e .[dev]
  OR
  $ make develop

Start PyWPS service
-------------------

After successful installation you can start the service using the ``pywps`` command-line.

.. code-block:: console

   # show help
   $ pywps -h

   # start service with default configuration (pywps.cfg)
   $ pywps -c pywps.cfg start

The deployed WPS service is by default available on:

http://localhost:5000/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors:

.. code-block:: console

   $ tail -f pywps.log

... or do it the lazy way
+++++++++++++++++++++++++

You can also use the ``Makefile`` to start and the service:

.. code-block:: console

  $ make start
  $ tail -f pywps.log

Run Emu as Docker container
---------------------------

You can also run Emu as a Docker container, see the :ref:`Tutorial <tutorial>`.

Use Ansible to deploy Emu on your System
----------------------------------------

Use the `Ansible playbook`_ for PyWPS to deploy Emu on your system.

.. _Ansible playbook: http://ansible-wps-playbook.readthedocs.io/en/latest/index.html

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

.. code-block:: sh

    $ conda install -c birdhouse -c conda-forge emu
    $ emu --help


Install from GitHub
-------------------

Check out code from the Emu GitHub repo and start the installation:

.. code-block:: sh

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ conda env create -f environment.yml
   $ source activate emu
   $ python setup.py develop

... or do it the lazy way
+++++++++++++++++++++++++

The previous installation instructions assume you have Anaconda installed.
We provide also a ``Makefile`` to run this installation without additional steps:

.. code-block:: sh

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ make clean    # cleans up a previous Conda environment
   $ make install  # installs Conda if necessary and runs the above installation steps

Start Emu PyWPS service
-----------------------

After successful installation you can start the service using the ``emu`` command-line.

.. code-block:: sh

   $ emu start --help # show help
   $ emu start       # start service with default configuration

   OR

   $ emu start --daemon # start service as daemon
   loading configuration
   forked process id: 42

The deployed WPS service is by default available on:

http://localhost:5000/wps?service=WPS&version=1.0.0&request=GetCapabilities.

.. NOTE:: Remember the process ID (PID) so you can stop the service with ``kill PID``.

You can find which process uses a given port using the following command (here for port 5000):

.. code-block:: sh

   $ netstat -nlp | grep :5000

Check the log files for errors:

.. code-block:: sh

   $ tail -f  pywps.log

... or do it the lazy way
+++++++++++++++++++++++++

You can also use the ``Makefile`` to start and stop the service:

.. code-block:: sh

  $ make start
  $ make status
  $ tail -f pywps.log
  $ make stop

Run Emu as Docker container
---------------------------

You can also run Emu as a Docker container, see the :ref:`Tutorial <tutorial>`.

Use Ansible to deploy Emu on your System
----------------------------------------

Use the `Ansible playbook`_ for PyWPS to deploy Emu on your system.
Follow the `example`_ for Emu given in the playbook.

Building the docs
-----------------

First install dependencies for the documentation::

  $ make bootstrap_dev
  $ make docs

.. _Ansible playbook: http://ansible-wps-playbook.readthedocs.io/en/latest/index.html
.. _example: http://ansible-wps-playbook.readthedocs.io/en/latest/tutorial.html

.. _devguide:

Developer Guide
===============

.. contents::
    :local:
    :depth: 1

.. _testing:

Running unit tests
---------------------------------------

Run quick tests::

    $ make test

Run all tests (slow, online)::

    $ make testall

Check pep8::

    $ make pep8

.. _wps_test_env:

Running WPS service in test environment
---------------------------------------

For development purposes you can run the WPS service without nginx and supervisor.
Use the following instructions:

.. code-block:: sh

    # get the source code
    $ git clone https://github.com/bird-house/emu.git
    $ cd emu

    # create conda environment
    $ conda env create -f environment.yml

    # activate conda environment
    $ source activate emu

    # install emu code into conda environment
    $ python setup.py develop

    # start the WPS service
    $ emu

    # open your browser on the default service url
    $ firefox http://localhost:5000/wps

    # ... and service capabilities url
    $ firefox http://localhost:5000/wps?service=WPS&request=GetCapabilities

The ``emu`` service command-line has more options:

.. code-block:: sh

    $ emu -h

For example you can start the WPS with enabled debug logging mode:

.. code-block:: sh

    $ emu --debug

Or you can overwrite the default `PyWPS`_ configuration by providing your own
PyWPS configuration file (just modifiy the options you want to change):

.. code-block:: sh

    # edit your local pywps configuration file
    $ cat mydev.cfg
    [logging]
    level = WARN
    file = /tmp/mydev.log

    # start the service with this configuration
    $ emu -c mydev.cfg

.. _PyWPS: http://pywps.org/

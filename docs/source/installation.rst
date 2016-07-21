.. _installation:

Installation
============

The installation is using the Python distribution system `Anaconda`_ to maintain software dependencies. 
Anaconda will be installed during the installation processes in your home directory ``~/anaconda``.
 
The installation process setups a conda environment named ``emu`` with all dependent conda (and pip) packages. The installation folder (for configuration files etc) is by default ``~/birdhouse``. Configuration options can be overriden in the buildout ``custom.cfg`` file.

Now, check out the emu code from GitHub and start the installation:

.. code-block:: sh

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ make clean install

After successful installation you need to start the services:

.. code-block:: sh

   $ make start  # starts supervisor services
   $ make status # shows supervisor status

The depolyed WPS service is available on http://localhost:8094/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors::

   $ tail -f  ~/birdhouse/var/log/pywps/emu.log

You will find more information about the installation in the `Makefile documentation <http://birdhousebuilderbootstrap.readthedocs.io/en/latest/>`_.

Start Emu with docker-compose
-----------------------------

Run Emu with mapped ports (8094) on localhost:

.. code-block:: sh

    $ docker-compose run --service-ports -e HOSTNAME=localhost emu

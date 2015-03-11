.. _installation:

.. _`Anaconda`: http://www.continuum.io/

Installation
============

The installation is using the Python distribution system `Anaconda`_ to maintain software dependencies. 
You may use an existing (shared, read-only access possible) Anaconda installation. For this set an environment variable to the location of your existing Anaconda, for example::

   $ export ANACONDA_HOME=/opt/anaconda

If Anaconda is not available then a minimal Anaconda will be installed during the installation processes in your home directory ``~/anaconda``. 

The installation process setups a conda environment named ``birdhouse``. All additional packages and configuration files are going into this conda environment. The location is ``~/.conda/envs/birdhouse``.

Now, check out the emu code from github and start the installation::

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ make

After successful installation you need to start the services. All installed files (config etc ...) are below the conda environment ``birdhouse`` which is by default in your home directory ``~/.conda/envs/birdhouse``. Now, start the services::

   $ make start  # starts supervisor services
   $ make status # shows supervisor status

The depolyed WPS service is available on http://localhost:8094/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors::

   $ cd ~/.conda/envs/birdhouse
   $ tail -f  var/log/pywps/emu.log
   $ tail -f  var/log/pywps/emu_trace.log

You will find more information about the installation in the `Makefile documentation <http://birdhousebuilderbootstrap.readthedocs.org/en/latest/>`_.

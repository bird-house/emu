Emu
===

Emu (the bird)
  *Emus are curious birds who are known to follow and watch other animals and humans. Emus do not sleep continuously at night but in several short stints sitting down. [..].* (`Wikipedia https://en.wikipedia.org/wiki/Emu`_).


Emu is a Python package with some test proccess for  Web Processing Services (WPS). Currently it is using the `PyWPS https://github.com/geopython/PyWPS`_ server.

Installation
------------

Check out code from the emu github repo and start the installation::

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ ./requirements.sh
   $ ./install.sh


After successful installation you need to start the services. Emu is using `Anaconda http://www.continuum.io/`_ Python distribution system. All installed files (config etc ...) are below the Anaconda root folder which is by default in your home directory ``~/anaconda``. Now, start the services::

   $ cd ~/anaconda
   $ etc/init.d/supervisor start
   $ etc/init.d/nginx start

The depolyed WPS service is available on http://localhost:8094/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors::

   $ tail -f  ~/anaconda/var/log/pywps/emu.log
   $ tail -f  ~/anaconda/var/log/pywps/emu_trace.log

Configuration
-------------

If you want to run on a different hostname or port then change the default values in ``custom.cfg``::

   $ cd emu
   $ vim custom.cfg
   $ cat custom.cfg
   [settings]
   hostname = localhost
   http-port = 8094

After any change to your ``custom.cfg`` you **need** to run ``install.sh`` again and restart the ``supervisor`` service::

  $ ./install.sh
  $  ~/anaconda/etc/init.d/supervisor restart


Update
------

When updating your installation you may run ``clean.sh`` to remove outdated Python dependencies::

   $ cd emu
   $ git pull
   $ ./clean.sh
   $ ./requirement.sh
   $ ./install.sh

And then restart the ``supervisor`` and ``nginx`` service.


Authors
-------

* `DKRZ http://www.dkrz.de`_
* `Climate Service Center http://www.climate-service-center.de/`_
* `IPSL http://www.ipsl.fr/`_




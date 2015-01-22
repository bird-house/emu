Emu
===

Emu (the bird)
  *Emus are curious birds who are known to follow and watch other animals and humans. Emus do not sleep continuously at night but in several short stints sitting down. [..].* (`Wikipedia <https://en.wikipedia.org/wiki/Emu>`_).


Emu is a Python package with some test proccess for  Web Processing Services (WPS). Currently it is using the `PyWPS <https://github.com/geopython/PyWPS>`_ server.

Installation
------------

Check out code from the emu github repo and start the installation::

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ make


After successful installation you need to start the services. Emu is using `Anaconda <http://www.continuum.io/>`_ Python distribution system. All installed files (config etc ...) are below the Anaconda root folder which is by default in your home directory ``~/anaconda``. Now, start the services::

   $ make start  # starts supervisor services
   $ make status # shows supervisor status

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

After any change to your ``custom.cfg`` you **need** to run ``make install`` again and restart the ``supervisor`` service::

  $ make install
  $ make restart


Example: Using Docker
---------------------

If you just want to try the Emu Web Processing Service you can also use the `Docker https://www.docker.com`_ image::

  $ docker run -i -d -p 9001:9001 -p 8090:8090 -p 8094:8094 --name=emu_wps birdhouse/emu

Check the docker logs::

  $ docker logs emu_wps

Show running docker containers::

  $ docker ps

Open your browser and enter the url of the supervisor service:: 

  http://localhost:9001

Run a GetCapabilites WPS request::

  http://localhost:8094/wps?service=WPS&version=1.0.0&request=getcapabilities

Run DescribeProcess WPS request for *Hello World*::

  http://localhost:8094/wps?service=WPS&version=1.0.0&request=describeprocess&identifier=helloworld

Execute *Hello World* process with you user name::

  http://localhost:8094/wps?service=WPS&version=1.0.0&request=execute&identifier=helloworld&DataInputs=user=Pingu

Install *Birdy* WPS command line tool from Anaconda (Anaconda needs to be installed and in your ``PATH``)::

  $ conda install -c https://conda.binstar.org/birdhouse birdhouse-birdy

Use Birdy to access Emu WPS service::

  $ export WPS_SERVICE=http://localhost:8094/wps
  $ birdy -h
  $ birdy helloworld -h
  $ birdy helloworld --user Pingu

Stop and remove docker container::

  $ docker stop emu_wps
  $ docker rm emu_wps

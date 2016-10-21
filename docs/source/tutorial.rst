.. _tutorial:

Example: Using Docker
=====================

If you just want to try the Emu Web Processing Service you can also use the `Docker <https://hub.docker.com/r/birdhouse/emu/>`_ image:

.. code-block:: sh

  $ docker run -i -d -p 8080:8080 -p 8000:8000 -p 9001:9001 --name=emu birdhouse/emu

Check the docker logs:

.. code-block:: sh

  $ docker logs emu

Show running docker containers:

.. code-block:: sh

  $ docker ps

Run a GetCapabilites WPS request:

  http://localhost:8080/wps?service=WPS&version=1.0.0&request=getcapabilities

Run DescribeProcess WPS request for *Hello*:

  http://localhost:8080/wps?service=WPS&version=1.0.0&request=describeprocess&identifier=hello

Execute *Hello* process with you user name:

  http://localhost:8080/wps?service=WPS&version=1.0.0&request=execute&identifier=hello&DataInputs=name=Pingu

Install *Birdy* WPS command line tool from Anaconda (Anaconda needs to be installed and in your ``PATH``):

.. code-block:: sh

  $ conda install -c birdhouse birdhouse-birdy

Use Birdy to access Emu WPS service:

.. code-block:: sh

  $ export WPS_SERVICE=http://localhost:8080/wps
  $ birdy -h
  $ birdy hello -h
  $ birdy hello --name Pingu

Stop and remove docker container:

.. code-block:: sh

  $ docker stop emu_wps
  $ docker rm emu_wps

Using docker-compose
--------------------

You can also start the docker container with ``docker-compose``:

.. code-block:: sh

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ docker-compose up -d
   $ docker-compose logs emu

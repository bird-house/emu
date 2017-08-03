.. _using_docker_tutorial:

Tutorial: using Docker
======================

Emu WPS is available as docker image. You can download the docker image from `DockerHub <https://hub.docker.com/r/birdhouse/emu/>`_
or build it from the provided Dockerfile.

Start the container with the following command:

.. code-block:: sh

  $ docker run -i -d -p 8080:8080 -p 8000:8000 -p 9001:9001 --name=emu birdhouse/emu

The ports are:

  * PyWPS port: 8080
  * NGINX file service port for the outputs: 8000
  * Supervisor port: 9001 (optional)

You can map the container port also to another port on your machine, for example: ``-p 8094:8080``
(your machine port=8094, container port=8080).

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

Use `docker-compose <https://docs.docker.com/compose/install/>`_ (you need a recent version > 1.7) to start the container:

.. code-block:: sh

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ docker-compose up -d
   $ docker-compose logs emu

You can change the ports and hostname with environment variables:

.. code-block:: sh

   $ HOSTNAME=emu HTTP_PORT=8094 SUPERVISOR_PORT=48094 docker-compose up

Now the WPS is available on port 8094: http://emu:8094/wps?service=WPS&version=1.0.0&request=GetCapabilities.

You can also customize the ``docker-compose.yml`` file.
See the `docker-compose documentation <https://docs.docker.com/compose/environment-variables/>`_.

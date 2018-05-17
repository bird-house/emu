.. _using_docker_tutorial:

Tutorial: using Docker
======================

Emu WPS is available as docker image. You can download the docker image from `DockerHub`_
or build it from the provided Dockerfile.

Start the container with the following command:

.. code-block:: sh

  $ docker run -d -p 5000:5000 --name=emu birdhouse/emu

It is using the port 5000 for the PyWPS service and also to access the WPS outputs.

You can map the container port also to another port on your machine, for example: ``-p 8094:5000``
(your machine port=8094, container port=5000).

Check the docker logs:

.. code-block:: sh

  $ docker logs emu

Show running docker containers:

.. code-block:: sh

  $ docker ps

Run a GetCapabilites WPS request:

  http://localhost:5000/wps?service=WPS&version=1.0.0&request=getcapabilities

Run DescribeProcess WPS request for *Hello*:

  http://localhost:5000/wps?service=WPS&version=1.0.0&request=describeprocess&identifier=hello

Execute *Hello* process with you user name:

  http://localhost:5000/wps?service=WPS&version=1.0.0&request=execute&identifier=hello&DataInputs=name=Pingu

Install *Birdy* WPS command line tool from Conda:

.. code-block:: sh

  $ conda install -c birdhouse birdhouse-birdy

Use Birdy to access Emu WPS service:

.. code-block:: sh

  $ export WPS_SERVICE=http://localhost:5000/wps
  $ birdy -h
  $ birdy hello -h
  $ birdy hello --name Pingu

Stop and remove docker container:

.. code-block:: sh

  $ docker stop emu

Using docker-compose
--------------------

Use `docker-compose`_ (you need a recent version > 1.7) to start the container:

.. code-block:: sh

   $ git clone https://github.com/bird-house/emu.git
   $ cd emu
   $ docker-compose up -d
   $ docker-compose logs emu

Execute ``tail`` command in the running container to see the logs::

  $ docker ps   # get the container name
  NAMES
  emu_emu_1
  $ docker exec -it emu_emu_1 tail -f /opt/wps/pywps.log

You can customize the ``docker-compose.yml`` file.
See the `docker-compose documentation`_.

Stop the container with:

.. code-block:: sh

  $ docker-compose down

Build image using docker-compose
--------------------------------

You can build locally a new docker image from the Dockerfile by running docker-compose:

.. code-block:: sh

    $ docker-compose build

.. _DockerHub: https://hub.docker.com/r/birdhouse/emu/
.. _docker-compose: https://docs.docker.com/compose/install/
.. _docker-compose documentation: https://docs.docker.com/compose/environment-variables/

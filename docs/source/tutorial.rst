.. _tutorial:

Example: Using Docker
=====================

If you just want to try the Emu Web Processing Service you can also use the `Docker <https://hub.docker.com/r/birdhouse/emu/>`_ image::

  $ docker run -i -d -p 38094:38094 -p 8094:8094 --name=emu_wps birdhouse/emu

Check the docker logs::

  $ docker logs emu_wps

Show running docker containers::

  $ docker ps

Run a GetCapabilites WPS request:

  http://localhost:8094/wps?service=WPS&version=1.0.0&request=getcapabilities

Run DescribeProcess WPS request for *Hello World*:

  http://localhost:8094/wps?service=WPS&version=1.0.0&request=describeprocess&identifier=helloworld

Execute *Hello World* process with you user name:

  http://localhost:8094/wps?service=WPS&version=1.0.0&request=execute&identifier=helloworld&DataInputs=user=Pingu

Install *Birdy* WPS command line tool from Anaconda (Anaconda needs to be installed and in your ``PATH``)::

  $ source activate birdhouse # activate birdhouse environment (optional)
  $ conda install -c birdhouse birdhouse-birdy

Use Birdy to access Emu WPS service::

  $ export WPS_SERVICE=http://localhost:8094/wps
  $ birdy -h
  $ birdy helloworld -h
  $ birdy helloworld --user Pingu

Stop and remove docker container::

  $ docker stop emu_wps
  $ docker rm emu_wps


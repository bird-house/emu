.. _configuration:

Configuration
=============


Use a custom configuration file
-------------------------------

You can overwrite the default `PyWPS`_ configuration by providing your own
PyWPS configuration file.
Use the existing ``pywps.cfg`` file as example and copy it to ``custom.cfg``.

For example change the hostname (*demo.org*) and logging level:

.. code-block:: sh

   $ cd emu
   $ cp pywps.cfg custom.cfg
   $ vim custom.cfg
   $ cat custom.cfg
   [server]
   url = http://demo.org:5000/wps
   outputurl = http://demo.org:5000/outputs

   [logging]
   level = DEBUG

Start the service with your custom configuration:

.. code-block:: sh

   # start the service with this configuration
   $ pywps -c custom.cfg start


.. _PyWPS: http://pywps.org/

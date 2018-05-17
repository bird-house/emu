.. _configuration:

Configuration
=============

You can overwrite the default `PyWPS`_ configuration by providing your own
PyWPS configuration file (just modifiy the options you want to change).
Use one of the existing ``sample-*.cfg`` files as example and copy them to ``etc/custom.cfg``.

For example change the hostname (*demo.org*) and logging level:

.. code-block:: sh

   $ cd emu
   $ vim etc/custom.cfg
   $ cat etc/custom.cfg
   [server]
   url = http://demo.org:5000/wps
   outputurl = http://demo.org:5000/outputs

   [logging]
   level = DEBUG

Start the service with your custom configuration:

.. code-block:: sh

   # start the service with this configuration
   $ emu -c etc/custom.cfg


.. _PyWPS: http://pywps.org/

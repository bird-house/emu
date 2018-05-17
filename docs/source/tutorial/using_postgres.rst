.. _using_postgres_tutorial:

Tutorial: using postgres database
=================================

You can use a postgres database for PyWPS, the default is sqlite.
PyWPS is using `SQLAlchemy`_, see the `PYWPS documentation`_ for details.

First run the Emu default installation:

.. code-block:: sh

    $ git clone https://github.com/bird-house/emu.git
    $ cd emu
    $ make clean install

The default installation is using sqlite. We now need a postgres database.
If you don't have one yet you can use a `postgres docker container <https://store.docker.com/images/postgres>`_.

.. code-block:: sh

    $ docker pull postgres
    $ docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres

The postgres database is now available on default port 5432.

SQLAlchemy needs the  `psycopg2 <https://pypi.python.org/pypi/psycopg2>`_  postgres adapter.
You can install it via Conda into the ``emu`` environment.

.. code-block:: sh

    $ conda install -n emu psycopg2


The `SQLAlchemy connection string <http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html#dialect-postgresql-psycopg2-connect>`_
for this database is::

    # postgresql+psycopg2://user:password@host:port/dbname
    postgresql+psycopg2://postgres:postgres@localhost:5432/postgres

Configure this connection string in ``etc/custom.cfg``, ``logging`` section, ``database`` option:

.. code-block:: sh

    $ vim etc/custom.cfg
    [logging]
    level = INFO
    database = postgresql+psycopg2://postgres:postgres@localhost:5432/postgres

Start the emu service:

.. code-block:: sh

    $ emu -c etc/custom.cfg

Your Emu WPS service should be available at the following URL:

.. code-block:: sh

    $ firefox http://localhost:5000/wps?request=GetCapabilities&service=WPS

.. _SQLAlchemy: http://docs.sqlalchemy.org/en/latest/index.html
.. _PYWPS documentation: http://pywps.readthedocs.io/en/latest/

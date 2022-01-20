===========
Sensor
===========

What is this?
=============

**The Problem**: A small play-around repo with a few things:
    - ``/sensor/generate_signals.py`` generates fake signals and adds them, via an API, to the database.
    - ``api.py`` is the location of the API which routes the signals.
    - We use a Postgres DB to store the timeseries data in ``long format``_.



How Do I Use This?
==================

1. The API and DB are dockerized.  Running

    docker-compose up --build

will set up the docker images.  **Important Note: if you re-run this, you may need to delete the previous volume created by docker.**  Check this with ``docker volume ls`` to see if the previous run created a volume --- if so, remove it.

2. Running

    python sensor/generate_signals.py

will automatically begin to generate signals every few seconds.  If the API and DB are running, the DB should be updated with the new signal values.

.. _``long format``: https://en.wikipedia.org/wiki/Wide_and_narrow_data

Things To Do:
=============
- [ ] Logger.

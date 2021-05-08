Installing with Docker
######################

Running CameraHub with Docker is a simple choice if you simply want to use CameraHub for yourself and don't want to make changes to the code.

This guide assumes you already have an installation of Docker on your system. If not, follow `these instructions <https://docs.docker.com/install/>`_ first.

To create a named container running CameraHub, use the following command. You can change the `-p` settings
if you wish to serve CameraHub on a different port.

A persistent volume will be created to store the SQLite database file.

Several Docker tags are available. Each release of CameraHub is tagged like ``0.1.0``, ``0.2.1``, etc, in accordance with
`the releases on Github <https://github.com/camerahub/camerahub/releases>`_. The ``latest`` tag points at the latest version tag. This is what you get by default.
Additionally, there is a `testing` tag which contains the code at `master <https://github.com/camerahub/camerahub/tree/master>`_
which should form the next tagged release.::

    docker create --name camerahub --mount source=camerahub-sqlite,target=/camerahub/db -p 8000:8000 camerahub/camerahub

Start CameraHub by running::

    docker start camerahub

and navigate to `http://localhost:8000 <http://localhost:8000>`_. Login with default username ``admin`` and password ``admin``.

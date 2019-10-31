# Installing with Docker

Running PhotoDB with Docker is a simple choice if you simply want to use PhotoDB for yourself and don't want to make changes to the code.

This guide assumes you already have an installation of Docker on your system. If not, follow [these instructions](https://docs.docker.com/install/) first.

To create a named container running PhotoDB, use the following command. You can change the `-p` settings
if you wish to serve PhotoDB on a different port.

A persistent volume will be created to store the SQLite database file.

Several Docker tags are available. Each release of PhotoDB is tagged like `0.1.0`, `0.2.1`, etc, in accordance with
[the releases on Github](https://github.com/djjudas21/photodb/releases).  The `latest` tag points at the latest version tag. This is what you get by default.
Additionally, there is a `testing` tag which contains the code at [master](https://github.com/djjudas21/photodb/tree/master)
which should form the next tagged release.

```sh
docker create --name photodb --mount source=photodb-sqlite,target=/var/www/photodb/db -p 8000:8000 djjudas21/photodb
```

Start PhotoDB by running:

```sh
docker start photodb
```

and navigate to [http://localhost:8000](http://localhost:8000). Login with default username `admin` and password `admin`.

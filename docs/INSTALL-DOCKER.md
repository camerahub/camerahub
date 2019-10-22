# Installing with Docker

Running PhotoDB with Docker is a simple choice if you simply want to use PhotoDB for yourself and don't want to make changes to the code.

This guide assumes you already have an installation of Docker on your system. If not, follow [these instructions](https://docs.docker.com/install/) first.

To create a named container running PhotoDB, use the following command. You can change the `-p` settings
if you wish to serve PhotoDB on a different port.

A persistent volume will be created to store the SQLite database file.

```sh
docker create --name photodb --mount source=photodb-sqlite,target=/var/www/photodb/db -p 8000:8000 djjudas21/photodb
```

Start PhotoDB by running:

```sh
docker start photodb
```

and navigate to [http://localhost:8000](http://localhost:8000). Login with default username `admin` and password `admin`.
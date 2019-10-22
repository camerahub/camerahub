# PhotoDB

PhotoDB is a web app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully
catalogue a collection of photographic equipment as well as the pictures that are made with them. Read the [Concepts](docs/CONCEPTS.md)
section for full details on the capabilities of PhotoDB.

It replaces an earlier command-line project, also called [PhotoDB](https://github.com/djjudas21/photodb-perl), which has now been deprecated.

## Installing PhotoDB

There are several ways of installing PhotoDB, depending on your needs:

* With Pip
* [From source](docs/INSTALL_SOURCE.md)
* [With Docker](docs/INSTALL-DOCKER.md)
* [With Kubernetes](docs/INSTALL-KUBERNETES.md)

## Configuring PhotoDB

PhotoDB requires no additional config to run with default settings. However the database backend can be configured by setting
the `DB_*` environment variables. The following variables are supported:

* `DB_ENGINE` - the database engine (default `django.db.backends.sqlite3`)
* `DB_NAME` - the name of the database schema, or path to the SQLite db file (default `db/db.sqlite3`)
* `DB_USER` - database username
* `DB_PASS` - database password
* `DB_HOST` - database hostname or IP address
* `DB_PORT` - database port

## See also

* [Concepts](docs/CONCEPTS.md)
* [Screenshots](docs/SCREENSHOTS.md)
* [Contributing](docs/CONTRIBUTING.md)

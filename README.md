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
the `DATABASE_URL` environment variable. The following settings are supported:

| Engine     | Django Backend                | URL                                     |
| ---------- | ----------------------------- | --------------------------------------- |
| PostgreSQL | django.db.backends.postgresql | postgres://USER:PASSWORD@HOST:PORT/NAME |
| MySQL      | django.db.backends.mysql      | mysql://USER:PASSWORD@HOST:PORT/NAME    |
| SQLite     | django.db.backends.sqlite3    | sqlite:///PATH                          |

## See also

* [Concepts](docs/CONCEPTS.md)
* [Screenshots](docs/SCREENSHOTS.md)
* [Contributing](docs/CONTRIBUTING.md)

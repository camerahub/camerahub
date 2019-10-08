# PhotoDB

PhotoDB is an app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully
catalogue a collection of photographic equipment as well as the pictures that are made with them. Read the [Concepts](docs/CONCEPTS.md)
section for full details on the capabilities of PhotoDB.

## Installing PhotoDB

### From pip

```sh
pip install PhotoDB
```

### From source

To install PhotoDB from source, clone this repo and run:

```sh
pip install .
```

This method of installation is required if you want to work on the source code.

### With Docker

To create a named container running PhotoDB, use the following command. You can change the `-p` settings
if you wish to serve PhotoDB on a different port.

A persistent volume will be created to store the SQLite database file.

To provide additional config, e.g. [connection info for external databases](https://docs.djangoproject.com/en/2.2/ref/settings/#databases),
create a config file `~/photodb/local_settings.py` with your settings in. This will be mounted into the container.

```sh
docker create --name photodb --mount source=photodb-sqlite,target=/var/www/photodb/db -v "$HOME/photodb":/var/www/photodb/photodb/local_settings -p 8000:8000 djjudas21/photodb-django
```

## Configuring PhotoDB

PhotoDB will run out of the box with no additional configuration, by creating an SQLite database in its own directory.

If you wish to use an external database then copy `photodb/local_settings/local_settings.py.template` to
`photodb/local_settings/local_settings.py` and customise the database settings for your environment.

After the database is configured, apply the migrations and create your user account:

```sh
python manage.py migrate
python manage.py createsuperuser
```

## Running PhotoDB

### From pip or source

```sh
python manage.py runserver
```

and navigate to [http://localhost:8000](http://localhost:8000). Log in with the superuser account you created above.

### From Docker

```sh
docker start photodb
```

and navigate to [http://localhost:8000](http://localhost:8000). Login with default username `admin` and password `admin`.

## See also

* [Concepts](docs/CONCEPTS.md)
* [Contributing](docs/CONTRIBUTING.md)
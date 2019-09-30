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

```sh
docker run djjudas21/photodb-django:0.0.10
```

## Configuring PhotoDB

PhotoDB will run out of the box with no additional configuration, by creating an SQLite database in its own directory.

If you wish to use an external database then copy `photodb/local_settings.py.template` to
`photodb/local_settings.py` and customise the database settings for your environment.

After the database is configured, apply the migrations and create your user account:

```sh
python manage.py migrate
python manage.py createsuperuser
```

## Running PhotoDB

At the moment, PhotoDB is not packaged for production use. To run it in development mode, execute:

```sh
python manage.py runserver
```

and navigate to [http://localhost:8000](http://localhost:8000)

## See also

* [Concepts](docs/CONCEPTS.md)
* [Contributing](docs/CONTRIBUTING.md)
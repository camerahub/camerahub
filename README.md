# PhotoDB

PhotoDB is an app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully
catalogue a collection of photographic equipment as well as the pictures that are made with them. Read the [Concepts](docs/CONCEPTS.md)
section for full details on the capabilities of PhotoDB.

## Installing PhotoDB

At the moment, PhotoDB is not packaged for production use. To install it in development mode, clone this repo and run:

```sh
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## Configuring PhotoDB

PhotoDB will run out of the box with no additional configuration, by creating an Sqlite database in its own directory.

## Running PhotoDB

At the moment, PhotoDB is not packaged for production use. To run it in development mode, execute:

```sh
python manage.py runserver
```

and navigate to [http://localhost:8000](http://localhost:8000)

## See also

* [Concepts](docs/CONCEPTS.md)
* [Contributing](docs/CONTRIBUTING.md)
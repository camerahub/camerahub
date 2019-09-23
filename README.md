# PhotoDB

PhotoDB is an app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully
catalogue a collection of photographic equipment as well as the pictures that are made with them. Read the CONCEPTS section for full details on the
capabilities of PhotoDB.

## Installing PhotoDB

At the moment, PhotoDB is not packaged for production use. To install it in development mode, clone this repo and run:

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
# Installing from source

This method of installation is required if you want to work on the source code. To install PhotoDB from source, clone this repo and run
these steps to create a virtualenv with all the dependencies:

```sh
git clone https://github.com/djjudas21/photodb.git
cd photodb
virtualenv venv
source venv/bin/activate
pip install .
```

PhotoDB will run out of the box with no additional configuration, by creating an SQLite database in its own directory.

If you wish to use an external database then copy `photodb/local_settings/local_settings.py.template` to
`photodb/local_settings/local_settings.py` and customise the database settings for your environment.

After the database is configured, apply the migrations and create your user account:

```sh
python manage.py migrate
python manage.py createsuperuser
```

To run PhotoDB, run:

```sh
# Use default SQLite database
python manage.py runserver

# Override database
DB_HOST=localhost DB_ENGINE=django.db.backends.postgresql DB_USER=admin DB_PASS=admin DB_PORT=5432 DB_NAME=photodb python3 manage.py runserver
```

and navigate to [http://localhost:8000](http://localhost:8000). Log in with the superuser account you created above.
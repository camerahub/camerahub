# Installing from source

This method of installation is required if you want to work on the source code. To install CameraHub from source, clone this repo and run
these steps to create a virtualenv with all the dependencies:

```sh
git clone https://github.com/djjudas21/camerahub.git
cd camerahub
virtualenv venv
source venv/bin/activate
pip install .
```

CameraHub will run out of the box with no additional configuration, by creating an SQLite database in its own directory.

If you wish to use an external database then copy `camerahub/local_settings/local_settings.py.template` to
`camerahub/local_settings/local_settings.py` and customise the database settings for your environment.

After the database is configured, apply the migrations and create your user account:

```sh
python manage.py migrate
python manage.py createsuperuser
```

To run CameraHub, run:

```sh
# Use default SQLite database
python manage.py runserver

# Override database
CAMERAHUB_DB_HOST=localhost CAMERAHUB_DB_ENGINE=django.db.backends.postgresql CAMERAHUB_DB_USER=admin CAMERAHUB_DB_PASS=admin CAMERAHUB_DB_PORT=5432 CAMERAHUB_DB_NAME=camerahub python3 manage.py runserver
```

and navigate to [http://localhost:8000](http://localhost:8000). Log in with the superuser account you created above.

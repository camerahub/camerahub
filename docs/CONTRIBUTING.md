## Development

PhotoDB is written in [Python](https://www.python.org/) using the [Django](https://www.djangoproject.com/) framework. Despite having a complex
data model, the app itself is quite simple.

Bugs and feature requests should be raised in the [issue tracker](https://github.com/djjudas21/photodb/issues). All feature suggestions will be considered
but there is no promise of development effort. Contributions of code from the community are welcomed.

Features should be developed in branches and submitted via pull request. Pull requests must pass any relevant CI tests before being accepted.

### Development environment

Fork and clone PhotoDB, then do the following to set up your development environment:

```sh
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

PhotoDB will run out of the box with no additional configuration, by creating an Sqlite database in its own directory.

Run PhotoDB by using the integrated web server. Editing and saving the code will cause the server to reload so you can test your changes.

```sh
python manage.py runserver
```

### Migrations

If your work requires changes to the database schema, make these changes by editing `schema/models.py`. Then generate a migration by running

```sh
python manage.py createmigration
```

Check the resulting migration file into git.

Always test your migrations by running

```sh
python manage.py migrate
```

The schema can be reset at any time by deleting `db.sqlite`. After this you will need to reapply all migrations, set up the super user, etc.

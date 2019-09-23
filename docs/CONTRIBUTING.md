## Development

Features should be developed in branches and submitted via pull request.

### Migrations

If your work requires changes to the database schema, make these changes by editing `schema/models.py`. Then generate a migration by running

```
python manage.py createmigration
```

Check the resulting migration file into git.
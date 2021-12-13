#!/bin/sh
set -e

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    poetry install --no-dev --no-root
    python manage.py migrate --noinput
    python manage.py installwatson
    python manage.py buildwatson
    python manage.py populate_history --auto
    python manage.py collectstatic -c --noinput
    python manage.py updatedoc -b camerahub
    python manage.py clear_cache
fi

exec "$@"

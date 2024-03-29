#!/bin/sh
set -e

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    poetry install --no-dev --no-root
    python manage.py migrate --noinput
    python manage.py installwatson
    python manage.py buildwatson
    python manage.py collectstatic -c --noinput
fi

exec "$@"

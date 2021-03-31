#!/bin/sh
set -e

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
    python manage.py installwatson
    python manage.py buildwatson
    python manage.py populate_history --auto
    python manage.py collectstatic
fi

exec "$@"

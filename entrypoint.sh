#!/bin/sh
set -e

if [ "x$DJANGO_MANAGEPY_MIGRATE" = 'xon' ]; then
    python manage.py migrate --noinput
    python manage.py installwatson
    python manage.py buildwatson
fi

exec "$@"

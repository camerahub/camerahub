# PhotoDB
FROM python:3-alpine
LABEL maintainer "Jonathan Gazeley"

# Project Files and Settings
ARG PROJECT_DIR=/var/www/photodb
RUN mkdir -p $PROJECT_DIR/static
ADD . $PROJECT_DIR
WORKDIR $PROJECT_DIR

# Install deps from apk and pip
RUN apk --no-cache add pcre mailcap libpq \
  && apk --no-cache add --virtual .build-deps gcc musl-dev linux-headers pcre-dev postgresql-dev git \
  && pip install . --no-cache-dir \
  && apk --no-cache del .build-deps

# Specify production mode
ENV DJANGO_PROD true

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN python manage.py collectstatic --noinput

# Tell uWSGI where to find your wsgi file (change this):
ENV UWSGI_WSGI_FILE=photodb/wsgi.py

# Base uWSGI configuration (you shouldn't need to change these):
ENV UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_HTTP_AUTO_CHUNKED=1 UWSGI_HTTP_KEEPALIVE=1 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Number of uWSGI workers and threads per worker (customize as needed):
ENV UWSGI_WORKERS=2 UWSGI_THREADS=4

# uWSGI static file serving configuration (customize or comment out if not needed):
ENV UWSGI_STATIC_MAP="/static/=/var/www/photodb/static/" UWSGI_STATIC_EXPIRES_URI="/static/.*\.[a-f0-9]{12,}\.(css|js|png|jpg|jpeg|gif|ico|woff|ttf|otf|svg|scss|map|txt) 315360000"

# Deny invalid hosts before they get to Django (uncomment and change to your hostname(s)):
# ENV UWSGI_ROUTE_HOST="^(?!localhost:8000$) break:400"

# Run migrations
RUN python manage.py migrate

# Create superuser
RUN python manage.py createsuperuserwithpassword --username admin --password admin --email admin@example.com --preserve

# Server
EXPOSE 8000
STOPSIGNAL SIGINT

# Start uWSGI
ENTRYPOINT ["./entrypoint.sh"]
CMD ["uwsgi", "--show-config"]
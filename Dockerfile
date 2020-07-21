# CameraHub
FROM python:3.8-alpine
LABEL maintainer "Jonathan Gazeley"

# Project Files and Settings
ARG PROJECT_DIR=/var/www/camerahub
RUN mkdir -p $PROJECT_DIR/static $PROJECT_DIR/media
ADD . $PROJECT_DIR
WORKDIR $PROJECT_DIR

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install deps from apk and poetry
RUN apk --no-cache add pcre mailcap libpq jpeg libmagic \
  && apk --no-cache add --virtual .build-deps gcc musl-dev linux-headers pcre-dev postgresql-dev git libffi-dev zlib-dev jpeg-dev \
  && pip install poetry \
  && poetry config virtualenvs.create false \
  && poetry install -E pgsql --no-dev -n \
  && apk --no-cache del .build-deps

# Call collectstatic (customize the following line with the minimal environment variables needed for manage.py to run):
RUN python manage.py collectstatic --noinput

# Run migrations
ENV DJANGO_MANAGEPY_MIGRATE=on

# Server
EXPOSE 8000
STOPSIGNAL SIGINT

# Start uWSGI
ENTRYPOINT ["./entrypoint.sh"]
CMD ["uwsgi", "--ini uwsgi.ini", "--show-config"]

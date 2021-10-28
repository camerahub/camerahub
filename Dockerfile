# CameraHub
FROM python:3.9-slim
LABEL maintainer "Jonathan Gazeley"

# Project Files and Settings
ARG PROJECT_DIR=/camerahub
RUN mkdir -p $PROJECT_DIR/static $PROJECT_DIR/media
ADD . $PROJECT_DIR
WORKDIR $PROJECT_DIR

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Install runtime deps
RUN runDeps='libpq5 libgdal28 libmagic1 mime-support postgresql-client' \
  && apt-get update && apt-get install -y $runDeps --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# Install built deps
RUN buildDeps='build-essential  libpq-dev git libffi-dev zlib1g-dev libjpeg-dev libgdal-dev' \
    && set -x \
    && apt-get update && apt-get install -y $buildDeps --no-install-recommends \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install -E pgsql --no-dev -n \
    && apt-get purge -y --auto-remove $buildDeps \
    && rm -rf /var/lib/apt/lists/*

# Run migrations
ENV DJANGO_MANAGEPY_MIGRATE=on

# Server
EXPOSE 8000
STOPSIGNAL SIGINT

# Start uWSGI
ENTRYPOINT ["./entrypoint.sh"]
CMD ["uwsgi", "uwsgi.ini"]

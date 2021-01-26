# CameraHub

CameraHub is a web app for film photography that can be used to track cameras, lenses, accessories, films, negatives and prints, to fully
catalogue a collection of photographic equipment as well as the pictures that are made with them.

It replaces an earlier command-line project, called [PhotoDB](https://github.com/djjudas21/photodb-perl), which has now been deprecated.

## Installing CameraHub

There are several ways of installing CameraHub, depending on your needs:

* With Pip
* [From source](docs/INSTALL_SOURCE.md)
* [With Docker](docs/INSTALL-DOCKER.md)
* [With Kubernetes](docs/INSTALL-KUBERNETES.md)

## Configuring CameraHub

CameraHub requires almost no additional config to run with default settings. However it is insecure in this configuration so at least `CAMERAHUB_SECRET_KEY` and
`CAMERAHUB_PROD` must be set if you are running in production.

The following environment variables are supported:

### `CAMERAHUB_ADMIN_EMAIL`

Email address for the `admin` account
Default: `admin@example.com`

### `CAMERAHUB_ADMIN_PASSWORD`

Password for the `admin` account
Default: `admin`

### `CAMERAHUB_DB_ENGINE`

[Database engine](https://docs.djangoproject.com/en/3.0/ref/settings/#engine)
Default: `django.db.backends.sqlite3`

### `CAMERAHUB_DB_HOST`

[Database hostname or IP address](https://docs.djangoproject.com/en/3.0/ref/settings/#host) if an engine other than SQLite is configured

### `CAMERAHUB_DB_NAME`

[Database schema or path to SQLite db](https://docs.djangoproject.com/en/3.0/ref/settings/#name)
`db/db.sqlite3`

### `CAMERAHUB_DB_PASS`

[Database password](https://docs.djangoproject.com/en/3.0/ref/settings/#password) if an engine other than SQLite is configured

### `CAMERAHUB_DB_PORT`

[Database port](https://docs.djangoproject.com/en/3.0/ref/settings/#port) if an engine other than SQLite is configured

### `CAMERAHUB_DB_USER`

[Database username](https://docs.djangoproject.com/en/3.0/ref/settings/#user) if an engine other than SQLite is configured

### `CAMERAHUB_PROD`

Enable [Django production mode](https://docs.djangoproject.com/en/3.0/ref/settings/#debug)
Default: `false`

### `CAMERAHUB_SECRET_KEY`

Random secret value. The default string is for testing only and is insecure in production. Generate a new one [here](https://miniwebtool.com/django-secret-key-generator/)
Default: `OverrideMe!`

### `CAMERAHUB_EMAIL_BACKEND`

[Email backend](https://docs.djangoproject.com/en/3.1/topics/email/#email-backends)
Default: `django.core.mail.backends.filebased.EmailBackend`

### `CAMERAHUB_SENDGRID_KEY`

API key for Sendgrid email backend

### `CAMERAHUB_EMAIL_USE_TLS`'

Enable TLS for SMTP

### `CAMERAHUB_EMAIL_USE_SSL`'

Enable TLS for SMTP

### `CAMERAHUB_EMAIL_HOST`

SMTP server hostname

### `CAMERAHUB_EMAIL_HOST_USER`

SMTP server username

### `CAMERAHUB_EMAIL_HOST_PASSWORD`

SMTP server password

### `CAMERAHUB_EMAIL_PORT`

SMTP server port number

### `CAMERAHUB_FROM_EMAIL`

[From email address](https://docs.djangoproject.com/en/3.0/ref/settings/#default-from-email)
Default: `noreply@camerahub.info`

### `CAMERAHUB_DOMAIN`

[Site domain](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts)
Default: `camerahub.info`

### `CAMERAHUB_REDIS`

Enable [Redis caching](https://docs.djangoproject.com/en/3.0/topics/cache/)
Default: `false`

### `CAMERAHUB_REDIS_HOST`

Redis hostname or IP address
Default: `127.0.0.1`

### `CAMERAHUB_REDIS_PORT`

Redis port
Default: `6379`

## See also

* [Screenshots](docs/SCREENSHOTS.md)
* [Contributing](docs/CONTRIBUTING.md)
* [Changelog](https://github.com/camerahub/camerahub/releases)
* [Icons](docs/ICONS.md)
* [API](docs/API.md)
* [Operations](docs/OPS.md)

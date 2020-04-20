# Development

CameraHub is written in [Python](https://www.python.org/) using the [Django](https://www.djangoproject.com/) framework. Despite having a complex
data model, the app itself is quite simple.

Bugs and feature requests should be raised in the [issue tracker](https://github.com/djjudas21/camerahub/issues). All feature suggestions will be considered
but there is no promise of development effort. Contributions of code from the community are welcomed.

Features should be developed in branches and submitted via pull request. Pull requests must pass any relevant CI tests before being accepted.

## Development environment

Fork and clone CameraHub, then do the following to set up your development environment:

```sh
pip install -r .
python manage.py migrate
python manage.py createsuperuser
```

## Testing

### Using the integrated web server

CameraHub will run out of the box with no additional configuration, by creating an Sqlite database in its own directory.

Run CameraHub by using the integrated web server. Editing and saving the code will cause the server to reload so you can quickly test your changes.

```sh
python manage.py runserver
```

Then browse to [http://localhost:80](http://localhost:8000). Login with default username `admin` and password `admin`.

### Using microk8s

The integrated web server is extremely convenient but does not test all aspects of CameraHub, especially the Postgres database backend,
Redis caching and other production-like features. The best way to test these features is to run microk8s on your local computer, which gives
you a full Kubernetes environment.

After installing microk8s, ensure you have these addons:

```sh
microk8s.enable dns ingress storage registry
```

The development Kustomize overlay configures CameraHub as a single replica deployment of CameraHub, deployed from the `testing` Docker image,
which is built locally on your system. It uses a single Postgresql replica to store its data. It creates a NodePort Service resource on
`localhost` on a high port.

```sh
# Build testing image
docker build -t camerahub:testing .

# Push to local registry
docker tag camerahub:testing localhost:32000/camerahub:testing
docker push localhost:32000/camerahub:testing

# Apply development manifests
kubectl apply -k kubernetes/overlays/dev
```

Then browse to [http://localhost:80](http://localhost:80). Login with default username `admin` and password `admin`.

## Migrations

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

## Releases

CameraHub uses [semver](https://semver.org/) versioning. To make a new release:

1. Ensure that everything you need is merged into `master` and all tests are passing
1. Decide which version number to use by looking at previous versions `git tag`
1. Add a new section to [CHANGELOG.md](../docs/CHANGELOG.md) outlining the new features/fixes
1. Update references to the version number, e.g. the Docker tag in the Kubernetes [deployment](../kubernetes/kustomize/camerahub/deployment.yaml)
1. Create a new release from `master` in Github which includes the CHANGELOG notes
1. [Travis CI](https://travis-ci.org/djjudas21/camerahub) will build the release and publish in on [PyPI](https://pypi.org/project/CameraHub) and [Docker Hub](https://hub.docker.com/repository/docker/djjudas21/camerahub)

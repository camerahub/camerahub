# API

CameraHub has a simple API to allow integrations with other apps. At the moment it is not comprehensive and endpoints are added as required.

## Endpoints

### `/api/films/`

Returns a list of the current user's films

```sh
curl -H 'Accept: application/json; indent=4' -u admin:admin  http://127.0.0.1:8000/api/film/
```

### `/api/negative/`

Returns a list of the current user's negatives, filtered by film

```sh
curl -H 'Accept: application/json; indent=4' -u admin:admin  http://127.0.0.1:8000/api/negative/?film=1
```

### `/api/scan/`

Returns a list of the current user's scans

```sh
curl -H 'Accept: application/json; indent=4' -u admin:admin  http://127.0.0.1:8000/api/scan/
```

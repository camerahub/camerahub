# API

CameraHub has a simple RESTful API to allow integrations with other apps. It is implemented with [Django REST framework](https://www.django-rest-framework.org/). At the moment it is not comprehensive and endpoints are added as required.

## Endpoints

### `/api/films/`

Returns a list of the current user's films

```sh
curl -H 'Accept: application/json; indent=4' -u admin:admin  http://127.0.0.1:8000/api/film/
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "id_owner": 1,
            "title": null
        },
        {
            "id_owner": 2,
            "title": null
        },
        {
            "id_owner": 3,
            "title": null
        }
    ]
}
```

```sh
curl -H 'Accept: application/json; indent=4' -u admin:admin  http://127.0.0.1:8000/api/film/2/
{
    "id_owner": 2,
    "title": null
}
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

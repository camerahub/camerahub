# API

CameraHub has a simple RESTful API to allow integrations with other apps. It is implemented with [Django REST framework](https://www.django-rest-framework.org/). At the moment it is not comprehensive and endpoints are added as required. Example queries here are executed with [httpie](https://httpie.io/).

## Authentication

All endpoints require authentication, which is done using the username and password of the user. There is currently no support for tokens or keys.

The examples on this page are made with a local development version of CameraHub on `http://127.0.0.1:8000` instead of `https://camerahub.info`, with a default credential set of `admin:admin`.

If you are using `curl` or `http`, you must pass credentials on the command line.

```sh
coreapi credentials add 127.0.0.1 admin:admin --auth basic
Added credentials
127.0.0.1 "Basic YWRtaW46YWRtaW4="
```

## Endpoints

### `/api/`

List all endpoints. This is the only endpoint that does not require authentication.

```sh
http http://127.0.0.1:8000/api/
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 261
Content-Type: application/json
Date: Wed, 11 Nov 2020 21:42:41 GMT
Expires: Wed, 11 Nov 2020 21:52:41 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "camera": "http://127.0.0.1:8000/api/camera/",
    "film": "http://127.0.0.1:8000/api/film/",
    "lens": "http://127.0.0.1:8000/api/lens/",
    "negative": "http://127.0.0.1:8000/api/negative/",
    "print": "http://127.0.0.1:8000/api/print/",
    "scan": "http://127.0.0.1:8000/api/scan/"
}
```

### `/api/films/`

Returns a list of the current user's films

```sh
http -a admin:admin http://127.0.0.1:8000/api/film/
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 135
Content-Type: application/json
Date: Mon, 09 Nov 2020 20:36:28 GMT
Expires: Mon, 09 Nov 2020 20:46:28 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

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

Return a specific film

```sh
http -a admin:admin http://127.0.0.1:8000/api/film/2/
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 27
Content-Type: application/json
Date: Mon, 09 Nov 2020 20:38:34 GMT
Expires: Mon, 09 Nov 2020 20:48:34 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "id_owner": 2,
    "title": null
}
```

### `/api/negative/`

Returns a list of the current user's negatives

```sh
http -a admin:admin http://127.0.0.1:8000/api/negative/
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 262
Content-Type: application/json
Date: Mon, 09 Nov 2020 21:25:49 GMT
Expires: Mon, 09 Nov 2020 21:35:49 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "caption": "Hello",
            "film": "http://127.0.0.1:8000/api/film/1/",
            "film_id": "1",
            "frame": "2",
            "id_owner": 1
        },
        {
            "caption": "Another test",
            "film": "http://127.0.0.1:8000/api/film/2/",
            "film_id": "2",
            "frame": "1",
            "id_owner": 2
        }
    ]
}
```

Returns a list of the current user's negatives, filtered by film

```sh
http -a admin:admin http://127.0.0.1:8000/api/negative/?film_id=2
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 160
Content-Type: application/json
Date: Mon, 09 Nov 2020 21:25:56 GMT
Expires: Mon, 09 Nov 2020 21:35:56 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "caption": "Another test",
            "film": "http://127.0.0.1:8000/api/film/2/",
            "film_id": "2",
            "frame": "1",
            "id_owner": 2
        }
    ]
}
```

Return a specific negative

```sh
[jonathan@latitude camerahub]$ http -a admin:admin http://127.0.0.1:8000/api/negative/2/
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 154
Content-Type: application/json
Date: Mon, 09 Nov 2020 22:20:46 GMT
Expires: Mon, 09 Nov 2020 22:30:46 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "caption": "Another test",
    "film": "http://127.0.0.1:8000/api/film/2/",
    "film_id": "2",
    "frame": "1",
    "id_owner": 2,
    "url": "http://127.0.0.1:8000/api/negative/2/"
}
```

### `/api/scan/`

Returns a list of the current user's scans

```sh
http -a admin:admin http://127.0.0.1:8000/api/scan/
HTTP/1.1 200 OK
Allow: GET, POST, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 827
Content-Type: application/json
Date: Mon, 09 Nov 2020 22:02:31 GMT
Expires: Mon, 09 Nov 2020 22:12:31 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "filename": "test.jpg",
            "negative": {
                "caption": "Hello",
                "film": "http://127.0.0.1:8000/api/film/1/",
                "film_id": "1",
                "frame": "2",
                "id_owner": 1,
                "url": "http://127.0.0.1:8000/api/negative/1/"
            },
            "url": "http://127.0.0.1:8000/api/scan/33dfafdf-95ca-4781-9bef-a422491f2754/",
            "uuid": "33dfafdf-95ca-4781-9bef-a422491f2754"
        },
        {
            "filename": "test.jpg",
            "negative": {
                "caption": "Hello",
                "film": "http://127.0.0.1:8000/api/film/1/",
                "film_id": "1",
                "frame": "2",
                "id_owner": 1,
                "url": "http://127.0.0.1:8000/api/negative/1/"
            },
            "url": "http://127.0.0.1:8000/api/scan/18e6bb82-1aca-4de1-961b-e8d588982ff2/",
            "uuid": "18e6bb82-1aca-4de1-961b-e8d588982ff2"
        },
        {
            "filename": "tes2t.jpg",
            "negative": null,
            "url": "http://127.0.0.1:8000/api/scan/3152c143-9a3b-4ff1-a9e0-d48ed2fc0d9e/",
            "uuid": "3152c143-9a3b-4ff1-a9e0-d48ed2fc0d9e"
        }
    ]
}
```

Return a specific scan

```sh
http -a admin:admin http://127.0.0.1:8000/api/scan/33dfafdf-95ca-4781-9bef-a422491f2754/
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 305
Content-Type: application/json
Date: Mon, 09 Nov 2020 22:23:35 GMT
Expires: Mon, 09 Nov 2020 22:33:35 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "filename": "test.jpg",
    "negative": {
        "caption": "Hello",
        "film": "http://127.0.0.1:8000/api/film/1/",
        "film_id": "1",
        "frame": "2",
        "id_owner": 1,
        "url": "http://127.0.0.1:8000/api/negative/1/"
    },
    "url": "http://127.0.0.1:8000/api/scan/33dfafdf-95ca-4781-9bef-a422491f2754/",
    "uuid": "33dfafdf-95ca-4781-9bef-a422491f2754"
}
```

Creates a new scan

```sh
http -a admin:admin POST http://127.0.0.1:8000/api/scan/ filename=api.jpg
HTTP/1.1 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Length: 174
Content-Type: application/json
Date: Mon, 16 Nov 2020 20:12:47 GMT
Location: http://127.0.0.1:8000/api/scan/079585ed-6093-4177-be1c-66abb45fe9c4/
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "filename": "api.jpg",
    "negative": null,
    "print": null,
    "url": "http://127.0.0.1:8000/api/scan/079585ed-6093-4177-be1c-66abb45fe9c4/",
    "uuid": "079585ed-6093-4177-be1c-66abb45fe9c4"
}
```

Updates an existing scan

```sh
http -a admin:admin PUT http://127.0.0.1:8000/api/scan/079585ed-6093-4177-be1c-66abb45fe9c4/ filename=api2.jpg
HTTP/1.1 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Length: 175
Content-Type: application/json
Date: Mon, 16 Nov 2020 20:17:01 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "filename": "api2.jpg",
    "negative": null,
    "print": null,
    "url": "http://127.0.0.1:8000/api/scan/079585ed-6093-4177-be1c-66abb45fe9c4/",
    "uuid": "079585ed-6093-4177-be1c-66abb45fe9c4"
}
```

### `/api/print/`

Return a list of the current user's prints

```sh
http -a admin:admin http://127.0.0.1:8000/api/print/
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 792
Content-Type: application/json
Date: Wed, 11 Nov 2020 21:49:35 GMT
Expires: Wed, 11 Nov 2020 21:59:35 GMT
Server: WSGIServer/0.2 CPython/3.8.5
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "negative": {
                "aperture": "4.0",
                "caption": "Hello",
                "copy_of": null,
                "date": "2020-11-03T20:41:00Z",
                "exposure_program": "Landscape",
                "film": {
                    "camera": "http://127.0.0.1:8000/api/camera/1/",
                    "id_owner": 1,
                    "title": null,
                    "url": "http://127.0.0.1:8000/api/film/1/"
                },
                "film_id": "1",
                "filter": "Variable ND",
                "flash": false,
                "focal_length": 50,
                "frame": "2",
                "id_owner": 1,
                "lens": {
                    "lensmodel": {
                        "manufacturer": "Canon",
                        "model": "FD 50mm f/1.8"
                    },
                    "serial": "22222",
                    "url": "http://127.0.0.1:8000/api/lens/2/"
                },
                "location": "51.4538022,-2.5972985",
                "metering_mode": "None",
                "mount_adapter": null,
                "notes": "",
                "photographer": null,
                "shutter_speed": "&sup1;/3000",
                "teleconverter": "Tamron Tamron",
                "url": "http://127.0.0.1:8000/api/negative/1/"
            },
            "pk": 1,
            "url": "http://127.0.0.1:8000/api/print/1/"
        }
    ]
}
```

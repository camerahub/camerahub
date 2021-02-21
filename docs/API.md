# API

CameraHub has a simple RESTful API to allow integrations with other apps. It is implemented with [Django REST framework](https://www.django-rest-framework.org/).
At the moment it is not comprehensive and endpoints are added as required. Example queries here are executed with [httpie](https://httpie.io/).

## Domains

The examples on this page are made with a local development version of CameraHub on `http://127.0.0.1:8000`. It is also possible to use the following
public deployments, provided they are at v0.27.0 or higher.

* https://camerahub.info
* https://dev.camerahub.info
* https://test.camerahub.info

## Authentication

Public endpoints (e.g. camera models, manufacturers) do not require authentication for read-only access. All private endpoints (e.g. cameras, negatives)
require authentication, which is done using the username and password of the user. There is currently no support for tokens or keys.

`http://localhost:8000` runs with with a default credential set of `admin:admin`.

If you are using `curl` or `http`, you must pass credentials on the command line.

```sh
coreapi credentials add 127.0.0.1 admin:admin --auth basic
Added credentials
127.0.0.1 "Basic YWRtaW46YWRtaW4="
```

## Endpoints

The CameraHub API is designed to be easily browsable in a browser as well as on the command line.

### `/api/`

List all endpoints.

```sh
http http://127.0.0.1:8000/api/
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 1530
Content-Type: application/json
Date: Tue, 16 Feb 2021 22:24:43 GMT
Expires: Tue, 16 Feb 2021 22:34:43 GMT
Server: WSGIServer/0.2 CPython/3.9.1
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "accessory": "http://127.0.0.1:8000/api/accessory/",
    "archive": "http://127.0.0.1:8000/api/archive/",
    "battery": "http://127.0.0.1:8000/api/battery/",
    "bulkfilm": "http://127.0.0.1:8000/api/bulkfilm/",
    "camera": "http://127.0.0.1:8000/api/camera/",
    "cameramodel": "http://127.0.0.1:8000/api/cameramodel/",
    "developer": "http://127.0.0.1:8000/api/developer/",
    "enlarger": "http://127.0.0.1:8000/api/enlarger/",
    "enlargermodel": "http://127.0.0.1:8000/api/enlargermodel/",
    "film": "http://127.0.0.1:8000/api/film/",
    "filmstock": "http://127.0.0.1:8000/api/filmstock/",
    "filter": "http://127.0.0.1:8000/api/filter/",
    "flash": "http://127.0.0.1:8000/api/flash/",
    "flashmodel": "http://127.0.0.1:8000/api/flashmodel/",
    "format": "http://127.0.0.1:8000/api/format/",
    "lens": "http://127.0.0.1:8000/api/lens/",
    "lensmodel": "http://127.0.0.1:8000/api/lensmodel/",
    "manufacturer": "http://127.0.0.1:8000/api/manufacturer/",
    "mount": "http://127.0.0.1:8000/api/mount/",
    "mountadapter": "http://127.0.0.1:8000/api/mountadapter/",
    "negative": "http://127.0.0.1:8000/api/negative/",
    "negativesize": "http://127.0.0.1:8000/api/negativesize/",
    "order": "http://127.0.0.1:8000/api/order/",
    "paperstock": "http://127.0.0.1:8000/api/paperstock/",
    "person": "http://127.0.0.1:8000/api/person/",
    "print": "http://127.0.0.1:8000/api/print/",
    "process": "http://127.0.0.1:8000/api/process/",
    "scan": "http://127.0.0.1:8000/api/scan/",
    "teleconverter": "http://127.0.0.1:8000/api/teleconverter/",
    "teleconvertermodel": "http://127.0.0.1:8000/api/teleconvertermodel/",
    "toner": "http://127.0.0.1:8000/api/toner/"
}
```

### `/api/schema`

Return an OpenAPI schema describing all other endpoints. The output of the command is too long to list here.

## Examples

### List all camera models

```sh
http -a admin:admin http://127.0.0.1:8000/api/cameramodel/
HTTP/1.1 200 OK
Allow: GET, HEAD, OPTIONS
Cache-Control: max-age=600
Content-Length: 13014
Content-Type: application/json
Date: Tue, 16 Feb 2021 22:30:54 GMT
Expires: Tue, 16 Feb 2021 22:40:54 GMT
Server: WSGIServer/0.2 CPython/3.9.1
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "count": 8,
    "next": null,
    "previous": null,
    "results": [
        {
            "af_points": null,
            "aperture_blades": null,
            "battery_qty": null,
            "battery_type": null,
            "body_type": null,
            "bulb": null,
            "cable_release": null,
            "closest_focus": null,
            "coating": null,
            "continuous_fps": null,
            "date_imprint": null,
            "disambiguation": "",
            "discontinued": null,
            "dof_preview": null,
            "elements": null,
            "exposure_programs": [],
            "ext_flash": null,
            "external_power_drive": null,
            "fastest_shutter_speed": null,
            "filter_thread": null,
            "focus_type": null,
            "format": null,
            "groups": null,
            "hood": null,
            "image": "http://127.0.0.1:8000/media/clickii.jpg",
            "image_attribution": null,
            "image_attribution_link": null,
            "int_flash": false,
            "int_flash_gn": null,
            "interchangeable_backs": null,
            "interchangeable_finders": null,
            "internal_power_drive": null,
            "introduced": null,
            "lens_manufacturer": {
                "city": "Tokyo",
                "country": "JP",
                "dissolved": null,
                "founded": 1956,
                "link": null,
                "name": "Bronica"
            },
            "lens_model_name": "jjjj",
            "link": "http://google.com",
            "magnification": null,
            "manufacturer": {
                "city": null,
                "country": "US",
                "dissolved": null,
                "founded": null,
                "link": null,
                "name": "Bell & Howell"
            },
            "max_aperture": null,
            "max_focal_length": null,
            "max_iso": null,
            "meter_max_ev": null,
            "meter_min_ev": null,
            "metering": null,
            "metering_modes": [],
            "metering_type": null,
            "min_aperture": null,
            "min_focal_length": null,
            "min_iso": null,
            "mirror_lockup": null,
            "model": "66 mk18",
            "mount": null,
            "multiple_exposures": null,
            "negative_size": null,
            "nominal_max_angle_diag": null,
            "nominal_min_angle_diag": null,
            "notes": "",
            "other_names": "||",
            "pc_sync": null,
            "self_timer": null,
            "shoe": null,
            "shutter_model": null,
            "shutter_type": null,
            "slowest_shutter_speed": null,
            "strap_lugs": null,
            "time": null,
            "tripod": null,
            "viewfinder_coverage": null,
            "weight": null,
            "x_sync": null,
            "zoom": null
        },
        ...
    ]
}
```

## Old examples

These examples are for an earlier version of the API which used hyperlinking and a restricted list of fields.

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

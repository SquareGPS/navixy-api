---
title: Tracking route OSRM
description: Tracking route OSRM
---

# Tracking route OSRM

API path: `/route/osrm`.

### get

Gets route points via [OSRM API](https://github.com/Project-OSRM/osrm-backend/wiki/Server-api#requesting-routes).

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| start | Location JSON object. Start of route. | JSON object |
| end | Location JSON object. End of route. | JSON object |
| waypoints | Optional. List of transitional points. `[{locationA},{locationN}]` | array of JSON objects |
| point_limit | Optional. If specified, the returned route will be simplified to contain this number of points (or less). Min=2. | int |

Where **location** described in [data types description section](../../../getting-started.md#data-types).

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/route/osrm/get' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "start": {"lat": 56.827001, "lng": 60.594296}, "end": {"lat": 52.835601, "lng": 60.514721}}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/route/osrm/get?hash=a6aa75587e5c59c32d347da438505fc3&start={"lat": 56.827001, "lng": 60.594296}&end={"lat": 52.835601, "lng": 60.514721}
    ```

#### response

```json
{
    "success": true,
    "distance": 2546,
    "time": 194,
    "list": [{"lat": 56.827001, "lng": 60.594296}, {"lat": 52.835601, "lng": 60.514721}],
    "key_points": [{
      "id": 123,
      "lat": 56.827,
      "lng": 60.594296
    }] 
}
```

* `distance` - int. Length in meters.
* `time` - int. Duration in seconds.
* `list` - list of route points. Location objects.
* `key_points` - list of points corresponding to `start` point, `waypoints` and `end` point (in that sequence).
    * `id` - int. index in points `list`.
    * `lat` - float. Latitude.
    * `lng` - float. Longitude.

#### errors

* 215 (External service error).
* 218 (Malformed external service parameters).
    ```json
    {
        "success": false,
        "status": {
            "code": 218,
            "description": "Malformed external service parameters"
        },
        "errors": [
            {
                "status": "NOT_FOUND",
                "status_code": 207,
                "message": "Cannot find route between points"
            }
        ]
    }
    ```
  
    * `status` - string enum.
        * `NOT_FOUND` – indicates at least one of the locations specified in the request's origin, destination, or 
        waypoints could not be geocoded, or OSRM cannot find route.
        * `UNKNOWN_ERROR` – unexpected OSRM error code.
    * `status_code` - int. OSRM status code (don't rely on it).
    * `message` - string. OSRM error message (don't rely on it).
    
* 236 (Feature unavailable due to tariff restrictions) – if there is at least one tracker without “routing” tariff 
feature.

---
title: /osrm
description: /osrm
---

## get(…)
Get route points via [OSRM API](https://github.com/Project-OSRM/osrm-backend/wiki/Server-api#requesting-routes).

#### parameters:
*   **start** – (location JSON object) start of route
*   **end** – (location JSON object) end of route
*   **waypoints** = \[ ${location}, ... \] – (optional) list of transitional points.
*   **point_limit** – (optional. int. min=2) If specified, the returned route will be simplified to contain this number of points (or less).

Where **location** described in [data types description section](../../../getting-started.md#data-types).

#### return:
```js
{
    "success": true,
    "distance": 2546, // (int) length in meters
    "time": 194,      // (int) duration in seconds
    "list": [ ${location}, ... ], // list of route points
    "key_points": [ ${key_point}, ... ] 
}
```

**key_points** is list of points corresponding to **start** point, **waypoints** and **end** point (in that sequence). Where **key_point** is JSON object:
```js
{
    "id": 123,        // (int) index in points 'list'
    "lat": 56.827,    // latitude
    "lng": 60.594296  // longitude
}
```

#### errors:
*   215 (External service error)
*   218 (Malformed external service parameters)
    ```js
    {
        "success": false,
        "status": {
            "code": 218,
            "description": "Malformed external service parameters"
        },
        "errors": [
            {
                "status": "NOT_FOUND", // NOT_FOUND or UNKNOWN_ERROR
                "status_code": 207,    // OSRM status code (don't rely on it)
                "message": "Cannot find route between points" // OSRM error message (don't rely on it)
            }
        ]
    }
    ```
    where status is one of:

    *   `NOT_FOUND` – indicates at least one of the locations specified in the request's origin, destination, or waypoints could not be geocoded, or OSRM cannot find route.
    *   `UNKNOWN_ERROR` – unexpected OSRM error code.

*   236 (Feature unavailable due to tariff restrictions) – if there is at least one tracker without “routing” tariff feature

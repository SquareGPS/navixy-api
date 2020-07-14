---
title: /google
description: /google
---

## get(…)

Get route points using [Google Directions API](https://developers.google.com/maps/documentation/directions/intro).

#### parameters:

*   **start** – (location JSON object) start of route
*   **end** – (location JSON object) end of route
*   **waypoints** = \[ ${location}, ... \] – (optional) list of transitional points.
*   **point_limit** – (int. optional. min=2) If specified, the returned route will be simplified to contain this number of points (or less).

Where **location** described in [data types description section](../../../getting-started.md#data-types).

#### return:
```js
{
    "success": true,
    "distance": 13482, // (int) length in meters
    "time": 844,       // (int) duration in seconds
    "list": [ ${location}, ... ], // list of route points
    "key_points": [ ${key_point}, ... ] 
}
```

**key_points** is list of points corresponding to **start** point, **waypoints** and **end** point (in that sequence). Where **key_point** is JSON object:
```js
{
    "id": 123,        // (int) index in points 'list'
    "lat": 56.827,    // latitude
    "lng": 60.594296, // longitude
    "distance": 482,  // (int) length of full path from start in meters (0 for start point)
    "time": 144       // (int) duration of full path from start in seconds (0 for start point)
}
```

#### errors:
*   215 (External service error)
```js
{
    "success": false,
    "status": {
        "code": 215,
        "description": "External service error"
    },
    "errors": [${status}] // one string or nothing
}
```
where **status** is one of:
    *   **OVER\_QUERY\_LIMIT** – indicates the service has received too many requests from your application within the allowed time period.
    *   **REQUEST_DENIED** – indicates that the service denied use of the directions service by your application.
    *   **UNKNOWN_ERROR** – indicates directions request could not be processed due to a server error. The request may succeed if you try again.

*   218 (Malformed external service parameters)
```js
{
    "success": false,
    "status": {
        "code": 218,
        "description": "Malformed external service parameters"
    },
    "errors": [${status}] // string
}
```
where status is one of:
    *   **NOT_FOUND** – indicates at least one of the locations specified in the request's origin, destination, or waypoints could not be geocoded.
    *   **ZERO_RESULTS** – indicates no route could be found between the origin and destination.
    *   **MAX\_WAYPOINTS\_EXCEEDED** – indicates that too many waypoints were provided in the request. The maximum allowed waypoints is 8, plus the origin, and destination. (Google Maps API for Business customers may contain requests with up to 23 waypoints.)
    *   **INVALID_REQUEST** – indicates that the provided request was invalid. Common causes of this status include an invalid parameter or parameter value.

*   236 (Feature unavailable due to tariff restrictions) – if there is at least one tracker without “routing” tariff feature

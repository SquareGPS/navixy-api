---
title: /route
description: /route
---

## get(…)
Get route points via specified route provider.

#### parameters:

*   **start** – (location JSON object) start of route
*   **end** – (location JSON object) end of route
*   **waypoints** = \[ ${location}, ... \] – (optional) list of transitional points.
*   **point_limit** – (optional. int. min=2) If specified, the returned route will be simplified to contain this number of points (or less).
*   **provider_type** – (optional, string, one of `progorod|google|osrm`) If not specified, the default user provider is used.

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
*   236 (Feature unavailable due to tariff restrictions) – if there is at least one tracker without “routing” tariff feature

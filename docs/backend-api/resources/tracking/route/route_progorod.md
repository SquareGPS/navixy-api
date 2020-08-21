---
title: Tracking route progorod
description: Tracking route progorod
---

# Tracking route progorod

API path: `/tracking/route/progorod`.


### get
Get route points using [Progorod router](https://giswiki.tmcrussia.com/index.php?title=%D0%9C%D0%B0%D1%80%D1%88%D1%80%D1%83%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F).

#### parameters
*   **start** – (location JSON object) start of route
*   **end** – (location JSON object) end of route
*   **waypoints** = \[ ${location}, ... \] – (optional) list of transitional points.
*   **point_limit** – (optional. int. min=2) If specified, the returned route will be simplified to contain this number of points (or less).
*   **minsize** – (optional. double) smoothing parameter in conventional meters. **Default:** 5\. Not recommended to set it less than distance between two neighbouring pixels on current zoom.
*   **use_traffic** – (optional. boolean) **If** it is _false_ **then** use _mode=optimal_ and _use\_traffic=0_ **else** _mode=comfort_ and _use\_traffic=1_. **Default:** _false_.

Where **location** described in [data types description section](../../../getting-started.md#data-types). Order of waypoints may be changed.

#### response
```js
{
    "success": true,
    "distance": 2546, // (int) length in meters
    "time": 194,      // (int) duration in seconds
    "list": [ ${location}, ... ], // list of route points
    "key_points": [ ${key_point}, ... ] 
}
```

**key_points** is list of points corresponding to **start** point, **waypoints** and **end** point (in that sequence). If some of key points not found then they don't listed there. Where **key_point** is JSON object:
```js
{
    "id": 123,        // (int) index in points 'list'
    "lat": 56.827,    // latitude
    "lng": 60.594296  // longitude
}
```

#### errors

*   215 (External service error)
*   218 (Malformed external service parameters) – Contains info about error:
```js
{
    "success": false,
    "status": {
        "code": 218,
        "description": "Malformed external service parameters"
    },
    "errors": [{
        "type": "malformed", // type of error. one of: "not_set", "malformed" and "isolated"
        "point": "start",    // error point. one of: "start", "end", "waypoint" and "all"
        "index": 3           // passed only for waypoint. index of bad point in waypoints array
    }]
}
```

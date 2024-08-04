---
title: Getting route with Progorod
description: API call for getting the route to destination point using Progorod router.
---

# Getting route with Progorod

API call for getting the route to destination point using [Progorod router](https://giswiki.tmcrussia.com/index.php?title=%D0%9C%D0%B0%D1%80%D1%88%D1%80%D1%83%D1%82%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F).


## API actions

API path: `/route/progorod`.

### `get`

Gets route points using Progorod router.

#### Parameters

| name        | description                                                                                                                                                    | type                  |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| start       | Location JSON object. Start of route.                                                                                                                          | JSON object           |
| end         | Location JSON object. End of route.                                                                                                                            | JSON object           |
| waypoints   | Optional. List of transitional points. `[{locationA},{locationN}]`.                                                                                            | array of JSON objects |
| point_limit | Optional. If specified, the returned route will be simplified to contain this number of points (or less). Min=2.                                               | int                   |
| minsize     | Optional. Default=5. Smoothing parameter in conventional meters. Not recommended to set it less than distance between two neighbouring pixels on current zoom. | double                |
| use_traffic | Optional. Default=`false` If it is `false` then use `mode=optimal` and use traffic=0, else `mode=comfort` and use traffic=1.                                   | boolean               |

Where **location** described in [data types description section](../../../getting-started/introduction.md#data-types). Order of 
waypoints may be changed.

#### Response

```json
{
    "success": true,
    "distance": 1340584,
    "time": 43500,
    "list": [{"lat": 34.178868, "lng": -118.599672}, {"lat": 31.738386, "lng": -106.453854}],
    "key_points": [{
      "id": 123,
      "lat": 35.365948,
      "lng": -108.112104
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

#### Errors

* 215 - External service error.
* 218 - Malformed external service parameters – Contains info about error:

```json
{
    "success": false,
    "status": {
        "code": 218,
        "description": "Malformed external service parameters"
    },
    "errors": [{
        "type": "malformed",
        "point": "start",
        "index": 3
    }]
}
```

* `type` - [enum](../../../getting-started/introduction.md#data-types). Type of error. One of: "not_set", "malformed" and "isolated".
* `point` - [enum](../../../getting-started/introduction.md#data-types). Error point. One of: "start", "end", "waypoint" and "all".
* `index` - int. Passed only for a waypoint. Index of bad point in waypoints array.

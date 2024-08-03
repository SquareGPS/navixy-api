---
title: Getting route with OSRM
description: API call for getting the route to destination point using OSRM API.
---

# Getting route with OSRM

API call for getting the route to destination point using [OSRM API](https://github.com/Project-OSRM/osrm-backend/wiki/Server-api#requesting-routes).


## API actions

API path: `/route/osrm`.

### `get`

Gets route points via OSRM API.

#### Parameters

| name        | description                                                                                                      | type                  |
|:------------|:-----------------------------------------------------------------------------------------------------------------|:----------------------|
| start       | Location JSON object. Start of route.                                                                            | JSON object           |
| end         | Location JSON object. End of route.                                                                              | JSON object           |
| waypoints   | Optional. List of transitional points. `[{locationA},{locationN}]`.                                              | array of JSON objects |
| point_limit | Optional. If specified, the returned route will be simplified to contain this number of points (or less). Min=2. | int                   |

Where **location** described in [data types description section](../../../getting-started/introduction.md#data-types).

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/route/osrm/get' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "start": {34.178868, "lng": -118.599672}, "end": {35.365948, "lng": -108.112104}}'
    ```

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
* 218 - Malformed external service parameters.
  
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
  
    * `status` - [enum](../../../getting-started/introduction.md#data-types).
        * `NOT_FOUND` – indicates at least one of the locations specified in the request's origin, destination, or 
        waypoints could not be geocoded, or OSRM cannot find route.
        * `UNKNOWN_ERROR` – unexpected OSRM error code.
    * `status_code` - int. OSRM status code (don't rely on it).
    * `message` - string. OSRM error message (don't rely on it).
    
* 236 - Feature unavailable due to tariff restrictions – if there is at least one tracker without "routing" tariff 
feature.

---
title: Getting the route with Google
description: API call for getting the route to destination point using Google Directions API.
---

# Getting the route with Google

API call for getting the route to destination point using [Google Directions API](https://developers.google.com/maps/documentation/directions/intro).


## API actions

API path: `/route/google`.

### `get`

Gets route points using Google Directions API.

#### Parameters

| name        | description                                                                                                      | type                  |
|:------------|:-----------------------------------------------------------------------------------------------------------------|:----------------------|
| start       | Location JSON object. Start of route.                                                                            | JSON object           |
| end         | Location JSON object. End of route.                                                                              | JSON object           |
| waypoints   | Optional. List of transitional points. `[{locationA},{locationN}]`.                                              | array of JSON objects |
| point_limit | Optional. If specified, the returned route will be simplified to contain this number of points (or less). Min=2. | int                   |

Where **location** described in [data types description section](../../../getting-started/introduction.md#data-types).

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/route/google/get' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "start": {"lat": 34.178868, "lng": -118.599672}, "end": {"lat": 31.738386, "lng": -106.453854}}'
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
      "lng": -108.112104,
      "distance": 1052511,
      "time": 37800
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
    * `distance` - int. Length of full path from start in meters (0 for start point).
    * `time` - int. Duration of full path from start in seconds (0 for start point).
    

#### Errors

215 - External service error.

```json
    {
        "success": false,
        "status": {
            "code": 215,
            "description": "External service error"
        },
        "errors": ["OVER_QUERY_LIMIT"]
    }
```

* `errors` - [enum](../../../getting-started/introduction.md#data-types) array. Status. 
    *   `OVER_QUERY_LIMIT` – indicates the service has received too many requests from your application within the 
    allowed time period.
    *   `REQUEST_DENIED` – indicates that the service denied use of the directions service by your application.
    *   `UNKNOWN_ERROR` – indicates directions request could not be processed due to a server error. The request may 
    succeed if you try again.

218 - Malformed external service parameters.

```json
    {
        "success": false,
        "status": {
            "code": 218,
            "description": "Malformed external service parameters"
        },
        "errors": ["NOT_FOUND"]
    }
```

* `errors` - [enum](../../../getting-started/introduction.md#data-types) array. Status.
    *   `NOT_FOUND` – indicates at least one of the locations specified in the request's origin, destination, or 
    waypoints could not be geocoded.
    *   `ZERO_RESULTS` – indicates no route could be found between the origin and destination.
    *   `MAX_WAYPOINTS_EXCEEDED` – indicates that too many waypoints provided in the request. The maximum allowed 
    waypoints is 8, plus the origin, and destination. Google Maps API for Business customers may contain requests with 
    up to 23 waypoints.
    *   `INVALID_REQUEST` – indicates that the provided request was invalid. Common causes of this status include 
    an invalid parameter or parameter value.

236 - Feature unavailable due to tariff restrictions – if there is at least one tracker without "routing" tariff 
feature.

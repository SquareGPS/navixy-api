---
title: Getting route
description: API call for getting the route to destination point.
---

# Getting route

API call for getting the route to destination point.


## API actions

API path: `/route`.

### `get`

Gets route points via specified route provider.

#### Parameters

| name          | description                                                                                                      | type                                           |
|:--------------|:-----------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|
| start         | Location JSON object. Start of route.                                                                            | JSON object                                    |
| end           | Location JSON object. End of route.                                                                              | JSON object                                    |
| waypoints     | Optional. List of transitional points. `[{locationA},{locationN}]`.                                              | array of JSON objects                          |
| point_limit   | Optional. If specified, the returned route will be simplified to contain this number of points (or less). Min=2. | int                                            |
| provider_type | Optional. If not specified, the default user provider is used. One of "progorod", or "google", "osrm".           | [enum](../../../getting-started/introduction.md#data-types) |

* `location` object described in [data types description section](../../../getting-started/introduction.md#data-types).

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/route/get' \
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
* 236 - Feature unavailable due to tariff restrictions – if there is at least one tracker without "routing" tariff feature.

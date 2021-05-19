---
title: Tracking route
description: API call for getting the route to destination point.
---

# Tracking route

API path: `/route`.

API call for getting the route to destination point.

### get

Gets route points via specified route provider.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| start | Location JSON object. Start of route. | JSON object |
| end | Location JSON object. End of route. | JSON object |
| waypoints | Optional. List of transitional points. `[{locationA},{locationN}]`. | array of JSON objects |
| point_limit | Optional. If specified, the returned route will be simplified to contain this number of points (or less). Min=2. | int |
| provider_type | Optional. If not specified, the default user provider is used. One of "progorod", or "google", "osrm". | [enum](../../../getting-started.md#data-types) |

* `location` object described in [data types description section](../../../getting-started.md#data-types).

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/route/get' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "start": {"lat": 56.827001, "lng": 60.594296}, "end": {"lat": 52.835601, "lng": 60.514721}}'
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

* 215 - External service error.
* 218 - Malformed external service parameters.
* 236 - Feature unavailable due to tariff restrictions – if there is at least one tracker without "routing" tariff feature.

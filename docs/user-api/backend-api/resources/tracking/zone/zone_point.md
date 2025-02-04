---
title: Geofence point
description: All actions to retrieve and manipulate points of the geofence.
---

# Geofence point

All actions to retrieve and manipulate points of the geofence. Note that `circle` geofence type can't have points.


## Point object structure

```json
{
  "lat": 11.0,
  "lng": 22.0,
  "node": true
}
```

* `lat` - float. Point latitude.
* `lng` - float. Point latitude.
* `node` - boolean. Will be `true` if this point is a route node.


## API actions

API base path: `/zone/point`.

### `list`

Get points of user's geofence with `zone_id`.

#### Parameters

| name    | description                                                                                    | type | format  |
|:--------|:-----------------------------------------------------------------------------------------------|:-----|:--------|
| zone_id | ID of a geofence.                                                                              | int  | 1234567 |
| count   | Optional. If specified, the returned list will be simplified to contain this number of points. | int  | 300     |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/point/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone_id": 1234567}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/zone/point/list?hash=a6aa75587e5c59c32d347da438505fc3&zone_id=1234567
    ```

#### Response

```json
{
    "success": true,
    "list": [{
      "lat": 11.0,
      "lng": 22.0,
      "node": true
    }]
}
```

* `list` - array of objects. List of point objects. 

#### Errors

* 201 - Not found in the database – if geofence with the specified ID cannot be found or belongs to another user.
* 230 - Not supported for this entity type – if geofence cannot have any points associated with it (e.g. if geofence is circle).


### `update`

Update points for user's geofence with `zone_id`.

**required sub-user rights**: `zone_update`.

#### Parameters

| name    | description                                                                                                                 | type                  |
|:--------|:----------------------------------------------------------------------------------------------------------------------------|:----------------------|
| zone_id | ID of a geofence.                                                                                                           | int                   |
| points  | Array of new points for this geofence. Must contain at least 3 elements. Maximum number of points depends on geofence type. | array of JSON objects |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/point/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone_id": 1234567, "points": [{"lat": 11.0, "lng": 22.0, "node": true},{"lat": 11.2, "lng": 22.2, "node": true},{"lat": 11.4, "lng": 22.4, "node": true}]}'
    ```

#### Response

```json
{ 
  "success": true
}
```

#### Errors

* 201 - Not found in the database – if geofence with the specified ID cannot be found or belongs to another user.
* 202 - Too many points in a geofence – if "points" array size exceeds limit for this geofence type. Max allowed points count 
  for a geofence is 500 for a polygon or 1024 for a sausage.
* 230 - Not supported for this entity type – if geofence cannot have any points associated with it (e.g., if geofence is circle).
* 284 - Not enough points for the zone. The minimum number of points for polygon: 3; the minimum for sausage: 2.

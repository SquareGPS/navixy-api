---
title: Zone point
description: Zone point
---

# Zone point

API base path: `/zone/point`.

All actions to retrieve and manipulate points of the zone. Note that “circle” zone type cannot have points.

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

### list

Get points of user’s zone with `zone_id`.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| zone_id | Id of a zone. | int | 1234567 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/point/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone_id": "1234567"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/zone/point/list?hash=a6aa75587e5c59c32d347da438505fc3&zone_id=1234567
    ```

#### response
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

#### errors
* 201 (Not found in the database) – if zone with the specified ID cannot be found or belongs to another user.
* 230 (Not supported for this entity type) – if zone cannot have any points associated with it (e.g. if zone is circle).

### update

Update points for user’s zone with `zone_id`.

**required sub-user rights**: `zone_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| zone_id | Id of a zone. | int |
| points | Array of new points for this zone. Must contain at least 3 elements. Maximum number of points depends on zone type. | array of JSON objects |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/zone/point/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "zone_id": "1234567", "points": [{"lat": 11.0, "lng": 22.0, "node": true},{"lat": 11.2, "lng": 22.2, "node": true},{"lat": 11.4, "lng": 22.4, "node": true}]}'
    ```

#### response
```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if zone with the specified ID cannot be found or belongs to another user.
* 202 (Too many points in a zone) – if “points” array size exceeds limit for this zone type. Max allowed points count 
for a zone is 100 for a polygon or 1024 for sausage.
* 230 (Not supported for this entity type) – if zone cannot have any points associated with it (e.g. if zone is circle).

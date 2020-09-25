---
title: Zone point
description: Zone point
---

# Zone point

API base path: `/zone/point`.

All actions to retrieve and manipulate points of the zone. Note that “circle” zone type cannot have points.

```json
<point> =
    {
        "lat": <point latitude, e.g. 11.0>, //float
        "lng": <point longitude 22.0>, //float
        "node": <true if this point is a route node> //bool
    }
```

### list

Get points of user’s zone with ID = `<zone_id>`

#### parameters

*   zone_id

#### response
```json
{
    "success": true,
    "list": [ <point>, ... ]
}
```

#### errors
*   201 (Not found in database) – if zone with the specified ID cannot be found or belongs to another user
*   230 (Not supported for this entity type) – if zone cannot have any points associated with it (e.g. if zone is circle)

### update
Update points for user’s zone with ID = `<zone_id>`.

**required subuser rights**: zone_update

#### parameters

*   **zone_id** (Int) – ID of the zone. Specified zone must support points. (e.g. it cannot be circle)
*   **points** (<point>[]) – Array of new points for this zone. Must contain at least 3 elements. Maximum number of points depends on zone type.

#### response
```json
{ "success": true }
```

#### errors

*   201 (Not found in database) – if zone with the specified ID cannot be found or belongs to another user
*   202 (Too many points in zone) – if “points” array size exceeds limit for this zone type. Max allowed points count for zone is 100 for polygon or 1024 for sausage
*   230 (Not supported for this entity type) – if zone cannot have any points associated with it (e.g. if zone is circle)

---
title: /lbs
description: /lbs
---

## read()
Get LBS for the specified tracker.

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return:
```javascript
{
    "success": true,
    "max_radius": <int>  //max allowed radius for LBS points
}
```

#### errors:
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

## update()
Update LBS settings for the specified tracker.

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **max_radius** - **int**. See read(…). min=0, max=10000

#### return:
```javascript
{"success": true}
```

#### errors:
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

---
title: /settings
description: /settings
---

### read
Get base settings for the specified tracker.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return
```javascript
{
    "success": true,
    "settings": {
        "label": <string>, // user-defined label for this tracker, e.g. "Courier"
        "group_id": <int>  // tracker group id, 0 if tracker does not belong to any group
    }
}
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)


### update
Update the settings of the specified tracker.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **group_id** - **int**. Tracker group id, 0 if tracker does not belong to any group. The specified group must exist.
* **label** - **string**. User-defined label for this tracker, e.g. “Courier”. Must consist of prontable characters and have length between 1 and 60. Cannot contain ‘<‘ and ‘>’ symbols.

#### return
```javascript
{ "success": true }
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   204 – Entity not found (if there is no group with the specified group id)


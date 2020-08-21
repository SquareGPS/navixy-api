---
title: /unconfirmed
description: /unconfirmed
---

API base path: `/tracker/command/unconfirmed`

### count
Get number of commands in queue for the specified tracker.

#### parameters
* **tracker_id** - **int**.  Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### response
```json5
{
    "success": true,
    "count": <number of commands, e.g. 0> //int
}
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

### reset
Remove all pending SMS commands from the queue for the specified tracker.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### response

```json5
{ "success": true }
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

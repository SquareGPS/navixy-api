---
title: /led
description: /led
---

## read()
Get LED status for the specified tracker.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return
```javascript
{
    "success": true,
    "value": true    // LED status, true - ON, false - OFF
}
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device

## update()
Switch LED state for a specified tracker.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **value** - **boolean**. new LED state, true – ON, false – OFF

#### return

```json
{ "success": true }
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device


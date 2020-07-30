---
title: /stats/engine_hours
description: /stats/engine_hours
---

# /tracker/stats/engine_hours

## read()
Returns engine hours (time when engine is on) count in specified period.

#### parameters
*   **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
*   **from** - **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone).
*   **to** - **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). Specified date must be after "from" date.

#### return
```json
{
    "success": true,
    "value": 42.0
}
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   211 – Requested time span is too big (if interval between "from" and "to" is too big (maximum value is specified in API config))
*   214 – Requested operation or parameters are not supported by the device (if device does not have ignition input)
*   219 – Not allowed for clones of the device (if specified tracker is a clone)

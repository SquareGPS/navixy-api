---
title: /readings
description: /readings
---

API base path: `/tracker/readings`

### list
Get last values for all metering sensors and state values

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### response
```js
{
  "success": true,
  "inputs": [
    {
            "value": 5.66, // float
            "label": "", // string
            "units": "", // string
            "name": "fuel_level",
            "type": "fuel",
            "units_type": "custom",
            "update_time": "2019-03-16 11:15:19"
        },
    ...
  ],
  "states": [
    {
       "field": "obd_mil_status",
       "value": false,  // string | int | float | bool | null
       "update_time": "2019-03-16 11:15:19"
    },
    ...
  ]
}
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)


---
title: /apn_settings
description: /apn_settings
---

## read()
Returns APN settings for the tracker.

#### parameters:
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return:
```json
{
    "success": true,
    "value": {
        "name":"internet",
        "user":"",
        "password":""
    }
}
```

#### errors:
*   201 – Not found in database (if tracker or APN settings are not found)
*   208 – Device blocked
*   214 – Requested operation not supported by the device (if the tracker does not have a GSM module or uses a bundled SIM card, the number of which is hidden from the user)

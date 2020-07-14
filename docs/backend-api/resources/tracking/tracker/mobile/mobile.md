---
title: /mobile
description: /mobile
---

## register()
**IMPORTANT**

**This call is deprecated!** Use tracker/register(..)

Register new mobile client application.

**required subuser rights:** tracker_register

#### parameters:
Part of parameters are registration plugin-specific. See “Registration plugins” section.

Common parameters are:
* **label** - **string**. User-defined label for this tracker, e.g. “Сourier”. Must consist of prontable characters and have length between 1 and 60.
* **group_id** - **int**. Tracker group id, 0 if tracker does not belong to any group. The specified group must exist.
* **device_id** - **string**. Device IMEI.

#### return:
```javascript
{
    "success": true,
    "value": <tracker> //a newly created tracker
}
```

#### errors:
*   13 – Operation not permitted – if user has insufficient rights
*   204 – Entity not found (if specified group does not exist)
*   221 – Device limit exceeded (if device limit set for the user’s dealer has been exceeded)
*   224 – Device ID already in use (if specified device ID already registered in the system)
*   225 – Not allowed for this legal type (if tariff of the new device is not compatible with user’s legal type)

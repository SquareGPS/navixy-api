---
title: /tracking
description: /tracking
---

## read()
Get tracking settings for the specified tracker.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return
Returned fields may differ from model to model. See tracking profiles for more information.
```javascript
{
    "success": true,
    "value" : <tracking settings>
}
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device (if device model has no tracking settings at all)

## update()
Send new tracking settings to the specified tracker.

**required subuser rights:** tracker_configure

#### parameters
* **tracker_id** - **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **tracking_settings** - **JSON object**. [tracking profiles](./tracking_profiles.md).
`<tracking settings>` is a set of fields which differ from model to model. See tracking profiles for more information.

#### return
Returned fields may differ from model to model. See tracking profiles for more information.
```javascript
{ "success": true }
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device (if device model has no tracking settings at all)
*   219 – Not allowed for clones of the device (if specified tracker is clone of another tracker)

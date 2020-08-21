---
title: /engine_immobilizer
description: /engine_immobilizer
---

API base path: `/tracker/engine_immobilizer`

### read
Request to read the state of engine immobilizer.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### response
```js
{
   "success": true,
   "enabled": <true if engine immobilizer is enabled> //boolean
}
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device (if device does not support alarm mode)

### set
Request to change the engine immobilizer state of the device. The device must be online.

**required subuser rights:** tracker_set_output

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **enabled** - **boolean**. True if immobilizer should be enabled.

#### response

```json
{ "success": true }
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   213 – Cannot perform action: the device is offline (if corresponding tracker is not connected to the server)
*   214 – Requested operation or parameters are not supported by the device (if device does not support alarm mode)
*   219 – Not allowed for clones of the device (if tracker is clone)


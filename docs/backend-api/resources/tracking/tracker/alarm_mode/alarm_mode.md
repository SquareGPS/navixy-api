---
title: Alarm mode
description: Alarm mode for tracker
---

## read()

Gets the state of alarm mode of device.

#### parameters:

| name | description | type | format |
| :------: | :------: | :-----:| :-----:|
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999199 |

#### example:

```abap
    $ curl -X POST 'https://api.navixy.com/v2/tracker/alarm_mode/read' \
      -H 'Content-Type: application/json' \ 
      -d '{"tracker_id": "999199", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response:

```json
{
   "success": true,
   "enabled": {boolean} // true if alarm mode is enabled
}
```

#### errors:

*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device (if device does not support alarm mode)

## set()

Changes the state of alarm mode of device. The device must be online.

#### parameters:

| name | description | type | format |
| :------: | :------: | :-----:| :-----:|
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999199 |
| enabled |  True if alarm mode should be enabled | boolean | true/false |

#### example:

```abap
    $ curl -X POST 'https://api.navixy.com/v2/tracker/alarm_mode/set' \
      -H 'Content-Type: application/json' \ 
      -d '{"tracker_id": "999199", "enabled": "true", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response:

```json
{"success": true}
```

#### errors:

*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   213 – Cannot perform action: the device is offline (if corresponding tracker is not connected to the server)
*   214 – Requested operation or parameters are not supported by the device (if device does not support alarm mode)
*   219 – Not allowed for clones of the device (if tracker is clone)

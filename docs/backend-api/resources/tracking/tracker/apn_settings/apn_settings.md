---
title: APN settings by tracker ID
description: APN settings by tracker ID
---

## read()

Gets the APN name/user/password and mobile operator of device by tracker_id.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 999199 |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/fsm/tracker/apn_settings/read' \
-H 'Content-Type: application/json' \ 
-d '{"tracker_id": "999199", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```
#### response

```json
{
    "success": true,
    "value": {
        "name":"fast.tmobile.com",
        "user":"tmobile",
        "password":"tmobile"
    }
}
```

#### errors

* 201 – Not found in database (if tracker or APN settings are not found)
* 208 – Device blocked
* 214 – Requested operation not supported by the device (if the tracker does not have a GSM module or uses a bundled SIM card, the number of which is hidden from the user)

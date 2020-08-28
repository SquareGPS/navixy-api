---
title: APN settings by tracker ID
description: APN settings by tracker ID
---
# APN settings by tracker ID

API base path: `/tracker/apn_settings`

APN is short of Access Point Name and provides a device with the information needed to connect to wireless service. Using this call you can get APN settings by a tracker ID.

### read

Gets the APN name/user/password and mobile operator of device by a tracker_id.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 999199 |

#### examples

=== "HTTP POST application/json

```abap
curl -X POST '{{ extra.api_example_url }}/tracker/apn_settings/read' \
    -H 'Content-Type: application/json' \ 
    -d '{"tracker_id": "123456", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

=== "GET"

```abap
{{ extra.api_example_url }}/tracker/apn_settings/read?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
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

* 201 – Not found in the database (if tracker or APN settings not found).
* 208 – Device blocked.
* 214 – Requested operation not supported by the device (if the tracker does not have a GSM module or uses a bundled SIM card, the number of which is hidden from the user).

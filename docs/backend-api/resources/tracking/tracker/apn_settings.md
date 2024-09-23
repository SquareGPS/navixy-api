---
title: APN settings by tracker ID
description: Contains API call to get APN settings by tracker ID.
---
# APN settings by tracker ID

This resource contains API call to get APN settings by tracker ID. APN is short of Access Point Name and provides a device 
with the information needed to connect to wireless service. 


## API actions

API base path: `/tracker/apn_settings`.

### `read`

Gets the APN name/user/password and mobile operator of device by a `tracker_id`.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 999199 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/apn_settings/read' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/apn_settings/read?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

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

#### Errors

* 201 – Not found in the database - if tracker or APN settings not found.
* 208 – Device blocked.
* 214 – Requested operation not supported by the device - if the tracker does not have a GSM module or uses a bundled SIM
 card, the number of which is hidden from the user.

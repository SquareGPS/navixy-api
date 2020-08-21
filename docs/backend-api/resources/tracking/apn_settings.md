---
title: APN settings of tracker
description: APN settings of tracker
---

# APN settings

API base path: `/apn_settings`.

### read

Gets the APN name/user/password and mobile operator for registered device by phone number.

#### parameters

| name | description | type | format |
| :------: | :------: | :-----:| :-----:|
| phone | string representing valid international phone number without '+' sign | int | 1234567890 |

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/apn_settings/read' \
  -H 'Content-Type: application/json' \ 
  -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "phone": "3389665944572"}' 
```

#### response

```json5
    {
        "success": true,
        "value": {
            "name":"internet",
            "user":"",
            "password":"",
            "operator_name":"Deutsche Telekom"
        }
    }
```

#### errors

*   201 – The phone number not found in database

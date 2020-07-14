---
title: /apn_settings
description: /apn_settings
---

## read(…)

Gets APN, user, password, operatorName by phone number

#### structure:

    [api_base_url]/apn_settings/read?hash=your_hash&phone=phone_number

#### parameters:

| name | description | type | format |
| :------: | :------: | :-----:| :-----:|
| phone | string representing valid international phone number without '+' sign | int | 1234567890 |

#### example:

    [api_base_url]/apn_settings/read?hash=22eac1c27af4be7b9d04da2ce1af111b&phone=3389665944572

#### response:

```javascript
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

#### errors:

*   201 – Not found in database
---
title: APN settings of tracker
description: APN settings of tracker
---

## Get APN settings of tracker

### read(...)

Gets APN, APN user, APN password, Operator Name for registered device by phone number

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

*   201 – The phone number not found in database

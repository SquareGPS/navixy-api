---
title: APN settings of tracker
description: API call to get APN settings by device's phone number.
---

# APN settings

API base path: `/apn_settings`.

API call to get APN settings by device's phone number.

### read

Gets the APN name/user/password and mobile operator for registered device by phone number.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| phone | string representing valid international phone number without `+` sign. | string | "1234567890" |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/apn_settings/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "phone": "1234567890"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/apn_settings/read?hash=a6aa75587e5c59c32d347da438505fc3&phone=1234567890
    ```

#### response

```json
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

* 201 – The phone number not found in the database.

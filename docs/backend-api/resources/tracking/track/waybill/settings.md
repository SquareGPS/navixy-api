---
title: Waybill settings
description: Contains API call to get the last waybill number.
---

# Waybill settings

Contains API call to get the last waybill number. Waybill number saved when new waybill had downloaded. If it had only digits, 
then it was incremented before saving.


## API actions

API base path: `track/waybill/settings/`.

### `read`

Gets last waybill number. 

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/track/waybill/settings/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/track/waybill/settings/read?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "value": {
        "number": "test123"
    }
}
```

#### Errors

* 201 - Not found in the database – if user have never downloaded a waybill.

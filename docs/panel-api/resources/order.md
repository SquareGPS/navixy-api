---
title: Order
description: Contains API call to read the order by its ID.
---

# Order

API call to read the order by its ID.


## API actions

API path: `panel/order`.

### `read`

Reads order by specified ID.

*required permissions*: `tracker_bundles: "read"`.

#### Parameters

| name     | description | type |
|:---------|:------------|:-----|
| order_id | Order ID.   | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/order/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "order_id": 12341}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/order/read?hash=fa7bf873fab9333144e171372a321b06&order_id=12341
    ```

#### Response

```json
    {
      "success": true,
      "value": {
        "id": 3,
        "user_id": 11346,
        "seller_id": 1,
        "amount": 1,
        "sum": 34300.00,
        "type": "equip",
        "payer": "Leonard Bernstein",
        "recipient": "Leonard Bernstein",
        "contacts": "",
        "place": "111111 Leipzig, Leipzig Tieckstrasse, 2",
        "comment": "",
        "creation_time": "2009-12-10 01:00:36",
        "status": "created",
        "bundles": [
          {
            "id": 2,
            "equip_id": 117,
            "equip_vendor": "Trackers of different manufacturers",
            "equip_name": "GPS/GSM terminal Teltonika FM1100",
            "equip_model": "FM1200",
            "model_code": "gv500",
            "imei": "355085050027285",
            "iccid": "89701010064407635201",
            "assign_time": "2014-12-15 13:42:54",
            "order_id": 3
          }
        ]
      }
    }
```

#### Errors

* 201 – Not found in the database - if specified order does not exist.
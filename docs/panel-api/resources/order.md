---
title: /order
description: /order
---

## read()

Read order by ID

#### parameters

*   **order_id** – **int**. Order ID

#### required permissions:

*   **tracker_bundles**: "read"

#### return

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


#### errors

*   201 – Not found in database (if specified order does not exist)
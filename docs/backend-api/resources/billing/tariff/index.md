---
title: Tariff
description: Tariff
---

# Tariff

API path: `/tariff`.

#### Tariff JSON object structure:

```json5
{
    "id": 10, // (int) unique id
    "name": "Business", // (string) tariff description
    "group_id": 2, // (int) group of tariffs. user can change the tariff only on the tariff in the same group.
    "active": true, // (boolean). user can change the tariff only on the active tariff.
    "type": "monthly", // (string). tariff type. one of: "monthly", "everyday", "activeday"
    "price": 13.0, // (double). price per month for "monthly" and "everyday" tariff or price per "active" day for "activeday" tariff
    "early_change_price": 23.0, // (double) price of change tariff from current to other
            // with the last change in less than 30 days (**tariff.freeze.period** config option).
            // When not passed or "null" user cannot change tariff frequently.
    "device_limit": 1000, // (int) maximum number of devices per account
    "has_reports" : true // (boolean) true if reports are allowed, false otherwise
    "paas_free": false, // (boolean) true if this tariff is free for PaaS owner, false otherwise
    "store_period": "12m", // data storage period, e.g. "2h" (2 hours), "3d" (3 days), "5m" (5 months), "1y" (one year)
    "features": [
        "map_layers"
    ],
    "map_filter": {
        "exclusion": true,
        "values": []
    }
}
```



### list

Get list of device’s tariffs available to user.<br>
If user’s dealer if **default dealer** or **paas** then listed tariffs of that dealer<br>
else listed tariffs of parent dealer.<br>
Listed only tariffs [available for user’s legal type](#tariff).

#### parameters

* **device_type** – (string) one of ‘tracker’, ‘camera’ or ‘socket’.

#### response
```json5
{
  "success": true,
  "list": [${tariff}, ...] // list of JSON objects
}
```

See **tariff** object structure [here](#tariff).

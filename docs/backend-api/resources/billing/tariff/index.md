---
title: Tariff
description: Tariff object description and API call to get the list of device's tariffs available to user.
---

# Tariff

Tariff object description and API call to get the list of device's tariffs available to user.

<hr>

## Tariff object

```json
{
    "id": 10,
    "name": "Business",
    "group_id": 2,
    "active": true,
    "type": "monthly",
    "price": 13.0,
    "early_change_price": 23.0,
    "device_limit": 1000,
    "has_reports" : true,
    "paas_free": false,
    "store_period": "12m",
    "auto_prolong":true,
    "features": [
        "map_layers"
    ],
    "map_filter": {
        "exclusion": true,
        "values": []
    }
}
```

* `id` - int. Unique id.
* `name` - string. Tariff's label.
* `group_id` - int. Group of tariffs. User can change the tariff only on the tariff in the same group.
* `active` - boolean. Tariff is active if `true`. User can change the tariff only on the active tariff.
* `type` - [enum](../../../getting-started.md#data-types). Tariff type. Can be "monthly", "everyday", "activeday".
* `price` - double. Price per month for "monthly" and "everyday" tariff or price per "active" day for "activeday" tariff.
* `early_change_price` - double. Price of change tariff from current to other. With the last change in less than 
30 days (**tariff.freeze.period** config option). When not passed or "null" user cannot change tariff frequently.
* `device_limit` - int. Maximum number of devices per account.
* `has_reports` - boolean. `true` if reports allowed, `false` otherwise.
* `paas_free` - boolean. `true` if this tariff is free for PaaS owner, `false` otherwise.
* `store_period` - string. Data storage period, e.g. "2h" (2 hours), "3d" (3 days), "5m" (5 months), "1y" (one year).
* `auto_prolong` - boolean. `true` if this tariff plan prolongs automatically.
* `features` - string array. Available features for the user.
* `map_filter` - object with available maps for the user.
    * `exclusion` - boolean. If `true` maps from `values` will be not active, `false` - maps from values will be active.

<hr>

## API actions

API path: `/tariff`.

### list

Gets list of device's tariffs available to user.<br>
If user's dealer is **default dealer** or **paas** then listed tariffs of that dealer, else listed tariffs of parent dealer.<br>
Listed only tariffs [available for user's legal type](#tariff).

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tariff/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tariff/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
  "success": true,
  "list": [{
       "id": 10,
       "name": "Business",
       "group_id": 2,
       "active": true,
       "type": "monthly",
       "price": 13.0,
       "early_change_price": 23.0,
       "device_limit": 1000,
       "has_reports" : true,
       "paas_free": false,
       "store_period": "12m",
       "auto_prolong":true,
       "features": [
           "map_layers"
       ],
       "map_filter": {
           "exclusion": true,
           "values": []
       }
  }] 
}
```

* `list` - array of objects. List of [tariff objects](#tariff-object).

#### errors

* [General](../../../getting-started.md#error-codes) types only.


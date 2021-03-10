---
title: Tariff
description: API calls for interaction with tariff plans.
---

# Tariff

API calls for interaction with tariff plans.

API path: `panel/tariff`

## Tariff object

```json
{
    "id": 12163,
    "name": "Premium",
    "group_id": 3,
    "active": true,
    "type": "monthly",
    "price": 12.55,
    "early_change_price": 23.0,
    "device_limit": 2000,
    "has_reports": true,
    "store_period": "1y",
    "device_type": "tracker",
    "proportional_charge": false,
    "service_prices": {
      "incoming_sms": 0.3, 
      "outgoing_sms": 0.3, 
      "service_sms": 0.2,  
      "phone_call": 0.6,   
      "traffic": 0.09
    }
}
``` 

* `id` - int. Tariff ID.
* `name` - string. Tariff name.
* `group_id` - int. Tariff group number.
* `active` - boolean. `true` if user allowed change his current tariff to this one.
* `type` - [enum](../../backend-api/getting-started.md#data-types). Type of tariff. Can be "monthly" or "activeday" 
(for "tracker" device_type only).
* `price` - double. Tariff subscription price (usually per month).
* `early_change_price` - double. Price of change tariff from current to other. With the last change in less than 30 days
 (`tariff.freeze.period` config option). When not passed or `null` user cannot change tariff frequently.
* `device_limit` - int. A maximum limit of devices per user. Not used for cameras and sockets.
* `has_reports` - boolean. If `true` the tariff has reports.
* `store_period` - string. Data storage period, e.g. "2h" (2 hours), "3d" (3 days), "5m" (5 months), "1y" (one year).
* `device_type` - [enum](../../backend-api/getting-started.md#data-types). Device type. Can be "tracker", "camera" or "socket".
* `proportional_charge` - boolean. `true` if monthly fee will be smaller when device was blocked during month (for "monthly" tariffs only).
* `service_prices` - JSON object with service prices.
    * `incoming_sms` - double. Incoming sms price.
    * `outgoing_sms` - double. Outgoing sms price.
    * `service_sms` - double. Service sms price.
    * `phone_call` - double. Phone voice notification sms price.
    * `traffic` - double. Traffic price per 1 MB.
    
### create

Creates a new tariff.

*required permissions*: `"tariffs": "create"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tariff | Tariff object without ID field. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tariff": {"name": "Premium", "group_id": 3, "active": true, "type": "monthly", "price": 12.55, "early_change_price": 23.0, "device_limit": 2000, "has_reports": true, "store_period": "1y", "device_type": "tracker", "proportional_charge": false, "service_prices": {"incoming_sms": 0.3, "outgoing_sms": 0.3, "service_sms": 0.2, "phone_call": 0.6, "traffic": 0.09}}}'
    ```

#### response

```json
{
    "success": true,
    "id" : 123568
}
```

* `id` - int. An id of the created tariff.

#### errors

* 201 – Not found in the database - if specified tariff does not exist or belongs to different dealer.
* 214 – Requested operation or parameters are not supported by the device - when `device_type` does not support specified tariff `type`.
* 244 – Duplicate entity label - if there's another dealer's tariff with the same `name`.

### list

Returns list of all tariffs belonging to dealer.

If "filter" is used, entities will be returned only if filter string contains one of the following fields:
`id`, `name`, `price`, `device_type`.

*required permissions*: `"tariffs": "read"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| device_type | Optional. Filter by device type. One of "tracker", "camera" or "socket". | [enum](../../backend-api/getting-started.md#data-types) |
| filter | Optional. Text filter. | string |
| order_by | Optional. List ordering. One of: `id`, `name`, `device_type`, `group_id`, `price`. | string |
| ascending | Optional. Default is `true`. If `true`, ordering will be ascending, descending otherwise. | boolean |
| offset | Optional. Default is `0`. Starting offset, used for pagination. | int |
| limit | Optional. Max number of records to return, used for pagination. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tariff/list?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
    "success": true,
    "list" : [{
       "id": 12163,
       "name": "Premium",
       "group_id": 3,
       "active": true,
       "type": "monthly",
       "price": 12.55,
       "early_change_price": 23.0,
       "device_limit": 2000,
       "has_reports": true,
       "store_period": "1y",
       "device_type": "tracker",
       "proportional_charge": false,
       "service_prices": {
         "incoming_sms": 0.3, 
         "outgoing_sms": 0.3, 
         "service_sms": 0.2,  
         "phone_call": 0.6,   
         "traffic": 0.09
       }
    }],
    "wholesale_service_prices" : {
       "incoming_sms": 0.27, 
       "outgoing_sms": 0.27, 
       "service_sms": 0.17,  
       "phone_call": 0.55,   
       "traffic": 0.05
    }
    "count" : 42
}
```

* `list` - objects array. List of tariff plans. See tariff object [here](#tariff-object).
* `wholesale_service_prices` - JSON object. Wholesale prices for all services (what dealer will pay per sms, per call, per mb).
* `count` - int. Total number of records (ignoring offset and limit).

### read

Returns tariff with specified id.

*required permissions*: `"tariffs": "read"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tariff_id | Tariff ID to read. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tariff_id": 12163}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tariff/read?hash=fa7bf873fab9333144e171372a321b06&tariff_id=12163
    ```

#### response

```json
{
    "success": true,
    "value": {
        "id": 12163,
        "name": "Premium",
        "group_id": 3,
        "active": true,
        "type": "monthly",
        "price": 12.55,
        "early_change_price": 23.0,
        "device_limit": 2000,
        "has_reports": true,
        "store_period": "1y",
        "device_type": "tracker",
        "proportional_charge": false,
        "service_prices": {
          "incoming_sms": 0.3, 
          "outgoing_sms": 0.3, 
          "service_sms": 0.2,  
          "phone_call": 0.6,   
          "traffic": 0.09
        }
    }
```

* `value` - JSON object. See tariff object [here](#tariff-object).

#### errors

* 201 – Not found in the database - if specified tariff does not exist or belongs to different dealer.

### update

Updates existing tariff.

*required permissions*: `tariffs: "update"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tariff | Tariff object without `device_type` field. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tariff": {"id": 12345, "name": "Premium", "group_id": 3, "active": true, "type": "monthly", "price": 12.55, "early_change_price": 23.0, "device_limit": 2000, "has_reports": true, "store_period": "1y", "proportional_charge": false, "service_prices": {"incoming_sms": 0.3, "outgoing_sms": 0.3, "service_sms": 0.2, "phone_call": 0.6, "traffic": 0.09}}}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 201 – Not found in the database - if specified tariff does not exist or belongs to different dealer.
* 214 – Requested operation or parameters are not supported by the device when `device_type` does not support specified tariff `type`.
* 244 – Duplicate entity label - if there's another dealer's tariff with the same `name`.

## defaults object

```json
{
    "tariff_id": 1234,
    "activation_bonus": 1.1,
    "free_days": 14,
    "free_days_device_limit": 3
}
```

* `tariff_id` - int. An id of the default tariff for this device type.
* `activation_bonus` - double. Activation bonus - money added to bonus balance upon device registration.
* `free_days` - int. Amount of free (without tariff fee) days after device registration.
* `free_days_device_limit` - int. A maximum number of activated user's devices with free period (null means no limit).

### defaults/read

Returns current tariff defaults for trackers and cameras.

*required permissions*: `tariffs: "read"`.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/defaults/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/tariff/defaults/read?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
    "success": true,
    "tracker": {
        "tariff_id": 1234,
        "activation_bonus": 1.1,
        "free_days": 14,
        "free_days_device_limit": 3
    },
    "camera": {
        "tariff_id": 1289,
        "activation_bonus": 0.5,
        "free_days": 7,
        "free_days_device_limit": 3
    }
}
```

#### errors

[General](../../backend-api/getting-started.md#error-codes) types only.

### defaults/update

Updates current tariff defaults for trackers and cameras.

*required permissions*: `tariffs: "update"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tracker | Defaults object with ID field. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/defaults/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker": {"tariff_id": 1234, "activation_bonus": 1.1, "free_days": 14, "free_days_device_limit": 3}}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 239 – New tariff doesn't exist - if tariff with specified id does not exist.
* 237 – Invalid tariff - if new tariff has incompatible device type.
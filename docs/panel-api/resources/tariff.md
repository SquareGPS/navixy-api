---
title: Plan
description: API calls for interaction with user plans.
---

# Plans

API calls for managing user plans within the service platform (PaaS or Sub Paas).


## Plan object

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

* `id` - int. Plan ID.
* `name` - string. Plan name.
* `group_id` - int. Plan group number.
* `active` - boolean. `true` if user allowed change his current plan to this one.
* `type` - [enum](../../user-api/backend-api/getting-started/introduction.md#data-types). Type of plan. Can be "monthly" or "activeday" 
(for "tracker" device_type only).
* `price` - double. Plan subscription price (usually per month).
* `early_change_price` - double. Price of change plan from current to another. With the last change in less than 30 days
 (`tariff.freeze.period` config option). When not passed or `null` user cannot change plan frequently.
* `device_limit` - int. A maximum limit of devices per user. Not used for cameras and sockets.
* `has_reports` - boolean. If `true` the plan has reports.
* `store_period` - string. Data storage period, e.g. "2h" (2 hours), "3d" (3 days), "5m" (5 months), "1y" (one year).
* `device_type` - [enum](../../user-api/backend-api/getting-started/introduction.md#data-types). Device type. Can be "tracker", "camera" or "socket".
* `proportional_charge` - boolean. `true` if monthly fee will be smaller when device was blocked during month (for "monthly" tariffs only).
* `service_prices` - JSON object with service prices.
    * `incoming_sms` - double. Incoming sms price.
    * `outgoing_sms` - double. Outgoing sms price.
    * `service_sms` - double. Service sms price.
    * `phone_call` - double. Phone voice notification sms price.
    * `traffic` - double. Traffic price per 1 MB.
  

## API actions

API path: `panel/tariff`.

### `create`

Creates a new plan.

*required permissions*: `"tariffs": "create"`.

#### Parameters

| name   | description                   | type        |
| :----- | :---------------------------- | :---------- |
| tariff | Plan object without ID field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tariff": {"name": "Premium", "group_id": 3, "active": true, "type": "monthly", "price": 12.55, "early_change_price": 23.0, "device_limit": 2000, "has_reports": true, "store_period": "1y", "device_type": "tracker", "proportional_charge": false, "service_prices": {"incoming_sms": 0.3, "outgoing_sms": 0.3, "service_sms": 0.2, "phone_call": 0.6, "traffic": 0.09}}}'
    ```

#### Response

```json
{
    "success": true,
    "id" : 123568
}
```

* `id` - int. An ID of the created plan.

#### Errors

* 201 – Not found in the database - if specified plan does not exist or belongs to different dealer.
* 214 – Requested operation or parameters are not supported by the device - when `device_type` does not support specified plan `type`.
* 244 – Duplicate entity label - if there's another dealer's plan with the same `name`.


### `list`

Returns list of all plans belonging to dealer.

If "filter" is used, entities will be returned only if filter string contains one of the following fields:
`id`, `name`, `price`, `device_type`.

*required permissions*: `"tariffs": "read"`.

#### Parameters

| name        | description                                                                               | type                                                                          |
|:------------|:------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------|
| device_type | Optional. Filter by device type. One of "tracker", "camera" or "socket".                  | [enum](../../user-api/backend-api/getting-started/introduction.md#data-types) |
| filter      | Optional. Text filter.                                                                    | string                                                                        |
| order_by    | Optional. List ordering. One of: `id`, `name`, `device_type`, `group_id`, `price`.        | string                                                                        |
| ascending   | Optional. Default is `true`. If `true`, ordering will be ascending, descending otherwise. | boolean                                                                       |
| offset      | Optional. Default is `0`. Starting offset, used for pagination.                           | int                                                                           |
| limit       | Optional. Max number of records to return, used for pagination.                           | int                                                                           |

#### Examples

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

#### Response

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
    },
    "count" : 42
}
```

* `list` - objects array. List of plans. See plan object [here](#plan-object).
* `wholesale_service_prices` - JSON object. Wholesale prices for all services (what dealer will pay per sms, per call, per mb).
* `count` - int. Total number of records (ignoring offset and limit).


### `read`

Returns plan with specified ID.

*required permissions*: `"tariffs": "read"`.

#### Parameters

| name      | description        | type |
|:----------|:-------------------|:-----|
| tariff_id | Tariff ID to read. | int  |

#### Examples

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

#### Response

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
}
```

* `value` - JSON object. See plan object [here](#plan-object).

#### Errors

* 201 – Not found in the database - if specified plan does not exist or belongs to different dealer.


### `update`

Updates existing plan.

*required permissions*: `tariffs: "update"`.

#### Parameters

| name   | description                                | type        |
|:-------|:-------------------------------------------|:------------|
| tariff | Tariff object without `device_type` field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tariff": {"id": 12345, "name": "Premium", "group_id": 3, "active": true, "type": "monthly", "price": 12.55, "early_change_price": 23.0, "device_limit": 2000, "has_reports": true, "store_period": "1y", "proportional_charge": false, "service_prices": {"incoming_sms": 0.3, "outgoing_sms": 0.3, "service_sms": 0.2, "phone_call": 0.6, "traffic": 0.09}}}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if specified plan does not exist or belongs to different dealer.
* 214 – Requested operation or parameters are not supported by the device when `device_type` does not support specified plan `type`.
* 244 – Duplicate entity label - if there's another dealer's plan with the same `name`.


## defaults object

```json
{
    "tariff_id": 1234,
    "activation_bonus": 1.1,
    "free_days": 14,
    "free_days_device_limit": 3
}
```

* `tariff_id` - int. An ID of the default plan for this device type.
* `activation_bonus` - double. Activation bonus - money added to bonus balance upon device registration.
* `free_days` - int. Amount of free (without a fee) days after device registration.
* `free_days_device_limit` - int. A maximum number of activated user's devices with free period (null means no limit).


### defaults/read

Returns current plan defaults for trackers and cameras.

*required permissions*: `tariffs: "read"`.

#### Parameters

Only session `hash`.

#### Examples

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

#### Response

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

#### Errors

[General](../../user-api/backend-api/getting-started/errors.md#error-codes) types only.


### defaults/update

Updates current plan defaults for trackers and cameras.

*required permissions*: `tariffs: "update"`.

#### Parameters

| name    | description                    | type        |
|:--------|:-------------------------------|:------------|
| tracker | Defaults object with ID field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/tariff/defaults/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "tracker": {"tariff_id": 1234, "activation_bonus": 1.1, "free_days": 14, "free_days_device_limit": 3}}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 239 – New plan doesn't exist - if plan with specified ID does not exist.
* 237 – Invalid plan - if new plan has incompatible device type.
---
title: Activation code
description: API calls for interacting with activation codes used for device registration.
---

# Activation code

API base path: `panel/dealer/activation_code`

## Activation code object

```json
{
    "tariff_id": 12163,
    "bonus_amount": 0,
    "free_days": 14,
    "money_amount": 0,
    "device_type": "tracker",
    "code": "5248654776",
    "activated": false,
    "activation_date": null,
    "device_id": 0,
    "tariff_name": "Tracker demo tariff"
}
```

* `tariff_id` - int. A tariff id.
* `bonus_amount` - int. Bonus that will be added to a user's balance when the device with this code activates.
* `free_days` - int. Count of free days.
* `money_amount` - int. Money that will be added to a user's balance.
* `code` - string. A code value.
* `activated` - boolean. If `true` it is activated.
* `device_id` - int. A device id which activated with this code. It will be `0` if code not activated yet.
* `tariff_name` - string. Tariff name.

### create

Creates specified `count` of activation codes with passed `tariff_id`, `bonus_amount` and `free_days`. Returns count of 
created codes.

*required permissions*: `activation_code: ["read", "create"]`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| count | A count of codes to creation. | int |
| tariff_id | An id of new tariff (must belong to current dealer). | int |
| bonus_amount | A new bonus amount. | int |
| free_days | A new free period. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/activation_code/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "count": 10, "tariff_id": 12457, "bonus_amount": 3, "free_days": 5}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/dealer/activation_code/create?hash=fa7bf873fab9333144e171372a321b06&count=10&tariff_id=12457&bonus_amount=3&free_days=5
    ```

#### response

```json
{
    "success": true,
    "count": 10
}
```

* `count` - int. Count of actually created codes.

#### errors

* 201 - Not found in the database - when tariff with `tariff_id` not found for a current dealer.

### list

Lists all dealer activation codes. If `filter` is used, entities will be returned only if filter string will contain one 
of the following fields: `code`, `tariff_id`, `device_id`, `device_type`. 

*required permissions*: `activation_code: "read"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| filter | Optional. Text filter string. | string |
| order_by | Optional. Specify list ordering. Can be one of "code", "activated", "tariff_id", "tariff_name", "device_type", "money_amount", "bonus_amount", "free_days". | string |
| ascending | Optional. If `true`, ordering will be ascending, descending otherwise. Default is `true`. | boolean |
| offset | Optional. Starting offset, used for pagination. Default is `0`. | int |
| limit | Optional. Max number of records to return, used for pagination. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/activation_code/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/dealer/activation_code/list?hash=fa7bf873fab9333144e171372a321b06
    ```

#### response

```json
{
    "success": true,
    "list": [{
         "tariff_id": 12163,
         "bonus_amount": 0,
         "free_days": 14,
         "money_amount": 0,
         "device_type": "tracker",
         "code": "1201245293",
         "activated": true,
         "activation_date": "2020-11-12 20:00:08",
         "device_id": 464606,
         "tariff_name": "Tracker demo tariff"
    }],
    "count" : 1
}
```

* `list` - array of objects. List of [activation code objects](#activation-code-object).
* `count` - int. Total number of records (ignoring offset and limit).

### update

Changes `tariff_id`, `bonus_amount` and `free_days` for all activation codes which:
* has `code` listed in `codes` parameter.
* belongs to a current dealer.
* not activated yet.
* belongs to the same `device_type` as a new tariff and return count of updated codes.

*required permissions*: `activation_code: "update"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| codes | Codes to update. | string array |
| tariff_id | An id of a new tariff. Have to belong to a current dealer. | int |
| bonus_amount | A new bonus. | int |
| free_days | A new free period | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/activation_code/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06",  "codes": ["12315124", "12451576"], "tariff_id": 12457, "bonus_amount": 3, "free_days": 5}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/dealer/activation_code/update?hash=fa7bf873fab9333144e171372a321b06&codes=["12315124", "12451576"]&tariff_id=12457&bonus_amount=3&free_days=5
    ```

#### response

```json
{
    "success": true,
    "count": 5
}
```

* `count` - int. Count of actually updated codes.

#### errors

* 201 - Not found in the database - when a tariff with `tariff_id` not found for a current dealer.
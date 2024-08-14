---
title: Bill
description: Bill object description and API calls for work with user's bills.
---

# Bill

Bill object description and API calls for work with user's bills.


## Bill object

```json
{
    "order_id": 63602,
    "created": "2012-03-05 11:55:03",
    "sum": 150.0,
    "status": "created",
    "positions": ["The subscription fee for the services of Account W3"],
    "link": "http://bill.navixy.com/xK1QEYK"
}
```

* `order_id` - int. Unique bill ID.
* `created` - [date/time](../../getting-started/introduction.md#data-types). When the bill created.
* `sum` - float. A bill sum in default currency of the panel.
* `status` - [enum](../../getting-started/introduction.md#data-types). Bill order status. Can be one of:
    * `created` – but not settled.
    * `settled`.
    * `canceled`.
* `positions` - string array. List of position names. Usually contains one element for a bill.
* `link` - string. URL to order.


## API actions

API path: `/bill`.

### `create`

Creates a new bill for the user. 

**required sub-user rights**: `payment_create`.

#### Parameters

| name  | description                                  | type   |
|:------|:---------------------------------------------|:-------|
| payer | Some payer description.                      | string |
| sum   | A bill sum in default currency of the panel. | double |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/bill/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "payer": "Jon Doe", "sum": 100.0}'
    ```

#### Response

```json
{
    "success": true,
    "value": 6421
}
```

* `value` - int. Created bill ID.

#### Errors

* 222 – Plugin not found - when plugin **29** not available for user.


### `list`

Shows list of bills with their parameters in array. 

**required sub-user rights**: `payment_create`.

#### Parameters

| name   | description                                                                 | type |
|:-------|:----------------------------------------------------------------------------|:-----|
| limit  | Optional. A maximum number of bills in list. Maximum and default is 10 000. | int  |
| offset | Optional. Get bills starting from `offset`. Default 0.                      | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/bill/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/bill/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "count": 7,
    "bills": [{
      "order_id": 63602,
      "created": "2012-03-05 11:55:03",
      "sum": 150.0,
      "status": "created",
      "positions": ["The subscription fee for the services of Account W3"],
      "link": "http://bill.navixy.com/xK1QEYK"
    }]
}
```

* `count` - int. Total number of bills.
* `bills` - array of objects. A list of [bill objects](#bill-object).

If bill created using [/bill/create](#create) call then **positions** will contain exactly one element.

!!! note "For Standalone version base part of **link** may be changed by **billing.orders.baseUrl** config option."

#### Errors

* 222 – Plugin not found - when plugin **29** not available for user.

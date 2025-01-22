---
title: Tariff tracker
description: API calls on user's actions with tracker tariffs
---

# Tracker plans

API calls on user's actions with tracker plans.

User of **dealer** can switch tracker from the plan **t1** to plan **t2** if:

1. Tracker belongs to user and isn't a **clone**.
2. Tracker's tariff last changed more than **tariff.freeze.period** (config option. default 30 days) ago.
3. **t1.tariff_id** != **t2.tariff_id**, i.e. the new plan must be different from the current.
4. **t1.dealer_id** = **t2.dealer_id** = **dealer.effectiveDealerId**, i.e. current and new plans must belong to user's effective dealer.
5. **t2.active** = **1**, i.e. new plan is **active** (plan's option "Allow users to switch to this plan independently" in **panel** is set **on**).
6. **t1.grouping** = **t2.grouping**, i.e. user can change tariff only within one group of tariffs.
7. **t2.device** = **tracker**, i.e. new plan must be for trackers.
8. The new plan is [available to user's legal type](index.md#plan).

User's **effective dealer** is

1. User's dealer if its **dealer_id** = **defaultDealerId** (config option) or **dogovor_type** = 'paas'.
2. Parent of user's dealer otherwise.


## API actions

API path: `/tariff/tracker/`.

### `change`

Changes plan of tracker (with `tracker_id`) to new plan (with `tariff_id`).

**required sub-user rights**: `admin` (available only to master users).

| name       | description                                                                                    | type |
|:-----------|:-----------------------------------------------------------------------------------------------|:-----|
| tracker_id | ID of a tracking device (aka "object_id"). The tracking device must belong to authorized user. | int  |
| tariff_id  | If of the new plan.                                                                            | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tariff/tracker/change' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 345215, "tariff_id": 12}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tariff/tracker/change?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=345215&tariff_id=12
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if user doesn't have trackers with given `tracker_id`.
* 219 – Not allowed for clones of the device.
* 237 – Invalid plan - if there are no plan with specified `tariff_id` and belongs to user's **effective dealer**.
* 221 - Device limit exceeded – when new plan limit for devices is less than the current count of devices in the account.
* 238 - Changing plan is not allowed – user can't switch tracker to that plan.
* 239 – New plan doesn't exist.
* 240 - Not allowed changing plan too frequently – plan last changed less or equal to 30 days (**tariff.freeze.period** config option).


### `list`

List plans on which user can switch the passed tracker (even when tariff last changed less or equal than **tariff.freeze.period** time ago).

#### Parameters

| name       | description                                                                  | type |
|:-----------|:-----------------------------------------------------------------------------|:-----|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tariff/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 345215}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tariff/tracker/list?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=345215
    ```

#### Response

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
       "features": [
           "map_layers"
       ],
       "map_filter": {
           "exclusion": true,
           "values": []
       }
  }],
  "days_to_next_change": 11
}
```

* `list` - array of objects. List of [plan objects](index.md#plan-object).
* `days_to_next_change` - int. Days to the next free change, or 0 if free change available.

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.
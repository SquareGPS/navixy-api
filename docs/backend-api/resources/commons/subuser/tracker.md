---
title: Subuser tracker
description: Contains API calls to control which tracker is available to which sub-user.
---

# Subuser tracker

Contains API calls to control which tracker is available to which sub-user.


## API actions

API path: `/subuser/tracker`.

### `bind`

Gives access for sub-user to the specified trackers.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                                                                                    | type      |
|:-----------|:---------------------------------------------------------------------------------------------------------------|:----------|
| subuser_id | ID of the sub-user belonging to current account.                                                               | int       |
| trackers   | List of tracker IDs to associate with the specified sub-user. All trackers must belong to current master user. | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/tracker/bind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951, "trackers": [127830]}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/tracker/bind?hash=a6aa75587e5c59c32d347da438505fc3&subuser_id=204951&trackers=[127830]
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.
* 262 – Entries list is missing some entries or contains nonexistent entries – if one or more of specified tracker IDs don't exist.


### `list`

Gets a list of tracker IDs to which this sub-user has access.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                      | type |
|:-----------|:-------------------------------------------------|:-----|
| subuser_id | ID of the sub-user belonging to current account. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/tracker/list?hash=a6aa75587e5c59c32d347da438505fc3&subuser_id=204951
    ```

#### Response

```json
{
    "success": true,
    "list" : [124588]
}
```

* `list` - int array. List of tracker IDs to which this sub-user has access.

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.


### `unbind`

Disables access for sub-user to the specified trackers.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                                                                                    | type      |
|:-----------|:---------------------------------------------------------------------------------------------------------------|:----------|
| subuser_id | ID of the sub-user belonging to current account.                                                               | int       |
| trackers   | List of tracker IDs to associate with the specified sub-user. All trackers must belong to current master user. | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/tracker/unbind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951, "trackers": [127830]}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/tracker/unbind?hash=a6aa75587e5c59c32d347da438505fc3&subuser_id=204951&trackers=[127830]
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without `multilevel_access` tariff feature).
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.
* 262 – Entries list is missing some entries or contains nonexistent entries – if one or more of specified tracker IDs don't exist.

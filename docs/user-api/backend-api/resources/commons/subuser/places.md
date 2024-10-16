---
title: Subuser places
description: Contains API calls to control which places is available to which sub-user.
---

# Subuser places

Contains API calls to control which places is available to which sub-user.


## API actions

API path: `/subuser/places`.

### `bind`

Gives access for sub-user to specified places.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name          | description                                                                                                        | type      |
|:--------------|:-------------------------------------------------------------------------------------------------------------------|:----------|
| subuser_id    | ID of a sub-user belonging to current account.                                                                     | int       |
| access_to_all | Optional. If `true` then sub-user will have access to all places of master user.                                   | boolean   |
| place_ids     | Optional. List of place IDs to associate with a specified sub-user. All places must belong to current master user. | int array |

!!! warning "At least one of **access_to_all** and **place_ids** parameters must be not null."

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/places/bind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951, "access_to_all": false, "place_ids": [7548]}'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – if sub-user/place does not exist or does not belong to current master user.
* 236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without `multilevel_access` tariff feature).

### `unbind`

Disables access for a sub-user to specified places.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                                                                              | type      |
|:-----------|:---------------------------------------------------------------------------------------------------------|:----------|
| subuser_id | ID of a sub-user belonging to current account.                                                           | int       |
| place_ids  | List of place IDs to associate with a specified sub-user. All places must belong to current master user. | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/places/unbind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951, "place_ids": [7548]}'
    ```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – if sub-user/place not exist or does not belong to current master user.
* 236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without `multilevel_access` tariff feature).

### `list_ids`

Gets a list of place IDs to which this sub-user has access.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                    | type |
|:-----------|:-----------------------------------------------|:-----|
| subuser_id | ID of a sub-user belonging to current account. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/places/list_ids' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951}'
    ```

#### Response

```json
{
  "success": true,
  "access_to_all": true,
  "list" : [7548]
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.
* 236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without `multilevel_access` tariff feature).

### `list`

Gets a list of places to which this sub-user has access.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                                                                                                                     | type                                                        |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|
| subuser_id | ID of a sub-user belonging to current account.                                                                                                  | int                                                         |
| filter     | Optional. Filter for place label, description, address, external ID and custom fields.                                                          | string                                                      |
| tag_ids    | Optional. Tag IDs assigned to places. Places found must include all tags from a list.                                                           | int array                                                   |
| offset     | Optional. Offset from start of found places for pagination.                                                                                     | int                                                         |
| limit      | Optional. Limit of found places for pagination.                                                                                                 | int                                                         |
| order      | Optional. Specify list ordering. Can be any of `id`, `label`, `description`, `location`, `external_id`, `assigned_date`. Default order by `id`. | [enum](../../../getting-started/introduction.md#data-types) |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/places/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951, "offset": 0, "limit": 1000}'
    ```

#### Response

```json
{
  "success": true,
  "access_to_all": false,
  "list" : [<place>, ...],
  "count": 12
}
```

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.
* 236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without `multilevel_access` tariff feature).

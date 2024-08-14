---
title: Working status
description: Contains status object and API calls to interact with them.
---

# Working status

Contains status object and API calls to interact with them. Working statuses used to track current activity for employees (in 
fact, of tracking devices owned by employees). The simplest example is "busy" | "not busy". This is a status listing 
consisting of two elements. Different trackers can be assigned different status lists.

Find details on working status usage in our [guides](../../../guides/field-service-management/change-task-statuses.md).


## Status object structure

```json
{
    "id": 5,
    "label": "Busy",
    "color": "E57373"
}
```

* `id` - int. A unique identifier of the working status. Read-only.
* `label` - string. Human-readable label for the working status.
* `color` - string. Hex-representation of RGB color used to display this working status.


## API actions

API base path: `/status/`.

### `create`

Creates new possible working status for the specified working status list.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                          | type        |
|:-----------|:-----------------------------------------------------|:------------|
| listing_id | ID of the list for this working status to attach to. | int         |
| status     | Status object without ID field.                      | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing_id": 12345, "status": {"label": "Busy", "color": "E57373"}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. ID of the created working status.

#### Errors

* 201 - Not found in the database – if listing with the specified ID does not exist.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature 
available.
* 268 - Over quota – if the user's quota for working statuses exceeded.


### `delete`

Deletes working status entry.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name      | description                                            | type |
|:----------|:-------------------------------------------------------|:-----|
| status_id | ID of the working status belonging to authorized user. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "status_id": 123}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/delete?hash=a6aa75587e5c59c32d347da438505fc3&status_id=123
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if working status with the specified ID does not exist.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature 
available.


### `list`

Gets working statuses belonging to the specified status list.

#### Parameters

| name       | description                                          | type |
|:-----------|:-----------------------------------------------------|:-----|
| listing_id | ID of the list for this working status to attach to. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing_id": 12345}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/list?hash=a6aa75587e5c59c32d347da438505fc3&listing_id=12345
    ```

#### Response

```json
{
    "success": true,
    "list":[{
      "id": 5,
      "label": "Busy",
      "color": "E57373"
    },{
      "id": 6,
      "label": "Free",
      "color": "A27373"
    }]
}
```

* `list` - ordered array of <status> objects.

#### Errors

* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff 
feature available.


### `update`

Updates working status properties.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name   | description                  | type        |
|:-------|:-----------------------------|:------------|
| status | Status object with ID field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "status": {"id": 5, "label": "Busy", "color": "E57373"}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if working status with the specified ID does not exist.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" 
tariff feature available.

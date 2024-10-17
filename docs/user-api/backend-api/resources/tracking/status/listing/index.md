---
title: Working status list
description: Contains status listing object and API calls to interact with working status list.
---

# Working status list

Contains status listing object and API calls to interact with status listings. Status listings are lists of possible 
statuses that can be assigned to trackers.


## Status listing object structure

```json
{
    "id": 1,
    "label": "Taxi driver statuses",
    "employee_controlled": true,
    "supervisor_controlled": false,
    "entries": [ 5, 2, 1, 4, 6]
}
```

* `id` - int. A unique identifier of this working status list. Read-only.
* `label` - string. Human-readable label for the working status list.
* `employee_controlled` - boolean. If `true` employees can change their own working status, e.g. using mobile tracking app.
* `supervisor_controlled` - boolean. If `true` supervisors can change working status, e.g. using mobile monitoring app.
* `entries` - int array. List of IDs of working statuses which belong to this list. Order matters, and is preserved.


## API actions

API base path: `/status/listing/`.

### `create`

Creates new empty working status list.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name    | description                                                                                                               | type        |
|:--------|:--------------------------------------------------------------------------------------------------------------------------|:------------|
| listing | [status_listing](index.md#status-listing-object-structure) object without "id" and "entries" fields. | JSON object |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing": {"label": "Taxi driver statuses", "employee_controlled": false, "supervisor_controlled": true}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. ID of the created working status list.

#### Errors

* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature 
available.
* 268 - Over quota – if the user's quota for working status lists exceeded.


### `delete`

Deletes working status list.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                                 | type |
|:-----------|:------------------------------------------------------------|:-----|
| listing_id | ID of the working status list for this status to attach to. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing_id": 12345}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/listing/delete?hash=a6aa75587e5c59c32d347da438505fc3&listing_id=12345
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if working status list with the specified ID does not exist.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature 
available.


### `list`

Gets working status lists belonging to authorized user.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/listing/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list":[{
      "id": 1,
      "label": "Taxi driver statuses",
      "employee_controlled": true,
      "supervisor_controlled": false,
      "entries": [ 5, 2, 1, 4, 6]
    }]
}
```

* `list` - ordered array of [status_listing](index.md#status-listing-object-structure) objects.

#### Errors

* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature 
available.


### `update`

Updates working status list properties.

**required sub-user rights:** `tracker_update`.

`entries` field allows changing order of statuses attached to this working status list.

#### Parameters

| name    | description                                                                                                            | type        |
|:--------|:-----------------------------------------------------------------------------------------------------------------------|:------------|
| listing | [status_listing](index.md#status-listing-object-structure) object with "id" and "entries" fields. | JSON object |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing": {"id": 12345, "label": "Taxi driver statuses", "employee_controlled": false, "supervisor_controlled": true, "entries": [ 5, 2, 1, 4, 6]}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if working status list with the specified ID does not exist.
* 236 - Feature unavailable due to tariff restrictions – if there are no trackers with "statuses" tariff feature
 available.
* 262 - Entries list is missing some entries or contains nonexistent entries – if entries does not contain full set of
 status IDs associated with this working status list, or if it contains nonexistent status IDs.

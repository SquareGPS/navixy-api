---
title: Status
description: Status
---

# Status

Statuses used to track current activity for employees (in fact, of tracking devices owned by employees). 
The simplest example is "busy" | "not busy". This is a status listing consisting of two elements. Different trackers 
can be assigned different status lists.

API base path: `/status/`

## Status object structure

```json
{
    "id": 5,
    "label": "Busy",
    "color": "E57373"
}
```

* `id` - int. A unique identifier of the status. Read-only.
* `label` - string. Human-readable label for the status.
* `color` - string. Hex-representation of RGB color used to display this status.

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

* `id` - int. A unique identifier of this status listing. Read-only.
* `label` - string. Human-readable label for the status listing.
* `employee_controlled` - boolean. If `true` employees can change their own status, e.g. using mobile tracking app.
* `supervisor_controlled` - boolean. If `true` supervisors can change status, e.g. using mobile monitoring app.
* `entries` - array of int. List of IDs of statuses which belong to this listing. Order matters, and is preserved.

### create

Creates new possible status for the specified status listing.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| listing_id | ID of the listing for this status to attach to. | int |
| status | Status object without ID field. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing_id": "12345", "status": {"label": "Busy", "color": "E57373"}}'
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. ID of the created status.

#### errors

* 201 (Not found in the database) – if listing with the specified ID does not exist.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature 
available.
* 268 (Over quota) – if the user's quota for statuses exceeded.

### delete

Deletes status entry.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| status_id | ID of the status belonging to authorized user. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "status_id": "123"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/delete?hash=a6aa75587e5c59c32d347da438505fc3&status_id=123
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if status with the specified ID does not exist.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature 
available.

### list

Gets statuses belonging to the specified status listing.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| listing_id | ID of the listing for this status to attach to. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing_id": "12345"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/list?hash=a6aa75587e5c59c32d347da438505fc3&listing_id=12345
    ```

#### response

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

#### errors

* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff 
feature available.

### update

Updates status properties.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| status | Status object with ID field. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "status": {"id": "5", "label": "Busy", "color": "E57373"}}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if status with the specified ID does not exist.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" 
tariff feature available.

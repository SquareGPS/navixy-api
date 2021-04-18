---
title: Listing
description: Listing
---

# Listing

API base path: `/status/listing/`

### create

Creates new empty status listing.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| listing | [status_listing](../../status/index.md#status-listing-object-structure) object without "id" and "entries" fields. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing": {"label": "Taxi driver statuses", "employee_controlled": false, "supervisor_controlled": true}'
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. ID of the created status listing.

#### errors

* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature 
available.
* 268 (Over quota) – if the user's quota for listings exceeded.

### delete

Deletes status listing.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| listing_id | ID of the listing for this status to attach to. | int |

#### examples

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

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if listing with the specified ID does not exist.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature 
available.

### list

Gets status listings belonging to authorized user.

#### examples

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

#### response

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

* `list` - ordered array of [status_listing](../../status/index.md#status-listing-object-structure) objects.

#### errors

* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature 
available.

### update

Updates status listing properties.

**required sub-user rights:** `tracker_update`

`entries` field allows changing order of statuses attached to this listing.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| listing | [status_listing](../../status/index.md#status-listing-object-structure) object with "id" and "entries" fields. | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/listing/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "listing": {"id": 12345, "label": "Taxi driver statuses", "employee_controlled": false, "supervisor_controlled": true, "entries": [ 5, 2, 1, 4, 6]}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if status listing with the specified ID does not exist.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature
 available.
* 262 (Entries list is missing some entries or contains nonexistent entries) – if entries does not contain full set of
 status IDs associated with this status listing, or if it contains nonexistent status IDs.

---
title: Garage
description: Garage
---

# Garage

API path: `/garage`.

## Garage object

```json
{
    "id": 222,
    "location": {
        "lat": 40.4,
        "lng": -3.6,
        "address": "Calle Salitre, 58",
        "radius": 150
    },
    "mechanic_name": "Martinez",
    "dispatcher_name": "Velasquez",
    "organization_name": "Bankia"
}
```

* `id` - int. Garage id.
* `location` - valid location or null.

### list

Get all garages belonging to user.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/garage/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/garage/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
        "id": 222,
        "location": {
         "lat": 40.4,
         "lng": -3.6,
         "address": "Calle Salitre, 58",
         "radius": 150
        },
        "mechanic_name": "Martinez",
        "dispatcher_name": "Velasquez",
        "organization_name": "Bankia"
    }]
}
```

#### errors

[General](../../getting-started.md#error-codes) types only.

### create

Creates a new garage.

**required sub-user rights**: `vehicle_update`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| garage | An [garage object](#garage) without `id` field. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/garage/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "garage": {"location": {"lat": 40.4, "lng": -3.6, "address": "Calle Salitre, 58", "radius": 150}, "mechanic_name": "Martinez", "dispatcher_name": "Velasquez", "organization_name": "Bankia"}}'
    ```

#### response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An id of a created garage.

#### errors

[General](../../getting-started.md#error-codes) types only.

### update

Updates existing garage with the specified id.

**required sub-user rights**: `vehicle_update`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| garage | An [garage object](#garage) with `id` field. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/garage/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "garage": {"id": 222, location": {"lat": 40.4, "lng": -3.6, "address": "Calle Salitre, 58", "radius": 150}, "mechanic_name": "Martinez", "dispatcher_name": "Velasquez", "organization_name": "Bankia"}}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no garage with such an id).


### delete

Deletes a garage with the specified id.

**required sub-user rights**: `vehicle_update`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| garage_id | Id of the garage to delete. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/garage/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "garage_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/garage/delete?hash=a6aa75587e5c59c32d347da438505fc3&garage_id=111
    ```

#### response

```json
{ "success": true }
```
    
#### errors

* 201 – Not found in the database (if there is no garage with such an id).
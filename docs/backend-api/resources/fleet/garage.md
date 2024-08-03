---
title: Depot
description: Contains garage object and API calls to interact with it.
---

# Garage

Contains garage object and API calls to interact with it. Depot (garage object) contains name, address, name of the mechanic, name
of the dispatcher and others. This data can be used for more convenient and efficient maintenance and task management.


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

* `id` - int. Depot ID.
* `location` - location object. Valid location or null.
* `mechanic_name` - string. Mechanic name or null.
* `dispatcher_name` - string. Dispatcher name or null.
* `organization_name` - string. Organization name or null.


## API actions

API path: `/garage`.

### `list`

Gets all depots belonging to user.

#### Examples

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

#### Response

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

#### Errors

[General](../../getting-started/errors.md#error-codes) types only.


### `create`

Creates a new depot.

**required sub-user rights**: `vehicle_update`.

#### Parameters

| name   | description                                     | type        |
|:-------|:------------------------------------------------|:------------|
| garage | An [garage object](#garage) without `id` field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/garage/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "garage": {"location": {"lat": 40.4, "lng": -3.6, "address": "Calle Salitre, 58", "radius": 150}, "mechanic_name": "Martinez", "dispatcher_name": "Velasquez", "organization_name": "Bankia"}}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An ID of a created depot.

#### Errors

[General](../../getting-started/errors.md#error-codes) types only.


### `update`

Updates existing depot with the specified ID.

**required sub-user rights**: `vehicle_update`.

#### Parameters

| name   | description                                  | type        |
|:-------|:---------------------------------------------|:------------|
| garage | An [garage object](#garage) with `id` field. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/garage/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "garage": {"id": 222, location": {"lat": 40.4, "lng": -3.6, "address": "Calle Salitre, 58", "radius": 150}, "mechanic_name": "Martinez", "dispatcher_name": "Velasquez", "organization_name": "Bankia"}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no depot with such an ID.


### `delete`

Deletes a depot with the specified ID.

**required sub-user rights**: `vehicle_update`.

#### Parameters

| name      | description                | type |
|:----------|:---------------------------|:-----|
| garage_id | ID of the depot to delete. | int  |

#### Examples

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

#### Response

```json
{ "success": true }
```
    
#### Errors

* 201 – Not found in the database - if there is no depot with such an ID.

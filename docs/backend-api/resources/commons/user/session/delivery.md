---
title: Delivery
description: Calls to work with "delivery" type sessions. Those are special sessions to integrate order (task) 
             tracking functionality into external systems.
---

# Delivery

Calls to work with "delivery" type sessions. Those are special sessions to integrate order (task) 
tracking functionality into external systems.


## API actions

API path: `/user/session/delivery`.

### `create`

Creates new user delivery session.
In demo session allowed to create a new session only if it not already exists.

**required sub-user rights**: `admin` (available only to master users).

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/delivery/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/session/delivery/create?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "value": "42fc7d3068cb98d233c3af749dee4a8d"
}
```

* `value` - string. Created delivery session hash key.

#### Errors

* 101 - In demo mode this function disabled – current session is demo but weblocator session already exists.
* 236 – Feature unavailable due to tariff restrictions.


### `read`

Returns current user delivery session key.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/delivery/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/session/delivery/read?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "value": "42fc7d3068cb98d233c3af749dee4a8d"
}
```

* `value` - string. Delivery session hash.

#### Errors

* 201 – Not found in the database - if there is no delivery session.

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.

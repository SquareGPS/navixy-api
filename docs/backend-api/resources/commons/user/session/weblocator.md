---
title: Weblocator
description: Calls to work with "weblocator" type sessions. Those are special sessions to integrate tracking device functionality into external systems.
---

# User sessions weblocator

Calls to work with "weblocator" type sessions. Those are special sessions to integrate tracking 
device functionality into external systems.

<hr>

## API actions

API path: `/user/sessions/weblocator`.

### create

Creates a new user weblocator session.
In demo session allowed to create a new session only if it not already exists.

**required sub-user rights**: `admin` (available only to master users).

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/weblocator/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/session/weblocator/create?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "value": "42fc7d3068cb98d233c3af749dee4a8d"
}
```

* `value` - string. Created session hash key.

#### errors

* 101 - In demo mode this function disabled – current session is demo but weblocator session already exists.
* 236 – Feature unavailable due to tariff restrictions.

<hr>

### read

Returns current user weblocator session key.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/weblocator/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/session/weblocator/read?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "value": "42fc7d3068cb98d233c3af749dee4a8d"
}
```

* `value` - string. Session hash key.

#### errors

* 201 – Not found in the database - if there is no weblocator session.

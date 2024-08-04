---
title: Subuser session
description: Sub-user session actions to obtain its hash
---

# Subuser session

Sub-user session actions to obtain its hash.


## API actions

API path: `/subuser/session/`.

### `create`

Creates a new session for the specified sub-user and obtain its hash. Can be used to log in to sub-user's accounts.

**required tariff features:** `multilevel_access` – for ALL trackers.
**required sub-user rights:** `admin` (available only to master users).

#### Parameters

| name       | description                                      | type |
|:-----------|:-------------------------------------------------|:-----|
| subuser_id | ID of the sub-user belonging to current account. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/subuser/session/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "subuser_id": 204951}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/subuser/session/create?hash=a6aa75587e5c59c32d347da438505fc3&subuser_id=204951
    ```

#### Response

```json
{
    "success": true,
    "hash" : "22eac1c27af4be7b9d04da2ce1af111b"
}
```

* `hash` - string. Hash of the created sub-user session.

#### Errors

* 13 – Operation not permitted – if user has insufficient rights.
* 236 – Feature unavailable due to tariff restrictions - if there is at least one tracker without `multilevel_access` tariff feature.
* 201 – Not found in the database – if sub-user with such an ID does not exist or does not belong to current master user.


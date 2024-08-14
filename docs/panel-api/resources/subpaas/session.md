---
title: Session
description: API call to create a subpaas session.
---

# Subpaas session key

API call to create a SubPaaS session key.


## API actions

API base path: `panel/subpaas/session`.

### `create`

Creates a SubPaaS session.

#### Parameters

| name       | description  | type |
|:-----------|:-------------|:-----|
| subpaas_id | Subpaas' ID. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/subpaas/session/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "subpaas_id": 97834}'
    ```
       
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/subpaas/session/create?hash=fa7bf873fab9333144e171372a321b06&subpaas_id=97834
    ```


#### Response

```json
{
    "success": true,
    "hash": "600d4a5400000000600d4a5400000000"
}
```

#### Errors

* 13 –
    * The dealer is not PaaS type.
    * The dealer has a status other than `NOT_BLOCKED`.
    * The dealer's tariff does not allow SubPaaS accounts.
    * The found SubPaaS is not in `NOT_BLOCKED` status.


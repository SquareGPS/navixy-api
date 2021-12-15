---
title: Session
description: API call to create a subpaas session.
---

# Subpaas session key

API call to create a subpaas's session key.

***

## API actions

API base path: `panel/subpaas/session`.

### create

Creates a subpaas session.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| subpaas_id | Subpaas's id. | int |

#### examples

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


#### response

```json
{
    "success": true,
    "hash": "600d4a5400000000600d4a5400000000"
}
```

#### errors

* 13 –
    * The dealer is not paas.
    * The dealer has different status than `NOT_BLOCKED`.
    * The dealer's tariff doesn't allow subpaases.
    * Found subpaas is not in `NOT_BLOCKED` status.


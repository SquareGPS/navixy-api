---
title: Password
description: API call to change subpaas's password.
---

# Change password

API base path: `panel/subpaas/password`.

API call to change subpaas's password.

### change 

Changes subpaas's password.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| subpaas_id | Subpaas's id. | int |
| new_password | New subpaas's password, 6 to 20 printable characters. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/subpaas/password/change' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "subpaas_id": 99874, "new_password": "Fr1d@Y$"}'
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* 13 –
    * The dealer is not paas.
    * The dealer has different status than `NOT_BLOCKED`.
    * The dealer's tariff doesn't allow subpaases.
    * Found subpaas is in `DELETED` status.


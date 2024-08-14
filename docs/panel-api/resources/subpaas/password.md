---
title: Password
description: API call to change subpaas password.
---

# Change password

API base path: `panel/subpaas/password`.

API call to change the password of a Subdealer (SubPaaS) account.


## API actions

API base path: `panel/subpaas/password`.

### `change` 

Changes SubPaaS password.

#### Parameters

| name         | description                                          | type   |
|:-------------|:-----------------------------------------------------|:-------|
| subpaas_id   | Subpaas' ID.                                         | int    |
| new_password | New subpaas' password, 6 to 20 printable characters. | string |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/subpaas/password/change' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "subpaas_id": 99874, "new_password": "Fr1d@Y$"}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 13 –
    * The dealer is not paas.
    * The dealer has different status than `NOT_BLOCKED`.
    * The dealer's tariff does not allow subpaases.
    * Found subpaas is in `DELETED` status.


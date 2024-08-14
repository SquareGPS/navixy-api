---
title: Update password
description: API call to update dealer's password.
---

# Password

API call to update Dealer's password.


## API actions

API base path: `panel/dealer/password`.

### `update`

Changes password for the authorized Dealer. 

*required permissions*: `password: "update"`.

#### Parameters

| name         | description                                                | type   |
|:-------------|:-----------------------------------------------------------|:-------|
| old_password | Current dealer's password.                                 | string |
| new_password | New password for the dealer, 6 to 20 printable characters. | string |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/password/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "old_password": "qwerty", "new_password": "B1r7d@Y"}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 245 - New password must be different - if `old_password` = `new_password`.
* 248 - Wrong password - if `old_password` is wrong.
---
title: Update password
description: API call to update dealer's password.
---

# Password

## API actions

API base path: `panel/dealer/password`.

### update

Changes password for the authorized Dealer.

_required permissions_: `password: "update"`.

#### Parameters

| name          | description              | type   |
| ------------- | ------------------------ | ------ |
| old\_password | Current dealer password. | string |
| new\_password | New dealer password.     | string |

{% include "../../../.gitbook/includes/password-requirements.md" %}

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/panel/dealer/password/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06", "old_password": "qwerty", "new_password": "B1r7d@Y"}'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 245 - New password must be different - if `old_password` = `new_password`.
* 248 - Wrong password - if `old_password` is wrong.

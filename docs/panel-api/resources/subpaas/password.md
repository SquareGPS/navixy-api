---
title: Password
description: API call to change subpaas password.
---

# Change password

API base path: `panel/subpaas/password`.

API call to change the password of a Subdealer (SubPaaS) account.

## API actions

API base path: `panel/subpaas/password`.

### change

Changes SubPaaS password.

#### Parameters

| name          | description           | type   |
| ------------- | --------------------- | ------ |
| subpaas\_id   | Subpaas ID.           | int    |
| new\_password | New subpaas password. | string |

{% include "../../../.gitbook/includes/password-requirements.md" %}

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/panel/subpaas/password/change' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "fa7bf873fab9333144e171372a321b06", "subpaas_id": 99874, "new_password": "Fr1d@Y$"}'
```
{% endcode %}

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

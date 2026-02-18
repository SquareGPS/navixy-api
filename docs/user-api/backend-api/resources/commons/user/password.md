---
title: User password
description: Contains API calls to change and set users' passwords.
---

# User password

## API actions

API path: `/user/password`.

### change

Changes password of user with the provided session hash (it is contained in a password restore link from email sent to user by user/restore\_password).

> This call will receive only session hash from a password restore email. Any other hash will result in result error code 4 (User or API key not found or session ended).

#### Parameters

| name     | description                | type   |
| -------- | -------------------------- | ------ |
| password | New password for the user. | string |

{% include "../../../../../.gitbook/includes/password-requirements.md" %}

#### Example

cURL

```sh
curl -X POST 'https://api.eu.navixy.com/v2/user/password/change' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "password": "12@14Y$"}'
```

#### Response

```json
{
  "success": true
}
```

#### Errors

* 101 – In demo mode this function disabled - if specified session hash belongs to demo user.

### set

Changes password for login user.\
Works only with standard user session (not with API key).

#### Parameters

| name          | description                                              | type   |
| ------------- | -------------------------------------------------------- | ------ |
| old\_password | Current password of the user.                            | string |
| new\_password | New password for the user. 6 to 20 printable characters. | string |

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/user/password/set' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "old_password": "qwert1", "new_password": "12@14Y$"}'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 101 – In demo mode this function disabled - if specified session hash belongs to demo user.
* 245 – New password must be different - if `old_password` = `new_password`.
* 248 – Wrong password - if `old_password` is wrong.

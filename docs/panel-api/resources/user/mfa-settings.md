# Multi-factor authentication settings

> **Work in progress!**\
> This API is a work in progress and may change in future releases.\
> In this version, allowing MFA to a user automatically enables it for them.

## API actions

API path: `panel/user/mfa/settings`.

### update

Updates users' MFA settings.

_required permissions_: `users: "update"`.

#### Parameters

| name     | description                | type                                           |
| -------- | -------------------------- | ---------------------------------------------- |
| target   | Target of the update.      | [Update target](mfa-settings.md#update-target) |
| settings | MFA settings for the user. | [MFA settings](mfa-settings.md#mfa-settings)   |

**Update target**

| name | description                                                                | type                       |
| ---- | -------------------------------------------------------------------------- | -------------------------- |
| type | Specifies the type of the target: it could be either `all` or `selected`.  | string                     |
| ids  | Used only when the `type` is `selected`. Specifies the `ids` of the users. | array of positive integers |

#### Example

{% code title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/panel/user/mfa/settings/update' \
    -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
    -H 'Content-Type: application/json' \
    -d '{ "target": { "type": "all" }, "settings": { "type": "disallowed" } }'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database — if the specified user does not exist or belongs to a different dealer.

### read default

Reads default MFA settings which are applied to the newly created users.

_required permissions_: `users: "read"`.

#### Example

{% code title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/panel/user/mfa/settings/default/read' \
    -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
```
{% endcode %}

#### Response

```json
{
  "success": true,
  "value": {
    "type": "disallowed"
  }
}
```

* `value` - optional [MFA settings](mfa-settings.md#mfa-settings).

### update default

Updates default MFA settings which are applied to the newly created users.

_required permissions_: `users: "update"`.

#### Parameters

| name     | description                 | type                                         |
| -------- | --------------------------- | -------------------------------------------- |
| settings | MFA settings for the users. | [MFA settings](mfa-settings.md#mfa-settings) |

#### Example

{% code title="cURL" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/panel/user/mfa/settings/default/update' \
    -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
    -H 'Content-Type: application/json' \
    -d '{ "settings": { "type": "disallowed" } }'
```
{% endcode %}

#### Response

```json
{
  "success": true
}
```

## Types

### MFA settings

```json
{
  "type": "allowed",
  "factor_types": ["email"]
}
```

* `type` - [settings action type](mfa-settings.md#settings-action-type).
* `factor_types` - optional array of [factor types](mfa-settings.md#factor-type). Required if `type` is `allowed`.

### Settings action type

* `allowed` - MFA with specified types is allowed for the users.
* `disallowed` - MFA is disallowed for the users.

### Factor type

* `email` - a multi-digit code sent by email.

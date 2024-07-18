# Multi-factor authentication settings

## MFA settings object

```json
{
  "is_enabled": true,
  "accepted_types": ["email_code"]
}
```

* `is_enabled` - boolean. If true, second factor will be requested after successfully entering correct login and password.
* `accepted_types` - array of [factor types](#factor-type). Which factors will be accepted by the server. Cannot be empty.

### Factor type

* `email_code` - a multi-digit code sent by email.

## API actions

API path: `panel/user/mfa/settings`.

### read

Reads user's MFA settings.

*required permissions*: `users: "read"`.

#### parameters

| name    | description   | type |
|:--------|:--------------|:-----|
| user_id | ID of a user. | int  |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/mfa/settings/read' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "user_id": 231432 }'
    ```

#### response

```json
{
  "success": true,
  "value": {
    "is_enabled": true,
    "accepted_types": ["email_code"]
  }
}
```

* `value` - optional [MFA settings object](#mfa-settings-object).

#### errors

* 201 – Not found in the database - if specified user does not exist or belongs to different dealer.

### update

Updates users' MFA settings.

*required permissions*: `users: "update"`.

#### parameters

| name     | description                | type                                        |
|:---------|:---------------------------|:--------------------------------------------|
| target   | Target of the update.      | [Update target](#update-target)             |
| settings | MFA settings for the user. | [MFA settings object](#mfa-settings-object) |

##### Update target

| name | description                                                                | type                       |
|------|----------------------------------------------------------------------------|----------------------------|
| type | Specifies the type of the target: it could be either `all` or `selected`.  | string                     |
| ids  | Used only when the `type` is `selected`. Specifies the `ids` of the users. | array of positive integers |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/mfa/settings/update' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "target": { "type": "all" }, "settings": { "is_enabled": true, "accepted_types": ["email_code"] } }'
    ```

#### response

```json
{
  "success": true
}
```

#### errors

* 201 – Not found in the database - if specified user does not exist or belongs to different dealer.

### read default

Reads default MFA settings which are applied to the newly created users.

*required permissions*: `users: "read"`.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/mfa/settings/default/read' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
    ```

#### response

```json
{
  "success": true,
  "value": {
    "is_enabled": true,
    "accepted_types": ["email_code"]
  }
}
```

* `value` - optional [MFA settings object](#mfa-settings-object).

### update default

Updates default MFA settings which are applied to the newly created users.

*required permissions*: `users: "update"`.

#### parameters

| name     | description                 | type                                        |
|:---------|:----------------------------|:--------------------------------------------|
| settings | MFA settings for the users. | [MFA settings object](#mfa-settings-object) |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/mfa/settings/default/update' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "settings": { "is_enabled": true, "accepted_types": ["email_code"] } }'
    ```

#### response

```json
{
  "success": true
}
```

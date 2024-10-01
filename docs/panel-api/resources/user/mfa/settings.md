# Multi-factor authentication settings

!!! warning "Work in progress"
    This API is a work in progress and may change in future releases.
    In this version allowing MFA to a user automatically enables it for them.

## API actions

API path: `panel/user/mfa/settings`.

### update

Updates users' MFA settings.

*required permissions*: `users: "update"`.

#### parameters

| name     | description                | type                            |
|:---------|:---------------------------|:--------------------------------|
| target   | Target of the update.      | [Update target](#update-target) |
| settings | MFA settings for the user. | [MFA settings](#mfa-settings)   |

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
        -d '{ "target": { "type": "all" }, "settings": { "type": "disallowed" } }'
    ```

#### response

```json
{
  "success": true
}
```

#### errors

* 201 – Not found in the database — if the specified user does not exist or belongs to a different dealer.

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
    "type": "disallowed"
  }
}
```

* `value` - optional [MFA settings](#mfa-settings).

### update default

Updates default MFA settings which are applied to the newly created users.

*required permissions*: `users: "update"`.

#### parameters

| name     | description                 | type                          |
|:---------|:----------------------------|:------------------------------|
| settings | MFA settings for the users. | [MFA settings](#mfa-settings) |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/user/mfa/settings/default/update' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "settings": { "type": "disallowed" } }'
    ```

#### response

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

* `type` - [settings action type](#settings-action-type).
* `factor_types` - optional array of [factor types](#factor-type). Required if `type` is `allowed`.

### Settings action type

* `allowed` - MFA with specified types is allowed for the users.
* `disallowed` - MFA is disallowed for the users.

### Factor type

* `email` - a multi-digit code sent by email.

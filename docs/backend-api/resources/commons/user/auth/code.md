---
title: User authentication code
description: A user authentication code account lets you authenticate yourself as part of multi-factor authentication.
---

# User authentication code

A user authentication code account lets you authenticate yourself as part of multi-factor authentication.

***

## API actions

API path: `/user/auth/code`.

### resend

Resends an authentication code for multi-factor authentication to the email specified at the registration.
This action has a special rate-limit in 5 minutes to avoid abuse.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/auth/code/resend' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
    ```

#### response

```json
{
  "success": true
}
```

***

### verify

Verifies given authentication code as a part in multi-factor authentication.
On successful verification, you'll receive a normal session hash.

#### parameters

| name | description                       | type   |
|:-----|:----------------------------------|:-------|
| code | An authentication code to verify. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/auth/code/verify' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "code": "123456" }'
    ```

#### response

```json
{
  "success": true,
  "hash": "22eac1c27af4be7b9d04da2ce1af111b"
}
```

* `hash` - string. Session hash.

#### errors

* 282 – Wrong authentication code.

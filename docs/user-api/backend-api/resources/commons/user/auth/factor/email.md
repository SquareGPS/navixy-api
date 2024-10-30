---
title: Email authentication factor
description: Methods to authenticate the current session for dangerous actions (suc as changing the password) with an email as a second factor.
---

# Email authentication factor

Methods to authenticate the current session for dangerous actions (such as changing the password) with an email as a second factor.

***

## API actions

API path: `/user/auth/factor/email`.

### send

Sends a new authentication code to the user's email.

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/auth/factor/email' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b'
    ```

#### response

```json
{
  "success": true
}
```

#### errors

* 15 – Too many requests (rate limit exceeded).

***

### verify

Authenticates the current session using an authentication code against a previously sent one by email.

#### parameters

| name | description                       | type   |
|:-----|:----------------------------------|:-------|
| code | An authentication code to verify. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/auth/factor/email/verify' \
        -H 'Authorization: NVX 22eac1c27af4be7b9d04da2ce1af111b' \
        -H 'Content-Type: application/json' \
        -d '{ "code": "123456" }'
    ```

#### response

```json
{
  "success": true
}
```

* `hash` - string. Session hash.

#### errors

* 15 – Too many requests (rate limit exceeded).
* 282 – Wrong authentication code.

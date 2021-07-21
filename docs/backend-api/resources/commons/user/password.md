---
title: User password
description: Contains API calls to change and set users' passwords.
---

# User password

Contains API calls to change and set users' passwords.


<hr>

## API actions

API path: `/user/password`.

### change

Changes password of user with the provided session hash (it is contained in a password restore link from email sent to
 user by user/restore_password.

!!! note "This call will receive only session hash from a password restore email. Any other hash will result in result  error code 4 (user not found or session ended)."

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| password | New password for the user. 6 to 20 printable characters. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/password/change' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "password": "12@14Y$"}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 101 – In demo mode this function disabled - if specified session hash belongs to demo user.

<hr>

### set

Changes password for login user.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| old_password | Current password of the user. | string |
| new_password | New password for the user. 6 to 20 printable characters. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/password/set' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "old_password": "qwert1", "new_password": "12@14Y$"}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 101 – In demo mode this function disabled - if specified session hash belongs to demo user.
* 225 – New password must be different - if `old_password` = `new_password`.
* 248 – Wrong password - if `old_password` is wrong.

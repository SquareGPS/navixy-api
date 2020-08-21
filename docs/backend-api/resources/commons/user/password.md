---
title: User password
description: User password
---

# User password

API path: `/user/password`.

### change

Changes password of user with the provided session hash (it is contained in password restore link from email sent to user by “user/restore_password”.

**NOTE:** this call will receive only session hash from password restore email. Any other hash will result in result error code 4 (user not found or session ended)

#### parameters

*   **password** (string) – New password for the user, 6 to 20 printable characters

#### response

```json5
{ "success": true }
```

#### errors

*   101 – In demo mode this function is disabled (if specified session hash belongs to demo user)

### set

Changes password for logined user.

#### parameters

*   **old_password** (string) – Current password of the user
*   **new_password** (string) – New password for the user, 6 to 20 printable characters

#### response

```json5
{ "success": true }
```

#### errors

*   101 – In demo mode this function is disabled (if specified session hash belongs to demo user)
*   225 – New password must be different (if **old_password** = **new_password**)
*   248 – Wrong password (if **old_password** is wrong)

---
title: Weblocator
description: Weblocator
---

# User sessions weblocator

API path: `/user/sessions/weblocator`.

### create

Create new user weblocator session.
In demo session allowed to create a new session only if it not already exists.

**required subuser rights**: admin (available only to master users)

#### response

```js
{
    "success": true,
    "value": "42fc7d3068cb98d233c3af749dee4a8d" // created session hash key
}
```

#### errors

*   101 (In demo mode this function is disabled) – current session is demo but weblocator session already exists.
*   236 – Feature unavailable due to tariff restrictions


### read

Return current user weblocator session key.

#### response

```js
{
    "success": true,
    "value": <string> // session hash key
}
```

#### errors

*   201 – Not found in database (if there is no weblocator session).

---
title: /account
description: /account
---

## auth(…)

#### parameters:

*   **login** – **string**. login
*   **password** – **string**. password

Does not require session hash and does not need any permissions. Auth dealer in panel (planned also for dealer's "sub-users") 

#### return:

```json
{
    "success": true,
    "hash": <string>,       // session key
    "permissions": <object> // account permissions, e.g. { "base": ["get_dealer_info"] }
}
```

See: panel account [permissions](../getting-started.md#panel-api-permissions).
    
#### errors:

*   11 - Access denied (if dealer blocked)
*   12 - Dealer not found


## get_permissions()

Does not need any permissions. Returns permissions for current panel session 

#### return:

```json
{
    "success": true,
    "permissions": <object> // account permissions, e.g. { "base": ["get_dealer_info"] }
}
```

#### errors:

Only standard errors.

## logout()

Ends the current session.

#### return

```json
{
    "success": true
}
```

#### errors:
standard errors
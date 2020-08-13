---
title: Get session hash
description: About session hash key
---

# How to get session Hash

"Hash" or "Session key" is a randomly generated string that is used to verify and authenticate actions.
Nearly all API calls require a session key to operate.

To get hash use the next API calls with credentials of a user:

    https://api.navixy.com/v2/fsm/user/auth?login=user_login&password=user_password

It will respond:

```json
{ "success": true, "hash": "..." }
```

Received hash should be saved and used in API calls. For security reasons, 
hash has a lifetime of 30 days and will expire in certain situations:

*	after 30 days
*	user has changed their password
*	user logged out and ended the session
*	user was deleted

Correct work with hash is crucial. There is no need to receive a new hash before each request, 
instead, your hash should be stored and validity checked, in most cases you just need to
prolong the session.

To prolong the session, use the [next API call](../resources/commons/user/session/session.md#renew):

    https://api.navixy.com/v2/fsm/user/session/renew?hash=you_hash

You can disable the current hash with the [next call](../resources/commons/user/user.md#logout):

    https://api.navixy.com/v2/fsm/user/user/logout?hash=your_hash

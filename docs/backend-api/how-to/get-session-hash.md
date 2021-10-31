---
title: Obtain session hash
description: How to obtain a session hash key
---

# Obtaining session hash

"Hash" or "Session key" is a randomly generated string that is used to verify and authenticate actions.
Nearly all API calls require a session key to operate.

To get hash use the [user/auth](../resources/commons/user/index.md#auth) call with credentials of a user:

    {{ extra.api_example_url }}/user/auth?login=user_login&password=user_password

The response will be like this:

```json
{ "success": true, "hash": "882fb333405d006df0d5a3f410115e92" }
```                                                             

Where resulting hash is `882fb333405d006df0d5a3f410115e92` (just an example, you will get a different hex string).

Received hash should be saved and used in API calls. For security reasons, 
hash has a lifetime of 30 days and will expire in certain situations:

* After 30 days.
* User has changed their password.
* User logged out and ended the session.
* User was deleted.

**Correct work with hash is crucial.** There is **no need to receive a new hash before each request**, 
instead, your hash should be **stored and reused**. To prevent expiration, in most cases you just need to
prolong the session.

To prolong the session, use the [following API call](../resources/commons/user/session/index.md#renew):

    {{ extra.api_example_url }}/user/session/renew?hash=you_hash

You can disable the current hash with the [following call](../resources/commons/user/index.md#logout):

    {{ extra.api_example_url }}/user/logout?hash=your_hash

***

## Using hash

You must pass session hash with most API calls along other parameters required to make the call.

For example, if you want to make a call with the single parameter `id` equal to 1, and you obtained hash equal to
`882fb333405d006df0d5a3f410115e92` (fake hash, just for example) you must pass the following parameters in HTTP request:
`id=1&hash=882fb333405d006df0d5a3f410115e92` (example is for POST/`x-www-form-urlencoded` or GET requests).

Otherwise, you will get an error response:

```json
{
    "success": false,
    "status": {
        "code": 3,
        "description": "Wrong user hash"
    }
}
``` 

Whenever you see such response, it means that you did not pass hash value properly.

If session expired or was logged out, you will receive the following response:

```json
{
    "success": false,
    "status": {
        "code": 4,
        "description": "User not found or session ended"
    }
}
```

It means that you need to obtain new user hash through [user/auth](../resources/commons/user/index.md#auth) API action. 
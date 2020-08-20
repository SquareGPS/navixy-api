---
title: Subuser session
description: Subuser session
---

# Subuser session

API path: `/subuser/session/`.

### create

Create new session for the specified sub-user and obtain its hash. Can be used to log in to sub-user’s accounts.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters

* **subuser_id** - **int**. id of the sub-user belonging to current account

#### return

```js
{
    "success": true,
    "hash" : ${hash of the created subuser session}
}
```

Subuser object is described [here](./subuser.md#sub-user-object-structure).

#### errors

*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)
*   201 – Not found in database – if sub-user with such id does not exist or does not belong to current master user.


---
title: Subuser tracker
description: Subuser tracker
---

# Subuser tracker

API path: `/subuser/tracker`.

Contains API calls to control which tracker is available to which sub-user.

## bind()

Give access for sub-user to the specified trackers.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
* **subuser_id** - **int**. id of the sub-user belonging to current account.
* **trackers** - **array of int**. array of tracker id-s to associate with the specified sub-user. All trackers must belong to current master user.

#### return

```json
{
    "success": true
}
```

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)
*   201 – Not found in database – if sub-user with such id does not exist or does not belong to current master user.
*   262 – Entries list is missing some entries or contains nonexistent entries – if one or more of specified tracker ids don’t exist.

## list()

Get a list of tracker ids to which this sub-user has access.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
* **subuser_id** - **int**. id of the sub-user belonging to current account.

#### return

```js
{
    "success": true,
    "list" : [${tracker_id1}, ...] //list of tracker ids to which this sub-user has acccess
}
```

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)
*   201 – Not found in database – if sub-user with such id does not exist or does not belong to current master user.

## unbind()

Disable access for sub-user to the specified trackers.

**required tariff features:** multilevel_access – for ALL trackers
**required subuser rights:** admin (available only to master users)

#### parameters
* **subuser_id** - **int**. id of the sub-user belonging to current account.
* **trackers** - **array of int**. array of tracker id-s to associate with the specified sub-user. All trackers must belong to current master user.

#### return

```json
{
    "success": true
}
```

#### errors
*   13 – Operation not permitted – if user has insufficient rights
*   236 – Feature unavailable due to tariff restrictions (if there is at least one tracker without “multilevel_access” tariff feature)
*   201 – Not found in database – if sub-user with such id does not exist or does not belong to current master user.
*   262 – Entries list is missing some entries or contains nonexistent entries – if one or more of specified tracker ids don’t exist.


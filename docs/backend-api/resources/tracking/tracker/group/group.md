---
title: /group
description: /group
---

## group
Tracker group is used to organize trackers in user interface. Currently, its function is purely visual.

#### Group structure:

```js
<group> = {
    "id": <int>,       // group id. used to reference group in objects and API calls. Read-only, assigned automatically by the server.
    "title": <string>, // user-specified group title, 1 to 60 printable characters, e. g. "Employees"
    "color": <string>  // group color in web format (without #), e.g. "FF6DDC". Determines the color of tracker markers on the map.
}
```

#### Example:

```js
{
    "id": 167,
    "title": "Main office",
    "color": "FF6DDC"
}
```

## assign()
Assign multiple trackers to the specified group.

**required subuser rights:** admin (available only to master users)

#### parameters:
* **id** - **int**. group id, or 0 if trackers should be removed from any group
* **trackers** - **array of int**. array of tracker ids

#### errors:
*   201 (Not found in database) – if no group was found with the specified id (or group belongs to another user)
*   217 (List contains nonexistent entities) – if one or more of tracker ids belong to nonexistent tracker (or to a tracker belonging to different user)

## create()
Create a new empty group.

**required subuser rights:** admin (available only to master users)

#### parameters:
* **title** - **string**. user-specified group title, 1 to 60 printable characters
* **color** - **string**. group color, e.g. “FF6DDC”

#### return:
```js
{
    "success": true,
    "id": <int> // id of the group that was created, e.g. 222
}
```

#### errors:
general types only

## delete()
Delete group with the specified Id. The group must belong to authorized user. All trackers from this group will be assigned to default group (0).

**required subuser rights:** admin (available only to master users)

#### parameters:
* **id** - **int**. id of group to delete

#### return:

```json
{ "success": true }
```

#### errors:
*   201 (Not found in database) – if no group was found with the specified id (or group belongs to another user)

## list()
Get all user’s tracker groups.

There is always “default” unnamed group with id = 0. It cannot be modified, deleted, and is not returned by this API call.

#### return:

```json
{ "success": true }
```

#### errors:
general types only

## update()
Update specified tracker group. Group must belong to the authorized user.

required subuser rights: admin (available only to master users)

#### parameters:
* `<group>`

#### return:

```json
{ "success": true }
```

#### errors:
*   201 (Not found in database) – if no group was found with the specified id (or group belongs to another user)

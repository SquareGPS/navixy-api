---
title: /group
description: /group
---

API base path: `/tracker/group`

### group
Tracker group is used to organize trackers in user interface. Currently, its function is purely visual.
In FSM api, groups are read-only and represent departments of the employees assigned to trackers.
Group id `0` means employee has no department, group id `-1` means tracker has no employee assigned.

#### Group structure:

```json
<group> = {
    "id": <int>,       // group id. used to reference group in objects and API calls. Read-only, assigned automatically by the server.
    "title": <string>, // user-specified group title, 1 to 60 printable characters, e. g. "Employees"
    "color": <string>  // group color in web format (without #), e.g. "FF6DDC". Determines the color of tracker markers on the map.
}
```

#### example

```json
{
    "id": 167,
    "title": "Main office",
    "color": "FF6DDC"
}
```

### list
Get all user’s tracker groups.

There is always “default” unnamed group with id = 0. It cannot be modified, deleted, and is not returned by this API call.

#### response

```json
{ "success": true }
```

#### errors
general types only

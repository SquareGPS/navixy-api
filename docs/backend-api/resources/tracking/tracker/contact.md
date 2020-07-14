---
title: /contact
description: /contact
---

## list()

Get all user’s trackers with special grouping by “contacts”.

#### example:

    [api_base_url]/contact/list?hash=22eac1c27af4be7b9d04da2ce1af111b

#### response:
```javascript
    {
        "success": true,
        "contacts": [ <contact>, ... ] // all established contacts
        "trackers": [ <tracker>, ... ] // normal trackers belonging to current user
    }
```
where **contact** is:
```javascript
    {
        "user_id": 12059,  //id of the user with which "contact" is established
        "first_name": "Adam",
        "middle_name": "James",
        "last_name": "Williams",
        "trackers": [ <tracker>, ... ] //trackers belonging to "contact" which locations were shared with current user
    }
```

Click to see descriptions of type [tracker](tracker.md#tracker-object-structure).

#### errors:

201 – Not found in database

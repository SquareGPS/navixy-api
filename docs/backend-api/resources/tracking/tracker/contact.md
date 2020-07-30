---
title: Contact
description: Contact
---

## list()

Gets all user’s trackers with special grouping by “contacts”.

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/contact/list' \
-H 'Content-Type: application/json' \ 
-d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
```

#### response

```js
{
    "success": true,
    "contacts": [ <contact>, ... ] // all established contacts
    "trackers": [ <tracker>, ... ] // normal trackers belonging to current user
}
```
where **contact** object is:

```js
{
    "user_id": 12059, //id of the user with which "contact" is established
    "first_name": "Adam",
    "middle_name": "James",
    "last_name": "Williams",
    "trackers": [ <tracker>, ... ] //trackers belonging to "contact" which locations were shared with current user
}
```

Click to see descriptions of type [tracker](tracker.md#tracker-object-structure).

#### errors

* 201 – Not found in database

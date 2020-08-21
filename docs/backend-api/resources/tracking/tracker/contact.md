---
title: Contact
description: Contact
---

!!! warning "Deprecated"
    This API action is deprecated and should not be used.

API base path: `/tracker/contact`

### list

Gets all user’s trackers with special grouping by “contacts”.

#### example

```abap
$ curl -X POST '{{ extra.api_example_url }}/tracker/contact/list' \
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

Click to see descriptions of type [tracker](index.md#tracker-object-structure).

#### errors

* 201 – Not found in database

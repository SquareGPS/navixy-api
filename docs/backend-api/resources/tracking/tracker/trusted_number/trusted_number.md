---
title: /trusted_number
description: /trusted_number
---

## list()
Get list of trusted numbers for the specified tracker.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return
```javascript
{
    "success": true,
    "list": [<string>, ...] // List of strings containing trusted phone numbers in international format without "+", e.g. ["496156680000", "496156680001"]
}
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

## update()
Replaces the list of trusted numbers for a specified tracker with the new one.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **list** - **array of string**. Array of phone numbers (10-15 digits) represented as strings, e.g. [“496156680001″,”496156680000”].

#### return
```javascript
{ "success": true }
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)


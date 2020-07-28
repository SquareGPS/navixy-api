---
title: /value
description: /value
---

## get()

#### parameters:
* **tracker_id** - **int**. id of the tracker.
* **type** - **string**. counter type. one of ["odometer", "fuel_consumed", "engine_hours"].

#### return:
```js
{
    "success": true,
    "value": 18.9  // float. last value of counter
}
```

#### errors:
*   204 (Entity not found) – if there is no tracker with such id belonging to authorized user, counter does not exist or there are no values yet. use /tracker/counter/set() to create new counter (if not exist) and save some value.
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.

## list()
Get values for counters of passed **type** and **trackers**

#### parameters:
* **trackers** - **array of int**. List of the tracker’s Ids belonging to authorized user.
* **type** - **string**. counter type, one of ["odometer", "fuel_consumed", "engine_hours"].

#### return:
```js
{
  "success": true,
  "value": { // Map with tracker's ids as keys
    "14": 18.9
    ...
  }
}
```
#### errors:
*   204 (Entity not found) – if one of the specified counter does not exist or there are no values yet. use /tracker/counter/set() to create new counter (if not exist) and save some value.
*   217 (List contains nonexistent entities) – if one of the specified trackers does not exist or is blocked

## set()
Creates new counter of passed **type** (if not) and update its **value**.

#### parameters:
* **tracker_id** - **int**. ID of the tracker.
* **type** - **string**. Counter type, one of ["odometer", "fuel_consumed", "engine_hours"].
* **value** - **float**. A new value of counter.

#### return:

```json
{ "success": true }
```

#### errors:
*   8 (Queue service error, try again later) – can't set counter value, try later.
*   204 (Entity not found) – if there is no tracker with such id belonging to authorized user.
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
*   219 (Not allowed for clones of the device) – if specified tracker is a clone.


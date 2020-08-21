---
title: Counter Value
description: Counter Value
---

### get

Gets value of specified **type** of sensor.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 123456 |
| type | counter type. one of ["odometer", "fuel_consumed", "engine_hours"] | string enum | odometer |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/counter/value/read' \
    -H 'Content-Type: application/json' \ 
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489", "type": "odometer"}'
```

#### response

```json
{
    "success": true,
    "value": 18.9  //float. last value of counter
}
```

#### errors
* 204 (Entity not found) – if there is no tracker with such id belonging to authorized user, counter does not exist or there are no values yet. use /tracker/counter/set to create new counter (if not exist) and save some value.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.

### list

Get values for counters of passed **type** and **trackers**

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| trackers | List of the tracker’s Ids belonging to authorized user | array of int | [123456, 234567] |
| type | counter type. one of ["odometer", "fuel_consumed", "engine_hours"] | string enum | odometer |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/counter/value/list' \
    -H 'Content-Type: application/json' \ 
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": "[123456, 265489]", "type": "odometer"}'
```

#### response

```json
{
  "success": true,
  "value": { //map with tracker's ids as keys
    "14": 18.9
    ...
  }
}
```

#### errors

* 204 (Entity not found) – if one of the specified counter does not exist or there are no values yet. use /tracker/counter/set to create new counter (if not exist) and save some value.
* 217 (List contains nonexistent entities) – if one of the specified trackers does not exist or is blocked.

### set

Creates new counter of passed **type** (if not) and update its **value**.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 123456 |
| type | counter type. one of ["odometer", "fuel_consumed", "engine_hours"] | string enum | odometer |
| value | a new value of counter | float | 233.21 |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/counter/value/set' \
    -H 'Content-Type: application/json' \ 
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489", "type": "odometer", "value": "233.21"}'
```

#### response

```json
{ "success": true }
```

#### errors

* 8 (Queue service error, try again later) – can't set counter value, try later.
* 204 (Entity not found) – if there is no tracker with such id belonging to authorized user.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 (Not allowed for clones of the device) – if specified tracker is a clone.


---
title: Unconfirmed commands
description: Unconfirmed commands
---

### count

Gets number of commands in queue for the specified tracker.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 123456 |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/command/unconfirmed/count' \
    -H 'Content-Type: application/json' \ 
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489"}'
```

#### response

```js
{
    "success": true,
    "count": <number of commands, e.g. 0> //int
}
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).

### reset

Removes all pending SMS commands from the queue for the specified tracker.

**required sub-user rights:** tracker_update

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 123456 |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/command/unconfirmed/reset' \
    -H 'Content-Type: application/json' \ 
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489"}'
```

#### response

```json
{ "success": true }
```

#### errors
* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).

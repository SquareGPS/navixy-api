---
title: Counter actions
description: Counter actions
---

### read

Reads counter of passed **type**.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 123456 |
| type | counter type. one of ["odometer", "fuel_consumed", "engine_hours"] | string enum | odometer |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/counter/read' \
    -H 'Content-Type: application/json' \ 
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489", "type": "odometer"}'
```
#### response

```json
{
  "success": true,
  "value": {
    "id": 111,
    "type": "odometer",
    "multiplier": 1.0
  }
}
```

#### errors
* 204 (Entity not found) – if there is no tracker with such id belonging to authorized user.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 (Not allowed for clones of the device) – if specified tracker is a clone.

### update

Updates counter of passed **type**.

**required sub-user rights:** tracker_update

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked | int | 123456 |
| type | counter type. one of ["odometer", "fuel_consumed", "engine_hours"] | string enum | odometer |
| multiplier | new value of counter multiplier | float | 1.34 |
| sensor_id | id of the sensor, which must be used as the source of odometer data (in case when parameter “type” equals “odometer”). if “type” is not “odometer”, “sensor_id” must be null | int | 123 |

#### example

```abap
$ curl -X POST 'https://api.navixy.com/v2/tracker/counter/update' \
    -H 'Content-Type: application/json' \ 
    -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489", "type": "odometer", "multiplier": "1.34", "sensor_id": "1234"}'
```

#### response

```json
{ "success": true }
```

#### errors
* 8 (Queue service error, try again later) – cannot set counter value, try later.
* 204 (Entity not found) – if there is no tracker with such id belonging to authorized user.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 (Not allowed for clones of the device) – if specified tracker is a clone.
* 7 (Invalid parameters) –
 * if type is not “odometer”  and sensor_id is not null,
 * if sensor with specified sensor_id is not a metering sensor
 * if sensor with specified sensor_id belongs to another tracker
 * if sensor_id is negative
 * if sensor with such a sensor_id is not exist
 * if type value is not one of list above


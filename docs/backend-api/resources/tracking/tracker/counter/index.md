---
title: Counter actions
description: Counter actions
---

API base path: `/tracker/counter`

### read
Read counter of passed **type**.

#### parameters
* **tracker_id** - **int**. id of the tracker
* **type** - **string**. counter type. one of ["odometer", "fuel_consumed", "engine_hours"]

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
*   204 (Entity not found) – if there is no tracker with such id belonging to authorized user.
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
*   219 (Not allowed for clones of the device) – if specified tracker is a clon.

### update
Updates counter of passed **type**.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. id of the tracker.
* **type** - **string**. counter type. one of ["odometer", "fuel_consumed", "engine_hours"].
* **multiplier** - **float**. new value of counter multiplier.
* **sensor_id** - **int**. id of the sensor, which must be used as the source of odometer data (in case when parameter “type” equals “odometer”). if “type” is not “odometer”, “sensor_id” must be null.

#### response

```json
{ "success": true }
```

#### errors
*   8 (Queue service error, try again later) – can not set counter value, try later
*   204 (Entity not found) – if there is no tracker with such id belonging to authorized user
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if specified tracker is a clone
*   7 (Invalid parameters) –
    * if type is not “odometer”  and sensor_id is not null,
    * if sensor with specified sensor_id is not a metering sensor
    * if sensor with specified sensor_id belongs to another tracker
    * if sensor_id is negative
    * if sensor with such sensor_id is not exist
    * if type value is not one of list above


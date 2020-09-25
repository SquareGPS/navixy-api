---
title: Sensor actions
description: Sensor actions
---

API base path: `/tracker/sensor`

### sensor
Data types
Sensor sub-types
Metering sensor

```json
{
    "type": "metering",
    "id": <int>,
    "sensor_type": <string>,
    "name": <string>,
    "input_name": <string>,
    "divider": <double>,
    "accuracy": <int>,
    "units": <string>,
    "parameters": <parameters object>
}
```

where **parameters** is

```json
{
    "parent_ids": <array>, //optional, array of parent_ids for composite sensor
    "volume": <double>,    //optional, volume for composite sensor
    "min": <double>,       //optional, min acceptable raw value for sensor
    "max": <double>,       //optional, max acceptable raw value for sensor
    "max_lowering_by_time": <double>,       //optional, max legal value lowering per hour
    "max_lowering_by_mileage": <double>,    //optional, max legal value lowering per 100km
}
```

Discrete input

```json
{
    "type": "discrete",
    "id": <int>,
    "sensor_type": <string>,
    "name": <string>,
    "input_number": <int>
}
```

### batch_list
List tracker sensors binded to trackers with specified identificators (parameter **trackers**).

There exist a similar method for working with a single tracker - [list](#list).

#### parameters
**trackers** - **array of ints**. Set of tracker identificators. Each of the relevant trackers must belong to  authorized user and not be blocked.
Number of trackers (length of array) is limited to a maximum of 500 (this number may be changed in future).

#### response
Contains a map, where keys are IDs from **trackers** parameter and values are lists of [sensor](#sensor) objects.
```json
{
  "success": true,
  "result": {
    "11": [
      {
        "id": 1,
		"type": "discrete",
        "sensor_type": "fuel",
        "name": "",
        "input_name": "fuel_level",
        "group_type": null,
        "divider": 1,
        "accuracy": 0,
        "units": null,
        "units_type": "custom"
      },  
     ... ]
   }
}
```

#### errors
* 217 (List contains nonexistent entities) -  if one of **trackers** either does not exist or is blocked.
* 221 (Device limit exceeded) - if too many ids were passed in **trackers** parameter.


### create

Create a sensor.

**required sub-user rights:** tracker_update
#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **sensor** - [JSON object](#sensor). Sensor object.

#### response

```json
{
    "success": true,
    "id": 937 // int. id of created sensor
}
```

#### errors
*   232 (Input already in use) – if given input number (for discrete input) or input name (for metering sensor) already in use
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if tracker is clone
*   270 (Too many sensors of same type) - the number of tracker's sensors, having same `sensor_type` is limited

### delete
Delete sensor with **sensor_id** from the database.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **sensor_id** - **int**. Sensor id.

#### response

```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if sensor with sensor_id is not exists or owned by other user
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   219 – Not allowed for clones of the device (if tracker is clone)

### list
List tracker sensors binded to tracker with specified id (**tracker_id** parameter).

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### response
```json
{
   "success": true,
   "list": [ <sensor>, ... ] // list of sensors
}
```
See [sensor](#sensor) type description.

#### errors
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason

### update
Update sensor.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **sensor** - [JSON object](#sensor). Sensor object.

#### response

```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if sensor not exists or owned by other user
*   232 (Input already in use) – if given input number (for discrete input) or input name (for metering sensor) already in use
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if tracker is clone

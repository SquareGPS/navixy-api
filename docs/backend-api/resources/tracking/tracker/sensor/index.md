---
title: Sensor actions
description: Sensor actions
---

# Sensor actions

API base path: `/tracker/sensor`

### sensor

Data types

Sensor sub-types:
Metering sensor

```json
{
    "type": "metering",
    "id": 860250,
    "sensor_type": "temperature",
    "name": "OBD Coolant temperature",
    "input_name": "obd_coolant_t",
    "divider": 1.0,
    "accuracy": 0,
    "units": "",
    "units_type": "celsius"
    "parameters": {
      "parent_ids": [123042, 123566]
      "volume": 0.7,
      "min": 0.0,
      "max": 12.0,
      "max_lowering_by_time": 120.0
      "max_lowering_by_mileage": 120.0
    }
}
```

* `id` - int. Sensor's id.
* `sensor_type` - string enum.
* `name` - string. A name of sensor.
* `input_name` - string. 
* `divider` - double. 
* `accuracy` - int.
* `units` - string.
* `units_type` - string enum. Units type for a sensor.
* `parameters` - optional object with additional parameters.
    * `parent_ids` - optional array of parent_ids for composite sensor.
    * `volume` - double. Optional. Volume for composite sensor.
    * `parent_ids` - optional. Array of int. Array of `parent_ids` for composite sensor.
    * `volume` - optional. Double. Volume for composite sensor.
    * `min` - optional. Double. Min acceptable raw value for a sensor.
    * `max` - optional. Double. Max acceptable raw value for a sensor.
    * `max_lowering_by_time` - optional. Double. Max legal value lowering per hour.
    * `max_lowering_by_mileage` - optional. Double. Max legal value lowering per 100 km.

Discrete input

```json
{
  "type": "discrete",
  "id": 888951,
  "sensor_type": "ignition",
  "name": "Ignition",
  "input_number": 4
}
```

* `id` - int. An id of a sensor.
* `sensor_type` - string enum. Type of the sensor.
* `name` - string.
* `input_number` - int. Assigned input number.

### create

Creates a sensor.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int |
| sensor | [Sensor object](#sensor). | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "sensor": {"type": "metering", "id": 860250,"sensor_type": "temperature", "name": "OBD Coolant temperature", "input_name": "obd_coolant_t", "divider": 1.0, "accuracy": 0, "units": "", "units_type": "celsius"}'
    ```

#### response

```json
{
    "success": true,
    "id": 937
}
```

* `id` - int. An id of created sensor.

#### errors

* 232 (Input already in use) – if given input number (for discrete input) or input name (for metering sensor) already 
in use.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 (Not allowed for clones of the device) – if tracker is clone.
* 270 (Too many sensors of same type) - the number of tracker's sensors, having same `sensor_type` is limited.

### delete

Deletes a sensor with `sensor_id` from the database.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| sensor_id | Sensor id. | int | 234567 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "sensor_id": "23456"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/delete?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&sensor_id=23456
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 - Not found in the database (if sensor with a sensor_id is not exists or owned by other user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 219 – Not allowed for clones of the device (if tracker is clone).

### list

List tracker sensors binded to tracker with specified id (`tracker_id` parameter).

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/list?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### response

```json
{
   "success": true,
   "list": [{
    "type": "metering",
    "id": 860250,
    "sensor_type": "temperature",
    "name": "OBD Coolant temperature",
    "input_name": "obd_coolant_t",
    "divider": 1.0,
    "accuracy": 0,
    "units": "",
    "units_type": "celsius" 
   }]
}
```

* `list` - list of sensor objects. See [sensor](#sensor) object description.

#### errors

* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions, or some other reason.

### update

Updates sensor.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int |
| sensor | [Sensor object](#sensor). | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "sensor": {"type": "metering", "id": 860250,"sensor_type": "temperature", "name": "OBD Coolant temperature", "input_name": "obd_coolant_t", "divider": 1.0, "accuracy": 0, "units": "", "units_type": "celsius"}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if sensor not exists or owned by other user.
* 232 (Input already in use) – if given input number (for discrete input) or input name (for metering sensor) already 
in use.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 (Not allowed for clones of the device) – if tracker is clone.

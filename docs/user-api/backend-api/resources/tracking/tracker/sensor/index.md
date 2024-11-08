---
title: Sensor actions
description: API calls to interact with sensors.
---

# Sensor actions

Contains API calls to interact with sensors.


## Sensor sub-types

### Metering sensor

```json
{
    "type": "metering",
    "id": 860250,
    "sensor_type": "temperature",
    "name": "OBD Coolant temperature",
    "input_name": "obd_coolant_t",
    "divider": 1.0,
    "accuracy": 0.0,
    "units": "",
    "units_type": "celsius",
    "parameters": {
      "parent_ids": [123042, 123566],
      "volume": 0.7,
      "min": 0.0,
      "max": 12.0,
      "max_lowering_by_time": 120.0,
      "max_lowering_by_mileage": 120.0,
      "ignore_drains_in_move": true,
      "ignore_refuels_in_move": false,
      "refuel_gap_minutes": 11,
      "custom_field_name": false
    }
}
```

* `type` - string. Always "metering".
* `id` - int. Sensor's id.
* `sensor_type` - [metering sensor type](index.md#metering-sensor-type-values). Type of the sensor.
* `name` - string, max size 100. A name of sensor.
* `input_name` - string, max size 64. 
* `divider` - double. 
* `accuracy` - double. The minimum=`0.0`, maximum=`100.0` with step `0.25`.
* `units` - string.
* `units_type` - [enum](../../../../getting-started/introduction.md#data-types). Units type for a sensor.
* `parameters` - optional object with additional parameters.
    * `parent_ids` - optional array of parent_ids for composite sensor.
    * `volume` - double. Optional. Volume for composite sensor.
    * `parent_ids` - optional. int array. Array of `parent_ids` for composite sensor.
    * `volume` - optional. Double. Volume for composite sensor.
    * `min` - optional. Double. Min acceptable raw value for a sensor.
    * `max` - optional. Double. Max acceptable raw value for a sensor.
    * `max_lowering_by_time` - optional. Double. Maximum legal value lowering per hour.
    * `max_lowering_by_mileage` - optional. Double. Maximum legal value lowering per 100 km.
    * `ignore_drains_in_move` - optional. Boolean. Default is false. If true, the fuel drains will not be detected during movement.
    * `ignore_refuels_in_move` - optional. Boolean. Default is false. If true, the refuels will not be detected during movement.
    * `refuel_gap_minutes` -  optional. Integer. Default is 5. The time in minutes after the start of the movement, refuels will be detected during movement.
    * `custom_field_name` - optional. Boolean. Default false. The parameter determines whether the `input_name` field is a custom value was entered by user.
      This makes sense only if the [tracker model](../index.md#list_models) has the feature `has_custom_fields`.

#### Metering sensor type values

*   `fuel`
*   `temperature`
*   `rpm`
*   `custom`
*   `fuel_consumption`
*   `instant_consumption`
*   `power`
*   `speed`
*   `flow_meter`
*   `acceleration`


### Discrete input

```json
{
  "type": "discrete",
  "id": 888951,
  "sensor_type": "ignition",
  "name": "Ignition",
  "input_number": 4
}
```

* `type` - string. Always "discrete".
* `id` - int. An ID of a sensor.
* `sensor_type` - [discrete sensor type](index.md#discrete-sensor-type-values). Type of the sensor.
* `name` - string, max size 100.
* `input_number` - int, [1..8]. Assigned input number.

#### Discrete sensor type values

*   `ignition`
*   `sos_button`
*   `power`
*   `engine`
*   `car_alarm`
*   `door`
*   `charge`
*   `detach`
*   `custom`


### Virtual sensor

```json
{
  "type": "virtual",
  "id": 1700049,
  "sensor_type": "virtual_ignition",
  "name": "Virtual Ignition",
  "input_name": "board_voltage",
  "custom_field_name": false,
  "parameters": {
    "calc_method": "in_range",
    "range_from": 13.4,
    "value_titles": [{
        "value": "0",
        "title": "Off"
    }, {
        "value": "1",
        "title": "On"
    }]
  }
}
```

* `type` - string. Always "virtual".
* `id` - int. Sensor's id.
* `sensor_type` - [virtual sensor type](index.md#virtual-sensor-type-values). Type of the sensor. "virtual_ignition" for virtual ignition or "state" for others.
* `name` - string, max size 100. A name of sensor.
* `input_name` - string, max size 64. A source input field name (identifier).
* `custom_field_name` - optional. Boolean. Default false. The parameter determines whether the `input_name` field is a custom value was entered by user.
  This makes sense only if the [tracker model](../index.md#list_models) has the feature `has_custom_fields`.
* `parameters` - optional object with additional parameters.
    * `calc_method` - [enum](../../../../getting-started/introduction.md#data-types). A method of sensor value calculation. One of this: "in_range", "identity", "bit_index".
    * `range_from` - double. Low bound of range. It is used only with "in_range" calc method.
    * `range_to` - double. High bound of range. It is used only with "in_range" calc method.
    * `bit_index` - int, `[1..N]`. A bit index in input field source value. It is used only with "bit_index" calc method.
    * `value_titles` - mapping for bind special titles for sensor values, if it is necessary.
        * `value` - string, max size 64. Sensor value. 
        * `title` - string, max size 64. Title for the sensor value.

#### Virtual sensor type values

*   `state`
*   `virtual_ignition`

Some requirements:

* There can be only one virtual sensor with type `virtual_ignition` for tracker.
* One or both field `range_from` and `range_to` must be present for the calc method "in_range".
* Field `bit_index` must be present for the calc method "bit_index".
* There can be no more than 100 value titles.
* All values must be unique within `value_titles`.

Described work with virtual sensors in our [instructions](../../../../guides/data-retrieval/sensor-data.md).

## API actions

API base path: `/tracker/sensor`.

### batch_list

List tracker sensors bound to trackers with specified identifiers (parameter `trackers`).

There exists a similar method for working with a single tracker - [list](#list).

#### Parameters
| Name     | Description                                                                                                                                                                                                                         | Type      |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| trackers | Set of tracker identifiers. Each of the relevant trackers must be accessible to the authorized user and not be blocked. Number of trackers (length of array) is limited to a maximum of 500 (this number may be changed in future). | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/batch_list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [204104, 181451]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/batch_list?hash=a6aa75587e5c59c32d347da438505fc3&trackers=[204104, 181451]
    ```

#### Response

Contains a map, where keys are IDs from **trackers** parameter and values are lists of [sensor](#sensor-sub-types) objects.

```json
{
  "success": true,
  "result": {
    "11": [
      {
        "id": 1,
        "type": "discrete",
        "sensor_type": "fuel",
        "name": "Main tank",
        "input_name": "fuel_level",
        "group_type": null,
        "divider": 1,
        "accuracy": 0.0,
        "units": null,
        "units_type": "litre"
      }
    ]
  }
}
```

#### Errors

* 217 - List contains nonexistent entities -  if one of `trackers` either does not exist or is blocked.
* 221 - Device limit exceeded - if too many IDs were passed in `trackers` parameter.


### `create`

Creates a sensor.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                                                                     | type        |
|:-----------|:------------------------------------------------------------------------------------------------|:------------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int         |
| sensor     | [Sensor object](#sensor-sub-types).                                                             | JSON object |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor": {"type": "metering", "id": 860250,"sensor_type": "temperature", "name": "OBD Coolant temperature", "input_name": "obd_coolant_t", "divider": 1.0, "accuracy": 0.0, "units": "", "units_type": "celsius"}'
    ```

#### Response

```json
{
    "success": true,
    "id": 937
}
```

* `id` - int. An ID of created sensor.

#### Errors

* 232 - Input already in use – if given input number (for discrete input) or input name (for metering sensor) already 
in use.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 - Not allowed for clones of the device – if tracker is clone.
* 270 - Too many sensors of same type - the number of tracker's sensors, having same `sensor_type` is limited.


### `delete`

Deletes a sensor with `sensor_id` from the database.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |
| sensor_id  | Sensor ID.                                                                                      | int  | 234567 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor_id": 23456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/delete?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&sensor_id=23456
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database - if sensor with a `sensor_id` does not exist or owned by another user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 – Not allowed for clones of the device - if tracker is a clone.


### `list`

List tracker sensors bound to tracker with specified ID (`tracker_id` parameter).

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/sensor/list?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### Response

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
    "accuracy": 0.0,
    "units": "",
    "units_type": "celsius" 
   }]
}
```

* `list` - list of sensor objects. See [sensor](#sensor-sub-types) object description.

#### Errors

* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions, or some other reason.


### `update`

Updates sensor.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                                                                     | type        |
|:-----------|:------------------------------------------------------------------------------------------------|:------------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int         |
| sensor     | [Sensor object](#sensor-sub-types).                                                             | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor": {"type": "metering", "id": 860250, "sensor_type": "temperature", "name": "OBD Coolant temperature", "input_name": "obd_coolant_t", "divider": 1.0, "accuracy": 0.0, "units": "", "units_type": "celsius"}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – if sensor does not exist or owned by another user.
* 232 - Input already in use – if given input number (for discrete input) or input name (for metering sensor) already 
in use.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 - Not allowed for clones of the device – if tracker is a clone.


### batch_copy

Copies sensors from one tracker to another.

!!! warning "Important"
    This operation will delete sensors of target trackers, and some sensor data could be lost!

**required sub-user rights:** `tracker_update`.

#### Parameters

| name            | description                                                                                                                              | type  | format           |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:------|:-----------------|
| base_tracker_id | ID of the base tracker (aka "object_id") from which you want to copy sensors. Tracker must belong to authorized user and not be blocked. | int   | 123456           |
| trackers        | ID of trackers. Target trackers for copying sensors.                                                                                     | [int] | `[12345, 54321]` |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/batch_copy' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "base_tracker_id": 123456, "trackers": [56789, 54321]}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 272 – Trackers must have the same model - if base tracker and one of target trackers has a different model.

### data/read

Gets all `metering` or `virtual` sensor readings with values and time per requested period.
It can't be used with discrete sensor. 

#### Parameters

| name       | description                                                                                                                                                                       | type                                                                | format                |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|:----------------------|
| tracker_id | ID of the base tracker (aka "object_id") from which you want to read sensor's data. Tracker must belong to authorized user and not be blocked.                                    | int                                                                 | 123456                |
| sensor_id  | Sensor ID.                                                                                                                                                                        | int                                                                 | 234567                |
| from       | Start date and time for searching.                                                                                                                                                | [date/time](../../../../getting-started/introduction.md#data-types) | "2022-02-28 00:00:00" |
| to         | End date and time for searching. Must be after `from` date. Maximum period is `maxReportTimeSpan`, default 30 days.                                                               | [date/time](../../../../getting-started/introduction.md#data-types) | "2022-03-28 23:59:00" |
| raw_data   | If `true` then the response will contain raw data without any calibration and multiplication. Affects only `metering` sensors. Default value is false for backward compatibility. | boolean                                                             | false                 |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/sensor/data/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "sensor_id": 1456789, "from": "2022-02-28 00:00:00", "to": "2022-03-28 23:59:00"}'
    ```

#### Response

```json
{
  "success": true,
  "list": [
    {
      "value": 100500,
      "get_time": "2022-02-28 00:00:00"
    },
    {
      "value": 100501,
      "get_time": "2022-02-28 00:00:30"
    }
  ]
}
```

* `value` - a value of sensor data. It can be double, int or string depending on the sensor type.
* `get_time` - time when value was received.

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 211 – Requested time span is too big - if interval between "from" and "to" is too big. Maximum period is `maxReportTimeSpan`.
* 228 – Not supported by the sensor - if sensor is not a metering or virtual sensor. 

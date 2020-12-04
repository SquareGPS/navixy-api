---
title: Counter actions
description: Counter actions
---

# Counter actions

API path: `/tracker/counter`.

### read

Reads counter of passed `type`.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| type | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`. | string enum | "odometer" |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}tracker/counter/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "type": "odometer"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}tracker/counter/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&type=odometer
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

Updates counter of passed `type`.

**required sub-user rights:** `tracker_update`

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| type | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`. | string enum | "odometer"|
| multiplier | A new value of counter multiplier. | float | 1.34 |
| sensor_id | Id of the sensor, which must be used as the source of odometer data (in case when parameter "type" equals "odometer"). If "type" is not "odometer", "sensor_id" must be null. | int | 123 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}tracker/counter/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "type": "odometer", "multiplier": "3.14", "sensor_id": "1234"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}tracker/counter/update?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&type=odometer&multiplier=3.14&sensor_id=1234
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
 * if type is not "odometer"  and `sensor_id` is not null.
 * if sensor with specified `sensor_id` is not a metering sensor.
 * if sensor with specified `sensor_id` belongs to another tracker.
 * if `sensor_id` is negative.
 * if sensor with such a `sensor_id` is not exist.
 * if type value is not one of list above.


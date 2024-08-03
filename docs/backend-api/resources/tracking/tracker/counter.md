---
title: Counters
description: This resource contains counter specific actions
---

# Counters

This resource contains counter specific actions

Find information on how to get counters data [here](../../../guides/data-retrieval/sensor-data.md).


## Resource specific actions

Actions with counter entities:

* [/tracker/counter/read](#read)
* [/tracker/counter/update](#update)

Actions with counter values:

* [/tracker/get_counters](#get_counters)
* [/tracker/counter/value/get](#valueget)
* [/tracker/counter/value/list](#valuelist)
* [/tracker/counter/value/set](#valueset)
* [/tracker/counter/data/read](#dataread)


### `read`

Reads counter of passed `type`.

#### Parameters

| name       | description                                                                                     | type                                           | format     |
|:-----------|:------------------------------------------------------------------------------------------------|:-----------------------------------------------|:-----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int                                            | 123456     |
| type       | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`.                           | [enum](../../../getting-started/introduction.md#data-types) | "odometer" |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "type": "odometer"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/counter/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&type=odometer
    ```

#### Response

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

#### Errors

* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 - Not allowed for clones of the device – if specified tracker is a clone.


### `update`

Updates counter of passed `type`.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name       | description                                                                                                                                                                   | type                                           | format     |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------|:-----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.                                                                               | int                                            | 123456     |
| type       | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`.                                                                                                         | [enum](../../../getting-started/introduction.md#data-types) | "odometer" |
| multiplier | A new value of counter multiplier.                                                                                                                                            | float                                          | 1.34       |
| sensor_id  | ID of the sensor, which must be used as the source of odometer data (in case when parameter "type" equals "odometer"). If "type" is not "odometer", "sensor_id" must be null. | int                                            | 123        |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "type": "odometer", "multiplier": 3.14, "sensor_id": 1234}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/counter/update?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&type=odometer&multiplier=3.14&sensor_id=1234
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 8 - Queue service error, try again later – cannot set counter value, try later.
* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 - Not allowed for clones of the device – if specified tracker is a clone.
* 7 - Invalid parameters –
    * if type is not "odometer"  and `sensor_id` is not null.
    * if sensor with specified `sensor_id` is not a metering sensor.
    * if sensor with specified `sensor_id` belongs to another tracker.
    * if `sensor_id` is negative.
    * if sensor with such a `sensor_id` is not exists.
    * if type value is not one of list above.


### `get_counters`

Gets last values of the tracker's counters.

#### Parameters

| name       | description                   | type | format |
|:-----------|:------------------------------|:-----|:-------|
| tracker_id | Tracker ID (aka "object_id"). | int  | 999119 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/get_counters' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 265489}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/get_counters?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489
    ```

#### Response

```json
{
  "success": true,
  "user_time": "2014-07-09 07:50:58",
  "list": [
    {
      "type": "odometer",
      "value": 100500.1,
      "update_time": "2014-03-06 13:57:00"
    }
  ]
}
```

* `user_time` - date/time. Current time in user's timezone.
* `list` - array of counter value objects.
    * `type` - enum. One of predefined semantic counter types (see below).
    * `value` - double. Counter value.
    * `update_time` - date/time. Date and time when the data updated.

List of counter types:

* `odometer` - odometer.
* `fuel_consumed` - total fuel consumed.
* `engine_hours` - engine hours.

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.


### `value/get`

Gets actual value of specified `type` of sensor.

#### Parameters

| name       | description                                                                                     | type                                           | format     |
|:-----------|:------------------------------------------------------------------------------------------------|:-----------------------------------------------|:-----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int                                            | 123456     |
| type       | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`.                           | [enum](../../../getting-started/introduction.md#data-types) | "odometer" |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/value/get' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "type": "odometer"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/counter/value/get?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&type=odometer
    ```

#### Response

```json
{
    "success": true,
    "value": 18.9
}
```

* `value` - float. The last valuer of counter.

#### Errors

* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user, counter does not exist or
  there are no values yet. use /tracker/counter/set to create new counter (if not exist) and save some value.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.

### `value/list`

Get actual values for counters of passed `type` and `trackers`.

#### Parameters

| name     | description                                                           | type                                           | format             |
|:---------|:----------------------------------------------------------------------|:-----------------------------------------------|:-------------------|
| trackers | List of the tracker's ID belonging to authorized user.                | int array                                      | `[123456, 234567]` |
| type     | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`. | [enum](../../../getting-started/introduction.md#data-types) | "odometer"         |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/value/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [123456, 234567], "type": "odometer"}'
    ```

#### Response

```json
{
  "success": true,
  "value": {
    "14": 18.9
  }
}
```

* `value` - a map with tracker's IDs as keys.

#### Errors

* 204 - Entity not found – if one of the specified counter does not exist or there are no values yet. Use
  [`/tracker/counter/set`](#valueset) to create new counter (if not exist) and save some value.
* 217 - List contains nonexistent entities – if one of the specified trackers does not exist or is blocked.


### `value/set`

Creates new counter of passed `type` (if not) and update its `value`.

#### Parameters

| name       | description                                                                                     | type                                           | format     |
|:-----------|:------------------------------------------------------------------------------------------------|:-----------------------------------------------|:-----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int                                            | 123456     |
| type       | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`.                           | [enum](../../../getting-started/introduction.md#data-types) | "odometer" |
| value      | A new value of counter.                                                                         | float                                          | 233.21     |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/value/set' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "type": "odometer", "value": 233.21}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 8 - Queue service error, try again later - can't set counter value, try later.
* 204 - Entity not found – if there is no tracker with such ID belonging to authorized user.
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 - Not allowed for clones of the device – if specified tracker is a clone.


### `data/read`

Returns counter values for a period.

#### Parameters

| name       | description                                                           | type                                           | format                  |
|:-----------|:----------------------------------------------------------------------|:-----------------------------------------------|:------------------------|
| tracker_id | Tracker ID (aka "object_id").                                         | int                                            | 123456                  |
| type       | Counter type. One of `["odometer", "fuel_consumed", "engine_hours"]`. | [enum](../../../getting-started/introduction.md#data-types) | "odometer"              |
| from       | Requested period start.                                               | date/time                                      | `"2021-02-25 12:21:17"` |
| to         | Requested period end.                                                 | date/time                                      | `"2021-03-25 12:21:17"` |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/counter/data/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "type": "odometer", "from": "2021-02-01 00:00:00", "to": "2021-02-01 03:00:00"}'
    ```

#### Response

```json
{
  "success": true,
  "list": [{
      "value": 3835.52,
      "update_time": "2021-02-01 02:52:55"
  }, {
      "value": 3835.7,
      "update_time": "2021-02-01 02:57:18"
  }]
}
```

#### Errors

* 204 - Entity not found – if there is no tracker or counter belonging to authorized user.
* 211 - Requested time span is too big – if interval between "from" and "to" is too big (maximum value specified in API config)
* 208 - Device blocked – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 7 - Invalid parameters –
    * if `from` is after `to`;
    * if between `from` and `to` more than 31 days.


---
title: Sensor readings
description: API call to get last values for all metering sensors and state values. Includes CAN, OBD, and fuel.
---
# Sensor readings

API call to get last values for all metering sensors and state values. Includes CAN, OBD, and fuel. 

Described getting data from sensors in our [guides](../../../guides/data-retrieval/sensor-data.md). 


## API actions

API base path: `/tracker/readings`.

### `list`

Gets last values for all sensors, state values and counters.

#### Parameters

| name               | description                                                                                        | type                                                                                                                                                     | format |
|:-------------------|:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:-------|
| tracker_id         | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.    | int                                                                                                                                                      | 999199 |
| sensor_type        | Optional. If specified, state values and counters will be omitted. Used to filter sensors by type. | string<br/> [metering sensor type](sensor/index.md#metering-sensor-type-values) or [virtual sensor type](sensor/index.md#virtual-sensor-type-values) | "fuel" |
| include_components | Optional. Default is `true`. If set to `false`, parts of composite sensors will be excluded.       | boolean                                                                                                                                                  | true   |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/readings/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 265489}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/readings/list?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489
    ```

#### Response

```json
{
  "success": true,
  "inputs": [
    {
      "sensor_id": 37641,
      "value": 5.66,
      "label": "label",
      "units": "litres",
      "name": "fuel_level",
      "type": "fuel",
      "units_type": "custom",
      "update_time": "2023-06-28 06:05:59",
      "composite_sensor_ids": [37651, 37652]
    }
  ],
  "states": [
    {
      "field": "obd_mil_status",
      "value": 12345.23,
      "update_time": "2023-06-28 06:05:59"
    }
  ],
  "virtual_sensors": [
    {
      "sensor_id": 37643,
      "label": "Virtual Ignition",
      "value": "On",
      "type": "virtual_ignition",
      "update_time": "2023-06-28 06:05:59"
    },
    {
      "label": "Hood state",
      "value": "Closed",
      "type": "state",
      "update_time": "2023-06-28 06:05:59"
    }
  ],
  "counters": [
    {
      "type": "odometer",
      "value": 3232.9923342688653,
      "update_time": "2023-06-28 06:05:59"
    }
  ]
}
```

* `inputs` - an array of JSON objects containing information about the tracker sensors readings.
    * `sensor_id` - int. The ID of the sensor.
    * `value` - float. The value of the sensor.
    * `label` - string. The label of the sensor.
    * `units` - string. The units in which the sensor value is measured.
    * `name` - string. The name of the sensor.
    * `type` - [metering sensor type](sensor/index.md#metering-sensor-type-values). The type of the sensor.
    * `units_type` - string. The type of the units in which the sensor value is measured.
    * `update_time` - date/time. The time when the sensor value was updated.
    * `composite_sensor_ids` - array of int. The IDs of the composite sensors that include sensor. Optional.
* `states` - an array of JSON objects containing information about the tracker state readings.
    * `field` - string. The field name of the state.
    * `value` - can be string, int, float, boolean, or null. The value of the field.
    * `update_time` - date/time. The time when the field value was updated.
* `virtualSensors` - an array of JSON objects containing information about the tracker virtual sensors readings.
    * `sensor_id` - int. The ID of the virtual sensor.
    * `value` - float. The value of the virtual sensor.
    * `label` - string. The label of the virtual sensor.
    * `type` - [virtual sensor type](sensor/index.md#virtual-sensor-type-values). The type of the virtual sensor.
    * `update_time` - date/time. The time when the virtual sensor value was updated.
* `counters` - an array of JSON objects containing information about the tracker counter readings.
    * `type` - string. The type of the counter.
    * `value` - float. The value of the counter.
    * `update_time` - date/time. The time when the counter value was updated.

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.

### `batch_list`

Gets last values for all sensors, state values and counters on multiple trackers.

#### Parameters

| name               | description                                                                                        | type                                                                                                                                                     | format          |
|:-------------------|:---------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------|
| trackers           | An array of tracker IDs (aka "object_id"). Trackers must belong to authorized user.                | int                                                                                                                                                      | [999199,991999] |
| sensor_type        | Optional. If specified, state values and counters will be omitted. Used to filter sensors by type. | string<br/> [metering sensor type](sensor/index.md#metering-sensor-type-values) or [virtual sensor type](sensor/index.md#virtual-sensor-type-values) | "fuel"          |
| include_components | Optional. Default is `true`. If set to `false`, parts of composite sensors will be excluded.       | boolean                                                                                                                                                  | true            |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/readings/batch_list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "trackers": [10181215,10038816]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/readings/batch_list?hash=a6aa75587e5c59c32d347da438505fc3&trackers=[10181215,10038816]
    ```

#### Response

```json

{
  "result": {
    "10181215": {
      "inputs": [
        {
          "sensor_id": 37641,
          "label": "Tank 1",
          "units": "",
          "name": "lls_level_1",
          "type": "fuel",
          "min_value": 0.0,
          "max_value": 480.0,
          "value": 225.71,
          "units_type": "litre",
          "converted_units_type": null,
          "converted_value": null,
          "update_time": "2023-06-28 06:13:09",
          "composite_sensor_ids": [37651, 37652]
        },
        {
          "sensor_id": 37642,
          "label": "Tank 2",
          "units": "",
          "name": "lls_level_6",
          "type": "fuel",
          "min_value": 0.0,
          "max_value": 300.0,
          "value": 113.52,
          "units_type": "litre",
          "converted_units_type": null,
          "converted_value": null,
          "update_time": "2023-05-11 00:35:16"
        },
        {
          "sensor_id": 37643,
          "label": "Fuel",
          "units": "",
          "name": "composite",
          "type": "fuel",
          "min_value": 0.0,
          "max_value": 700.0,
          "value": 175.31,
          "units_type": "litre",
          "converted_units_type": null,
          "converted_value": null,
          "update_time": "2023-05-11 00:35:26"
        }
      ],
      "states": [
        {
          "field": "input_status",
          "value": 0,
          "update_time": "2023-06-28 06:13:09"
        },
        {
          "field": "output_status",
          "value": 0,
          "update_time": "2023-06-28 06:13:09"
        }
      ],
      "virtual_sensors": [
        {
          "sensor_id": 37644,
          "label": "Virtual Ignition",
          "value": "On",
          "type": "virtual_ignition",
          "update_time": "2023-06-28 06:05:59"
        },
        {
          "sensor_id": 37645,
          "label": "Hood state",
          "value": "Closed",
          "type": "state",
          "update_time": "2023-06-28 06:05:59"
        }
      ],
      "counters": [
        {
          "type": "odometer",
          "value": 3232.9923342688653,
          "update_time": "2023-06-28 06:05:59"
        }
      ]
    },
    "10038816": {
      "inputs": [],
      "states": [
        {
          "field": "input_status",
          "value": 0,
          "update_time": "2023-06-28 06:13:23"
        },
        {
          "field": "output_status",
          "value": 0,
          "update_time": "2023-06-28 06:13:23"
        }
      ],
      "counters": [
        {
          "type": "odometer",
          "value": 20854.422727641213,
          "update_time": "2023-06-28 06:12:23"
        }
      ]
    }
  },
  "success": true
}
```

* `inputs` - an array of JSON objects containing information about the tracker sensors readings.
    * `sensor_id` - int. The ID of the sensor.
    * `value` - float. The value of the sensor.
    * `label` - string. The label of the sensor.
    * `units` - string. The units in which the sensor value is measured.
    * `name` - string. The name of the sensor.
    * `type` - [metering sensor type](sensor/index.md#metering-sensor-type-values). The type of the sensor.
    * `units_type` - string. The type of the units in which the sensor value is measured.
    * `update_time` - date/time. The time when the sensor value was updated.
    * `min_value` - float. The minimum value of the sensor.
    * `max_value` - float. The maximum value of the sensor.
    * `converted_units_type` - string. The type of the units in which the sensor value is converted.
    * `converted_value` - float. The converted value of the sensor reading.
    * `composite_sensor_ids` - array of int. The IDs of the composite sensors that include sensor. Optional.
* `states` - an array of JSON objects containing information about the tracker state readings.
    * `field` - string. The field name of the state.
    * `value` - can be string, int, float, boolean, or null. The value of the field.
    * `update_time` - date/time. The time when the field value was updated.
* `virtualSensors` - an array of JSON objects containing information about the tracker virtual sensors readings.
    * `sensor_id` - int. The ID of the virtual sensor.
    * `value` - float. The value of the virtual sensor.
    * `label` - string. The label of the virtual sensor.
    * `type` - [virtual sensor type](./sensor/index.md#virtual-sensor-type-values). The type of the virtual sensor.
    * `update_time` - date/time. The time when the virtual sensor value was updated.
* `counters` - an array of JSON objects containing information about the tracker counter readings.
    * `type` - string. The type of the counter.
    * `value` - float. The value of the counter.
    * `update_time` - date/time. The time when the counter value was updated.

#### Errors

* 217 - List contains nonexistent entities.

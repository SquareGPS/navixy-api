---
title: Sensor readings
description: API call to get last values for all metering sensors and state values. Includes CAN, OBD, and fuel.
---
# Sensor readings

API call to get last values for all metering sensors and state values. Includes CAN, OBD, and fuel.

***

## API actions

API base path: `/tracker/readings`.

### list

Gets last values for all metering sensors, state values and counters.

#### parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 999199 |

#### examples

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

#### response

```json
{
  "success": true,
  "inputs": [
    {
      "value": 5.66,
      "label": "label",
      "units": "litres",
      "name": "fuel_level",
      "type": "fuel",
      "units_type": "custom",
      "update_time": "2023-06-28 06:05:59"
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

* `states.value` - can be string, int, float, boolean, or null.

#### errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.

### batch_list

Gets last values for all metering sensors, state values and counters on multiple trackers.

#### parameters

| name     | description                                                                         | type | format          |
|:---------|:------------------------------------------------------------------------------------|:-----|:----------------|
| trackers | An array of tracker IDs (aka "object_id"). Trackers must belong to authorized user. | int  | [999199,991999] |

#### examples

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

#### response

```json

{
  "result": {
    "10181215": {
      "inputs": [
        {
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
          "update_time": "2023-06-28 06:13:09"
        },
        {
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
          "field": "movement_state",
          "value": "parked",
          "update_time": "2023-06-28 06:13:09"
        },
        {
          "field": "tcp_status",
          "value": 2,
          "update_time": "2023-06-28 06:13:57"
        },
        {
          "field": "output_status",
          "value": 0,
          "update_time": "2023-06-28 06:13:09"
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
          "field": "movement_state",
          "value": "parked",
          "update_time": "2023-06-28 06:13:23"
        },
        {
          "field": "output_status",
          "value": 0,
          "update_time": "2023-06-28 06:13:23"
        },
        {
          "field": "tcp_status",
          "value": 2,
          "update_time": "2023-06-28 06:14:07"
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

* `states.value` - can be string, int, float, boolean, or null.

#### errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
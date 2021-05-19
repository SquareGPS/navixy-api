---
title: Sensor readings
description: API call to get last values for all metering sensors and state values. Includes CAN, OBD, and fuel.
---
# Sensor readings

API base path: `/tracker/readings`.

API call to get last values for all metering sensors and state values. Includes CAN, OBD, and fuel.

### list

Gets last values for all metering sensors and state values.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 999199 |

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
            "update_time": "2019-03-16 11:15:19"
        }
  ],
  "states": [
    {
       "field": "obd_mil_status",
       "value": 12345.23,
       "update_time": "2019-03-16 11:15:19"
    }
  ]
}
```

* `states.value` - can be string, int, float, boolean, or null.

#### errors

* 204 – Entity not found - if there is no tracker with such id belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.


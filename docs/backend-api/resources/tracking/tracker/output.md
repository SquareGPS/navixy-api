---
title: Output control
description: Output control
---
# Output control

API base path: `/tracker/output`

### set_all

Request to change the states of all digital outputs of the device. The device must be online.

**required sub-user rights:** `tracker_set_output`

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 999199 |
| outputs | Array of desired states of all digital outputs, e.g. [true, true, false] means output 1 is on, output 2 is on, output 3 is off. | array of boolean | [true, true, false] |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/output/set_all' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489", "outputs": [true, true, false]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/output/set_all?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489&outputs=[true, true, false]
    ```

#### response
```json
{ "success": true }
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 213 – Cannot perform action: the device is offline (if corresponding tracker is not connected to the server).
* 214 – Requested operation or parameters are not supported by the device (if device does not support batch mode, or has a different number of outputs).
* 219 – Not allowed for clones of the device (if tracker is clone).

### set

Request to change the state of the specified digital output of the device. The device must be online.

**required sub-user rights:** `tracker_set_output`

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 999199 |
| output | The number of the output to control, starting from 1. | int | 1 |
| enable | True if the requested output should be enabled, or false if it should be disabled. | boolean | true |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/output/set' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": "265489", "output": "1", "enable": "true"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/output/set?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489&output=1&enable=true
    ```

#### response

```json
{ "success": true }
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 213 – Cannot perform action: the device is offline (if corresponding tracker is not connected to the server).
* 214 – Requested operation or parameters are not supported by the device (if device does not support controlling single output, does not have specified digital output, or the specified output reserved to “engine block” feature. In this case, output cannot be controlled by this command for safety reasons).
* 219 – Not allowed for clones of the device (if tracker is clone).


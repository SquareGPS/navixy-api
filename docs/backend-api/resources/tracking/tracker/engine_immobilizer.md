---
title: Engine immobilizer
description: Engine immobilizer
---
# Engine immobilizer

API base path: `/tracker/engine_immobilizer`

Engine immobilizer is an electronic security device fitted to a motor vehicle that prevents the engine from running 
unless it must run. This prevents the vehicle from being "hot wired" after entry has been achieved and thus reduces 
motor vehicle theft. This API call allows manipulating with immobilizer state.

### read

Request to read the state of engine immobilizer.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/engine_immobilizer/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"tracker_id": "123456", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/engine_immobilizer/read?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
   "success": true,
   "enabled": true
}
```

* `enabled` - `true` if engine immobilizer enabled.

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 214 – Requested operation or parameters are not supported by the device (if device does not support alarm mode).

### set

Request to change the engine immobilizer state of the device. The device must be online.

**required sub-user rights:** `tracker_set_output`

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| enabled | `true` if immobilizer should be enabled. | boolean | true/false |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/engine_immobilizer/set' \
        -H 'Content-Type: application/json' \ 
        -d '{"tracker_id": "123456", "enabled": "true", "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/engine_immobilizer/set?tracker_id=123456&enabled=true&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{ "success": true }
```

#### errors

* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 213 – Cannot perform action: the device is offline (if corresponding tracker is not connected to the server).
* 214 – Requested operation or parameters are not supported by the device (if device does not support alarm mode).
* 219 – Not allowed for clones of the device (if tracker is clone).

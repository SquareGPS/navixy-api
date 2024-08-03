---
title: Engine immobilizer
description: API requests to read the state of immobilizer and to set the new state.
---
# Engine immobilizer

API calls to read the state of immobilizer and to set the new state. Engine immobilizer is an electronic security device
fitted to a motor vehicle that prevents the engine from running unless it must run. This prevents the vehicle from being
"hot wired" after entry has been achieved and thus reduces motor vehicle theft. This API call allows manipulating with 
immobilizer state.


## API actions

API base path: `/tracker/engine_immobilizer`.

### `read`

Requests to read the state of engine immobilizer.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/engine_immobilizer/read' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/engine_immobilizer/read?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
   "success": true,
   "enabled": true
}
```

* `enabled` - boolean. `true` if engine immobilizer enabled.

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device - if device does not support alarm mode.


### `set`

Requests to change the engine immobilizer state of the device. The device must be online.

**required sub-user rights:** `tracker_set_output`.

#### Parameters

| name       | description                                                                                     | type    | format     |
|:-----------|:------------------------------------------------------------------------------------------------|:--------|:-----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int     | 123456     |
| enabled    | `true` if immobilizer should be enabled.                                                        | boolean | true/false |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/engine_immobilizer/set' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "enabled": true, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/engine_immobilizer/set?tracker_id=123456&enabled=true&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 213 – Cannot perform action: the device is offline - if corresponding tracker is not connected to the server.
* 214 – Requested operation or parameters are not supported by the device - if device does not support alarm mode.
* 219 – Not allowed for clones of the device - if tracker is clone.

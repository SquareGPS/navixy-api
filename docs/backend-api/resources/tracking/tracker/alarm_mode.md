---
title: Alarm mode
description: Contains API calls to read and set alarm mode of device.
---
# Alarm mode for tracker

Contains API calls to read and set alarm mode of device.


## API actions

API base path: `/tracker/alarm_mode`.

### `read`

Gets the state of alarm mode of device.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 999199 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/alarm_mode/read' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/alarm_mode/read?tracker_id=123456&hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
 "success": true,
 "enabled": true
}
```

* `enabled` - `true` if alarm mode enabled.

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device - if device does not support alarm mode.


### `set`

Changes the state of alarm mode of device. The device must be online.

#### Parameters

| name       | description                                                                                     | type    | format     |
|:-----------|:------------------------------------------------------------------------------------------------|:--------|:-----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int     | 999199     |
| enabled    | `true` if alarm mode should be enabled.                                                         | boolean | true/false |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/alarm_mode/set' \
        -H 'Content-Type: application/json' \
        -d '{"tracker_id": 123456, "enabled": true, "hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/alarm_mode/set?tracker_id=123456&enabled=true&hash=a6aa75587e5c59c32d347da438505fc3
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

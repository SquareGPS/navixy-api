---
title: LED
description: API calls to get and update LED state of the tracker.
---
# LED

API calls to get and update LED state of the tracker. LED switch should be available for the device.


## API actions

API base path: `/tracker/led`.

### `read`

Gets LED status for the specified tracker.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 999199 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/led/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 265489}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/led/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489
    ```

#### Response

```json
{
    "success": true,
    "value": true
}
```

* `value` - boolean. LED status, `true` - ON, `false` - OFF.

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device.


### `update`

Switches LED state for a specified tracker.

#### Parameters

| name       | description                                                                                     | type    | format     |
|:-----------|:------------------------------------------------------------------------------------------------|:--------|:-----------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int     | 999199     |
| value      | The new LED state, `true` – ON, `false` – OFF.                                                  | boolean | true/false |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/led/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "tracker_id": 265489, "value": true}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/led/update?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=265489&value=true
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device.


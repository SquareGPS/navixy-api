---
title: LED
description: API calls to get and update LED state of the tracker.
---
# LED

API base path: `/tracker/led`.

API calls to get and update LED state of the tracker. LED switch should be available for the device.

### read

Gets LED status for the specified tracker.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 999199 |

#### examples

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

#### response

```json
{
    "success": true,
    "value": true
}
```

* `value` - boolean. LED status, `true` - ON, `false` - OFF.

#### errors

* 201 – Not found in the database - if there is no tracker with such id belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device.

### update

Switches LED state for a specified tracker.

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 999199 |
| value | The new LED state, `true` – ON, `false` – OFF. | boolean | true/false |

#### examples

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

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database - if there is no tracker with such id belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device.


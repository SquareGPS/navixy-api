---
title: Engine hours
description: API call to read engine hours (time when engine is on) counted for the specified period.
---

# Engine hours

Contains API call to read engine hours (time when engine is on) counted for the specified period.


## API actions

API base path: `/tracker/stats/engine_hours`.

### `read`

Returns engine hours counted for the specified period.

#### Parameters

| name       | description                                                                                     | type                                                         | format                |
|:-----------|:------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|:----------------------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int                                                          | 123456                |
| from       | From date/time.                                                                                 | [date/time](../../../../getting-started/introduction.md#datetime-formats) | "2020-09-24 03:24:00" |
| to         | To date/time. Specified date must be after "from" date.                                         | [date/time](../../../../getting-started/introduction.md#datetime-formats) | "2020-09-24 06:24:00" |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/stats/engine_hours/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "from": "2020-09-24 03:24:00", "to": "2020-09-24 06:24:00"}'
    ```

#### Response

```json
{
    "success": true,
    "value": 42.0
}
```

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 211 – Requested time span is too big - if interval between "from" and "to" is too big (maximum value specified in API config).
* 214 – Requested operation or parameters are not supported by the device - if device does not have ignition input.
* 219 – Not allowed for clones of the device - if specified tracker is a clone.

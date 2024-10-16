---
title: Schedule proposals
description: Schedule proposals are "preview" of what tasks and routes will be created at the specified date range.
---

# Schedule proposals

Schedule proposals are "preview" of what tasks and routes will be created at the specified date range.


## API actions

API base path: `/task/schedule/proposal`.

### `list`

Get all tasks and routes that will be created by schedule.

#### Parameters

| name     | description                                                                                         | type                                                    | 
|:---------|:----------------------------------------------------------------------------------------------------|:--------------------------------------------------------|
| trackers | Optional. IDs of the trackers to which task is assigned.                                            | int array                                               |
| from     | Show tasks that will be created AFTER this date, e.g. "2014-07-01 00:00:00", should not before now. | [date/time](../../../../getting-started/introduction.md#data-types)  |
| to       | Show tasks will be created BEFORE this date, e.g. "2014-07-01 00:00:00", should not before `from`.  | [date/time](../../../../getting-started/introduction.md#data-types)  |
| filter   | Optional. Filter for task schedule label and description.                                           | string                                                  |
| types    | Optional. Tasks or routes. For example: `["task", "route"]`.                                        | [enum](../../../../getting-started/introduction.md#data-types) array |

* If `trackers`, `filter`, `from` or `to` is not passed or _null_ then appropriate condition not used to filter results.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/proposal/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "2020-11-24 00:00:00", "to": "2020-11-25 00:00:00"}'
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 111,
         "user_id": 3,
         "tracker_id": 22,
         "location": {
             "lat": 51.283546,
             "lng": 7.301086,
             "address": "Fichtenstrasse 11",
             "radius": 150
         },
         "label": "Deliver parcels",
         "description": "Quickly",
         "creation_date": "2014-01-02 03:04:05",
         "from": "2014-02-03 04:05:06",
         "to": "2014-03-04 05:06:07",
         "external_id": null,
         "status": "assigned",
         "status_change_date": "2014-01-02 03:04:05",
         "max_delay" : 5,
         "min_stay_duration": 0,
         "arrival_date": "2014-01-02 03:04:05",
         "stay_duration": 0,
         "origin": "imported",
         "tags": [1, 2],
         "type": "task",
         "form": <form_object>
    }]
}
```

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types only.

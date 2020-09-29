---
title: Mileage
description: Mileage
---

# Mileage

API base path: `/tracker/stats/mileage`

### read

Returns mileage in kilometers in specified period grouped by trackers and day.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| from | From time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). | string date/time | "2020-09-24 03:24:00" |
| to | To time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). Specified date must be after "from" date. | string date/time | "2020-09-24 06:24:00" |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/stats/mileage/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": "123456", "from": "2020-09-24 03:24:00", "to": "2020-09-24 06:24:00"}'
    ```

#### response

```json
{
  "success": true,
  "result": {
    "<tracker_id>": {
      "2000-01-01": { "mileage": 0.0 },
      "2000-01-02": { "mileage": 0.0 },
      "2000-01-03": { "mileage": 199.09 }
    }
  },
  "limit_exceeded": false
}
```

#### errors

* 211 – Requested time span is too big (if interval between "from" and "to" is too big (maximum value specified in API config)).
* 217 – List contains nonexistent entities.
* 221 – Device limit exceeded.

---
title: Mileage
description: API call to get mileage in kilometers in specified period grouped by trackers and day.
---

# Mileage

Contains API call to read mileage counted for the specified period.


## API actions

API base path: `/tracker/stats/mileage`.

### `read`

Returns mileage in kilometers in specified period grouped by trackers and day.

#### Parameters

| name     | description                                                                                         | type                                                         |
|:---------|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
| trackers | Array of tracker IDs (aka "object_id"). Trackers must belong to authorized user and not be blocked. | int array                                                    |
| from     | From date/time.                                                                                     | [date/time](../../../../getting-started/introduction.md#datetime-formats) |
| to       | To date/time. Specified date must be after "from" date.                                             | [date/time](../../../../getting-started/introduction.md#datetime-formats) |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/stats/mileage/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [123456], "from": "2020-09-24 03:24:00", "to": "2020-09-24 06:24:00"}'
    ```

#### Response

```json
{
  "success": true,
  "result": {
    "123456": {
      "2000-01-01": { "mileage": 0.0 },
      "2000-01-02": { "mileage": 0.0 },
      "2000-01-03": { "mileage": 199.09 }
    }
  },
  "limit_exceeded": false
}
```

#### Errors

* 211 – Requested time span is too big - if interval between "from" and "to" is too big (maximum value specified in API config).
* 217 – List contains nonexistent entities.
* 221 – Device limit exceeded.

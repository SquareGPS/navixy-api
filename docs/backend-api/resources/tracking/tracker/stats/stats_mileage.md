---
title: /stats/mileage
description: /stats/mileage
---

# /tracker/stats/mileage

### read
Returns mileage in kilometers in specified period grouped by tracker and day.

#### parameters
*   **trackers** – **int[]**. IDs of the trackers.
*   **from** - **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone).
*   **to** - **string**. A string containing date/time in `yyyy-MM-dd HH:mm:ss` format (in user's timezone). Specified date must be after "from" date.

#### return
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
*   211 – Requested time span is too big (if interval between "from" and "to" is too big (maximum value is specified in API config)).
*   217 – List contains nonexistent entities.
*   221 – Device limit exceeded.

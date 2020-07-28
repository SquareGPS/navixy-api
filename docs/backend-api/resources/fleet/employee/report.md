---
title: /employee/report
description: /employee/report
---

# /employee/report

## generate(...)

Generate report based on employees

#### parameters

*   **from** – **string**. Period start, e.g. “2014-07-01 00:00:00”
*   **to** – **string**. Period end, e.g. “2014-07-01 00:00:00”
*   **time_filter** – **object**. Object with time and days, e.g.
    ```js
    {
        "from": "00:00:00",
        "to": "23:59:59",
        "weekdays": [1, 2, 3, 4, 5, 6, 7]
    }
    ```
*   **plugin** – **object**. Object with plugin_id and params
*   **geocoder** – **object**. (optional) Geocoder type
*   **employee_ids** – **int\[\]**. Employee ids

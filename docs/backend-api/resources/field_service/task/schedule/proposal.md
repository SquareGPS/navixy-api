---
title: Task schedule proposal
description: Task schedule proposal
---

# Task schedule proposal

API path: `/task/schedule/proposal`.


## list()

Get all tasks and routes that will be created by schedule.

#### parameters

*   **trackers** – **array of int**. (optional) ids of the trackers to which task is assigned
*   **from** – **string**. (optional) show tasks that will be created AFTER this date, e.g. “2014-07-01 00:00:00”, should not before now
*   **to** – **string**. (optional) show tasks will be created BEFORE this date, e.g. “2014-07-01 00:00:00”, should not before **from**
*   **filter** – **string**. (optional) filter for task schedule label and description<br>
    If **trackers**, **filter**, **from** or **to** is not passed or _null_ then appropriate condition not used to filter results.
*   **types** – **string\[\]**. Tasks or routes. For example: \["task", "route"\]

#### return

```js
{
    "success": true,
    "list": [ <task> or <route>, ... ]
}
```

#### errors

general types only

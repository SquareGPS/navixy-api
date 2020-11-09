---
title: History unread
description: History unread
---

# History unread

API path: `/history/unread`.

### list

List less than or equal to **limit** of the latest user's unread history entries.

#### parameters

*   limit, int, optional
*   from, date/time, optional

Default and max limit is [maxHistoryLimit](../../../getting-started.md#constants).

Type of **from** is [date/time](../../../getting-started.md#data-types). Default **from** is **now** minus one year.

#### response

```json
{
    "success": true,
    "list": [${history_entry}, ... ] //list of zero or more JSON objects
}
```

where **history_entry** described in [Tracker history entry](./index.md#tracker-history-entry)

#### errors

*   212 – Requested limit is too big (more [maxHistoryLimit](../../../getting-started.md#constants) config option)


### count

Get count of user's unread history messages from **from** date.

#### parameters

*   from – optional
*   type – optional

Type of **from** is [date/time](../../../getting-started.md#data-types). Default **from** is **now** minus one year.

#### response

```json
{
    "success": true,
    "count": 1
}
```
---
title: History unread
description: History unread
---

# History unread

API path: `/history/unread`.

### list

List less then or equal to **limit** of latest user’s unread history entries with optional **type** (tracker|camera|socket).

#### parameters

*   limit, int, optional
*   from, date/time, optional
*   type, string one of tracker,camera,socket, optional

Default and max limit is [maxHistoryLimit](../../../getting-started.md#constants).

Type of **from** is [date/time](../../../getting-started.md#data-types). Default **from** is **now** minus one year.

#### response

```json
{
    "success": true,
    "list": [${history_entry}, ... ] //list of zero or more JSON objects
}
```

where **history_entry** described in [History entries](index.md#history-entries)

#### errors

*   212 – Requested limit is too big (more [maxHistoryLimit](../../../getting-started.md#constants) config option)


### count

Get count of user’s unread history messages from **from** date with optional **type** (tracker|camera|socket).

#### parameters

*   from – optional
*   type – optional

Type of **from** is [date/time](../../../getting-started.md#data-types). Default **from** is **now** minus one year.

#### response

```json
{
    "success": true,
    "count": <count> // int
}
```
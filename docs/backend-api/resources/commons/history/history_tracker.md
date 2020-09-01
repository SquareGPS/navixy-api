---
title: Tracker history
description: Tracker history
---

# Tracker history

API path: `/history/tracker/`.

### list

List less then or equal to **limit** of tracker events filtered by event types (**events**) between **from** date/time and **to** date/time sorted by **time** field.

#### parameters

*   **trackers** – **\[int\]**. list of tracker’s ids
*   **from** – [date/time](../../../getting-started.md#data-types). start date/time for searching
*   **to** – [date/time](../../../getting-started.md#data-types). end date/time for searching. must be after “from” date
*   **events** – **\[“string”\]** (optional, default: all). list of history types
*   **limit** – **int** (optional, default: [maxHistoryLimit](../../../getting-started.md#constants). max count of entries in result
*   **ascending** – **boolean** (optional, default: **true**). Sort ascending by time when it is **true** and descending when **false**.

If **events** (event types) not passed then list all event types.

Available event types can be obtained by [/history/type](history_type.md) action.

Default and max limit is 1000 by default. (Note for StandAlone: this value configured by maxHistoryLimit config option).

#### example

    {{ extra.api_example_url }}/history/tracker/list?hash=user_hash&trackers=[tracker_id]&from=2018-02-19 10:29:00&to=2018-02-19 11:30:00&events=["event_type"]



#### response

```json
{
    "success": true,
    "list": [ ${history_entry}, ... ], // list of zero or more JSON objects
    "limit_exceeded": false // boolean. false when listed all history entries satisfied to conditions
    // and true otherwise
}
```

where `history_entry` described in [Tracker history entry](index.md#tracker-history-entry).

#### errors

*   211 – Requested time span is too big (time span between **from** and **to** is more than [maxReportTimeSpan](../../../getting-started.md#constants) days).
*   212 – Requested **limit** is too big (**limit** is more than [maxHistoryLimit](../../../getting-started.md#constants)).
*   217 – List contains nonexistent entities – if one of the specified trackers does not exist or is blocked.

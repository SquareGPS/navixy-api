---
title: /history/tracker
description: /history/tracker
---

# /history/tracker/

## list(…)

List less then or equal to **limit** of tracker events filtered by event types (**events**) between **from** date/time and **to** date/time sorted by **time** field.

#### parameters:

*   **trackers** – **\[int\]**. list of tracker’s ids
*   **from** – [date/time](../../../getting-started.md#data-types). start date/time for searching
*   **to** – [date/time](../../../getting-started.md#data-types). end date/time for searching. must be after “from” date
*   **events** – **\[“string”\]** (optional, default: all). list of history types
*   **limit** – **int** (optional, default: [maxHistoryLimit](../../../getting-started.md#constants). max count of entries in result
*   **ascending** – **boolean** (optional, default: **true**). Sort ascending by time when it is **true** and descending when **false**.

If **events** (event types) not passed then list all event types.

Available event types: alarmcontrol, battery\_off, bracelet\_close, bracelet\_open, crash\_alarm, detach, door\_alarm, driver\_changed, force\_location\_request, g\_sensor, gps\_lost, gps\_recover, gsm\_damp, harsh\_driving, hood\_alarm, idle\_end, idle\_start, ignition, info, input\_change, inroute, outroute, inzone, outzone, lowpower, obd\_plug\_in, obd\_unplug, obj\_control, offline, online, parking, poweroff, poweron, security\_control, sos, speedup, track\_end, track\_start, sensor\_inrange, sensor\_outrange, strap\_bolt\_cut, strap\_bolt\_ins, vibration\_start, vibration\_end, light\_sensor\_bright, light\_sensor\_dark

Default and max limit is 1000 by default. (Note for StandAlone: this value configured by maxHistoryLimit config option).

#### example:

    [api_base_url]/history/tracker/list?hash=user_hash&trackers=[tracker_id]&from=2018-02-19 10:29:00&to=2018-02-19 11:30:00&events=["event_type"]



#### return:

```json
{
    "success": true,
    "list": [ ${tracker_history_entry}, ... ], // list of zero or more JSON objects
    "limit_exceeded": false // boolean. false when listed all history entries satisfied to conditions
    // and true otherwise
}
```

where `tracker_history_entry` described in [History entries](./history.md#history-entries).

#### errors:

*   211 – Requested time span is too big (time span between **from** and **to** is more than [maxReportTimeSpan](api/getting-started/#constants) days)
*   212 – Requested **limit** is too big (**limit** is more than [maxHistoryLimit](../../../getting-started.md#constants))
*   217 – List contains nonexistent entities – if one of the specified trackers does not exist or is blocked

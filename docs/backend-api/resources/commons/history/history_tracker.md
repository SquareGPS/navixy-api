---
title: Tracker history
description: Tracker history
---

# Tracker history

API path: `/history/tracker/`.

## list()

List less then or equal to **limit** of tracker events filtered by event types (**events**) between **from** date/time and **to** date/time sorted by **time** field.

#### parameters

*   **trackers** – **\[int\]**. list of tracker’s ids
*   **from** – [date/time](../../../getting-started.md#data-types). start date/time for searching
*   **to** – [date/time](../../../getting-started.md#data-types). end date/time for searching. must be after “from” date
*   **events** – **\[“string”\]** (optional, default: all). list of history types
*   **limit** – **int** (optional, default: [maxHistoryLimit](../../../getting-started.md#constants). max count of entries in result
*   **ascending** – **boolean** (optional, default: **true**). Sort ascending by time when it is **true** and descending when **false**.

If **events** (event types) not passed then list all event types.

Available event types: `alarmcontrol, battery_off, bracelet_close, bracelet_open, crash_alarm, detach, door_alarm, 
 driver_changed, force_location_request, g_sensor, gps_lost, gps_recover, gsm_damp, harsh_driving, hood_alarm, 
 idle_end, idle_start, ignition, info, input_change, inroute, outroute, inzone, outzone, lowpower, 
 obd_plug_in, obd_unplug, obj_control, offline, online, parking, poweroff, poweron, 
 security_control, sos, speedup, track_end, track_start, sensor_inrange, sensor_outrange, 
 strap_bolt_cut, strap_bolt_ins, vibration_start, vibration_end, light_sensor_bright, light_sensor_dark`

Default and max limit is 1000 by default. (Note for StandAlone: this value configured by maxHistoryLimit config option).

#### example

    {{ extra.api_example_url }}/history/tracker/list?hash=user_hash&trackers=[tracker_id]&from=2018-02-19 10:29:00&to=2018-02-19 11:30:00&events=["event_type"]



#### return

```js
{
    "success": true,
    "list": [ ${tracker_history_entry}, ... ], // list of zero or more JSON objects
    "limit_exceeded": false // boolean. false when listed all history entries satisfied to conditions
    // and true otherwise
}
```

where `tracker_history_entry` described in [History entries](./history.md#history-entries).

#### errors

*   211 – Requested time span is too big (time span between **from** and **to** is more than [maxReportTimeSpan](../../../getting-started.md#constants) days).
*   212 – Requested **limit** is too big (**limit** is more than [maxHistoryLimit](../../../getting-started.md#constants)).
*   217 – List contains nonexistent entities – if one of the specified trackers does not exist or is blocked.

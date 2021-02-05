---
title: Report plugins
description: Contains report plugins with plugin-specific parameters.
---

# Report plugins

Contains report plugins with plugin-specific parameters.

### Trips report

A report on detailed trip history.

#### parameters

Default **plugin_id**: 4.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| include_summary_sheet_only | If `true` the report will contain only a summary sheet for all chosen devices. | boolean |
| split | Trips will be split by stops if `true`. | boolean |
| show_idle_duration | Will show idle duration in report if `true`. | boolean |
| show_coordinates | Every address will contain longitude and latitude if `true`. | boolean |
| filter | If `true` short trips will hide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| group_by_driver | Group trips by driver assigned to the device if `true`. | boolean | 

### Stops report

A report on detailed stops history.

#### parameters

Default **plugin_id**: 6.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| show_coordinates | Every address will contain longitude and latitude if `true`. | boolean |

### Trips and stops by shifts report

A report on trips and stops by shifts.

#### parameters

Default **plugin_id**: 77.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| shifts | List of shifts with names, start and end time. e.g. `[{"name":"Shift1","start_time":"00:00","end_time":"23:59"}]` | array of objects |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| show_coordinates | Every address will contain longitude and latitude if `true`. | boolean |
| split_at_midnight | Split shifts at midnight if `true`. | boolean |

* `shifts` is:

```json
{
  "shifts": [{
    "name":"Shift1",
    "start_time":"00:00", 
    "end_time":"23:59"
  }]
}
```

### Geofence visits report

A report on date, time, and mileage in geofence.

#### parameters

Default **plugin_id**: 8.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| show_mileage | Adds mileage to the report if `true`. | boolean |
| show_not_visited_zones | Will show non visited zones if `true`. | boolean |
| min_minutes_in_zone | Minimum minutes in a zone to start determining visit. If the device was in a zone less than a specified time - the visit not count. | int |
| zone_ids | List of zone ids. | array of int |
| hide_charts| If `true`, charts will be hidden. | boolean |

### POI visits report

A report on date, time, and the number of visits to POIs.

#### parameters

Default **plugin_id**: 85.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| show_mileage | Adds mileage to the report if `true`. | boolean |
| show_not_visited_places | Will show non visited POIs if `true`. | boolean |
| min_minutes_in_place | Minimum minutes in a place to start determining visit. If the device was in a place less than a specified time - the visit not count. | int |
| place_ids | List of place ids. | array of int |
| hide_charts| If `true`, charts will be hidden. | boolean |

### Car security report

A report on alarms, tow alerts, AutoControl events, and crashes.

#### parameters

Default **plugin_id**: 15.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Emergency button (SOS) report

A report on SOS button events log

#### parameters

Default **plugin_id**: 16.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Fall detection report

A report on fall detection sensor log.

#### parameters

Default **plugin_id**: 17.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Tracker detach report

A report on demounting devices from tracking objects.

#### parameters

Default **plugin_id**: 18.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Overall security report

A report on all events related to security and safety.

#### parameters

default **plugin_id**: 19.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| group_by_type | If `true` events will group by type. | boolean |

### Engine hours report

A report on time spent in motion and on idling.

#### parameters

default **plugin_id**: 7.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| show_detailed | If  `true` will contain detailed engine hours tab. | boolean |
| include_summary_sheet_only | If `true` the report will contain only a summary sheet for all chosen devices. | boolean |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |

### Fuel volume report

A report on fuel refills, drains, consumption (based on fuel level sensor).

#### parameters

default **plugin_id**: 10.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| graph_type | The type of X-axis. Can be "time" or "mileage". | [enum](../../../getting-started.md#data-types) |
| detailed_by_dates | If `true` show final data on fuel traffic for each day in the period. | boolean |
| include_summary_sheet_only | If `true` the report will contain only a summary sheet for all chosen devices. | boolean |
| use_ignition_data_for_consumption | Calculate consumption only when the ignition was on if `true`. | boolean |
| include_mileage_plot | Optional. Used if `graph_type = time`. Show mileage plot if `true`. | boolean |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| include_speed_plot | If `true` show speed plot. | boolean |
| smoothing | Smooth graph if `true`. Smoothing reduces the accuracy of calculating refills or drains. | boolean |
| surge_filter | If `true` enables surge filter. | boolean |
| surge_filter_threshold | Defines a level of surge filter. Can be 0.01 - 0.99. | float |
| speed_filter | If `true` enables speed filter. | boolean |
| speed_filter_threshold | Defines a speed filter threshold. | int |

### Flow meter report

A report on fuel consumption counted by flow meter sensors.

#### parameters

default **plugin_id**: 78.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| detailed_by_dates | If `true`, a table with statistics for every single day in selected date range will be added to the report. | boolean |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| include_summary_sheet_only | If `true` the report will contain only a summary sheet for all chosen devices. | boolean |

### Vehicle sensors report

A report on CAN-bus and OBD2-port data.

#### parameters

default **plugin_id**: 22.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| details_interval_minutes | The interval in minutes. Can be `[30, 60, 180, 360]`. | int |
| graph_type | The type of X-axis. Can be "time" or "mileage". | [enum](../../../getting-started.md#data-types) |
| smoothing | Smooth data if `true`. | boolean |
| sensors | List of objects containing tracker_id and sensor_id. | array of objects |

* `sensors` is:

```json
{
  "sensors":[{
    "tracker_id":37714,
    "sensor_id":57968
  }]
}
```

### Speed violation

A report on speeding instances.

#### parameters

default **plugin_id**: 27.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| min_duration_minutes | A minimum time in seconds when speed is more than `max_speed` to determine violation. | int |
| max_speed | A maximum speed to determine violation. | int |
| group_by_driver | Group violations by driver assigned to the device if `true`. | boolean |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |

### Device switching ON/OFF report

A report on switching device using hardware switch.

#### parameters

default **plugin_id**: 23.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### GSM connection lost

A report on long disruptions of server connection

#### parameters

default **plugin_id**: 13.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Measuring sensors report

A report on detailed sensor reading history.

#### parameters

default **plugin_id**: 9.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| details_interval_minutes | The interval in minutes. Can be `[5, 30, 60, 180, 360]`. | int |
| graph_type | The type of X-axis. Can be "time" or "mileage". | [enum](../../../getting-started.md#data-types) |
| smoothing | Smooth data if `true`. | boolean |
| show_address | Address of each reading appears in report if `true`. | boolean |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| sensors | List of objects containing tracker_id and sensor_id. | array of objects |

* `sensors` is:

```json
{
  "sensors":[{
    "tracker_id":37714,
    "sensor_id":57968
  }]
}
```

### Equipment working time

A report on activity and idle time of the equipment.

#### parameters

default **plugin_id**: 12.

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| min_working_period_duration | A minimum time in seconds the equipment works to determine activity. Min = 1. | int |
| show_idle_percent | If `true` show percentage of idling. | boolean |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| sensors | List of objects containing tracker_id and sensor_id. | array of objects |

* `sensors` is:

```json
{
  "sensors":[{
    "tracker_id":37714,
    "sensor_id":57968
  }]
}
```

### Tasks report

A report on tasks statuses.

#### parameters

default **plugin_id**: 42.

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| show_external_id | Show external ID of task if `true`. | boolean |
| show_description | Show description of task if `true`. | boolean |
| show_forms | Show forms when the task has it if `true`. | boolean |  
| show_places_and_zones | Show places and geofences if `true`. | boolean |

### Form completion statistics report

A report on form fields completion rate.

#### parameters

default **plugin_id**: 70.

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |

### Work statuses report

A report on status changes history.

#### parameters

default **plugin_id**: 47.

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Check-in report

A report on markers for Check-in function.

#### parameters

default **plugin_id**: 80

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| show_coordinates | If `true`, coordinates will be added to the report. | boolean |

### Driver shift change report

A report on driver identification.

#### parameters

default **plugin_id**: 66.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Trips by state

A report on trips breakdown by jurisdictions.

#### parameters

default **plugin_id**: 73.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| filter | If `true` short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| include_summary_sheet_only | If `true` the report will contain only a summary sheet for all chosen devices. | boolean |
| group_type | A group type. Can be "province" or "country". | [enum](../../../getting-started.md#data-types) |

### Report on all events

An overall report about any kind of events.

#### parameters

default **plugin_id**: 11.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| group_by_type | Groups events by type if `true`. | boolean |
| event_types | A list of event types that will be considered. | array of string |

* the object with all `event_types` is:

```json
{
  "event_types":["auto_geofence_in","auto_geofence_out","door_alarm","forward_collision_warning","gps_lost","gps_recover","gsm_damp","harsh_driving","headway_warning","hood_alarm","idle_end","idle_start","ignition","inroute","outroute","lane_departure","obd_plug_in","obd_unplug","peds_collision_warning","peds_in_danger_zone","odometer_set","online","output_change","security_control","tracker_rename","track_end","track_start","tsr_warning","sensor_inrange","sensor_outrange","work_status_change","call_button_pressed","driver_changed","driver_identified","driver_not_identified","fueling","drain","checkin_creation","tacho","antenna_disconnect","check_engine_light","location_response","backup_battery_low","fatigue_driving","inzone","outzone","speedup","alarmcontrol","battery_off","bracelet_close","bracelet_open","case_closed","case_opened","crash_alarm","detach","g_sensor","input_change","light_sensor_bright","light_sensor_dark","lock_closed","lock_opened","lowpower","offline","parking","poweroff","poweron","sos","strap_bolt_cut","strap_bolt_ins","vibration_start","vibration_end","proximity_violation_start","proximity_violation_end","force_location_request","info"]}
}
```

### Geofence entry/exit events

A report on ins ad outs of a certain geofence.

#### parameters

default **plugin_id**: 89.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |
| min_minutes_in_zone | Minimum minutes in a zone to start determining visit. If the device was in a zone less than a specified time - the visit not count. | int |


### SMS-locations report

A report on location requests over SMS channel.

#### parameters

default **plugin_id**: 20.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| hide_empty_tabs | If `true`, empty tabs will be hidden. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

### Eco-driving report

A report on safety driving.

#### parameters

default **plugin_id**: 46.

Plugin-specific parameters:

| name | description | type |
| ------ | ------------- | ------ |
| harsh_driving_penalties | A list of penalties for harsh driving. | array of objects |
| speeding_penalties | A list of penalties for speeding. | array of objects |
| speed_limit | Max permitted speed value.  | int |
| idling_penalty | Penalty for idling. | int |
| min_idling_duration | A minimum time in minutes to determine idling. | int |
| min_speeding_duration | A minimum time in minutes when speed is more than `speed_limit` to determine violation. | int |
| use_vehicle_speed_limit | If `true`vehicle speed limit used instead of `speed_limit` parameter. | boolean |
| show_seconds | If `true` timestamps will be with seconds. | boolean |

* `harsh_driving_penalties` is:

```json
{
  "harsh_driving_penalties":  {
    "harshAcceleration":5,
    "harshBraking":5,
    "harshTurn":5,
    "harshAccelerationNTurn":12,
    "harshBrakingNTurn":12,
    "harshQuickLaneChange":12
  }
}
```

* `speeding_penalties` is:

```json
{
  "speeding_penalties": {
    "10":2,
    "20":10,
    "30":25,
    "50":75}
}
```

"10", "20", "30", "50" - the number of penalty points assigned for speeding by 10, 20, 30, and 50 km/h.

### Stay in zones report

Custom report for AO NIPIGAZ

#### parameters

default **plugin_id**: 84

plugin-specific parameters:

| name | description | type
|------|-------------|------
| show_seconds | If true, time values in report should have format with seconds. Default is **false**. | boolean
| show_tags | If true, tags fields will be added to the report. Default is **false**. | boolean
| min_minutes_in_zone | Minimum time in zone (geofence). Default is **5**. | int, min value 1
| zone_ids | IDs of user zones, required, min size 1, max size 30 | list of ints |


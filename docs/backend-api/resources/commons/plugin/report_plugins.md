---
title: Report plugins
description: Contains report plugins with plugin-specific parameters.
---

# Report plugins

Contains report plugins with plugin-specific parameters.


### Trips report

A report on detailed trip history.

#### Parameters

Default **plugin_id**: 4.

Plugin-specific parameters:

| name                       | description                                                                                                                                                          | type    |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| hide_empty_tabs            | If `true`, empty tabs will be hidden.                                                                                                                                | boolean |
| show_seconds               | If `true`, timestamps will be with seconds.                                                                                                                          | boolean |
| include_summary_sheet_only | If `true`, report will contain only a summary sheet for all chosen devices.                                                                                          | boolean |
| include_summary_sheet      | If `true`, report will contain a summary sheet. Default is `true`.                                                                                                   | boolean |
| split                      | Trips will be split by stops if `true`.                                                                                                                              | boolean |
| show_idle_duration         | Will show idle duration in report if `true`.                                                                                                                         | boolean |
| show_coordinates           | Every address will contain longitude and latitude if `true`.                                                                                                         | boolean |
| filter                     | If `true`,short trips will hide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| group_by_driver            | Group trips by driver assigned to the device if `true`.                                                                                                              | boolean | 

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 4,
  "show_seconds": false,
  "include_summary_sheet_only": false,
  "include_summary_sheet": true,
  "split": true,
  "show_idle_duration": false,
  "show_coordinates": false,
  "filter": true,
  "group_by_driver": false
}
```


### Stops report

A report on detailed stops history.

#### Parameters

Default **plugin_id**: 6.

Plugin-specific parameters:

| name             | description                                                                                                                                                                       | type    |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| hide_empty_tabs  | If `true`, empty tabs will be hidden.                                                                                                                                             | boolean |
| show_seconds     | If `true`, timestamps will be with seconds.                                                                                                                                       | boolean |
| show_coordinates | Every address will contain longitude and latitude if `true`.                                                                                                                      | boolean |
| filter           | If `true`, short trips will be part of stops (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 6,
  "show_seconds": false,
  "show_coordinates": false,
  "filter": false
}
```


### Trips and stops by shifts report

A report on trips and stops by shifts.

#### Parameters

Default **plugin_id**: 77.

Plugin-specific parameters:

| name              | description                                                                                                                                                                  | type             |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| hide_empty_tabs   | If `true`, empty tabs will be hidden.                                                                                                                                        | boolean          |
| show_seconds      | If `true`,timestamps will be with seconds.                                                                                                                                   | boolean          |
| shifts            | List of shifts with names, start and end time. e.g. `[{"name":"Shift1", "start_time":"00:00", "end_time":"23:59"}]`                                                          | array of objects |
| filter            | If `true`,short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean          |
| show_coordinates  | Every address will contain longitude and latitude if `true`.                                                                                                                 | boolean          |
| split_at_midnight | Split shifts at midnight if `true`.                                                                                                                                          | boolean          |

* `shifts` is:

```json
{
  "shifts": [{
      "name": "Shift1",
      "start_time": "00:00",
      "end_time": "23:59"
    }]
}
```

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 77,
  "show_seconds": false,
  "shifts": [{
      "name": "Shift1",
      "start_time": "00:00",
      "end_time": "12:00"
    }, {
      "name": "Shift2",
      "start_time": "12:00",
      "end_time": "23:59"
  }],
  "filter": true,
  "show_coordinates": false,
  "split_at_midnight": true
}
```


### Geofence visits report

A report on date, time, and mileage in geofence.

#### Parameters

Default **plugin_id**: 8.

Plugin-specific parameters:

| name                       | description                                                                                                                         | type      |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-----------|
| hide_empty_tabs            | If `true`, empty tabs will be hidden.                                                                                               | boolean   |
| show_seconds               | If `true`, timestamps will be with seconds.                                                                                         | boolean   |
| show_mileage               | Adds mileage to the report if `true`.                                                                                               | boolean   |
| show_not_visited_zones     | Will show non visited zones if `true`.                                                                                              | boolean   |
| min_minutes_in_zone        | Minimum minutes in a zone to start determining visit. If the device was in a zone less than a specified time - the visit not count. | int       |
| zone_ids                   | List of zone IDs.                                                                                                                   | int array |
| hide_charts                | If `true`, charts will be hidden.                                                                                                   | boolean   |
| include_summary_sheet_only | If `true`, report will contain only a summary sheet.                                                                                | boolean   |
| include_summary_sheet      | If `true`, report will contain a summary sheet. Default is `true`.                                                                  | boolean   |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 8,
  "show_seconds": false,
  "include_summary_sheet_only": false,
  "include_summary_sheet": false,
  "show_mileage": false,
  "show_not_visited_zones": false,
  "min_minutes_in_zone": 5,
  "hide_charts": false,
  "zone_ids": [2143181, 2143182]
}
```


### POI visits report

A report on date, time, and the number of POIs visits.

#### Parameters

Default **plugin_id**: 85.

Plugin-specific parameters:

| name                       | description                                                                                                                           | type      |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------|
| hide_empty_tabs            | If `true`, empty tabs will be hidden.                                                                                                 | boolean   |
| show_seconds               | If `true`, timestamps will be with seconds.                                                                                           | boolean   |
| show_mileage               | Adds mileage to the report if `true`.                                                                                                 | boolean   |
| show_not_visited_places    | Will show non visited POIs if `true`.                                                                                                 | boolean   |
| min_minutes_in_place       | Minimum minutes in a place to start determining visit. If the device was in a place less than a specified time - the visit not count. | int       |
| place_ids                  | List of place IDs.                                                                                                                    | int array |
| hide_charts                | If `true`, charts will be hidden.                                                                                                     | boolean   |
| include_summary_sheet_only | If `true`, report will have only a summary sheet.                                                                                     | boolean   |
| include_summary_sheet      | If `true`, report will contain a summary sheet. Default is `true`.                                                                    | boolean   |
| fetch_places_by_employees  | If `true`, places will show assigned employee. Place should be assigned to an employee to show his name.                              | boolean   |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 85,
  "show_seconds": false,
  "include_summary_sheet_only": false,
  "show_mileage": false,
  "show_not_visited_places": false,
  "min_minutes_in_place": 5,
  "hide_charts": false,
  "fetch_places_by_employees": false,
  "place_ids": [1612957, 1886863, 1886864]
}
```


### Car security report

A report on alarms, towing alerts, AutoControl events, and crashes.

#### Parameters

Default **plugin_id**: 15.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 15,
  "show_seconds": false
}
```


### Emergency button (SOS) report

A report on SOS button events log

#### Parameters

Default **plugin_id**: 16.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 16,
  "show_seconds": false
}
```


### Fall detection report

A report on fall detection sensor log.

#### Parameters

Default **plugin_id**: 17.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 17,
  "show_seconds": false
}
```


### Tracker detach report

A report on demounting devices from tracking objects.

#### Parameters

Default **plugin_id**: 18.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 18,
  "show_seconds": false
}
```


### Overall security report

A report on all events related to security and safety.

#### Parameters

default **plugin_id**: 19.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |
| group_by_type   | If `true`,events will group by type.       | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 19,
  "show_seconds": false,
  "group_by_type": false
}
```


### Engine hours report

A report on time spent in motion and on idling.

#### Parameters

default **plugin_id**: 7.

Plugin-specific parameters:

| name                       | description                                                                                                                                                                   | type    |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| hide_empty_tabs            | If `true`, empty tabs will be hidden.                                                                                                                                         | boolean |
| show_seconds               | If `true`, timestamps will be with seconds.                                                                                                                                   | boolean |
| show_detailed              | If `true`, report will contain detailed engine hours tab.                                                                                                                     | boolean |
| include_summary_sheet_only | If `true`, report will contain only a summary sheet for all chosen devices.                                                                                                   | boolean |
| include_summary_sheet      | If `true`, report will contain a summary sheet. Default is `true`.                                                                                                            | boolean |
| filter                     | If `true`, short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 7,
  "show_seconds": false,
  "show_detailed": false,
  "include_summary_sheet_only": false,
  "filter": true
}
```


### Fuel volume report

A report on fuel refills, drains, consumption (based on fuel level sensor).

#### Parameters

default **plugin_id**: 10.

Plugin-specific parameters:

| name                              | description                                                                                                                                                                   | type                                           |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| show_seconds                      | If `true`, timestamps will be with seconds.                                                                                                                                   | boolean                                        |
| graph_type                        | The type of X-axis. Can be "time" or "mileage".                                                                                                                               | [enum](../../../getting-started/introduction.md#data-types) |
| detailed_by_dates                 | If `true`, show final data on fuel traffic for each day in the period.                                                                                                        | boolean                                        |
| include_summary_sheet_only        | If `true`, report will contain only a summary sheet for all chosen devices.                                                                                                   | boolean                                        |
| include_summary_sheet             | If `true`, report will contain a summary sheet. Default is `true`.                                                                                                            | boolean                                        |
| use_ignition_data_for_consumption | Calculate consumption only when the ignition was on if `true`.                                                                                                                | boolean                                        |
| include_mileage_plot              | Optional. Used if `graph_type = time`. Show mileage plot if `true`.                                                                                                           | boolean                                        |
| filter                            | If `true`, short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean                                        |
| include_speed_plot                | If `true`, show speed plot.                                                                                                                                                   | boolean                                        |
| smoothing                         | Smooth graph if `true`. Smoothing reduces the accuracy of calculating refills or drains.                                                                                      | boolean                                        |
| surge_filter                      | If `true`, enables surge filter.                                                                                                                                              | boolean                                        |
| surge_filter_threshold            | Defines a level of surge filter. Can be 0.01 - 0.99.                                                                                                                          | float                                          |
| speed_filter                      | If `true`, enables speed filter.                                                                                                                                              | boolean                                        |
| speed_filter_threshold            | Defines a speed filter threshold.                                                                                                                                             | int                                            |

#### plugin example

```json
{
  "show_seconds": false,
  "plugin_id": 10,
  "graph_type": "mileage",
  "detailed_by_dates": true,
  "include_summary_sheet_only": false,
  "use_ignition_data_for_consumption": false,
  "include_mileage_plot": false,
  "filter": true,
  "include_speed_plot": false,
  "smoothing": false,
  "surge_filter": true,
  "surge_filter_threshold": 0.2,
  "speed_filter": false,
  "speed_filter_threshold": 10
}
```


### Flow meter report

A report on fuel consumption counted by flow meter sensors.

#### Parameters

default **plugin_id**: 78.

Plugin-specific parameters:

| name                       | description                                                                                                                                                                   | type    |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| detailed_by_dates          | If `true`, a table with statistics for every single day in selected date range will be added to the report.                                                                   | boolean |
| filter                     | If `true`, short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |
| include_summary_sheet_only | If `true`, report will contain only a summary sheet for all chosen devices.                                                                                                   | boolean |
| include_summary_sheet      | If `true`, report will contain a summary sheet. Default is `true`.                                                                                                            | boolean |

#### plugin example

```json
{
  "detailed_by_dates": true,
  "plugin_id": 78,
  "include_summary_sheet_only": false,
  "filter": true
}
```


### Vehicle sensors report

A report on CAN-bus and OBD2-port data.

#### Parameters

default **plugin_id**: 22.

Plugin-specific parameters:

| name                     | description                                                          | type                                           |
|--------------------------|----------------------------------------------------------------------|------------------------------------------------|
| hide_empty_tabs          | If `true`, empty tabs will be hidden.                                | boolean                                        |
| details_interval_seconds | The interval in seconds. From 30 to 21600.                           | int                                            |
| details_interval_minutes | Deprecated! The interval in minutes. Can be `[5, 30, 60, 180, 360]`. | int                                            |
| graph_type               | The type of X-axis. Can be "time" or "mileage".                      | [enum](../../../getting-started/introduction.md#data-types) |
| smoothing                | Smooth data if `true`.                                               | boolean                                        |
| sensors                  | List of objects containing tracker_id and sensor_id.                 | array of objects                               |

* `sensors` is:

```json
{
  "sensors": [{
      "tracker_id": 37714,
      "sensor_id": 57968
  }]
}
```

!!! note "Parameter `details_interval_minutes` is deprecated. Please use `details_interval_seconds`."

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 22,
  "details_interval_seconds": 60,
  "graph_type": "time",
  "smoothing": false,
  "sensors": [{
      "tracker_id": 993495,
      "sensor_id": 1378566
  }]
}
```


### Speed violation

A report on speeding instances.

#### Parameters

default **plugin_id**: 27.

Plugin-specific parameters:

| name                 | description                                                                                                                                                                  | type    |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|
| hide_empty_tabs      | If `true`, empty tabs will be hidden.                                                                                                                                        | boolean |
| show_seconds         | If `true`,timestamps will be with seconds.                                                                                                                                   | boolean |
| min_duration_minutes | A minimum time in seconds when speed is more than `max_speed` to determine violation.                                                                                        | int     |
| max_speed            | A maximum speed to determine violation.                                                                                                                                      | int     |
| group_by_driver      | Group violations by driver assigned to the device if `true`.                                                                                                                 | boolean |
| filter               | If `true`,short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 27,
  "show_seconds": false,
  "min_duration_minutes": 5,
  "max_speed": 60,
  "group_by_driver": false,
  "filter": true
}
```


### Device switching ON/OFF report

A report on switching device using hardware switch.

#### Parameters

default **plugin_id**: 23.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 23,
  "show_seconds": false
}
```


### GSM connection lost

A report on long disruptions of server connection

#### Parameters

default **plugin_id**: 13.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 13,
  "show_seconds": false
}
```


### Measuring sensors report

A report on detailed sensor reading history.

#### Parameters

default **plugin_id**: 9.

Plugin-specific parameters:

| name                     | description                                                                                                                                                                  | type                                           |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| hide_empty_tabs          | If `true`, empty tabs will be hidden.                                                                                                                                        | boolean                                        |
| details_interval_seconds | The interval in seconds. From 30 to 21600.                                                                                                                                   | int                                            |
| details_interval_minutes | Deprecated! The interval in minutes. Can be `[5, 30, 60, 180, 360]`.                                                                                                         | int                                            |
| graph_type               | The type of X-axis. Can be "time" or "mileage".                                                                                                                              | [enum](../../../getting-started/introduction.md#data-types) |
| smoothing                | Smooth data if `true`.                                                                                                                                                       | boolean                                        |
| show_address             | Address of each reading appears in report if `true`.                                                                                                                         | boolean                                        |
| filter                   | If `true`,short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean                                        |
| sensors                  | List of objects containing tracker_id and sensor_id.                                                                                                                         | array of objects                               |

* `sensors` is:

```json
{
  "sensors": [{
      "tracker_id": 37714,
      "sensor_id": 57968
  }]
}
```

!!! note "Param `details_interval_minutes` is deprecated. Please sue `details_interval_seconds`."

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 9,
  "details_interval_seconds": 60,
  "graph_type": "time",
  "smoothing": false,
  "show_address": false,
  "filter": true,
  "sensors": [{
      "tracker_id": 993495,
      "sensor_id": 1378566
  }]
}
```


### Equipment working time

A report on activity and idle time of the equipment.

#### Parameters

default **plugin_id**: 12.

| name                        | description                                                                                                                                                                  | type             |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| hide_empty_tabs             | If `true`, empty tabs will be hidden.                                                                                                                                        | boolean          |
| show_seconds                | If `true`,timestamps will be with seconds.                                                                                                                                   | boolean          |
| min_working_period_duration | A minimum time in seconds the equipment works to determine activity. Min = 1.                                                                                                | int              |
| show_idle_percent           | If `true`,show percentage of idling.                                                                                                                                         | boolean          |
| filter                      | If `true`,short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean          |
| sensors                     | List of objects containing tracker_id and sensor_id.                                                                                                                         | array of objects |

* `sensors` is:

```json
{
  "sensors": [{
      "tracker_id": 37714,
      "sensor_id": 57968
  }]
}
```

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 12,
  "show_seconds": false,
  "min_working_period_duration": 60,
  "show_idle_percent": false,
  "filter": false,
  "sensors": [{
      "tracker_id": 993495,
      "sensor_id": 1378562
  }]
}
```


### Tasks report

A report on tasks statuses.

#### Parameters

default **plugin_id**: 42.

| name                  | description                                 | type    |
|-----------------------|---------------------------------------------|---------|
| hide_empty_tabs       | If `true`, empty tabs will be hidden.       | boolean |
| show_seconds          | If `true`,timestamps will be with seconds.  | boolean |
| show_external_id      | Show external ID of task, if `true`.        | boolean |
| show_description      | Show description of task, if `true`.        | boolean |
| show_forms            | Show forms when the task has it, if `true`. | boolean |  
| show_places_and_zones | Show places and geofences, if `true`.       | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 42,
  "show_seconds": false,
  "show_external_id": false,
  "show_description": false,
  "show_forms": true,
  "show_places_and_zones": false
}
```


### Form completion statistics report

A report on form fields completion rate.

#### Parameters

default **plugin_id**: 70.

| name             | description                                             | type    |
|------------------|---------------------------------------------------------|---------|
| hide_empty_tabs  | If `true`, empty tabs will be hidden.                   | boolean |
| show_nonselected | If `true`, not selected options in forms will be shown. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 70,
  "show_nonselected": true
}
```


### Work statuses report

A report on status changes history.

#### Parameters

default **plugin_id**: 47.

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 47,
  "show_seconds": false
}
```


### Check-in report

A report on markers for Check-in function. Available only for X-GPS Trackers.

#### Parameters

default **plugin_id**: 80

Plugin-specific parameters:

| name                  | description                                                   | type    |
|-----------------------|---------------------------------------------------------------|---------|
| show_coordinates      | If `true`, coordinates will be added to the report.           | boolean |
| hide_empty_tabs       | If `true`, empty tabs will be hidden.                         | boolean |
| show_coordinates      | Every address will contain longitude and latitude, if `true`. | boolean |
| show_places_and_zones | Show places and geofences, if `true`.                         |         |
| show_forms            | Show forms when the task has it, if `true`.                   | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 80,
  "show_coordinates": false,
  "show_places_and_zones": false,
  "show_forms": true
}
```


### Driver shift change report

A report on driver identification.

#### Parameters

default **plugin_id**: 66.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 66,
  "show_seconds": false
}
```


### Trips by state

A report on trips breakdown by jurisdictions.

#### Parameters

default **plugin_id**: 73.

Plugin-specific parameters:

| name                       | description                                                                                                                                                                   | type                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------|
| hide_empty_tabs            | If `true`, empty tabs will be hidden.                                                                                                                                         | boolean                                        |
| show_seconds               | If `true`, timestamps will be with seconds.                                                                                                                                   | boolean                                        |
| filter                     | If `true`, short trips will not coincide (shorter than 300m/have less than 4 points total and if the device circles around one point (e.g., star pattern from GPS drifting)). | boolean                                        |
| include_summary_sheet_only | If `true`, report will contain only a summary sheet for all chosen devices.                                                                                                   | boolean                                        |
| include_summary_sheet      | If `true`, the report will contain a summary sheet. Default is `true`.                                                                                                        | boolean                                        |
| group_type                 | A group type. Can be "province" or "country".                                                                                                                                 | [enum](../../../getting-started/introduction.md#data-types) |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 73,
  "show_seconds": false,
  "filter": false,
  "include_summary_sheet_only": false,
  "group_type": "province"
}
```


### Report on all events

An overall report about any kind of events.

#### Parameters

default **plugin_id**: 11.

Plugin-specific parameters:

| name            | description                                    | type         |
|-----------------|------------------------------------------------|--------------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.          | boolean      |
| show_seconds    | If `true`,timestamps will be with seconds.     | boolean      |
| group_by_type   | Groups events by type if `true`.               | boolean      |
| event_types     | A list of event types that will be considered. | string array |

* the object with all `event_types` is:

```json
{
  "event_types": [
    "auto_geofence_in",
    "auto_geofence_out",
    "door_alarm",
    "forward_collision_warning",
    "gps_lost",
    "gps_recover",
    "gsm_damp",
    "harsh_driving",
    "headway_warning",
    "hood_alarm",
    "idle_end",
    "idle_start",
    "ignition",
    "inroute",
    "outroute",
    "lane_departure",
    "obd_plug_in",
    "obd_unplug",
    "peds_collision_warning",
    "peds_in_danger_zone",
    "odometer_set",
    "online",
    "output_change",
    "security_control",
    "tracker_rename",
    "track_end",
    "track_start",
    "tsr_warning",
    "sensor_inrange",
    "sensor_outrange",
    "work_status_change",
    "call_button_pressed",
    "driver_changed",
    "driver_identified",
    "driver_not_identified",
    "fueling",
    "drain",
    "checkin_creation",
    "tacho",
    "antenna_disconnect",
    "check_engine_light",
    "location_response",
    "backup_battery_low",
    "fatigue_driving",
    "inzone",
    "outzone",
    "speedup",
    "alarmcontrol",
    "battery_off",
    "bracelet_close",
    "bracelet_open",
    "case_closed",
    "case_opened",
    "crash_alarm",
    "detach",
    "g_sensor",
    "input_change",
    "light_sensor_bright",
    "light_sensor_dark",
    "lock_closed",
    "lock_opened",
    "lowpower",
    "offline",
    "parking",
    "poweroff",
    "poweron",
    "sos",
    "strap_bolt_cut",
    "strap_bolt_ins",
    "vibration_start",
    "vibration_end",
    "proximity_violation_start",
    "proximity_violation_end",
    "force_location_request",
    "info"
  ]
}

```

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 11,
  "show_seconds": false,
  "group_by_type": false,
  "event_types": [
    "force_location_request",
    "info",
    "inzone",
    "outzone",
    "speedup"
  ]
}
```


### Geofence entry/exit events

A report on ins ad outs of a certain geofence.

#### Parameters

default **plugin_id**: 89.

Plugin-specific parameters:

| name                | description                                                                                                                         | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------|---------|
| hide_empty_tabs     | If `true`, empty tabs will be hidden.                                                                                               | boolean |
| show_seconds        | If `true`,timestamps will be with seconds.                                                                                          | boolean |
| min_minutes_in_zone | Minimum minutes in a zone to start determining visit. If the device was in a zone less than a specified time - the visit not count. | int     |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 89,
  "show_seconds": false,
  "min_minutes_in_zone": 5
}
```


### SMS-locations report

A report on location requests over SMS channel.

#### Parameters

default **plugin_id**: 20.

Plugin-specific parameters:

| name            | description                                | type    |
|-----------------|--------------------------------------------|---------|
| hide_empty_tabs | If `true`, empty tabs will be hidden.      | boolean |
| show_seconds    | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "hide_empty_tabs": true,
  "plugin_id": 20,
  "show_seconds": false
}
```

### Point report

Information on the points transmitted during the day. Maximum period is 24 hours.

#### Parameters

default **plugin_id**: 91.

Plugin-specific parameters:

| name         | description                                | type    |
|--------------|--------------------------------------------|---------|
| show_seconds | If `true`,timestamps will be with seconds. | boolean |

#### plugin example

```json
{
  "show_seconds": true,
  "plugin_id": 91
}
```


### Eco-driving report by trackers

A report on safety driving by trackers. For [report/generate](../report/report_tracker.md#generate) request use trackers
parameter.

#### Parameters

default **plugin_id**: 46.

Plugin-specific parameters:

| name                    | description                                                                             | type             |
|-------------------------|-----------------------------------------------------------------------------------------|------------------|
| harsh_driving_penalties | A list of penalties for harsh driving.                                                  | array of objects |
| speeding_penalties      | A list of penalties for speeding.                                                       | array of objects |
| speed_limit             | Max permitted speed value.                                                              | int              |
| idling_penalty          | Penalty for idling.                                                                     | int              |
| min_idling_duration     | A minimum time in minutes to determine idling.                                          | int              |
| min_speeding_duration   | A minimum time in minutes when speed is more than `speed_limit` to determine violation. | int              |
| use_vehicle_speed_limit | If `true`vehicle speed limit used instead of `speed_limit` parameter.                   | boolean          |
| show_seconds            | If `true`,timestamps will be with seconds.                                              | boolean          |

* `harsh_driving_penalties` is:

```json
{
  "harsh_driving_penalties": {
    "harshAcceleration": 5,
    "harshBraking": 5,
    "harshTurn": 5,
    "harshAccelerationNTurn": 12,
    "harshBrakingNTurn": 12,
    "harshQuickLaneChange": 12
  }
}
```

* `speeding_penalties` is:

```json
{
  "speeding_penalties": {
    "10": 2,
    "20": 10,
    "30": 25,
    "50": 75
  }
}
```

"10", "20", "30", "50" - the number of penalty points assigned for speeding by 10, 20, 30, and 50 km/h.

#### plugin example

```json
{
  "speeding_penalties": {
    "10": 2,
    "20": 10,
    "30": 25,
    "50": 75
  },
  "harsh_driving_penalties": {
    "harshAcceleration": 5,
    "harshBraking": 5,
    "harshTurn": 5,
    "harshBrakingNTurn": 12,
    "harshAccelerationNTurn": 12,
    "harshQuickLaneChange": 12
  },
  "speed_limit": 260,
  "idling_penalty": 5,
  "min_speeding_duration": 1,
  "min_idling_duration": 5,
  "use_vehicle_speed_limit": true,
  "plugin_id": 46,
  "show_seconds": false
}
```


### Eco-driving report by drivers

A report on safety driving by drivers. For [report/generate](../report/report_tracker.md#generate) request use employees
parameter.

#### Parameters

default **plugin_id**: 82.

Plugin-specific parameters:

| name                    | description                                                                             | type             |
|-------------------------|-----------------------------------------------------------------------------------------|------------------|
| harsh_driving_penalties | A list of penalties for harsh driving.                                                  | array of objects |
| speeding_penalties      | A list of penalties for speeding.                                                       | array of objects |
| speed_limit             | Max permitted speed value.                                                              | int              |
| idling_penalty          | Penalty for idling.                                                                     | int              |
| min_idling_duration     | A minimum time in minutes to determine idling.                                          | int              |
| min_speeding_duration   | A minimum time in minutes when speed is more than `speed_limit` to determine violation. | int              |
| use_vehicle_speed_limit | If `true`vehicle speed limit used instead of `speed_limit` parameter.                   | boolean          |
| show_seconds            | If `true`,timestamps will be with seconds.                                              | boolean          |

#### plugin example

```json
{
  "speeding_penalties": {
    "10": 2,
    "20": 10,
    "30": 25,
    "50": 75
  },
  "harsh_driving_penalties": {
    "harshAcceleration": 5,
    "harshBraking": 5,
    "harshTurn": 5,
    "harshBrakingNTurn": 12,
    "harshAccelerationNTurn": 12,
    "harshQuickLaneChange": 12
  },
  "speed_limit": 260,
  "idling_penalty": 5,
  "min_speeding_duration": 1,
  "min_idling_duration": 5,
  "use_vehicle_speed_limit": true,
  "plugin_id": 82,
  "show_seconds": false
}
```

### Stay in zones report

#### Parameters

default **plugin_id**: 84

plugin-specific parameters:

| name                | description                                                                           | type             |
|---------------------|---------------------------------------------------------------------------------------|------------------|
| show_seconds        | If `true`, time values in report should have format with seconds. Default is `false`. | boolean          |
| show_tags           | If `true`, tags fields will be added to the report. Default is `false`.               | boolean          |
| min_minutes_in_zone | Minimum time in zone (geofence). Default is `5`.                                      | int, min value 1 |
| zone_ids            | IDs of user zones, required, min size 1, max size 30                                  | int array        |

#### plugin example

```json
{
  "show_seconds": true,
  "show_tags": true,
  "min_minutes_in_zone": 1,
  "zone_ids": [2143181, 2143182],
  "plugin_id": 84
}
```


### Stay in places report

#### Parameters

default **plugin_id**: 85

plugin-specific parameters:

| name                      | description                                                                                                                                        | type      |
|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| fetch_places_by_employees | If `true`, report will be built for places that are related to selected trackers via custom fields. Cannot be used in conjunction with `place_ids` | boolean   |
| hide_charts               | If `true`, charts will be hidden.                                                                                                                  | boolean   |
| min_minutes_in_place      | Minimum time in spent in place. Minimum value is 1, default is `5`                                                                                 | int       |
| place_ids                 | IDs of user's POI. Min size 1, max size 30                                                                                                         | int array |
| show_mileage              | Adds mileage to the report if `true`.                                                                                                              | boolean   |
| show_not_visited_places   | Will show non visited POIs if `true`.                                                                                                              | boolean   |
| show_seconds              | If `true`, time values in report should have format with seconds. Default is `false`.                                                              | boolean   |

#### plugin example

```json
{
  "show_seconds": true,
  "min_minutes_in_place": 1,
  "fetch_places_by_employees": false,
  "hide_charts": true,
  "place_ids": [278645, 278646],
  "show_mileage": true,
  "show_not_visited_places": true,
  "plugin_id": 85
}
```



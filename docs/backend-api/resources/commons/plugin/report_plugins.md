---
title: Report plugins
description: Report plugins
---

# Report plugins

## Check-in report

A report on markers for Check-in function.

#### parameters
default **plugin_id**: 80

Plugin-specific parameters:

| name | description | type
|------|-------------|------
| show_coordinates | If true, coordinates will be added to the report. | boolean



## Flow meter report

A report on fuel consumption counted by flow meter sensors.

#### parameters
default **plugin_id**: 78

Plugin-specific parameters:

| name | description | type
|------|-------------|------
| detailed_by_dates | If true, a table with statistics for every single day in selected date range will be added to the report. | boolean
| filter | If true, smart filter will be applied to the report. | boolean



## Stay in zones report

Custom report for AO NIPIGAZ

#### parameters
default **plugin_id**: 84

plugin-specific parameters:

| name | description | type
|------|-------------|------
| show_seconds | If true, time values in report should have format with seconds. Default is **false** | boolean
| show_tags | If true, tags fields will be added to the report. Default is **false** | boolean
| min_minutes_in_zone | Minimum time in zone (geofence). Default is **5** | int, min value 1
| zone_ids | IDs of user zones | list of ints, required, min size 1, max size 30

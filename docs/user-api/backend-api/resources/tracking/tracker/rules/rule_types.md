---
title: Rule types
description: Rule types with all parameters to create. The rule availability depends on the device and rule integration for it.
---

# Rule types

Rule types with all parameters to create. The rule availability depends on the device, connected and configured equipment 
and rule integration for it.


### Geofence entrance or exit

A rule that triggers on device entering/exiting created on platform [geofences](../../zone/index.md#list).

#### Parameters

| name           | description                                                                    | type                                              |
|----------------|--------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `inoutzone` for this rule type.                                                | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification on entering geofence. It is for `inzone` event type. | string                                            |
| secondary_text | Text of rule notification on exiting geofence. It is for `outzone` event type. | string                                            |

#### extended parameters

| name              | description                                                                                     | type    |
|-------------------|-------------------------------------------------------------------------------------------------|---------|
| emergency         | If `true` enables emergency notification.                                                       | boolean |
| private_rule      | Affects only sub users. If `true` then the rule and notifications are visible only to sub user. | boolean |
| append_zone_title | Show or not the zone labels in a notification text.                                             | boolean |


### Parking state detection

A rule that triggers on detection of parking state calculated based on [parking detection settings](../settings/trip_detection.md).

#### Parameters

| name           | description                                                                   | type                                              |
|----------------|-------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `track_change` for this rule type.                                            | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification on parking start. It is for `track_end` event type. | string                                            |
| secondary_text | Text of rule notification on parking end. It is for `track_start` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |


### Speeding (hardware related)

A rule that triggers on speed exceeding determined by hardware. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                   | type                                              |
|--------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `over_speed_reported` for this rule type.                                                     | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when speeding detected. It is for `over_speed_reported` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Speeding (platform related)

A rule that triggers on speed exceeding determined by the platform. Based on received speed from device.

#### Parameters

| name         | description                                                               | type                                              |
|--------------|---------------------------------------------------------------------------|---------------------------------------------------|
| type         | `speedup` for this rule type.                                             | [enum](../../../../getting-started/introduction.md#data-types) |
| param        | Speed limit. It is for `speedup` event type.                              | int                                               |
| primary_text | Text of rule notification when speed exceeds the specified `param` value. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Deviation from the route

A rule that triggers on deviations from the route. Only the [route (sausage) type](../../zone/index.md#sausage) geofence may be assigned. 

#### Parameters

| name         | description                                                                                 | type                                              |
|--------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `route` for this rule type.                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device outs the route zone. It is for `outroute` event type. | string                                            |

#### extended parameters

| name                    | description                                                                                     | type    |
|-------------------------|-------------------------------------------------------------------------------------------------|---------|
| allow_exit_at_endpoints | If `true` disables notifications on deviations from the start and end points of a route.        | boolean |
| emergency               | If `true` enables emergency notification.                                                       | boolean |
| private_rule            | Affects only sub users. If `true` then the rule and notifications are visible only to sub user. | boolean |
| append_zone_title       | Show or not the zone labels in a notification text.                                             | boolean |


### Driving time

A rule that triggers when your employee drives more than allowed. The driving time is calculated based on [parking detection settings](../settings/trip_detection.md).

#### Parameters

| name           | description                                                                                            | type                                              |
|----------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `excessive_driving` for this rule type.                                                                | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when driving time exceeded. It is for `excessive_driving_start` event type.  | string                                            |
| secondary_text | Text of rule notification on driving time exceeding end. It is for `excessive_driving_end` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| max_driving_time    | Allowed driving time. How much time your employee can drive a car                                                             | int     |
| min_parking_time    | Minimum parking time to reset the timer. How much time your employee must wait until he can continue driving                  | int     |
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Parking time

A rule that triggers when your employee standstill more than allowed. The parking time is calculated based on [parking detection settings](../settings/trip_detection.md).

#### Parameters

| name           | description                                                                                                   | type                                              |
|----------------|---------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `excessive_parking` for this rule type.                                                                       | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when parking time exceeded. It is for `excessive_parking` event type.               | string                                            |
| secondary_text | Text of rule notification on parking time exceeding end. It is for `excessive_parking_finished` event type.   | string                                            |

#### extended parameters

| name                 | description                                                                                                                   | type    |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| max_parking_duration | Allowed parking time. How much time a car can standstill                                                                      | int     |
| emergency            | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule         | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted  | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title    | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Task performance

A rule that triggers when assigned to a tracker [task](../../../field_service/task/index.md) changes its status. 

#### Parameters

| name         | description                                                                                                 | type                                              |
|--------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `task_status_change` for this rule type.                                                                    | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when task changes its status to a chosen one or form is submitted or resubmitted. | string                                            |

#### extended parameters

| name                        | description                                                                                                                   | type         |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------|
| statuses                    | List of tracked statuses. Possible statuses are "arrived", "done","delayed", "failed".                                        | string array |
| on_form_submission          | If `true` form submission will track.                                                                                         | boolean      |
| on_repeated_form_submission | If `true` form resubmission will track.                                                                                       | boolean      |
| emergency                   | If `true` enables emergency notification.                                                                                     | boolean      |
| private_rule                | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean      |
| zone_limit_inverted         | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean      |
| append_zone_title           | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean      |


### Work status change

A rule that triggers when tracker [work status](../../status/tracker.md) changes. Choose specific status IDs from a currently 
assigned to tracker [status listing](../../status/listing/index.md).

#### Parameters

| name         | description                                                                                                     | type                                              |
|--------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `work_status_change` for this rule type.                                                                        | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when work status changes to a chosen one. It is for `work_status_change` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                                  | type      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| status_ids          | List of tracked status IDs. Choose specific status IDs from a currently assigned to tracker [status listing](../../status/listing/index.md). | int array |
| emergency           | If `true` enables emergency notification.                                                                                                    | boolean   |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                                              | boolean   |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                                       | boolean   |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`.                | boolean   |


### Excessive idling (hardware related)

A rule that triggers on excessive idling registered by hardware. Based on the configs on the device side.

#### Parameters

| name           | description                                                               | type                                              |
|----------------|---------------------------------------------------------------------------|---------------------------------------------------|
| type           | `idling` for this rule type.                                              | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when excessive idling detected by device.       | string                                            |
| secondary_text | Text of rule notification when excessive idling end detected by a device. | string                                            |

#### extended parameters

| name                | description                                                                                                                                  | type      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| emergency           | If `true` enables emergency notification.                                                                                                    | boolean   |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                                              | boolean   |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                                       | boolean   |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`.                | boolean   |


### Excessive idling (platform related)

A rule that triggers on excessive idling registered by the platform. The idling time is calculated based on [parking detection settings](../settings/trip_detection.md) and ignition state.

#### Parameters

| name           | description                                                                                                | type                                              |
|----------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `idling_soft` for this rule type.                                                                          | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when excessive idling detected by platform. It is for `idle_start` event type.   | string                                            |
| secondary_text | Text of rule notification when excessive idling end detected by platform. It is for `idle_end` event type. | string                                            |
| param          | Idle duration to send notification.                                                                        | int                                               | 

#### extended parameters

| name                | description                                                                                                                                  | type      |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| emergency           | If `true` enables emergency notification.                                                                                                    | boolean   |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                                              | boolean   |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                                       | boolean   |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`.                | boolean   |


### Fuel level change

Rule triggered by a drastic change in fuel level. A drastic change is when the fuel level changes faster than the 
accuracy of the sensor in a span of ten minutes.

#### Parameters

| name           | description                                                                                   | type                                              |
|----------------|-----------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `fuel_level_leap` for this rule type.                                                         | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification on drastically fuel level increase. It is for `fueling` event type. | string                                            |
| secondary_text | Text of rule notification on drastically fuel level decrease. It is for `drain` event type.   | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type         |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------|
| sensor_id           | ID of tracked sensor. Should be a fuel level sensor. Only specified if `tracker_params` is not specified.                     | int          |
| emergency           | If `true` enables emergency notification.                                                                                     | boolean      |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean      |
| display_value       | Show or not the fuel level in a notification text. Default is: `false`.                                                       | boolean      |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean      |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean      |
| tracker_params      | An optional object. Specifies a list of sensors to be tracked in the rule, including for different trackers.                  | JSON object  |

#### tracker_params

| name       | description                                                                                      | type    |
|------------|--------------------------------------------------------------------------------------------------|---------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.  | int     |
| sensor_id  | ID of tracked sensor. Should be a fuel level sensor.                                             | int     |

```json
{
  "tracker_params": [
    {
      "tracker_id": 10038820,
      "sensor_id": 279421
    },
    {
      "tracker_id": 10038821,
      "sensor_id": 279422
    }
  ]
}
```


### Harsh driving

A rule that triggers on harsh driving. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                         | type                                              |
|--------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `harsh_driving` for this rule type.                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device detects harsh driving. It is for `harsh_driving` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Advanced driver assistance systems (ADAS)

A rule that triggers on warnings from driver-assistance systems (ADAS). Detected by camera and based on the configs on the device side.

#### Parameters

| name         | description                                                               | type                                              |
|--------------|---------------------------------------------------------------------------|---------------------------------------------------|
| type         | `driver_assistance` for this rule type.                                   | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device detects some of chosen ADAS events. | string                                            |

#### extended parameters

| name                             | description                                                                                                                   | type    |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| lane_departure_enabled           | If `true` lane departure tracked. It is for `lane_departure` event type.                                                      | boolean |
| forward_collision_enabled        | If `true` forward collision tracked. It is for `forward_collision_warning` event type.                                        | boolean |
| headway_warning_enabled          | If `true` headway warning tracked. It is for `headway_warning` event type.                                                    | boolean |
| peds_in_danger_zone_enabled      | If `true` peds in danger zone tracked. It is for `peds_in_danger_zone` event type.                                            | boolean |
| peds_collision_warning_enabled   | If `true` peds collision warning works. It is for `peds_collision_warning` event type.                                        | boolean |
| traffic_sign_recognition_enabled | If `true` traffic sign recognition works. It is for `tsr_warning` event type.                                                 | boolean |
| emergency                        | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule                     | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted              | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title                | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Auto geofencing (unauthorized movement detected by location change)

A rule that triggers on auto geofencing. When a car's ignition is off, and it outs the automatically created radius around it.

#### Parameters

| name         | description                                                                                                                     | type                                              |
|--------------|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `auto_geofence` for this rule type.                                                                                             | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device outs automatically created geofence around it. It is for `auto_geofence_out` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Autocontrol related rules

Autocontrol related tracked rules like alarm, battery, doors and others. Based on the configs on the device side.

#### Parameters

| name         | description                                                                               | type                                              |
|--------------|-------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `autocontrol` for this rule type.                                                         | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device determines one of chosen autocontrol related rules. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type        |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|-------------|
| alarmcontrol        | Activation of car alarms. It is for `alarmcontrol` event type. Described below.                                               | JSON object |
| battery_off         | Disabling of external power supply. It is for `battery_off` event type. Described below.                                      | JSON object |
| door_alarm          | Opening doors/trunk. It is for `door_alarm` event type. Described below.                                                      | JSON object |
| hood_alarm          | Opening hood. It is for `hood_alarm` event type. Described below.                                                             | JSON object |
| ignition            | Ignition. It is for `ignition` event type. Described below.                                                                   | JSON object |
| parking             | Unauthorized movement. It is for `parking` event type. Described below.                                                       | JSON object |
| gsm_damp            | GSM-signal dumping (low signal level). It is for `gsm_damp` event type. Described below.                                      | JSON object |
| security_control    | Switching ON/OFF security mode. It is for `security_control` event type. Described below.                                     | JSON object |
| emergency           | If `true` enables emergency notification.                                                                                     | boolean     |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean     |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean     |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean     |

???+ example "Map of sub-rules settings"
```json
{
  "alarmcontrol": {
    "enabled": true,
    "sms": false,
    "call": false,
    "email": true,
    "push": true,
    "always_notify": false
  },
  "battery_off": {
    "enabled": true,
    "sms": true,
    "call": false,
    "email": true,
    "push": true
  },
  "door_alarm": {
    "enabled": true,
    "sms": false,
    "call": false,
    "email": true,
    "push": true
  },
  "hood_alarm": {
    "enabled": true,
    "sms": false,
    "call": false,
    "email": true,
    "push": true
  },
  "ignition": {
    "enabled": true,
    "sms": false,
    "call": false,
    "email": true,
    "push": true
  },
  "parking": {
    "enabled": true,
    "sms": false,
    "call": false,
    "email": true,
    "push": true
  },
  "gsm_damp": {
    "enabled": true,
    "sms": false,
    "call": false,
    "email": true,
    "push": true
  },
  "security_control": {
    "enabled": true,
    "sms": false,
    "call": false,
    "email": true,
    "push": true
  }
}
```


### Car crash

A rule that triggers when device's sensors detect car crash. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                                       | type                                              |
|--------------|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `crash_alarm` for this rule type.                                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device determines crash by its accelerometer. It is for `crash_alarm` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Cruise control switched ON/OFF

A rule that triggers when a device provides cruise control switching event. Based on the configs on the device side.

#### Parameters

| name           | description                                                                                           | type                                              |
|----------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `cruise_control` for this rule type.                                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when cruise control switch on. It is for `cruise_control_on` event type.    | string                                            |
| secondary_text | Text of rule notification when cruise control switch off. It is for `cruise_control_off` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Distance between objects

A rule that triggers a change in distance between objects. The distance is measured by the last valid GPS coordinates between chosen objects.

#### Parameters

| name           | description                                                                                     | type                                              |
|----------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `distance_control` for this rule type.                                                          | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when distance is breached. It is for `distance_breached` event type.  | string                                            |
| secondary_text | Text of rule notification when distance is restored. It is for `distance_restored` event type.  | string                                            |

#### extended parameters

| name                    | description                                                                                                                   | type                                              |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| observed_trackers       | List of observed tracker IDs.                                                                                                 | int array                                         |
| control_type            | Type of distance control. One of `["moving_away", "approaching"]`.                                                            | [enum](../../../../getting-started/introduction.md#data-types) |
| control_distance_meters | Distance for control in meters.                                                                                               | int                                               |
| emergency               | If `true` enables emergency notification.                                                                                     | boolean                                           |
| private_rule            | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean                                           |
| zone_limit_inverted     | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean                                           |
| append_zone_title       | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean                                           |


### Driver absence

A rule that triggers when driver lefts or enters cabin. Detected by camera and based on the configs on the device side.

#### Parameters

| name           | description                                                                                 | type                                              |
|----------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `driver_enter_absence` for this rule type.                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when driver lefts a cabin. It is for `driver_absence` event type. | string                                            |
| secondary_text | Text of rule notification when driver enters a cabin. It is for `driver_enter` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Driver change

A rule that triggers on driver change automatically by the key or manually in widget with driver from a [drivers list](../../../field_service/employee/index.md).

#### Parameters

| name         | description                                                                                               | type                                              |
|--------------|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `driver_change` for this rule type.                                                                       | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when a new driver assigned to a device. It is for `driver_changed` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Driver distraction

A rule that triggers when driver distracts from the road. Detected by camera and based on the configs on the device side.

#### Parameters

| name           | description                                                                                                    | type                                              |
|----------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `driver_distraction` for this rule type.                                                                       | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when driver distraction detected. It is for `driver_distraction_started` event type. | string                                            |
| secondary_text | Text of rule notification when driver distraction ends. It is for `driver_distraction_finished` event type.    | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Fall detection

A rule that triggers when g-sensor or accelerometer detects falling.

#### Parameters

| name         | description                                                                                | type                                              |
|--------------|--------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `g_sensor` for this rule type.                                                             | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when g-sensor detects falling. It is for `g_sensor` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Fatigue driving

A rule that triggers on fatigue driving. Detected by camera and based on the configs on the device side.

#### Parameters

| name           | description                                                                                            | type                                              |
|----------------|--------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `fatigue_driving` for this rule type.                                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when fatigue driving is detected. It is for `fatigue_driving` event type.    | string                                            |
| secondary_text | Text of rule notification when fatigue driving ends. It is for `fatigue_driving_finished` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Identification via RFID/iButton/Camera

A rule that triggers on a driver identification with help of RFID, iButton or Camera. Based on the configs on the device side.

#### Parameters

| name           | description                                                                                                      | type                                              |
|----------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `driver_identification` for this rule type.                                                                      | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when the driver tag has been identified. It is for `driver_identified` event type.     | string                                            |
| secondary_text | Text of rule notification when the driver tag was not identified. It is for `driver_not_identified` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### No movement

A rule that triggers when the device does not detect motion for longer than the time set in its settings. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                                                                       | type                                              |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `no_movement` for this rule type.                                                                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when a device does not detect motion for longer than the time set in its settings. It is for `no_movement` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Pressing SOS button

A rule that triggers on SOS button pressing. Based on the configs on the device side.

#### Parameters

| name         | description                                                                    | type                                              |
|--------------|--------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `sos` for this rule type.                                                      | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when SOS button pressed. It is for `sos` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Social distancing monitoring

A rule that triggers on social distancing violation. Similar to distance between objects but related based on the configs on the device side.

#### Parameters

| name           | description                                                                                                | type                                              |
|----------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `proximity_violation` for this rule type.                                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when safety distance breached. It is for `proximity_violation_start` event type. | string                                            |
| secondary_text | Text of rule notification when safety distance restored. It is for `proximity_violation_end` event type.   | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Unauthorized movement (determined by accelerometer)

A rule that triggers on unauthorized movement detected by accelerometer when ignition is off. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                                  | type                                              |
|--------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `parking` for this rule type.                                                                                | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when movement detected by device's accelerometer. It is for `parking` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Backup battery low

A rule that triggers on backup battery low. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                             | type                                              |
|--------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `backup_battery_low` for this rule type.                                                                | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when backup battery charge is low. It is for `backup_battery_low` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Bracelet sensor

A rule that triggers on bracelet sensor opening/closing. Based on the configs on the device side.

#### Parameters

| name           | description                                                                            | type                                              |
|----------------|----------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `bracelet` for this rule type.                                                         | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when bracelet opened. It is for `bracelet_open` event type.  | string                                            |
| secondary_text | Text of rule notification when bracelet closed. It is for `bracelet_close` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Call button pressed

A rule that triggers on call button pressing. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                     | type                                              |
|--------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `call_button_pressed` for this rule type.                                                       | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when call button pressed. It is for `call_button_pressed` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Car alarm triggered

A rule that triggers on car alarm. Based on the configs on the device side.

#### Parameters

| name         | description                                                                              | type                                              |
|--------------|------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `alarmcontrol` for this rule type.                                                       | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when car alarm triggers. It is for `alarmcontrol` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Case intrusion

A rule that triggers on case intrusion. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                          | type                                              |
|--------------|------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `case_intrusion` for this rule type.                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device determines case intrusion. It is for `case_opened` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Check engine (MIL)

A rule that triggers on check engine (MIL) events. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                                        | type                                              |
|--------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `check_engine_light` for this rule type.                                                                           | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when check engine (MIL) detected by a device. It is for `check_engine_light` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Connection/disconnection to the OBDII port

A rule that triggers on connection/disconnection to the OBD2 port. Based on the configs on the device side.

#### Parameters

| name           | description                                                                                             | type                                              |
|----------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `obd_plug_unplug` for this rule type.                                                                   | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when device connected to OBDII port. It is for `obd_plug_in` event type.      | string                                            |
| secondary_text | Text of rule notification when device disconnected from OBDII port. It is for `obd_unplug` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Door opening in alarm mode

A rule that triggers on door opening in alarm mode. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                 | type                                              |
|--------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `door_alarm` for this rule type.                                                            | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when door opens in alarm mode. It is for `door_alarm` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### External device connection

A rule that triggers on connection/disconnection of an external device. Based on the configs on the device side.

#### Parameters

| name           | description                                                                                                                    | type                                              |
|----------------|--------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `external_device_connection` for this rule type.                                                                               | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when external device connected to tracker. It is for `external_device_connected` event type.         | string                                            |
| secondary_text | Text of rule notification when external device disconnected from tracker. It is for `external_device_disconnected` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### External power cut

A rule that triggers when device disconnects from car's battery. Based on the configs on the device side.

#### Parameters

| name           | description                                                                                    | type                                              |
|----------------|------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `battery_off` for this rule type.                                                              | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when external power disconnects. It is for `battery_off` event type. | string                                            |
| secondary_text | Text of rule notification when external power connects. It is for `battery_on` event type.     | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### GPS antenna disconnected

A rule that triggers on GPS antenna disconnect. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                                            | type                                              |
|--------------|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `antenna_disconnect` for this rule type.                                                                               | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device determines GPS antenna disconnection. It is for `antenna_disconnect` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### GPS jamming (signal dump)

A rule that triggers when device determines GPS jamming. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                    | type                                              |
|--------------|------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `gps_damp` for this rule type.                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device determines GPS jamming. It is for `gps_damp` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### GPS signal lost/recover

A rule that triggers on GPS signal lost/recover. Based on the configs on the device side.

#### Parameters

| name           | description                                                                              | type                                              |
|----------------|------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `gps_lost_recover` for this rule type.                                                   | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when GPS signal lost. It is for `gps_lost` event type.         | string                                            |
| secondary_text | Text of rule notification when GPS signal recovers. It is for `gps_recover` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### GSM jamming (signal dump)

A rule that triggers on GSM jamming. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                    | type                                              |
|--------------|------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `gsm_damp` for this rule type.                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device determines GSM jamming. It is for `gsm_damp` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Hood opening in alarm mode

A rule that triggers on hood opening in alarm mode. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                 | type                                              |
|--------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `hood_alarm` for this rule type.                                                            | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when hood opens in alarm mode. It is for `hood_alarm` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Ignition start in alarm mode

A rule that triggers on ignition start in alarm mode. This rule is not related to usual ignition status change. 
Based on the configs on the device side.

#### Parameters

| name         | description                                                                                    | type                                              |
|--------------|------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `ignition` for this rule type.                                                                 | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when ignition starts in alarm mode. It is for `ignition` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Light sensor

A rule that triggers on when light sensor detects bright/dark environment. Based on the configs on the device side.

#### Parameters

| name           | description                                                                                    | type                                              |
|----------------|------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `light_sensor` for this rule type.                                                             | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when environment bright. It is for `light_sensor_bright` event type. | string                                            |
| secondary_text | Text of rule notification when environment dark. It is for `light_sensor_dark` event type.     | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Location report on demand

A rule that triggers on location requests.

#### Parameters

| name         | description                                                                                                          | type                                              |
|--------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `location_response` for this rule type.                                                                              | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when location is requested manually from device. It is for `location_response` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Locking/unlocking (padlock)

A rule that triggers on locking/unlocking(padlock). Based on the configs on the device side.

#### Parameters

| name           | description                                                                     | type                                              |
|----------------|---------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `locking_unlocking` for this rule type.                                         | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when lock opens. It is for `lock_opened` event type.  | string                                            |
| secondary_text | Text of rule notification when lock closes. It is for `lock_closed` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Low battery

A rule that triggers on low internal battery. Based on the device's battery voltage and value specified for the model on the platform.

#### Parameters

| name         | description                                                                                     | type                                              |
|--------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `lowpower` for this rule type.                                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device's battery charge is low. It is for `lowpower` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Padlock tampering

A rule that triggers on padlock tampering. Based on the configs on the device side.

#### Parameters

| name           | description                                                                                       | type                                              |
|----------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `strap_bolt` for this rule type.                                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when padlock has been forced. It is for `strap_bolt_cut` event type.    | string                                            |
| secondary_text | Text of rule notification when padlock has been installed. It is for `strap_bolt_ins` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Tracker detach from the objects

A rule that triggers when someone detach tracker from the object. Based on the configs on the device side.

#### Parameters

| name         | description                                                                                             | type                                              |
|--------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `detach` for this rule type.                                                                            | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when device determines detach from the object. It is for `detach` event type. | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Tracker switch ON/OFF

A rule that triggers on tracker switch ON/OFF. Based on the configs on the device side.

#### Parameters

| name           | description                                                                           | type                                              |
|----------------|---------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `on_off` for this rule type.                                                          | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when tracker switched off. It is for `poweroff` event type. | string                                            |
| secondary_text | Text of rule notification when tracker switched on. It is for `poweron` event type.   | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Tracker switched OFF or lost connection

A rule that triggers when tracker loses connection with the server - gets red offline status and keeps it for X minutes.

#### Parameters

| name           | description                                                                                                    | type                                              |
|----------------|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `offline` for this rule type.                                                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when tracker switched off or lost connection. It is for `gps_lost` event type.       | string                                            |
| secondary_text | Text of rule notification when tracker switched on or connection restored. It is for `gps_recover` event type. | string                                            |
| param          | Offline time to notification in minutes.                                                                       | int                                               |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |


### Tracker switched ON

A rule that triggers on tracker switch ON. Based on the configs on the device side.

#### Parameters

| name         | description                                                                           | type                                              |
|--------------|---------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | `poweron` for this rule type.                                                         | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when tracker switches on. It is for `poweroff` event type.  | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Vibration sensor

A rule that triggers when vibration sensor determines vibration. Based on the configs on the device side.

#### Parameters

| name           | description                                                                              | type                                              |
|----------------|------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `vibration` for this rule type.                                                          | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when vibration starts. It is for `vibration_start` event type. | string                                            |
| secondary_text | Text of rule notification when vibration ends. It is for `vibration_end` event type.     | string                                            |

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Inputs triggering.

A rule that triggers when the input state changes.

#### Parameters

| name           | description                                                                                           | type                                              |
|----------------|-------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `input_change` for this rule type. Both events for switch on/off will have `input_change` event type. | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when input switches on.                                                     | string                                            |
| secondary_text | Text of rule notification when input switches off.                                                    | string                                            |
| param          | Discrete input number.                                                                                | int                                               | 

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Outputs triggering

A rule that triggers when the output state changes.

#### Parameters

| name           | description                                                                                             | type                                              |
|----------------|---------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | `output_change` for this rule type. Both events for switch on/off will have `output_change` event type. | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when output switches on.                                                      | string                                            |
| secondary_text | Text of rule notification when output switches off.                                                     | string                                            |
| param          | Output number.                                                                                          | int                                               | 

#### extended parameters

| name                | description                                                                                                                   | type    |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                                                     | boolean |
| private_rule        | Affects only sub users. If `true` then the rule and notifications are visible only to sub user.                               | boolean |
| zone_limit_inverted | The rule tracked inside of zones if `false` or outside if `true`. Default is: `false`.                                        | boolean |
| append_zone_title   | Show or not the zone labels in a notification text. Must be `null` or `false` if the zone_limit_inverted param set to `true`. | boolean |


### Parameter in range

A rule that triggers when value of a chosen measurement sensor gets into or out of specified range. One rule per one sensor and device.

#### Parameters

| name           | description                                                                                         | type                                                           |
|----------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| type           | `sensor_range` for this rule type.                                                                  | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text   | Text of rule notification when sensor value goes out range. It is for `sensor_outrange` event type. | string                                                         |
| secondary_text | Text of rule notification when sensor value goes into range. It is for `sensor_inrange` event type. | string                                                         |

#### extended parameters

| name           | description                                                                                                                              | type        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| sensor_id      | ID of a tracked sensor. Only specified if `tracker_params` is not specified.                                                             | int         |
| threshold      | A threshold for a sensor. If the parameter is omitted or null, the default value 0.03 is used. Ignored if `tracker_params` is specified. | double      |
| min            | A minimum range value. Ignored if `tracker_params` is specified.                                                                         | double      |
| max            | A maximum range value. Ignored if `tracker_params` is specified.                                                                         | double      |
| display_value  | Show or not the sensor value in a notification text. Default is: `true`.                                                                 | boolean     |
| tracker_params | An optional object. Specifies a list of parameters to be tracked in the rule, including for different trackers.                          | JSON object |

#### tracker_params

| name            | description                                                                                    | type   |
|-----------------|------------------------------------------------------------------------------------------------|--------|
| sensor_id       | ID of a tracked sensor.                                                                        | int    |
| threshold       | A threshold for a sensor. If the parameter is omitted or null, the default value 0.03 is used. | double |
| min             | A minimum range value.                                                                         | double |
| max             | A maximum range value.                                                                         | double |

Example:
```json
{
  "tracker_params": [{
    "tracker_id": 10181445,
    "trigger_value": "1",
    "state_field": "ble_magnet_sensor_3"
  }, {
    "tracker_id": 10181446,
    "trigger_value": "1",
    "virtual_sensor_id": 21212
  }
  ]
}
```
### State field value

A rule that triggers when specified value of a chosen state field sensor detected.

#### Parameters

| name         | description                                                                                                     | type                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| type         | `state_field_control` for this rule type.                                                                       | [enum](../../../../getting-started/introduction.md#data-types) |
| primary_text | Text of rule notification when state field determines chosen value. It is for `state_field_control` event type. | string                                                         |

#### extended parameters

| name                 | description                                                                                                     | type                                                           |
|----------------------|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| allow_repeat         | Allows notification repeating even if state field value doesn't change.                                         | bool                                                           |
| repeat_delay_seconds | How many seconds must pass with the same value before notification will be generated again.                     | int                                                            |
| trigger_value        | Expected value to trigger the rule. Only specified if `tracker_params` is not specified.                        | string                                                         |
| state_field          | State field code. Only specified if `virtual_sensor_id` and `tracker_params` are not specified.                 | [enum](../../../../getting-started/introduction.md#data-types) |
| virtual_sensor_id    | ID of virtual sensor. Only specified if `state_field` and `tracker_params` are not specified.                   | int                                                            |
| display_value        | Show or not the sensor value in a notification text. Default is: `false`.                                       | boolean                                                        |
| tracker_params       | An optional object. Specifies a list of parameters to be tracked in the rule, including for different trackers. | JSON object                                                    |

#### tracker_params

| name               | description                                                                                     | type                                                           |
|--------------------|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| tracker_id         | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int                                                            |
| trigger_value      | Expected value to trigger the rule.                                                             | string                                                         |
| state_field        | State field code. Only specified if `virtual_sensor_id` is not specified.                       | [enum](../../../../getting-started/introduction.md#data-types) |
| virtual_sensor_id  | ID of virtual sensor. Only specified if `state_field` is not specified.                         | int                                                            |

```json
{
  "tracker_params": [{
    "tracker_id": 10181445,
    "trigger_value": "1",
    "state_field": "ble_magnet_sensor_3"
  }, {
    "tracker_id": 10181446,
    "trigger_value": "1",
    "virtual_sensor_id": 21212
  }
  ]
}
```

---
title: Rule types
description: Rule types with all parameters to create. The rule availability depends on the device and rule integration for it.
---

# Rule types

Rule types with all parameters to create. The rule availability depends on the device, connected and configured equipment 
and rule integration for it.

***

### Common parameters

Common parameters exist in all rule types.

| name            | description                                                                                           | type        |
|-----------------|-------------------------------------------------------------------------------------------------------|-------------|
| description     | Rule's description.                                                                                   | string      |
| primary_text    | Primary text of rule notification.                                                                    | string      |
| alerts          | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule-object). | JSON object |
| suspended       | `true` if the rule suspended.                                                                         | boolean     |
| name            | Name of a rule.                                                                                       | string      |
| trackers        | List of bound tracker IDs.                                                                            | int array   |
| extended_params | Extended parameters for the rule. Described below.                                                    | JSON object |
| schedule        | The rule will work in specified period. Described in [rule_object](./rule.md#rule-object).            | JSON object |
| zone_ids        | List of bound zones.                                                                                  | int array   |

#### Common extended parameters

`extended_parameters` that used in all rule types.

| name                | description                                                                                         | type    |
|---------------------|-----------------------------------------------------------------------------------------------------|---------|
| emergency           | If `true` enables emergency notification.                                                           | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. Default is: `false`.                                      | boolean |
| private_rule        | Affects only sub users now. If `true` then the rule and notifications are visible only to sub user. | boolean |
| append_zone_title   | Show or not a label of zone in a notification.                                                      | boolean |

***

### Geofence entrance or exit

A rule that triggers on device entering/exiting created on platform [geofences](../../zone/index.md#list).

#### parameters

| name           | description                                              | type                                              |
|----------------|----------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "inoutzone".                             | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification on entering geofence.  | string                                            |
| secondary_text | Secondary text of rule notification on exiting geofence. | string                                            |

***

### Parking state detection

A rule that triggers on detection of parking state calculated based on [parking detection settings](../settings/trip_detection.md).

#### parameters

| name           | description                                         | type                                              |
|----------------|-----------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "track_change".                     | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification on parking start. | string                                            |
| secondary_text | Secondary text of rule notification on parking end. | string                                            |

***

### Speeding (hardware related)

A rule that triggers on speed exceeding determined by hardware. Based on the configs on the device side.

#### parameters

| name         | description                                          | type                                              |
|--------------|------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "over_speed_reported".               | [enum](../../../../getting-started.md#data-types) |

***

### Speeding (platform related)

A rule that triggers on speed exceeding determined by the platform. Based on received speed from device.

#### parameters

| name         | description                                          | type                                              |
|--------------|------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "speedup".                           | [enum](../../../../getting-started.md#data-types) |
| param        | Speed limit.                                         | int                                               |

***

### Deviation from the route

A rule that triggers on deviations from the route. The [route (sausage)](../../zone/index.md#sausage) geofence must be created. 

#### parameters

| name         | description                                         | type                                              |
|--------------|-----------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "route".                            | [enum](../../../../getting-started.md#data-types) |
| zone_ids     | Mandatory list of bound route zones. Can't be empty | int array                                         |


#### extended parameters

| name                    | description                                                                              | type    |
|-------------------------|------------------------------------------------------------------------------------------|---------|
| allow_exit_at_endpoints | If `true` disables notifications on deviations from the start and end points of a route. | boolean |

***

### Driving time

A rule that triggers when your employee drives more than allowed. The driving time is calculated based on [parking detection settings](../settings/trip_detection.md).

#### parameters

| name           | description                                                        | type                                              |
|----------------|--------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "excessive_driving".                               | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when driving time exceeded.      | string                                            |
| secondary_text | Secondary text of rule notification on driving time exceeding end. | string                                            |


#### extended parameters

| name             | description                                                                                                  | type |
|------------------|--------------------------------------------------------------------------------------------------------------|------|
| max_driving_time | Allowed driving time. How much time your employee can drive a car                                            | int  |
| min_parking_time | Minimum parking time to reset the timer. How much time your employee must wait until he can continue driving | int  |

***

### Parking time

A rule that triggers when your employee standstill more than allowed. The parking time is calculated based on [parking detection settings](../settings/trip_detection.md).

#### parameters

| name           | description                                                        | type                                              |
|----------------|--------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "excessive_parking".                               | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when parking time exceeded.      | string                                            |
| secondary_text | Secondary text of rule notification on parking time exceeding end. | string                                            |

#### extended parameters

| name                  | description                                              | type |
|-----------------------|----------------------------------------------------------|------|
| max_parking_duration  | Allowed parking time. How much time a car can standstill | int  |

***

### Task performance

A rule that triggers when assigned to a tracker [task](../../../field_service/task/index.md) changes its status. 

#### parameters

| name         | description                                                 | type                                              |
|--------------|-------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "task_status_change".                       | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name                        | description                                                                            | type         |
|-----------------------------|----------------------------------------------------------------------------------------|--------------|
| statuses                    | List of tracked statuses. Possible statuses are "arrived", "done","delayed", "failed". | string array |
| on_form_submission          | If `true` form submission will track.                                                  | boolean      |
| on_repeated_form_submission | If `true` form resubmission will track.                                                | boolean      |

***

### Work status change

A rule that triggers when tracker [work status](../../status/tracker.md) changes.

#### parameters

| name         | description                                                 | type                                              |
|--------------|-------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "work_status_change".                       | [enum](../../../../getting-started.md#data-types) |


#### extended parameters

| name       | description                 | type      |
|------------|-----------------------------|-----------|
| status_ids | List of tracked status IDs. | int array |

***

### Excessive idling (hardware related)

A rule that triggers on excessive idling registered by hardware. Based on the configs on the device side.

#### parameters

| name           | description                                                                         | type                                              |
|----------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "idling".                                                           | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when excessive idling detected by device.         | string                                            |
| secondary_text | Secondary text of rule notification when excessive idling end detected by a device. | string                                            |

***

### Excessive idling (platform related)

A rule that triggers on excessive idling registered by the platform. The idling time is calculated based on [parking detection settings](../settings/trip_detection.md) and ignition state.

#### parameters

| name           | description                                                                         | type                                              |
|----------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "idling_soft".                                                      | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when excessive idling detected by platform.       | string                                            |
| secondary_text | Secondary text of rule notification when excessive idling end detected by platform. | string                                            |
| param          | Idle duration to send notification.                                                 | int                                               | 

***

### Fuel level change

Rule triggered by a drastic change in fuel level. A drastic change is when the fuel level changes faster than the 
accuracy of the sensor in a span of ten minutes.

#### parameters

| name           | description                                                             | type                                              |
|----------------|-------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "fuel_level_leap".                                      | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification on drastically fuel level increase.   | string                                            |
| secondary_text | Secondary text of rule notification on drastically fuel level decrease. | string                                            |

#### extended parameters

| name      | description           | type |
|-----------|-----------------------|------|
| sensor_id | ID of tracked sensor. | int  |

***

### Harsh driving

A rule that triggers on harsh driving. Based on the configs on the device side.

#### parameters

| name         | description                                                        | type                                              |
|--------------|--------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "harsh_driving".                                   | [enum](../../../../getting-started.md#data-types) |

***

### Advanced driver assistance systems (ADAS)

A rule that triggers on warnings from driver-assistance systems (ADAS). Detected by camera and based on the configs on the device side.

#### parameters

| name         | description                                               | type                                              |
|--------------|-----------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "driver_assistance".                      | [enum](../../../../getting-started.md#data-types) |


#### extended parameters

| name                             | description                       | type    |
|----------------------------------|-----------------------------------|---------|
| lane_departure_enabled           | If `true` lane departure tracked. | boolean |
| forward_collision_enabled        | If `true` lane departure tracked. | boolean |
| headway_warning_enabled          | If `true` lane departure tracked. | boolean |
| peds_in_danger_zone_enabled      | If `true` lane departure tracked. | boolean |
| peds_collision_warning_enabled   | If `true` lane departure tracked. | boolean |
| traffic_sign_recognition_enabled | If `true` lane departure tracked. | boolean |

***

### Auto geofencing (unauthorized movement detected by location change)

A rule that triggers on auto geofencing. When a car's ignition is off, and it outs the automatically created radius around it.

#### parameters

| name         | description                                                                            | type                                              |
|--------------|----------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "auto_geofence".                                                       | [enum](../../../../getting-started.md#data-types) |

***

### Autocontrol related rules

Autocontrol related tracked rules like alarm, battery, doors and others. Based on the configs on the device side.

#### parameters

| name         | description                                                                | type                                              |
|--------------|----------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "autocontrol".                                             | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name             | description                                            | type        |
|------------------|--------------------------------------------------------|-------------|
| alarmcontrol     | Activation of car alarms. Described below              | JSON object |
| battery_off      | Disabling of external power supply. Described below    | JSON object |
| door_alarm       | Opening doors/trunk. Described below                   | JSON object |
| hood_alarm       | Opening hood. Described below                          | JSON object |
| ignition         | Ignition. Described below                              | JSON object |
| parking          | Unauthorized movement. Described below                 | JSON object |
| gsm_damp         | GSM-signal dumping (low signal level). Described below | JSON object |
| security_control | Switching ON/OFF security mode. Described below        | JSON object |

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

***

### Car crash

A rule that triggers when device's sensors detect car crash. Based on the configs on the device side.

#### parameters

| name         | description                                                           | type                                              |
|--------------|-----------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "crash_alarm".                                        | [enum](../../../../getting-started.md#data-types) |

***

### Cruise control switched ON/OFF

A rule that triggers when a device provides cruise control switching event. Based on the configs on the device side.

#### parameters

| name           | description                                                        | type                                              |
|----------------|--------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "cruise_control".                                  | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification for cruise control switch on.    | string                                            |
| secondary_text | Secondary text of rule notification for cruise control switch off. | string                                            |

***

### Distance between objects

A rule that triggers a change in distance between objects. The distance is measured by the last valid GPS coordinates between chosen objects.

#### parameters

| name           | description                                                    | type                                              |
|----------------|----------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "distance_control".                            | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when distance is breached.   | string                                            |
| secondary_text | Secondary text of rule notification when distance is restored. | string                                            |

#### extended parameters

| name                    | description                                                        | type                                              |
|-------------------------|--------------------------------------------------------------------|---------------------------------------------------|
| observed_trackers       | List of observed tracker IDs.                                      | int array                                         |
| control_type            | Type of distance control. One of `["moving_away", "approaching"]`. | [enum](../../../../getting-started.md#data-types) |
| control_distance_meters | Distance for control in meters.                                    | int                                               |

***

### Driver absence

A rule that triggers when driver lefts or enters cabin. Detected by camera and based on the configs on the device side.

#### parameters

| name           | description                                                     | type                                              |
|----------------|-----------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "driver_enter_absence".                         | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when driver lefts a cabin.    | string                                            |
| secondary_text | Secondary text of rule notification when driver enters a cabin. | string                                            |

***

### Driver change

A rule that triggers on driver change automatically by the key or manually in widget with driver from a [drivers list](../../../field_service/employee/index.md).

#### parameters

| name         | description                                                                    | type                                              |
|--------------|--------------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "driver_change".                                               | [enum](../../../../getting-started.md#data-types) |

***

### Driver distraction

A rule that triggers when driver distracts from the road. Detected by camera and based on the configs on the device side.

#### parameters

| name           | description                                                         | type                                              |
|----------------|---------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "driver_distraction".                               | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when driver distraction detected. | string                                            |
| secondary_text | Secondary text of rule notification when driver distraction ends.   | string                                            |

***

### Fall detection

A rule that triggers when g-sensor or accelerometer detects falling.

#### parameters

| name         | description                                                      | type                                              |
|--------------|------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "g_sensor".                                      | [enum](../../../../getting-started.md#data-types) |

***

### Fatigue driving

A rule that triggers on fatigue driving. Detected by camera and based on the configs on the device side.

#### parameters

| name           | description                                                         | type                                              |
|----------------|---------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "fatigue_driving".                                  | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when fatigue driving is detected. | string                                            |
| secondary_text | Secondary text of rule notification when fatigue driving ends.      | string                                            |

***

### Identification via RFID/iButton/Camera

A rule that triggers on a driver identification with help of RFID, iButton or Camera. Based on the configs on the device side.

#### parameters

| name           | description                                                                 | type                                              |
|----------------|-----------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "driver_identification".                                    | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when the driver tag has been identified.  | string                                            |
| secondary_text | Secondary text of rule notification when the driver tag was not identified. | string                                            |

***

### No movement

A rule that triggers when the device does not detect motion for longer than the time set in its settings. Based on the configs on the device side.

#### parameters

| name         | description                                                   | type                                              |
|--------------|---------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "no_movement".                                | [enum](../../../../getting-started.md#data-types) |

***

### Pressing SOS button

A rule that triggers on SOS button pressing. Based on the configs on the device side.

#### parameters

| name         | description                                                              | type                                              |
|--------------|--------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "sos".                                                   | [enum](../../../../getting-started.md#data-types) |

***

### Social distancing monitoring

A rule that triggers on social distancing violation. Similar to distance between objects but related based on the configs on the device side.

#### parameters

| name           | description                                                        | type                                              |
|----------------|--------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "proximity_violation".                             | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when safety distance breached.   | string                                            |
| secondary_text | Secondary text of rule notification when safety distance restored. | string                                            |

***

### Unauthorized movement (determined by accelerometer)

A rule that triggers on unauthorized movement detected by accelerometer when ignition is off. Based on the configs on the device side.

#### parameters

| name         | description                                                                            | type                                              |
|--------------|----------------------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "parking".                                                             | [enum](../../../../getting-started.md#data-types) |

***

### Backup battery low

A rule that triggers on backup battery low. Based on the configs on the device side.

#### parameters

| name         | description                                                | type                                              |
|--------------|------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "backup_battery_low".                      | [enum](../../../../getting-started.md#data-types) |

***

### Bracelet sensor

A rule that triggers on bracelet sensor opening/closing. Based on the configs on the device side.

#### parameters

| name           | description                                               | type                                              |
|----------------|-----------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "bracelet".                               | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when bracelet opened.   | string                                            |
| secondary_text | Secondary text of rule notification when bracelet closed. | string                                            |

***

### Call button pressed

A rule that triggers on call button pressing. Based on the configs on the device side.

#### parameters

| name         | description                                                             | type                                              |
|--------------|-------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "call_button_pressed".                                  | [enum](../../../../getting-started.md#data-types) |

***

### Car alarm triggered

A rule that triggers on car alarm. Based on the configs on the device side.

#### parameters

| name         | description                                                             | type                                              |
|--------------|-------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "alarmcontrol".                                         | [enum](../../../../getting-started.md#data-types) |

***

### Case intrusion

A rule that triggers on case intrusion. Based on the configs on the device side.

#### parameters

| name         | description                                                     | type                                              |
|--------------|-----------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "case_intrusion".                               | [enum](../../../../getting-started.md#data-types) |

***

### Check engine (MIL)

A rule that triggers on check engine (MIL) events. Based on the configs on the device side.

#### parameters

| name         | description                                                                | type                                              |
|--------------|----------------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "check_engine_light".                                      | [enum](../../../../getting-started.md#data-types) |

***

### Connection/disconnection to the OBDII port

A rule that triggers on connection/disconnection to the OBD2 port. Based on the configs on the device side.

#### parameters

| name           | description                                                                   | type                                              |
|----------------|-------------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "obd_plug_unplug".                                            | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when device connected to OBDII port.        | string                                            |
| secondary_text | Secondary text of rule notification when device disconnected from OBDII port. | string                                            |

***

### Door opening in alarm mode

A rule that triggers on door opening in alarm mode. Based on the configs on the device side.

#### parameters

| name         | description                                                           | type                                              |
|--------------|-----------------------------------------------------------------------|---------------------------------------------------|
| type         | Default `type`: "door_alarm".                                         | [enum](../../../../getting-started.md#data-types) |

***

### External device connection

A rule that triggers on connection/disconnection of an external device. Based on the configs on the device side.

#### parameters

| name           | description                                                                         | type                                              |
|----------------|-------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "external_device_connection".                                       | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when external device connected to tracker.        | string                                            |
| secondary_text | Secondary text of rule notification when external device disconnected from tracker. | string                                            |

***

### External power cut

A rule that triggers when device disconnects from car's battery. Based on the configs on the device side.

#### parameters

| name           | description                                                        | type                                              |
|----------------|--------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "battery_off".                                     | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when external power disconnects. | string                                            |
| secondary_text | Secondary text of rule notification when external power connects.  | string                                            |

***

### GPS antenna disconnected

A rule that triggers on GPS antenna disconnect. Based on the configs on the device side.

#### parameters

| name | description                           | type                                              |
|------|---------------------------------------|---------------------------------------------------|
| type | Default `type`: "antenna_disconnect". | [enum](../../../../getting-started.md#data-types) |

***

### GPS jamming (signal dump)

A rule that triggers when device determines GPS jamming. Based on the configs on the device side.

#### parameters

| name | description                 | type                                              |
|------|-----------------------------|---------------------------------------------------|
| type | Default `type`: "gps_damp". | [enum](../../../../getting-started.md#data-types) |

***

### GPS signal lost/recover

A rule that triggers on GPS signal lost/recover. Based on the configs on the device side.

#### parameters

| name           | description                                                   | type                                              |
|----------------|---------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "gps_lost_recover".                           | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when GPS signal lost.       | string                                            |
| secondary_text | Secondary text of rule notification when GPS signal recovers. | string                                            |

***

### GSM jamming (signal dump)

A rule that triggers on GSM jamming. Based on the configs on the device side.

#### parameters

| name | description                 | type                                              |
|------|-----------------------------|---------------------------------------------------|
| type | Default `type`: "gsm_damp". | [enum](../../../../getting-started.md#data-types) |

***

### Hood opening in alarm mode

A rule that triggers on hood opening in alarm mode. Based on the configs on the device side.

#### parameters

| name | description                   | type                                              |
|------|-------------------------------|---------------------------------------------------|
| type | Default `type`: "hood_alarm". | [enum](../../../../getting-started.md#data-types) |

***

### Ignition start in alarm mode

A rule that triggers on ignition start in alarm mode. This rule is not related to usual ignition status change. 
Based on the configs on the device side.

#### parameters

| name | description                 | type                                              |
|------|-----------------------------|---------------------------------------------------|
| type | Default `type`: "ignition". | [enum](../../../../getting-started.md#data-types) |

***

### Light sensor

A rule that triggers on when light sensor detects bright/dark environment. Based on the configs on the device side.

#### parameters

| name           | description                                                | type                                              |
|----------------|------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "light_sensor".                            | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when environment bright. | string                                            |
| secondary_text | Secondary text of rule notification when environment dark. | string                                            |

***

### Location report on demand

A rule that triggers on location requests.

#### parameters

| name | description                          | type                                              |
|------|--------------------------------------|---------------------------------------------------|
| type | Default `type`: "location_response". | [enum](../../../../getting-started.md#data-types) |

***

### Locking/unlocking (padlock)

A rule that triggers on locking/unlocking(padlock). Based on the configs on the device side.

#### parameters

| name           | description                                           | type                                              |
|----------------|-------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "locking_unlocking".                  | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when lock opens.    | string                                            |
| secondary_text | Secondary text of rule notification when lock closes. | string                                            |

***

### Low battery

A rule that triggers on low internal battery. Based on the device's battery voltage and value specified for the model on the platform.

#### parameters

| name | description                 | type                                              |
|------|-----------------------------|---------------------------------------------------|
| type | Default `type`: "lowpower". | [enum](../../../../getting-started.md#data-types) |

***

### Padlock tampering

A rule that triggers on padlock tampering. Based on the configs on the device side.

#### parameters

| name           | description                                                          | type                                              |
|----------------|----------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "strap_bolt".                                        | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when padlock has been forced.      | string                                            |
| secondary_text | Secondary text of rule notification when padlock has been installed. | string                                            |

***

### Tracker detach from the objects

A rule that triggers when someone detach tracker from the object. Based on the configs on the device side.

#### parameters

| name | description               | type                                              |
|------|---------------------------|---------------------------------------------------|
| type | Default `type`: "detach". | [enum](../../../../getting-started.md#data-types) |

***

### Tracker switch ON/OFF

A rule that triggers on tracker switch ON/OFF. Based on the configs on the device side.

#### parameters

| name           | description                                                   | type                                              |
|----------------|---------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "on_off".                                     | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when tracker switched off.  | string                                            |
| secondary_text | Secondary text of rule notification when tracker switched on. | string                                            |

***

### Tracker switched OFF or lost connection

A rule that triggers when tracker loses connection with the server - gets red offline status and keeps it for X minutes.

#### parameters

| name           | description                                                                          | type                                              |
|----------------|--------------------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "offline".                                                           | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when tracker switched off or lost connection.      | string                                            |
| secondary_text | Secondary text of rule notification when tracker switched on or connection restored. | string                                            |
| param          | Offline time to notification in minutes.                                             | int                                               |

***

### Tracker switched ON

A rule that triggers on tracker switch ON. Based on the configs on the device side.

#### parameters

| name | description                | type                                              |
|------|----------------------------|---------------------------------------------------|
| type | Default `type`: "poweron". | [enum](../../../../getting-started.md#data-types) |

***

### Vibration sensor

A rule that triggers when vibration sensor determines vibration. Based on the configs on the device side.

#### parameters

| name           | description                                              | type                                              |
|----------------|----------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "vibration".                             | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when vibration starts. | string                                            |
| secondary_text | Secondary text of rule notification when vibration ends. | string                                            |

***

### Inputs triggering.

A rule that triggers when the input state changes.

#### parameters

| name           | description                                                  | type                                              |
|----------------|--------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "input_change".                              | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when input switches on.    | string                                            |
| secondary_text | Secondary text of rule notification when input switches off. | string                                            |
| param          | Discrete input number.                                       | int                                               | 

***

### Outputs triggering

A rule that triggers when the output state changes.

#### parameters

| name           | description                                                   | type                                              |
|----------------|---------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "output_change".                              | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when output switches on.    | string                                            |
| secondary_text | Secondary text of rule notification when output switches off. | string                                            |
| param          | Output number.                                                | int                                               | 

***

### Parameter in range

A rule that triggers when value of a chosen measurement sensor gets into or out of specified range. One rule per one sensor and device.

#### parameters

| name           | description                                                            | type                                              |
|----------------|------------------------------------------------------------------------|---------------------------------------------------|
| type           | Default `type`: "sensor_range".                                        | [enum](../../../../getting-started.md#data-types) |
| primary_text   | Primary text of rule notification when sensor value goes out range.    | string                                            |
| secondary_text | Secondary text of rule notification when sensor value goes into range. | string                                            |

#### extended parameters

| name      | description               | type |
|-----------|---------------------------|------|
| threshold | A threshold for a sensor. | int  |
| sensor_id | ID of a tracked sensor.   | int  |
| min       | A minimum range value.    | int  |
| max       | A maximum range value.    | int  |

***

### State field value

A rule that triggers when specified value of a chosen state field sensor detected.

#### parameters

| name | description                            | type                                              |
|------|----------------------------------------|---------------------------------------------------|
| type | Default `type`: "state_field_control". | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name                 | description                                                                                 | type                                              |
|----------------------|---------------------------------------------------------------------------------------------|---------------------------------------------------|
| allow_repeat         | Allows notification repeating even if state field value doesn't change.                     | bool                                              |
| repeat_delay_seconds | How many seconds must pass with the same value before notification will be generated again. | int                                               |
| state_field          | State field code.                                                                           | [enum](../../../../getting-started.md#data-types) |
| trigger_value        | Expected value to trigger the rule.                                                         | string                                            |


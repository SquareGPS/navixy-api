---
title: Rule types
description: Rule types
---

# Rule types

Rule types with all parameters to create. The rule availability depends on the device and rule integration for it.

### Common parameters

Common parameters exist in all rule types.

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule-object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | int array |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule-object). | JSON object |
| zone_ids | List of bound zones. | int array |

#### Common extended parameters

`extended_parameters` that used in all rule types.

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. Default is: `false`. | boolean |
| private_rule | Affects only sub users now. If `true` then the rule and notifications are visible only to sub user. | boolean |

### Geofence entrance or exit

A rule that triggers on entering/exiting geofences.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "inoutzone". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| append_zone_title | Show or not a label of zone in a notification. | boolean |

### Speed exceeding

A rule that triggers on speed exceeding.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "speedup". | [enum](../../../../getting-started.md#data-types) |
| param | Speed limit. | int |

### Parking state detection

A rule that triggers on detection of parking state.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "track_change". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Deviation from the route

A rule that triggers on deviations from the route.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "route". | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| allow_exit_at_endpoints | If `true` disables notifications on deviations from the start and end points of a route. | boolean |

### Work status change

A rule that triggers on status changing. 

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "work_status_change". | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| status_ids | List of tracked status ids. | int array |

### Task performance

A rule that triggers on task status changes.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "work_status_change". | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| statuses | List of tracked statuses. Possible statuses are "arrived", "done","delayed", "failed". | string array |
| on_form_submission | If `true` form submission will track. | boolean |
| on_repeated_form_submission | If `true` form resubmission will track. | boolean |

### Excessive idling (hardware related)

A rule that triggers on excessive idling registered by hardware.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "idling". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Excessive idling (platform related)

A rule that triggers on excessive idling registered by the platform.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "idling_soft". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |
| param | Idle duration to send notification. | int | 

### Fuel level change

A rule that triggers on a fuel level change.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "fuel_level_leap". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| sensor_id | Id of tracked sensor. | int |

### Harsh driving

A rule that triggers on harsh driving.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "harsh_driving". | [enum](../../../../getting-started.md#data-types) |

### Pressing SOS button

A rule that triggers on SOS button pressing.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "sos". | [enum](../../../../getting-started.md#data-types) |

### Auto geofencing

A rule that triggers on auto geofencing.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "auto_geofence". | [enum](../../../../getting-started.md#data-types) |

### Fall detection

A rule that triggers on fall detection.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "g_sensor". | [enum](../../../../getting-started.md#data-types) |

### Unauthorized movement

A rule that triggers on unauthorized movement.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "parking". | [enum](../../../../getting-started.md#data-types) |

### Car crash

A rule that triggers on a car crash.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "crash_alarm". | [enum](../../../../getting-started.md#data-types) |

### Autocontrol related

Autocontrol related tracked rules.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "autocontrol". | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| alarmcontrol | Activation of car alarms. Described below | JSON object |
| battery_off | Disabling of external power supply. Described below | JSON object |
| door_alarm | Opening doors/trunk. Described below | JSON object |
| hood_alarm | Opening hood. Described below | JSON object |
| ignition | Ignition. Described below | JSON object |
| parking | Unauthorized movement. Described below | JSON object |
| gsm_damp | GSM-signal dumping (low signal level). Described below | JSON object |
| security_control | Switching ON/OFF security mode. Described below | JSON object |

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

### Advanced driver assistance systems (ADAS)

A rule that triggers on warnings from driver-assistance systems (ADAS).

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "driver_assistance". | [enum](../../../../getting-started.md#data-types) |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| lane_departure_enabled | If `true` lane departure tracked. |  boolean |
| forward_collision_enabled | If `true` lane departure tracked. |  boolean |
| headway_warning_enabled | If `true` lane departure tracked. |  boolean |
| peds_in_danger_zone_enabled | If `true` lane departure tracked. |  boolean |
| peds_collision_warning_enabled | If `true` lane departure tracked. |  boolean |
| traffic_sign_recognition_enabled | If `true` lane departure tracked. |  boolean |

### Identification via RFID/iButton

A rule that triggers on a driver identification.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "driver_identification". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Driver change

A rule that triggers on driver change.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "driver_change". | [enum](../../../../getting-started.md#data-types) |

### Fatigue driving

A rule that triggers on fatigue driving.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "fatigue_driving". | [enum](../../../../getting-started.md#data-types) |

### Social distancing monitoring

A rule that triggers on social distancing violation.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "proximity_violation". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Tracker switched OFF or lost connection

A rule that triggers on device switch OFF and lost connection.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "offline". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |
| param | Offline time to notification. | int |

### GSM signal dump

A rule that triggers on GSM signal dump.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "gsm_damp". | [enum](../../../../getting-started.md#data-types) |

### Low battery

A rule that triggers on low internal battery.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "lowpower". | [enum](../../../../getting-started.md#data-types) |

### Bracelet sensor

A rule that triggers on bracelet sensor opening/closing.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "bracelet". | [enum](../../../../getting-started.md#data-types) |

### Car alarm triggered

A rule that triggers on car alarm.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "alarmcontrol". | [enum](../../../../getting-started.md#data-types) |

### Tracker detach from the objects

A rule that triggers on a tracker detach from the object.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "detach". | [enum](../../../../getting-started.md#data-types) |

### External power cut

A rule that triggers on external power cut.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "battery_off". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Door opening in alarm mode

A rule that triggers on door opening in alarm mode.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "door_alarm". | [enum](../../../../getting-started.md#data-types) |

### Hood opening in alarm mode

A rule that triggers on hood opening in alarm mode.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "hood_alarm". | [enum](../../../../getting-started.md#data-types) |

### Location report on demand

A rule that triggers on location requests.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "location_response". | [enum](../../../../getting-started.md#data-types) |

### Connection/disconnection to the OBD2 port

A rule that triggers on connection/disconnection to the OBD2 port.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "obd_plug_unplug". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Tracker switch ON/OFF

A rule that triggers on tracker switch ON/OFF.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "on_off". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Locking/unlocking (padlock)

A rule that triggers on locking/unlocking(padlock).

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "locking_unlocking". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Backup battery low

A rule that triggers on backup battery low.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "backup_battery_low". | [enum](../../../../getting-started.md#data-types) |

### Case intrusion

A rule that triggers on case intrusion.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "case_intrusion". | [enum](../../../../getting-started.md#data-types) |

### GPS signal lost/recover

A rule that triggers on GPS signal lost/recover.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "gps_lost_recover". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Padlock tampering

A rule that triggers on padlock tampering.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "strap_bolt". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Vibration sensor

A rule that triggers on vibration sensor.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "vibration". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Light sensor

A rule that triggers on a light sensor.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "light_sensor". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

### Call button pressed

A rule that triggers on call button pressing. 

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "call_button_pressed". | [enum](../../../../getting-started.md#data-types) |

### Tracker switched ON

A rule that triggers on tracker switch ON.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "poweron". | [enum](../../../../getting-started.md#data-types) |

### GPS antenna disconnected

A rule that triggers on GPS antenna disconnect.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "antenna_disconnect". | [enum](../../../../getting-started.md#data-types) |

### Check engine (MIL)

A rule that triggers on check engine (MIL) events.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "check_engine_light". | [enum](../../../../getting-started.md#data-types) |

### Inputs triggering.

A rule on inputs triggering.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "input_change". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |
| param | Input number. | int | 

### Outputs triggering

A rule on outputs triggering.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "output_change". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |
| param | Output number. | int | 

### Parameter in range

A rule that triggers on a parameter in range.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "sensor_range". | [enum](../../../../getting-started.md#data-types) |
| secondary_text | Secondary text of rule notification. | string |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| threshold | A threshold for a sensor. | int |
| sensor_id | Id of a tracked sensor. | int |
| min | A minimum range value. | int |
| max | A maximum range value. | int |

### No movement

A rule that triggers when the device is stationary.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| type | Default `type`: "no_movement". | [enum](../../../../getting-started.md#data-types) |

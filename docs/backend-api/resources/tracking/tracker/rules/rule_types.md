---
title: Rule types
description: Rule types
---

# Rule types

Rule types with all parameters to create. The rule availability depends on the device and rule integration for it.

### Geofence entrance or exit

A rule that triggers on entering/exiting geofences.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "inoutzone". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. Default is: `false`. | boolean |
| append_zone_title | Show or not a label of zone in a notification. | boolean |

### Speed exceeding

A rule that triggers on speed exceeding.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "speedup". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| param | Speed limit. | int | 
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Parking state detection

A rule that triggers on detection of parking state.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "track_change". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Deviation from the route

A rule that triggers on deviations from the route.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "route". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |
| allow_exit_at_endpoints | If `true` disables notifications on deviations from the start and end points of a route. | boolean |

### Work status change

A rule that triggers on status changing. 

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "work_status_change". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |
| status_ids | List of tracked status ids. | array of int |

### Task performance

A rule that triggers on task status changes.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "work_status_change". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |
| statuses | List of tracked statuses. Possible statuses are "arrived", "done","delayed", "failed". | array of string |
| on_form_submission | If `true` form submission will track. | boolean |
| on_repeated_form_submission | If `true` form resubmission will track. | boolean |

### Excessive idling (hardware related)

A rule that triggers on excessive idling registered by hardware.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "idling". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Excessive idling (platform related)

A rule that triggers on excessive idling registered by the platform.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "idling_soft". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| param | Idle duration to send notification. | int | 
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Fuel level change

A rule that triggers on a fuel level change.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "fuel_level_leap". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |
| sensor_id | Id of tracked sensor. | int |

### Harsh driving

A rule that triggers on harsh driving.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "harsh_driving". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Pressing SOS button

A rule that triggers on SOS button pressing.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "sos". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Auto geofencing

A rule that triggers on auto geofencing.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "auto_geofence". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Fall detection

A rule that triggers on fall detection.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "g_sensor". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Unauthorized movement

A rule that triggers on unauthorized movement.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "parking". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Car crash

A rule that triggers on a car crash.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "crash_alarm". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Autocontrol related

Autocontrol related tracked rules.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "autocontrol". | string enum |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

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
```

### Advanced driver assistance systems (ADAS)

A rule that triggers on warnings from driver-assistance systems (ADAS).

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "driver_assistance". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |
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
| description | Rule's description. | string |
| type | Default `type`: "driver_identification". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Driver change

A rule that triggers on driver change.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "driver_change". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Fatigue driving

A rule that triggers on fatigue driving.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "fatigue_driving". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Social distancing monitoring

A rule that triggers on social distancing violation.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "proximity_violation". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Tracker switched OFF or lost connection

A rule that triggers on device switch OFF and lost connection.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "offline". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| param | Offline time to notification. | int |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### GSM signal dump

A rule that triggers on GSM signal dump.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "gsm_damp". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Low battery

A rule that triggers on low internal battery.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "lowpower". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Bracelet sensor

A rule that triggers on bracelet sensor opening/closing.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "bracelet". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Car alarm triggered

A rule that triggers on car alarm.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "alarmcontrol". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Tracker detach from the objects

A rule that triggers on a tracker detach from the object.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "detach". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### External power cut

A rule that triggers on external power cut.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "battery_off". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Door opening in alarm mode

A rule that triggers on door opening in alarm mode.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "door_alarm". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Hood opening in alarm mode

A rule that triggers on hood opening in alarm mode.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "hood_alarm". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Location report on demand

A rule that triggers on location requests.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "location_response". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Connection/disconnection to the OBD2 port

A rule that triggers on connection/disconnection to the OBD2 port.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "obd_plug_unplug". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Tracker switch ON/OFF

A rule that triggers on tracker switch ON/OFF.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "on_off". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Locking/unlocking (padlock)

A rule that triggers on locking/unlocking(padlock).

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "locking_unlocking". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Backup battery low

A rule that triggers on backup battery low.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "backup_battery_low". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Case intrusion

A rule that triggers on case intrusion.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "case_intrusion". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### GPS signal lost/recover

A rule that triggers on GPS signal lost/recover.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "gps_lost_recover". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Padlock tampering

A rule that triggers on padlock tampering.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "strap_bolt". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Vibration sensor

A rule that triggers on vibration sensor.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "vibration". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Light sensor

A rule that triggers on a light sensor.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "light_sensor". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Call button pressed

A rule that triggers on call button pressing. 

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "call_button_pressed". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Tracker switched ON

A rule that triggers on tracker switch ON.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "poweron". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### GPS antenna disconnected

A rule that triggers on GPS antenna disconnect.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "antenna_disconnect". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Check engine (MIL)

A rule that triggers on check engine (MIL) events.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "check_engine_light". | string enum |
| primary_text | Primary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Inputs triggering.

A rule on inputs triggering.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "input_change". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| param | Input number. | int | 
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Outputs triggering

A rule on outputs triggering.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "output_change". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| param | Output number. | int | 
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |

### Parameter in range

A rule that triggers on a parameter in range.

#### parameters

| name | description | type |
| ------ | ------------- | ------ |
| description | Rule's description. | string |
| type | Default `type`: "sensor_range". | string enum |
| primary_text | Primary text of rule notification. | string |
| secondary_text | Secondary text of rule notification. | string |
| alerts | Alerts object with destinations for notifications. Described in [rule_object](./rule.md#rule object). | JSON object |
| suspended | `true` if the rule suspended. | boolean |
| name | Name of a rule. | string |
| trackers | List of bound tracker ids. | array of int |
| extended_params | Extended parameters for the rule. Described below. | JSON object |
| schedule | The rule will work in specified period. Described in [rule_object](./rule.md#rule object). | JSON object |
| zone_ids | List of bound zones. | array of int |

#### extended parameters

| name | description | type |
| ------ | ------------- | ------ |
| emergency | If `true` enables emergency notification. | boolean |
| zone_limit_inverted | The rule tracked inside or outside zones. | boolean |
| threshold | A threshold for a sensor. | int |
| sensor_id | Id of a tracked sensor. | int |
| min | A minimum range value. | int |
| max | A maximum range value. | int |
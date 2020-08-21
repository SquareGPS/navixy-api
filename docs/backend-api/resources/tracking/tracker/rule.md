---
title: /rule
description: /rule
---

# Rule

A rule element consists of following fields:

```json
{
    "id": ${int},
    "name": ${string},
    "description": ${string},
    "zone_id": ${int}, // deprecated, use zone_ids instead on this, "zone_ids":[ ${int}, ... ] list of zone ids
    "trackers": [ ${int}, ... ], // list of tracker ids
    "type": ${string},
    "primary_text": ${string},
    "secondary_text": ${string},
    "param": ${int}, // common parameter
    "alerts": {
        "sms_phones": [ ${string}, ... ],
        "phones": [ ${string}, ... ], // phones for voice calls
        "emails": [ ${string}, ... ],
        "push_enabled": ${boolean}
    },
    "suspended": ${boolean},
    "schedule": [ ${schedule_interval}, ... ],
    "extended_params": ${extended_params}, // optional. object specified for concrete rule type
    "auto_created": ${boolean} // optional
}
```

where

* **type** is one of pre-defined types of rules
    * **alarmcontrol** - Car alarm triggered
    * **antenna_disconnect** - GPS antenna cut
    * **autocontrol** - Autocontrol related rules
    * **backup_battery_low** - Backup built-in battery low
    * **battery_off** - External power cut
    * **bracelet** - Bracelet sensor
    * **call_button_pressed** - Call button pressed
    * **case_intrusion** - Case intrusion
    * **crash_alarm** - Car crash
    * **detach** - Tracker detach from the object
    * **door_alarm** - Door opening in alarm mode
    * **driver_assistance** - Warnings from driver-assistance systems (ADAS)
    * **driver_change** - Driver change
    * **driver_identification** - Driver identification
    * **g_sensor** - Shock sensor
    * **gps_lost_recover** - GNSS signal lost/recover
    * **gsm_damp** - GSM signal damp
    * **harsh_driving** - Harsh driving
    * **hood_alarm** - Hood opening in alarm mode
    * **idling** - Excessive engine idling
    * **ignition** - Ignition ON/OFF
    * **inoutzone** - Entrance or exit from geofence
    * **input_change** - Inputs triggering
    * **light_sensor** - Light sensor
    * **location_response** - Location report on demand
    * **locking_unlocking** - Lock is opened/closed
    * **lowpower** - Low built-in battery
    * **obd_plug_unplug** - Connecting/Disconnecting with vehicle through OBDII interface
    * **offline** - Tracker switched OFF or lost connection
    * **on_off** - Tracker switch ON/OFF
    * **output_change** - Outputs triggering
    * **parking** - Unauthorized movement
    * **poweron** - Tracker switched ON
    * **route** - Deviation from the route
    * **security_control** - Alarm mode ON/OFF
    * **sensor_range** - Parameter in range
    * **sos** - Alarm (SOS) button pressed
    * **speedup** - Speed exceeding
    * **strap_bolt** - Strap (bolt) is cut/inserted
    * **task_status_change** - Task status change
    * **track_change** - Parking state detection
    * **vibration** - Vibration sensor
    * **work_status_change** - Change of status
    * **fuel_level_leap** - Fuel level change
    * **idling_soft** - Engine excessive idling (software)
    * **fatigue_driving** - Fatigue driving detection
    * **check_engine_light** - Check Engine (MIL)
* **schedule_interval** is one of:
    * **weekly_schedule_interval**
    ```javascript
    {
        "type": "weekly",
        "from": ${weekday_time},
        "to": ${weekday_time},
        "interval_id": ${int}
    }
    ```
    * **fixed_schedule_interval**
    ```javascript
    {
        "type": "fixed",
        "from": ${date/time},
        "to": ${date/time},
        "interval_id": ${int}
    }
    ```
    where **weekday_time** is:
    ```javascript
    {
        "weekday": ${int}, // from 1 to 7
        "time": ${local_time} // for example: "01:00:00"
    }
    ```
* **param** for
    * **input_change** – input number
    * **output_change** – output number
    * **idling_soft** – time threshold, minutes
    * **offline** – time threshold, minutes
    * **speedup** – speed threshold, kmh
* **extended_params** for
    * **any rule** can include following fields
    ```javascript
    {
        "zone_limit_inverted": ${boolean}, // optional
        "emergency": ${boolean} // optional, default `false`
        "append_zone_title":  ${boolean} // optional, using only for a rule "inoutzone". Show or not a label of zone in a notification.
    }
    ```
    * **type**=”**autocontrol**”
    Map of subrules settings.
    ```javascript
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
    * **type**=”**driver_assistance**”
    ```json
    {
        "forward_collision_enable" : ${boolean}, // enable/disable notifications about forward collision warnings
        "headway_warning_enabled" :  ${boolean}, // notifications about headway warnings
        "lane_departure_enabled" : ${boolean} // notifications about lane departures
    }
    ```
    * **type**=”**fuel_level_leap**”
    ```json
    {
       "sensor_id": 123
    }
    ```
    * **type**=”**sensor_range**”
    ```json
    {
        "sensor_id": 123,
        "min": 1.0, // (double) optional. null means negative infinity
        "max": 3.0, // (double) optional. null means positive infinity
        "threshold": 0.03 // (double) optional
    }
    ```
    * **type**=”**route**”
    ```json
    {
       "allow_exit_at_endpoints": ${boolean} // optional, disable notifications for deviations at start and end points
    }
    ```
* **date/time** and **local_time** types are described at 
  the [data types description section](../../../getting-started.md#data-types).

## API actions

API base path: `/tracker/rule`

### bind
Bind rule with **rule_id** to trackers list.

**required subuser rights:** tracker_rule_update

#### parameters
* **rule_id** - **int**.
* **trackers** - **array of int**. ids of trackers. Trackers which do not exist, owned by other user or deleted ignored without errors.
* **tracker_id** - **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### response
```javascript
{ "success": true }
```

#### errors
*   201 (Not found in database) – if rule with **rule_id** does not exist or owned by other user

### create
Create rule and scheduled intervals.

**required subuser rights:** tracker_rule_update

#### parameters
* **rule** - [JSON object](#rule).

#### response
```javascript
{
    "success": true,
    "id": ${int} // id of created rule
}
```

#### errors
*   204 (Entity not found) – when associated zone is not exists

### delete
Delete rule with rule_id and all related objects from the database.

**required subuser rights:** tracker_rule_update

#### parameters
* **rule_id** - **int**.

#### response

```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if rule with **rule_id** does not exist or owned by other user

### list
List tracker rules binded to tracker with id=**tracker_id** or all user’s tracker rules if **tracker_id** not passed.

#### response

```json
{
   "success": true,
   "list": [ <rule>, ... ] // list of rules
}
```

### unbind
Unbind trackers from rule with **rule_id**.

**required subuser rights:** tracker_rule_update

#### parameters
* **rule_id** - **int**.
* **trackers** - **array of int**. ids of trackers. Trackers which do not exist, owned by other user or deleted ignored without errors.

#### response

```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if rule with **rule_id** does not exist or owned by other user

### update
Update rule and scheduled intervals.

**required subuser rights:** tracker_rule_update

#### parameters
* **rule** - [JSON object](#rule).

#### response

```json
{ "success": true }
```

#### errors
*   201 (Not found in database) – if rule is not exists or owned by other user
*   204 (Entity not found) – when new associated zone is not exists

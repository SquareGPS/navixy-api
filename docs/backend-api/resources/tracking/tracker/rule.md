---
title: Rule
description: Rule
---

# Rule

A rule element consists of following fields:

```json
{
    "id": 1,
    "name": "rule",
    "description": "description",
    "zone_ids": [12, 15],
    "trackers": [ 123456, 234567 ],
    "type": "alarmcontrol",
    "primary_text": "ON",
    "secondary_text": "OFF",
    "param": 1,
    "alerts": {
      "sms_phones": ["98829991"],
      "phones": ["98829991"],
      "emails": ["example@test.com"],
      "push_enabled": true
    },
    "suspended": false,
    "schedule": [{
      "type":"weekly",
      "from":{"weekday":1,"time":"00:00:00"},
      "to":{"weekday":7,"time":"23:59:59"}],
    "extended_params": {
      "alarmcontrol": {
      "enabled": true,
      "sms": false,
      "call": false,
      "email": true,
      "push": true,
      "always_notify": false
    },
    "auto_created": true
}
```

* `id` - int. An id of a rule.
* `name` - string. Name of a rule.
* `description` - string. Rule's description.
* `zone_ids` - array of int. List of geofence ids.
* `trackers` - array of int. List of binded tracker ids.
* `type` - enum. One of pre-defined types of rules. See types below.
* `primary_text` - string. Primary text of rule notification.
* `secondary_text` - string. Secondary text of rule notification.
* `param` - int. A common parameter. See below.
* `alerts` - object with destinations for notifications. 
    * `sms_phones` - array of string. Phones for SMS notifications.
    * `phones` - array of string. Phones for voice calls.
    * `emails` - array of string. Emails for notifications.
    * `push_enabled` - boolean. If true push notifications available.
* `suspended` - boolean. True if the rule suspended.
* `shedule` - optional. 
* `extended_params` - optional. An object specified for concrete rule type. See below.
* `auto_created` - optional, boolean. True means that the rule created automatically.

Where 

* **types**

    * **alarmcontrol** - Car alarm triggered.
    * **antenna_disconnect** - GPS antenna cut.
    * **autocontrol** - Autocontrol related rules.
    * **backup_battery_low** - Backup built-in battery low.
    * **battery_off** - External power cut.
    * **bracelet** - Bracelet sensor.
    * **call_button_pressed** - Call button pressed.
    * **case_intrusion** - Case intrusion.
    * **crash_alarm** - Car crash.
    * **detach** - Tracker detach from the object.
    * **door_alarm** - Door opening in alarm mode.
    * **driver_assistance** - Warnings from driver-assistance systems (ADAS).
    * **driver_change** - Driver change.
    * **driver_identification** - Driver identification.
    * **g_sensor** - Shock sensor.
    * **gps_lost_recover** - GNSS signal lost/recover.
    * **gsm_damp** - GSM signal damp.
    * **harsh_driving** - Harsh driving.
    * **hood_alarm** - Hood opening in alarm mode.
    * **idling** - Excessive engine idling.
    * **ignition** - Ignition ON/OFF.
    * **inoutzone** - Entrance or exit from geofence.
    * **input_change** - Inputs triggering.
    * **light_sensor** - Light sensor.
    * **location_response** - Location report on demand.
    * **locking_unlocking** - Lock opened/closed.
    * **lowpower** - Low built-in battery.
    * **obd_plug_unplug** - Connecting/Disconnecting with vehicle through OBDII interface.
    * **offline** - Tracker switched OFF or lost connection.
    * **on_off** - Tracker switch ON/OFF.
    * **output_change** - Outputs triggering.
    * **parking** - Unauthorized movement.
    * **poweron** - Tracker switched ON.
    * **route** - Deviation from the route.
    * **security_control** - Alarm mode ON/OFF.
    * **sensor_range** - Parameter in range.
    * **sos** - Alarm (SOS) button pressed.
    * **speedup** - Speed exceeding.
    * **strap_bolt** - Strap (bolt) is cut/inserted.
    * **task_status_change** - Task status change.
    * **track_change** - Parking state detection.
    * **vibration** - Vibration sensor.
    * **work_status_change** - Change of status.
    * **fuel_level_leap** - Fuel level change.
    * **idling_soft** - Engine excessive idling (software).
    * **fatigue_driving** - Fatigue driving detection.
    * **check_engine_light** - Check Engine (MIL).
    
* **schedule_interval** is one of:

    * **weekly_schedule_interval**
    
    ```json
    {
      "type": "weekly",
      "from": {weekday_time},
      "to": {weekday_time},
      "interval_id": 1
    }
    ```
    * **fixed_schedule_interval**
    
    ```json
    {
      "type": "fixed",
      "from": "2014-07-09 07:50:58",
      "to": "2014-07-10 07:50:58",
      "interval_id": 3
    }
    ```
  
    where **weekday_time** is:
    
    ```json
    {
        "weekday": 1, // from 1 to 7.
        "time": "01:00:00" // string.
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
    
    ```json
    {
        "zone_limit_inverted": {boolean}, // optional
        "emergency": ${boolean} // optional, default `false`
        "append_zone_title":  {boolean} // optional, using only for a rule "inoutzone". Show or not a label of zone in a notification.
    }
    ```
    * **type**=”**autocontrol**”
    Map of sub-rules settings.
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
    * **type**=”**driver_assistance**”
    ```json
    {
        "forward_collision_enable" : {boolean}, // enable/disable notifications about forward collision warnings
        "headway_warning_enabled" :  {boolean}, // notifications about headway warnings
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
       "allow_exit_at_endpoints": {boolean} // optional, disable notifications for deviations at start and end points
    }
    ```
* **date/time** and **local_time** types described at 
the [data types description section](../../../getting-started.md#data-types).

## API actions

API base path: `/tracker/rule`

### bind

Binds rule with **rule_id** to trackers list.

**required sub-user rights:** `tracker_rule_update`

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| rule_id | Id of a rule. | int | 10 |
| trackers | Ids of trackers. Trackers which do not exist, owned by other user or deleted ignored without errors. | `[999199, 999119]` |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/bind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": "123", "trackers":[265489]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/bind?hash=a6aa75587e5c59c32d347da438505fc3&rule_id=123&trackers=[265489]
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if rule with **rule_id** does not exist or owned by other user.

### create

Creates rule and scheduled intervals.

**required sub-user rights:** `tracker_rule_update`

#### parameters

* **rule** - [JSON object](#rule).

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"description":"","type":"work_status_change","primary_text":"status changed","secondary_text":"","alerts":{"push_enabled":true,"emails":["example@gmail.com"],"emergency":false,"sms_phones":["745494878945"],"phones":[]},"suspended":"","append_zone_title":"","name":"Status changing","trackers":[123456],"extended_params":{"emergency":false,"zone_limit_inverted":false,"status_ids":[319281,319282,319283]},"param":"","schedule":[{"from":{"weekday":1,"time":"00:00:00"},"to":{"weekday":7,"time":"23:59:59"},"type":"weekly"}],"zone_ids":[],"group_id":1}}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/create?hash=a6aa75587e5c59c32d347da438505fc3&rule={"description":"","type":"work_status_change","primary_text":"status changed","secondary_text":"","alerts":{"push_enabled":true,"emails":["example@gmail.com"],"emergency":false,"sms_phones":["745494878945"],"phones":[]},"suspended":"","append_zone_title":"","name":"Status changing","trackers":[123456],"extended_params":{"emergency":false,"zone_limit_inverted":false,"status_ids":[319281,319282,319283]},"param":"","schedule":[{"from":{"weekday":1,"time":"00:00:00"},"to":{"weekday":7,"time":"23:59:59"},"type":"weekly"}],"zone_ids":[],"group_id":1}
    ```

#### response

```json
{
    "success": true,
    "id": 123
}
```

* `id` - int. An id of created rule.

#### errors

* 204 (Entity not found) – when associated zone is not exists.

### delete

Deletes rule with rule_id and all related objects from the database.

**required sub-user rights:** `tracker_rule_update`

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| rule_id | Id of a rule. | int | 10 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": "123"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/delete?hash=a6aa75587e5c59c32d347da438505fc3&rule_id=123
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if rule with **rule_id** does not exist or owned by other user.

### list

List tracker rules binded to tracker with id=**tracker_id** or all users' tracker rules if **tracker_id** not passed.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
   "success": true,
   "list": [{rule}]
}
```

* `list` - list of rules

### unbind

Unbinds trackers from rule with `rule_id`.

**required sub-user rights:** `tracker_rule_update`

#### parameters

| name | description | type | format |
| :------ | :------ | :----- | :----- |
| rule_id | Id of a rule. | int | 10 |
| trackers | Ids of trackers. Trackers which do not exist, owned by other user or deleted ignored without errors. | `[999199, 999119]` |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/unbind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule_id": "123", "trackers":[265489]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/unbind?hash=a6aa75587e5c59c32d347da438505fc3&rule_id=123&trackers=[265489]
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if rule with `rule_id` does not exist or owned by other user.

### update

Updates rule and scheduled intervals.

**required sub-user rights:** `tracker_rule_update`

#### parameters

* **rule** - [JSON object](#rule).

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/rule/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "rule": {"description":"","type":"work_status_change","primary_text":"status changed","secondary_text":"","alerts":{"push_enabled":true,"emails":["example@gmail.com"],"emergency":false,"sms_phones":["745494878945"],"phones":[]},"suspended":"","append_zone_title":"","name":"Status changing","trackers":[123456],"extended_params":{"emergency":false,"zone_limit_inverted":false,"status_ids":[319281,319282,319283]},"param":"","schedule":[{"from":{"weekday":1,"time":"00:00:00"},"to":{"weekday":7,"time":"23:59:59"},"type":"weekly"}],"zone_ids":[],"group_id":1}}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/rule/update?hash=a6aa75587e5c59c32d347da438505fc3&rule={"description":"","type":"work_status_change","primary_text":"status changed","secondary_text":"","alerts":{"push_enabled":true,"emails":["example@gmail.com"],"emergency":false,"sms_phones":["745494878945"],"phones":[]},"suspended":"","append_zone_title":"","name":"Status changing","trackers":[123456],"extended_params":{"emergency":false,"zone_limit_inverted":false,"status_ids":[319281,319282,319283]},"param":"","schedule":[{"from":{"weekday":1,"time":"00:00:00"},"to":{"weekday":7,"time":"23:59:59"},"type":"weekly"}],"zone_ids":[],"group_id":1}
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 (Not found in the database) – if rule is not exists or owned by other user.
* 204 (Entity not found) – when new associated zone is not exists.

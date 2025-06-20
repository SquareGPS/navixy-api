---
title: About special settings
description: >-
  About special settings. Some trackers provide additional specific kind of
  control which is defined with `special_control` field of tracker model.
---

# About special settings

### About special settings

Some trackers provide additional specific kind of control which is defined with `special_control` field of tracker model.\
This field contains `type`, which identifies a certain kind of settings. (For example "pwr\_off\_key" or "sos\_key", which\
you can see below)`special_control` = "none" means that tracker doesn't have specific kind of control. In other cases you can:

* **read** special settings with [api/tracker/settings/special/read](index.md#read),
* **update** special settings with [api/tracker/settings/special/update](index.md#update),
* **perform special control** with [api/tracker/send\_command](../../index.md#send_command).

Such control assumes tracker special settings

### API actions

API base path: `/tracker/settings/special`.

#### read

Gets special settings for the specified tracker.

**Parameters**

| name        | description                                                                                      | type                               | format                       |
| ----------- | ------------------------------------------------------------------------------------------------ | ---------------------------------- | ---------------------------- |
| tracker\_id | ID of the tracker (aka "object\_id"). Tracker must belong to authorized user and not be blocked. | int                                | 123456                       |
| type        | Optional. Type of special object.                                                                | [enum](../../../../../#data-types) | "electronic\_lock\_password" |

**Examples**

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/tracker/settings/special/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
```
````

\=== "HTTP GET"

````
```
{{ extra.api_example_url }}/tracker/settings/special/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
```
````

**Responses**

If parameter type is present:

```json
{
  "success": true,
  "value": {
    "type": "electronic_lock_password",
    "password": "4567879",
    "remember_password": false
  }
}
```

* `value` - settings object.

If parameter type omitted:

```json
{
  "success": true,
  "list": [
    {
      "type": "electronic_lock_password",
      "password": "4567879",
      "remember_password": false
    }, {
      "type": "hhd_lock_password",
      "password": "25698545",
      "remember_password": true
    }
  ]
}
```

* `list` - array of objects. Settings object array.

**Settings object structures by type:**

**electronic\_lock\_password**

```json
{
  "type": "electronic_lock_password",
  "password": "password",
  "remember_password": false
}
```

* `password` - string. Nullable.

**hhd\_lock\_password**

```json
{
  "type": "hhd_lock_password",
  "password": "56894567",
  "remember_password": true
}
```

* `password` - string. Nullable. 8 digits.

**jointech\_lock\_password**

```json
{
  "type": "jointech_lock_password",
  "password": "d45s6w",
  "remember_password": false
}
```

* `password` - string. Nullable. 6 non-space, non-comma symbols.

**vg\_lock\_password**

```json
{
  "type": "vg_lock_password",
  "password": "123456",
  "remember_password": true
}
```

* `password` - string. Nullable. 6 digits.

**autofon\_sms\_alerts**

```json
{
  "type": "autofon_sms_alerts",
  "low_battery_mode": "enable",
  "ext_input_mode": "disable",
  "sos_button_mode": "enable"
}
```

* `low_battery_mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `ext_input_mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `sos_button_mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".

**auto\_geofence\_telfm**

```json
{
  "type": "auto_geofence_telfm",
  "mode": "enable",
  "activation_timeout": 300,
  "radius": 50
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `activation_timeout` - int. 0-65535 seconds.
* `radius` - int. 50 - 10000 meters.

**bce\_tacho\_control**

```json
{
  "type": "bce_tacho_control",
  "function": "slot1"
}
```

* `function` - [enum](../../../../../#data-types). Can be "slot1" | "slot2" | "vu\_activities" | "vu\_no\_activities"

**call\_button**

```json
{
  "type": "call_button",
  "capacity": 1,
  "items": [
    {
      "phone": "45641784111"
    }
  ]
}
```

* `items` - Array of phone numbers (10-15 digits) represented as strings.
  * `phone` - string. Phone number in the international format without "+" sign.

**call\_buttons\_v40**

```json
{
  "type": "call_buttons_v40",
  "capacity": 4,
  "items": [
    {
      "phone": "45641784111"
    }
  ]
}
```

* `items` - Array of phone numbers (10-15 digits) represented as strings.
  * `phone` - string. Phone number in the international format without "+" sign.

**careu\_psm**

```json
{
  "type": "careu_psm",
  "sleep_when_ignition_off": true,
  "sleep_when_no_motion": true,
  "sleep_when_no_communication": true,
  "sleep_conditions_duration": 1,
  "deep_sleep_conditions_duration": 300,
  "wake_up_interval": 30,
  "wake_up_from_dsm_interval": 2
}
```

* `sleep_when_ignition_off` - boolean.
* `sleep_when_no_motion` - boolean.
* `sleep_when_no_communication` - boolean.
* `sleep_conditions_duration` – int. Delay between the moment when conditions met and sleep mode activation in minutes. Can be 1-255.
* `deep_sleep_conditions_duration` – int. Delay between sleep mode activation and deep sleep mode activation in minutes. Can be 0-65535.
* `wake_up_interval` – int. Delay before waking up from sleep mode in minutes. Can be 0-65535.
* `wake_up_from_dsm_interval` – int. Delay before waking up from deep sleep mode in hours. Can be 0-255.
* `0` in these fields means don't switch.

**castel\_alarms**

```json
{
  "type": "castel_alarms",
  "acceleration": {
    "report": true,
    "beep": true,
    "threshold": 0.4
  },
  "deceleration": {
    "report": false,
    "beep": false,
    "threshold": 0.7
  },
  "crash": {
    "report": true,
    "beep": true,
    "threshold": 1.0
  },
  "sharp_turn": {
    "report": true,
    "beep": true,
    "threshold": 0.3
  }
}
```

* `report` - boolean. If `true` will send notification to server upon an event.
* `beep` - boolean. If `true` will sound upon an event.
* `threshold` - double. Normal values range where event does not occur. Each unit equals 1 g.
  * `acceleration` - 0.2 - 0.8.
  * `deceleration` - 0.3 - 1.0.
  * `crash` - 1.0 - 2.0.
  * `sharp_turn` - 0.3 - 0.9.

**castel\_obd**

```json
{
  "type": "castel_obd",
  "enable_pid_reports": true,
  "pid_data_records_per_message": 1,
  "pid_data_collect_interval": 30
}
```

* `enable_pid_reports` - boolean.
* `pid_data_records_per_message` - int. Count of records per one message. Can be 1 - 20.
* `pid_data_collect_interval` - int. Data collect interval in seconds. Can be 30 - 600.

**charging\_gmt100**

```json
{
  "type": "charging_gmt100",
  "mode": "on_need"
}
```

* `mode` - [enum](../../../../../#data-types). Can be "on\_need" | "ign\_on\_only" | "ign\_on" | "low\_charge".

**ddd\_emails**

```json
{
  "type": "ddd_emails",
  "emails": ["test@email.com", "example@email.com"]
}
```

* `emails` - string array. Valid emails. Maximum size 5.

**digital\_password**

```json
{
  "type": "digital_password",
  "password": "123456"
}
```

* `password` - string. 6 digits.

**fcc\_telfm**

```json
{
  "type": "fcc_telfm",
  "fuel_type": "gasoline",
  "engine_volume": 10.0,
  "multiplier": 0.0
}
```

* `fuel_type` - [enum](../../../../../#data-types). Can be "gasoline" | "diesel" | "lpg".
* `engine_volume` - double. Can be 0.0 - 10.0.
* `multiplier` - double. Can be 0.0 - 10.0.

**galileo\_tacho\_control**

```json
{
  "type": "galileo_tacho_control",
  "function": "download"
}
```

**galileo\_hds**

```json
{
  "type": "galileo_hds",
  "mode": "enable",
  "max_acceleration_force": 1.26,
  "max_braking_force": 1.59,
  "max_cornering_force": 0.75
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `max_acceleration_force` - double. It is a max allowed acceleration force which can be reached while accelerating without\
  triggering harsh acceleration event.Can be 0 - 2.55.
* `max_braking_force` - double. It is a max allowed braking force which can be reached while braking without triggering\
  harsh braking event. Can be 0 - 2.55.
* `max_cornering_force` - double. It is a max allowed cornering angle which can be reached while cornering without triggering\
  harsh cornering event. Can be 0 - 2.55.

**harsh\_behavior\_hua\_sheng**

```json
{
  "type": "harsh_behavior_hua_sheng",
  "mode": "enable",
  "max_acceleration_force": 1.0,
  "max_braking_force": 0.5,
  "max_cornering_force": 0.1
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `max_acceleration_force` - double. It is a max allowed acceleration force which can be reached while accelerating without\
  triggering harsh acceleration event.Can be 0.1 - 1.0.
* `max_braking_force` - double. It is a max allowed braking force which can be reached while braking without triggering\
  harsh braking event. Can be 0.1 - 1.0.
* `max_cornering_force` - double. It is a max allowed cornering angle which can be reached while cornering without triggering\
  harsh cornering event. Can be 0.1 - 1.0.

**hbm\_telfm**

```json
{
  "type": "hbm_telfm",
  "mode": "enable",
  "max_acceleration_force": 0.3,
  "max_braking_force": 0.85,
  "max_angular_velocity": 0.1
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `max_acceleration_force` - double. It is a max allowed acceleration force which can be reached while accelerating without\
  triggering harsh acceleration event. Can be 0.25 - 0.85 g.
* `max_braking_force` - double. It is a max allowed braking force which can be reached while braking without triggering\
  harsh braking event. Can be 0.25 - 0.85 g.
* `max_cornering_force` - double. It is a max allowed cornering angle which can be reached while cornering without triggering\
  harsh cornering event. Can be 0.1 - 1.0 rad/s.

**hbm\_telfm5x**

```json
{
  "type": "hbm_telfm5x",
  "mode": "enable",
  "max_acceleration_force": 0.5,
  "max_braking_force": 3.0,
  "max_angular_velocity": 10.0
}
```

* `max_acceleration_force` – double. It is a max allowed acceleration force which can be reached while accelerating without\
  triggering harsh acceleration event. Can be 0.5 - 10.0 g.
* `max_braking_force` – double. It is a max allowed braking force which can be reached while braking without triggering\
  harsh braking event. Can be 0.5 - 10.0 g.
* `max_angular_velocity` – double. It is a max allowed cornering angle which can be reached while cornering without triggering\
  harsh cornering event. Can be 0.5 - 10.0 rad/s.

**hbm\_ql**

```json
{
  "type": "hbm_ql",
  "mode": "enable",
  "high_speed": 100,
  "high_speed_braking_delta": 50,
  "high_speed_acceleration_delta": 50,
  "medium_speed": 70,
  "medium_speed_braking_delta": 50,
  "medium_speed_acceleration_delta": 50,
  "low_speed_braking_delta": 50,
  "low_speed_acceleration_delta": 50
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `high_speed` - int. Can be 100 - 400.
* `high_speed_braking_delta` - int. Can be 0 - 100.
* `high_speed_acceleration_delta` - int. Can be 0 - 100.
* `medium_speed` - int. Can be 60 - 100.
* `medium_speed_braking_delta` - int. Can be 0 - 100.
* `medium_speed_acceleration_delta` - int. Can be 0 - 100.
* `low_speed_braking_delta` - int. Can be 0 - 100.
* `low_speed_acceleration_delta` - int. Can be 0 - 100.

**hbm\_ms\_ql**

```json
{
  "type": "hbm_ms_ql",
  "mode": "gps_only",
  "high_speed": 100,
  "high_speed_braking_delta": 50,
  "high_speed_acceleration_delta": 50,
  "medium_speed": 60,
  "medium_speed_braking_delta": 50,
  "medium_speed_acceleration_delta": 50,
  "low_speed_braking_delta": 50,
  "low_speed_acceleration_delta": 50,
  "turn_brake_threshold": 30,
  "turn_brake_duration": 320,
  "acceleration_threshold": 15,
  "acceleration_duration": 1200
}
```

* `mode` - [enum](../../../../../#data-types). Can be "disable" | "gps\_only" | "motion\_sensor\_only" | "gps\_and\_motion\_sensor".
* `high_speed` - int. Can be 100 - 400.
* `high_speed_braking_delta` - int. Can be 0 - 100.
* `high_speed_acceleration_delta` - int. Can be 0 - 100.
* `medium_speed` - int. Can be 60 - 100.
* `medium_speed_braking_delta` - int. Can be 0 - 100.
* `medium_speed_acceleration_delta` - int. Can be 0 - 100.
* `low_speed_braking_delta` - int. Can be 0 - 100.
* `low_speed_acceleration_delta` - int. Can be 0 - 100.
* `turn_brake_threshold` - int. Can be 30 - 70.
* `turn_brake_duration` - int. Can be 320 - 800 milliseconds.
* `acceleration_threshold` - int. Can be 15 - 50.
* `acceleration_duration` - int. Can be 400 - 2000 milliseconds.

**harsh\_behavior\_bce**

```json
{
  "type": "harsh_behavior_bce",
  "is_switched_off": false,
  "acceleration_limit": 0.04,
  "braking_limit": 1.21,
  "cornering_limit": 2.38
}
```

* `is_switched_off` - boolean.
* `acceleration_limit` - double. Can be 0.04 - 3.
* `braking_limit` - double. Can be 0.04 - 3.
* `cornering_limit` - double. Can be 0.04 - 3.

**harsh\_behavior\_concox\_x1**

```json
{
  "type": "harsh_behavior_concox_x1",
  "acc_speed": 40,
  "acc_detection_time": 4,
  "braking_speed": 60,
  "braking_detection_time": 2
}
```

* `acc_speed` - int. Can be 0 - 100.
* `acc_detection_time` - int. Can be 0 - 10.
* `braking_speed` - int. Can be 0 - 100.
* `braking_detection_time` - int. Can be 0 - 10.

**harsh\_behavior\_tramigo**

```json
{
  "type": "harsh_behavior_tramigo",
  "mode": "enable",
  "max_acceleration_force": 0.5,
  "max_braking_force": 1.3
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `max_acceleration_force` - double. Can be 0.1 - 8.
* `max_braking_force` - double. Can be 0.1 - 8.

**harsh\_behavior\_ruptela**

```json
{
  "type": "harsh_behavior_ruptela",
  "braking_limit": 30,
  "acceleration_limit": 60
}
```

* `braking_limit` - int. Can be 0 - 100.
* `acceleration_limit` - int. Can be 0 - 100.

**nimbelink\_accel**

```json
{
  "type": "nimbelink_accel",
  "mode": "enable",
  "x": 1.12,
  "y": 0.8,
  "z": 2.33
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `x` - double. Can be 0 - 2.55.
* `y` - double. Can be 0 - 2.55.
* `z` - double. Can be 0 - 2.55.

**hua\_sheng\_vibration\_sensitivity**

```json
{
  "type": "hua_sheng_vibration_sensitivity",
  "sensitivity": "easy"
}
```

* `sensitivity` - [enum](../../../../../#data-types). Can be "easy" | "normal" | "hard" | "hardest".

**ign\_ruptela**

For Ruptela devices. Represents configuration parameters related to ignition detection ("Engine detection" and "Custom ignition", as Ruptela documentation calls them).

[JSON-schema](https://json-schema.org):

```
{
  "$schema" : "http://json-schema.org/draft-07/schema#",
  "type" : "object",
  "properties" : {
    "mode" : {
      "$ref" : "ruptela_ignition_mode.json"
    },
    "use_voltage" : {
      "type" : [ "boolean", "null" ]
    },
    "voltage" : {
      "type" : [ "number", "null" ]
    }
  },
  "required" : [ "mode" ],
   "$id" : "ruptela-ignition.json"
}

{
  "$schema" : "http://json-schema.org/draft-07/schema#",
  "type" : "string",
  "enum" : [ "always_on", "din", "movement_sensor", "custom" ],
  "$id" : "ruptela_ignition_mode.json"
}
```

**ign\_src\_suntech**

```json
{
  "type": "ign_src_suntech",
  "mode": "power_voltage",
  "power_voltage_low_level": 12000,
  "power_voltage_high_level": 19000
}
```

* `mode` - [enum](../../../../../#data-types). Can be "power\_voltage" | "din1" | "movement".
* `power_voltage_low_level` - int. Can be 0 - 30000.
* `power_voltage_high_level` - int. Can be 0 - 30000.

**ign\_src\_telfm**

```json
{
  "type": "ign_src_telfm",
  "mode": "power_voltage",
  "power_voltage_low_level": 12000,
  "power_voltage_high_level": 24000
}
```

* `mode` - [enum](../../../../../#data-types). Can be "power\_voltage" | "din1" | "movement".
* `power_voltage_low_level` - int. Can be 0 - 30000.
* `power_voltage_high_level` - int. Can be 0 - 30000.

**locus\_sec**

```json
{
  "type": "locus_sec",
  "signature": "signature",
  "sms_password": "23145",
  "reset": false
}
```

* `signature` - string. Length 1 - 32.
* `sms_password` - string. Length 1 - 32.
* `reset` - boolean.

**phonebook\_gt300**

```json
{
  "type": "phonebook_gt300",
  "capacity": 20,
  "items": [
    {
      "name": "Karl",
      "phone": "555469874"
    }
  ]
}
```

* `items` - array of contacts.
  * `name` - string. Contact name.
  * `phone` - string. Phone number in the international format without "+" sign.

**phonebook\_pt100**

```json
{
  "type": "phonebook_pt100",
  "capacity": 3,
  "items": [
    {
      "name": "Karl",
      "phone": "555469874"
    }
  ]
}
```

* `items` - array of contacts.
  * `name` - string. Contact name.
  * `phone` - string. Phone number in the international format without "+" sign.

**pwr\_off\_key**

```json
{
  "type": "pwr_off_key",
  "mode": "enable"
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".

**scat\_mayak\_bt\_control**

```json
{
  "type": "scat_mayak_bt_control",
  "function": "bt_disable",
  "bt_state": true
}
```

* `function` - [enum](../../../../../#data-types). Can be "bt\_disable" | "bt\_enable" | "bt\_clear" | "bt\_write".
* `bt_state` - boolean.

**sos\_key**

```json
{
  "type": "sos_key",
  "mode": "report",
  "phone": "55548875236"
}
```

* `mode` - [enum](../../../../../#data-types). Can be "report" | "call\_report".
* `phone` - string. SOS phone to call. Phone number in the international format without "+" sign.

**starcom\_impact**

```json
{
  "type": "starcom_impact",
  "strong_duration": 12,
  "strong_force": 4,
  "strong_impact_enabled": true,
  "weak_duration": 9,
  "weak_force": 6,
  "weak_impact_enabled": true
}
```

* `strong_duration` - int. Required impact duration to trigger strong impact event. Each unit equals 2.5 milliseconds.\
  Can be 0 - 14.
* `strong_force` - int. Required impact force triggering strong impact event. Each unit equals about 1.1g. Can be 1 - 7.
* `strong_impact_enabled` - boolean.
* `weak_duration` - int. Required impact duration to trigger weak impact event. Each unit equals 2.5 milliseconds.\
  Can be 0 - 14.
* `weak_force` - int. Required impact force triggering weak impact event. Each unit equals about 1.1g. Can be 1 - 7.
* `weak_impact_enabled` - boolean.

**tacho\_company\_card**

```json
{
  "type": "tacho_company_card",
  "company_card_number": "A2332BF23EC3245A"
}
```

* `company_card_number` - string. 16 HEX digits (0-9A-F).

**tacho\_remote\_download**

```json
{
  "type": "tacho_remote_download",
  "company_card_number": "A2332BF23EC3245A",
  "vu_download_interval": 10,
  "card_download_interval": 2
}
```

* `company_card_number` - string. 16 HEX digits (0-9A-F).
* `vu_download_interval` - int. Min = 0.
* `card_download_interval` - int. Min = 0.

**teltonika\_tacho\_request**

```json
{
  "type": "teltonika_tacho_request",
  "data_type": "activities",
  "activities_start_time": "2020-09-01",
  "activities_end_time": "2020-09-16"
}
```

* `data_type` - [enum](../../../../../#data-types). Can be "overview" | "activities" | "eventsAndFaults" | "detailedSpeed" | "technicalData" |\
  "card1Download" | "card2Download".
* `activities_start_time` - string date. Format = "YYYY-MM-DD", not null only if data\_type = "activities".
* `activities_end_time` - string date. Format = "YYYY-MM-DD", not null only if data\_type = "activities".

**temporary\_digital\_password**

```json
{
  "type": "temporary_digital_password",
  "password": "231578",
  "duration_in_min": 17
}
```

* `password` - string. 6 digits.
* `duration_in_min` - int. Can be 10 - 255.

**time\_shift**

```json
{
  "type": "time_shift",
  "offset": 3.0
}
```

* `offset` - double. Can be -24.0 - 24.0 hours.

**tow\_detection\_ql**

```json
{
  "type": "tow_detection_ql",
  "mode": "enable",
  "engine_off_to_tow": 300,
  "fake_tow_delay": 300,
  "tow_interval": 12000,
  "rest_duration": 90,
  "motion_duration": 8300,
  "motion_threshold": 3
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `engine_off_to_tow` - int. A time parameter to judge whether the device considered towed after the engine off.\
  If the motion sensor doesn't detect stillness within the specified time after the engine off the device is being towed.\
  Can be 0 - 900 seconds.
* `fake_tow_delay` - int. After the engine off and stillness detected, if motion sensor detects moving again, the\
  device turns into a state called fake tow. If the device keeps in fake tow after a period defined by this parameter,\
  it is considered towed. Can be 0 - 600 seconds.
* `tow_interval` - int. The period to send alarm messages. Can be 0 - 86400 seconds.
* `rest_duration` - int. A time parameter to make sure the device enters stillness status, i.e. the status of the\
  device will be changed to stillness if the motion sensor detects stillness and maintains for a period defined by\
  this parameter. Can be 0 - 3825 seconds, step 15.
* `motion_duration` - int. A time parameter to make sure the device enters motion status. Can be 0 - 9900 milliseconds,\
  step 100.
* `motion_threshold` - int. The threshold for the motion sensor to measure whether the device is moving. Can be 2 - 9.

**tow\_detection\_ql2**

```json
{
  "type": "tow_detection_ql2",
  "mode": "enable",
  "engine_off_to_tow": 300,
  "fake_tow_delay": 300,
  "tow_interval": 12000,
  "rest_duration": 90,
  "motion_duration": 400,
  "motion_threshold": 3
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `engine_off_to_tow` - int. A time parameter to judge whether the device considered towed after the engine off.\
  If the motion sensor doesn't detect stillness within the specified time after the engine off the device is being towed.\
  Can be 0 - 900 seconds.
* `fake_tow_delay` - int. After the engine off and stillness detected, if motion sensor detects moving again, the\
  device turns into a state called fake tow. If the device keeps in fake tow after a period defined by this parameter,\
  it is considered towed. Can be 0 - 600 seconds.
* `tow_interval` - int. The period to send alarm messages. Can be 0 - 86400 seconds.
* `rest_duration` - int. A time parameter to make sure the device enters stillness status, i.e. the status of the\
  device will be changed to stillness if the motion sensor detects stillness and maintains for a period defined by this\
  parameter. Can be 0 - 3825 seconds, step 15.
* `motion_duration` - int. A time parameter to make sure the device enters motion status. Can be 100 - 1000\
  milliseconds, step 100.
* `motion_threshold` - int. The threshold for the motion sensor to measure whether the device is moving. Can be 2 - 9.

**tow\_detection\_telfm**

```json
{
  "type": "tow_detection_telfm",
  "mode": "enable",
  "activation_timeout": 5,
  "threshold": 0.30
}
```

* `mode` - [enum](../../../../../#data-types). Can be "enable" | "disable".
* `activation_timeout` - int. Can be 0 - 65535 minutes.
* `threshold` - double. Can be 0.10 - 5.00.

**video\_stream\_howen**

```json
{
  "type": "video_stream_howen"
}
```

**virtual\_ign\_ql**

```json
{
  "type": "virtual_ign_ql",
  "mode": "motion_sensor",
  "ign_on_voltage": 12000,
  "rest_duration_to_off": 120,
  "motion_duration_to_on": 75
}
```

* `mode` - [enum](../../../../../#data-types). Can be "disabled" | "power\_voltage" | "motion\_sensor".
* `ign_on_voltage` - int. Can be 250 - 28000.
* `rest_duration_to_off` – int. A time parameter to make sure the device enters stillness status, i.e. the status of\
  the device will be changed to stillness if the motion sensor detects stillness and maintains for a period of time\
  defined by this parameter. Can be 1 - 255.
* `motion_duration_to_on` – A time parameter to make sure the device enters motion status. Can be 1 - 255.

**no\_movement\_alarm**

```json
{
  "type": "no_movement_alarm",
  "enabled": true,
  "timeout": 300,
  "pre_alarm_duration": 120
}
```

* `timeout` - int. Can be 30 - 65500. A time parameter when the device doesn't move.
* `pre_alarm_duration` - int. Can be 0 - 65500. A time parameter when the device continues not to move after timeout.

**Errors**

* 201 – Not found in the database (if there is no tracker with such ID belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 214 – Requested operation or parameters are not supported by the device.

#### update

Sets special settings for a specified tracker with the new one.

**required sub-user rights:** `tracker_configure`.

**Parameters**

| name        | description                                                                                      | type        |
| ----------- | ------------------------------------------------------------------------------------------------ | ----------- |
| tracker\_id | ID of the tracker (aka "object\_id"). Tracker must belong to authorized user and not be blocked. | int         |
| value       | Settings object, see above.                                                                      | JSON object |

**Examples**

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/tracker/settings/special/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "value": {"type": "time_shift", "offset": 3.0}}'
```
````

**Response**

```json
{
  "success": true
}
```

**Errors**

* 201 – Not found in the database - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 214 – Requested operation or parameters are not supported by the device.

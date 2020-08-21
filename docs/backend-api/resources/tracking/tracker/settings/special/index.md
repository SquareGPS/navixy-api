---
title: About special settings
description: About special settings
---

## About special settings
Some trackers provides additional specific kind of control which is defined with "special_control" field of tracker model.
This field contains "type", which identifies certain kind of settings. (For example "pwr_off_key" or "sos_key", which you can see below)
"special_control" = "none" means that tracker have no specific kind of control. In other cases you can:

*  **read** special settings with [api/tracker/settings/special/read](#read),
*  **update** special settings with [api/tracker/settings/special/update](#update),
*  **perform special control** with [api/tracker/send_command](../../index.md#send_command).

Such control assumes

Tracker special settings

## API actions

API base path: `/tracker/settings/special`

### read
Get special settings for the specified tracker.

If parameter type is present:

#### response
```json5
{
    "success": true,
    "value": <settings object> //[Settings object]
}
```
If parameter type is omitted:

#### response
```json5
{
    "success": true,
    "list": [<settings object>] //[Settings objects array]
}
```

###### Settings object structures by type:

**electronic_lock_password**
```json5
{
    "type": "electronic_lock_password",
    "password": <string, nullable>,
    "remember_password": <boolean>
}
```

**hhd_lock_password**
```json5
{
    "type": "hhd_lock_password",
    "password": <string, nullable>, // 8 digits
    "remember_password": <boolean>
}
```

**jointech_lock_password**
```json5
{
    "type": "jointech_lock_password",
    "password": <string, nullable>, // 6 non-space, non-comma symbols
    "remember_password": <boolean>
}
```

**vg_lock_password**
```json5
{
    "type": "vg_lock_password",
    "password": <string, nullable>, // 6 digits
    "remember_password": <boolean>
}
```



**autofon_sms_alerts**
```json5
{
    "type": "autofon_sms_alerts",
    "low_battery_mode": <string, enable | disable>,
    "ext_input_mode": <string, enable | disable>,
    "sos_button_mode": <string, enable | disable>
}
```

**auto_geofence_telfm**
```json5
{
    "type": "auto_geofence_telfm",
    "mode": <string, enable | disable>,
    "activation_timeout": <int, 0 - 65535>, // seconds
    "radius": <int, 50 - 10000> // meters
}
```

**bce_tacho_control**
```json5
{
    "type": "bce_tacho_control",
    "function": <string, slot1 | slot2 | vu_activities | vu_no_activities>,
}
```

**call_button**
```json5
{
    "type": "call_button",
    "capacity": 1,
    "items": [{ "phone": <string> }]
}
```

**call_buttons_v40**
```json5
{
    "type": "call_buttons_v40",
    "capacity": 4,
    "items": [{ "phone": <string> }]
}
```

**careu_psm**
```json5
{
    "type": "careu_psm",
    "sleep_when_ignition_off": <boolean>,
    "sleep_when_no_motion": <boolean>,
    "sleep_when_no_communication": <boolean>,
    "sleep_conditions_duration": <int, 1-255>,
    "deep_sleep_conditions_duration": <int, 0-65535>,
    "wake_up_interval": <int, 0-65535>,
    "wake_up_from_dsm_interval": <int, 0-255> 
}
```

- `sleep_conditions_duration` – delay between the moment when conditions are met and sleep mode activation in minutes.
- `deep_sleep_conditions_duration` – delay between sleep mode activation and deep sleep mode activation in minutes.
- `wake_up_interval` – delay before waking up from sleep mode in minutes.
- `wake_up_from_dsm_interval` – delay before waking up from deep sleep mode in hours.

`0` in these fields means don't switch.

**castel_alarms**

```json5
{
    "type": "castel_alarms",
    "acceleration": {
        "report": <boolean>,
        "beep": <boolean>,
        "threshold": <double, 0.2 - 0.8>
    },
    "deceleration": {
        "report": <boolean>, 
        "beep": <boolean>, 
        "threshold": <double, 0.3 - 1.0>
    },
    "crash": {
        "report": <boolean>, 
        "beep": <boolean>, 
        "threshold": <double, 1.0 - 2.0> 
    },
    "sharp_turn": {
        "report": <boolean>, 
        "beep": <boolean>, 
        "threshold": <double, 0.3 - 0.9>
    }
}
```

- `report` - if true will send notification to server upon event
- `beep` - if true will sound upon event
- `threshold` - normal values range where event does not occur. Each unit equals 1 g.

**castel_obd**

```json5
{
    "type": "castel_obd",
    "enable_pid_reports": <boolean>,
    "pid_data_records_per_message": <int, 1 - 20>
    "pid_data_collect_interval": <int, 30 - 600> // seconds
}
```

**charging_gmt100**

```json5
{
    "type": "charging_gmt100",
    "mode": <string, on_need | ign_on_only | ign_on_|_low_charge>
}
```

**ddd_emails**

```json5
{
    "type": "ddd_emails",
    "emails": <array of strings, valid emails, max size 5>
}
```

**digital_password**

```json5
{
    "type": "digital_password",
    "password": <string> // 6 digits
}
```

**fcc_telfm**

```json5
{
    "type": "fcc_telfm",
    "fuel_type": <string, gasoline | diesel | lpg>,
    "engine_volume": <double, 0.0 - 10.0>,
    "multiplier": <double, 0.0 - 10.0>
}
```

**galileo_tacho_control**
```json5
{
    "type": "galileo_tacho_control",
    "function": "download"
}
```



**galileo_hds**
```json5
{
    "type": "galileo_hds",
    "mode": <string, disable | enable>,
    "max_acceleration_force": <double, 0 - 2.55>,
    "max_braking_force": <double, 0 - 2.55>,
    "max_cornering_force": <double, 0 - 2.55>
}
```

**harsh_behavior_hua_sheng**
```json5
{
    "type": "harsh_behavior_hua_sheng",
    "mode": <string, disable | enable>,
    "max_acceleration_force": <double, 0.1 - 1>,
    "max_braking_force": <double, 0.1 - 1>,
    "max_cornering_force": <double, 0.1 - 1>
}
```

**hbm_telfm**
```json5
{
    "type": "hbm_telfm",
    "mode": <string, disable | enable>,
    "max_acceleration_force": <double, 0.25-0.85>, //g
    "max_braking_force": <double, 0.25-0.85>, //g
    "max_angular_velocity": <double, 0.1-1.0> //rad/s
}
```

**hbm_telfm5x**
```json5
{
    "type": "hbm_telfm5x",
    "mode": <string, disable | enable>,
    "max_acceleration_force": <double, 0.5-10>, //g
    "max_braking_force": <double, 0.5-10>, //g
    "max_angular_velocity": <double, 0.5-10> //rad/s
}
```

- `max_acceleration_force` – It is max allowed acceleration force which can be reached while accelerating without
  triggering harsh acceleration event.
- `max_braking_force` – It is max allowed braking force which can be reached while braking without triggering
  harsh braking event.
- `max_angular_velocity` – It is max allowed cornering angle which can be reached while cornering without triggering
  harsh cornering event.

**hbm_ql**
```json5
{
    "type": "hbm_ql",
    "mode": <string, disable | enable>,
    "high_speed": <int, 100 - 400>,
    "high_speed_braking_delta": <int, 0 - 100>,
    "high_speed_acceleration_delta": <int, 0 - 100>,
    "medium_speed": <int, 60 - 100>,
    "medium_speed_braking_delta": <int, 0 - 100>,
    "medium_speed_acceleration_delta": <int, 0 - 100>,
    "low_speed_braking_delta": <int, 0 - 100>,
    "low_speed_acceleration_delta": <int, 0 - 100>
}
```

**hbm_ms_ql**
```json5
{
    "type": "hbm_ms_ql",
    "mode": <string, disable | gps_only | motion_sensor_only | gps_and_motion_sensor>,
    "high_speed": <int, 100 - 400>,
    "high_speed_braking_delta": <int, 0 - 100>,
    "high_speed_acceleration_delta": <int, 0 - 100>,
    "medium_speed": <int, 60 - 100>,
    "medium_speed_braking_delta": <int, 0 - 100>,
    "medium_speed_acceleration_delta": <int, 0 - 100>,
    "low_speed_braking_delta": <int, 0 - 100>,
    "low_speed_acceleration_delta": <int, 0 - 100>,
    "turn_brake_threshold": <int, 30 - 70>,
    "turn_brake_duration": <int, 320 - 800>, //milliseconds
    "acceleration_threshold": <int, 15 - 50>,
    "acceleration_duration": <int, 400 - 2000> //milliseconds

}
```

**harsh_behavior_bce**
```json5
{
    "type": "harsh_behavior_bce",
    "is_switched_off": <boolean>,
    "acceleration_limit": <double, 0.04 - 3>,
    "braking_limit": <double, 0.04 - 3>,
    "cornering_limit": <double, 0.04 - 3>
}
```

**harsh_behavior_concox_x1**
```json5
{
    "type": "harsh_behavior_concox_x1",
    "acc_speed": <int, 0 - 100>,
    "acc_detection_time": <int, 0 - 10>,
    "braking_speed": <int, 0 - 100>,
    "braking_detection_time": <int, 0 - 10>
}
```

**harsh_behavior_tramigo**
```json5
{
    "type": "harsh_behavior_tramigo",
    "mode": <string, disable | enable>,
    "max_acceleration_force": <double, 0.1-8>,
    "max_braking_force": <double, 0.1-8>
}
```

**harsh_behavior_ruptela**
```json5
{
    "type": "harsh_behavior_ruptela",
    "braking_limit": <int, 0 - 100>,
    "acceleration_limit": <int, 0 - 100>
}
```

**nimbelink_accel**
```json5
{
    "type": "nimbelink_accel",
    "mode": <string, disable | enable>,
    "x": <double, 0 - 2.55>,
    "y": <double, 0 - 2.55>,
    "z": <double, 0 - 2.55>
}
```



**hua_sheng_vibration_sensitivity**
```json5
{
    "type": "hua_sheng_vibration_sensitivity",
    "sensitivity": <string, easy | normal | hard | hardest>
}
```

**ign_src_suntech**
```json5
{
    "type": "ign_src_suntech",
    "mode": <string, power_voltage | din1 | movement>,
    "power_voltage_low_level": <int, 0 - 30000>,
    "power_voltage_high_level": <int, 0 - 30000>
}
```

**ign_src_telfm**
```json5
{
    "type": "ign_src_telfm",
    "mode": <string, power_voltage | din1 | movement>,
    "power_voltage_low_level": <int, 0 - 30000>,
    "power_voltage_high_level": <int, 0 - 30000>
}
```

**locus_sec**
```json5
{
    "type": "locus_sec",
    "signature": <string, length = 1 - 32>,
    "sms_password": <string, length = 1 - 32>,
    "reset": <boolean>
}
```

**phonebook_gt300**
```json5
{
    "type": "phonebook_gt300",
    "capacity": 20,
    "items": [{ "name": <string>, "phone": <string> }]
}
```

**phonebook_pt100**
```json5
{
    "type": "phonebook_pt100",
    "capacity": 3,
    "items": [{ "name": <string>, "phone": <string> }]
}
```

**pwr_off_key**
```json5
{
    "type": "pwr_off_key",
    "mode": <string, enable | disable>
}
```

**scat_mayak_bt_control**
```json5
{
    "type": "scat_mayak_bt_control",
    "function": <string, bt_disable | bt_enable | bt_clear | bt_write>,
    "bt_state": <boolean>
}
```

**sos_key**
```json5
{
    "type": "sos_key",
    "mode": <string, report | call_report>,
    "phone": <string> // SOS phone to call
}
```

**starcom_impact**
```json5
{
    "type": "starcom_impact",
    "strong_duration": <int, 0 - 14>,
    "strong_force": <int, 1 - 7>,
    "strong_impact_enabled": <boolean>,
    "weak_duration": <int, 0 - 14>,
    "weak_force": <int, 1 - 7>,
    "weak_impact_enabled": <boolean>
}
```
- `strong_duration` - required impact duration to trigger strong impact event. Each unit equals 2.5 milliseconds.
- `strong_force` - required impact force to trigger strong impact event. Each unit equals about 1.1g.
- `weak_duration` - required impact duration to trigger weak impact event. Each unit equals 2.5 milliseconds.
- `weak_force` - required impact force to trigger weak impact event. Each unit equals about 1.1g. 

**tacho_company_card**
```json5
{
    "type": "tacho_company_card",
    "company_card_number": <string> // 16 HEX digits (0-9A-F)
}
```

**tacho_remote_download**
```json5
{
    "type": "tacho_remote_download",
    "company_card_number": <string>, // 16 HEX digits (0-9A-F)
    "vu_download_interval": <int, min = 0>,
    "card_download_interval": <int, min = 0>
}
```

**teltonika_tacho_request**
```json5
{
    "type": "teltonika_tacho_request",
    "data_type": <string, overview | activities | eventsAndFaults | detailedSpeed | technicalData | card1Download | card2Download>,
    "activities_start_time": <date, format = "YYYY-MM-DD", not null only if data_type = "activities">,
    "activities_end_time": <date, format = "YYYY-MM-DD", not null only if data_type = "activities">
}
```

**temporary_digital_password**
```json5
{
    "type": "temporary_digital_password",
    "password": <string>, // 6 digits
    "duration_in_min": <int, 10 - 255>
}
```

**time_shift**
```json5
{
    "type": "time_shift",
    "offset": <double, -24.0 - 24.0> //hours
}
```

**tow_detection_ql**
```json5
{
    "type": "tow_detection_ql",
    "mode": <string, disable | enable>,
    "engine_off_to_tow": <int, 0 - 900>, //seconds
    "fake_tow_delay": <int, 0 - 600>, //seconds
    "tow_interval": <int, 30 - 86400> //seconds
    "rest_duration": <int, 15 - 3825>, //seconds, step 15
    "motion_duration": <int, 100 - 9900>, //milliseconds, step 100
    "motion_threshold": <int, 2 - 9>
}
```

**tow_detection_ql2**
```json5
{
    "type": "tow_detection_ql2",
    "mode": <string, disable | enable>,
    "engine_off_to_tow": <int, 300 - 900>, //seconds
    "fake_tow_delay": <int, 0 - 600>, //seconds
    "tow_interval": <int, 30 - 86400> //seconds
    "rest_duration": <int, 15 - 3825>, //seconds, step 15
    "motion_duration": <int, 100 - 1000>, //milliseconds, step 100
    "motion_threshold": <int, 2 - 9>
}
```

**tow_detection_telfm**
```json5
{
    "type": "tow_detection_telfm",
    "mode": <string, disable | enable>,
    "activation_timeout": <int, 0 - 65535>, //minutes
    "threshold": <double, 0.10 - 5.00>
}
```

**video_stream_howen**
```json5
{
    "type": "video_stream_howen"
}
```

**virtual_ign_ql**
```json5
{
    "type": "virtual_ign_ql",
    "mode": <string, disabled | power_voltage | motion_sensor>,
    "ign_on_voltage": <int, 250 - 28000>,
    "rest_duration_to_off": <int, 1 - 255>,
    "motion_duration_to_on": <int, 1 - 255>,
}
```

- `engine_off_to_tow` – A time parameter to judge whether the device is considered towed after the engine off. If the motion sensor doesn’t detect stillness within the specified time after engine off the device is being towed.
- `fake_tow_delay` – After engine off and stillness detected, if motion sensor detects moving again, the device turns into a state called fake tow. If the device keeps in fake tow after a period of time defined by this parameter, it is considered towed.
- `tow_interval` – The period to send alarm messages.
- `rest_duration` – A time parameter to make sure that the device enters stillness status, i.e. the status of the device will be changed to stillness if the motion sensor detects stillness and maintains for a period of time defined by this parameter.
- `motion_duration` – A time parameter to make sure that the device enters motion status.
- `motion_threshold` – The threshold for the motion sensor to measure whether the device is moving.

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device

### update
Set special settings for a specified tracker with the new one.

**required subuser rights:** tracker_configure

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **value** - **JSON object**. Settings object, see above

#### response

```json5
{ "success": true }
```

#### errors
*   201 – Not found in database (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   214 – Requested operation or parameters are not supported by the device


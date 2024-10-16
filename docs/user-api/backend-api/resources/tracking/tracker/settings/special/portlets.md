---
title: Specific portlets
description: Specific portlets that are used for models of three device manufacturers.
---
## Specific portlets

Specific portlets that are used for models of three device manufacturers:

* Engine event behavior for ATrack.
* Guard mode for Yatut.
* Harsh behavior for Suntech.


### engine_control_atrack

Special settings to set the engine event behavior for ATrack.

```json
{
    "power_voltage_high_level": 13800,
    "on_duration_seconds": 120,
    "power_voltage_low_level": 12800,
    "off_duration_seconds": 300
}
```

* `power_voltage_high_level` - int. Voltage in 0.001 volts for detecting engine ON state. Min=0, max=30000, 
default=13800 mV.
* `on_duration_seconds` - int. Duration in seconds that must elapse before the engine state change accepted. 
Min=0, max=600, default=1 second.
* `power_voltage_low_level` - int. Voltage in 0.001 volts for detecting engine OFF state. Min=0, max=30000, 
default=12800 mV.
* `off_duration_seconds` - duration in seconds that must elapse before the engine state change accepted. 
Min=0, max=600, default=5 seconds.


### guard_mode_yatut

Guard special settings for "Я ТУТ ПОИСК".

```json
{
    "motion_sensor_mode": "double_period",
    "motion_sensor_first_period": "23:00-07:00",
    "motion_sensor_second_period": "10:00-17:00",
    "motion_sensor_amplitude": 10,
    "motion_sensor_duration": 30,
    "motion_sensor_ignore_time": 50,
    "motion_sensor_double_check": false,
    "perimeter_mode": "once_triggering",
    "perimeter_diameter": 1
}
```

* `motion_sensor_mode` - [enum](../../../../../getting-started/introduction.md#data-types). Can be "off" | "permanent" | "single_period" | "double_period". Default="off".
* `motion_sensor_first_period` - string time. Format=`HH:mm-HH:mm`, default="23:00-07:00" Required 
for `motion_sensor_mode` in single_period/double_period.
* `motion_sensor_second_period` - string time. Format=`HH:mm-HH:mm`, default="10:00-17:00" Required 
for `motion_sensor_mode` in double_period.
* `motion_sensor_amplitude` - int. Min=1, max=255, default=5 Required for `motion_sensor_mode` != off.
* `motion_sensor_duration` - int. Min=1, max=255, default=5 seconds. Required for `motion_sensor_mode` != off.
* `motion_sensor_ignore_time` - int. Min=5, max=99, default=5 minutes. Required for `motion_sensor_mode` != off.
* `motion_sensor_double_check` - boolean. Default=`false`. Required for `motion_sensor_mode` != off.
* `perimeter_mode` - [enum](../../../../../getting-started/introduction.md#data-types). Can be "off" | "once_triggering" | "permanent" | "point_displacement". Default="off".
* `perimeter_diameter` - int. Min=1, max=999, default=1 kilometer. Required for `perimeter_mode` != off.


### harsh_behavior_suntech

Harsh driving settings for Suntech.

```json
{
    "mode": "enable",
    "max_acceleration_force": 1.5,
    "max_braking_force": 0.05,
    "max_cornering_force": 3,
    "type": "harsh_behavior_suntech"
}
```

* `mode` - string. Can be "enable" | "disable".
* `max_acceleration_force` - double. Can be 0.05 – 3.0 g.
* `max_braking_force` - double. Can be 0.05 – 3.0 g.
* `max_cornering_force` - double. Can be 0.05 – 3.0 g.
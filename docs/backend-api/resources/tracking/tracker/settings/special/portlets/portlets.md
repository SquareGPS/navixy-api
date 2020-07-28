---
title: /portlets
description: /portlets
---

## engine_control_atrack
Special settings to set the engine event behavior for ATrack.

```js
{
    "power_voltage_high_level": <int, mV, min=0, max=30000, default=13800> (required),
    "on_duration_seconds": <int, second, min=0, max=600, default=1> (required),
    "power_voltage_low_level": <int, mV, min=0, max=30000, default=12800> (required),
    "off_duration_seconds": <int, second, min=0, max=600, default=5> (required)
}
```

*   power_voltage_high_level: voltage in 0.001 volts for detecting engine ON state.
*   on_duration_seconds: duration in seconds that must elapse before engine state change is accepted.
*   power_voltage_low_level: voltage in 0.001 volts for detecting engine OFF state.
*   off_duration_seconds: duration in seconds that must elapse before engine state change is accepted.

## guard_mode_yatut

Guard special settings for “Я ТУТ ПОИСК”.

```js
{
    "motion_sensor_mode": <string, off|permanent|single_period|double_period, default=off> (required),
    "motion_sensor_first_period": <string, format='HH:mm-HH:mm', default='23:00-07:00'> (required for motion_sensor_mode in [single_period, double_period]),
    "motion_sensor_second_period": <string, format='HH:mm-HH:mm', default='10:00-17:00'> (required for motion_sensor_mode = double_period),
    "motion_sensor_amplitude": <int, min=1, max=255, default=5> (required for motion_sensor_mode != off),
    "motion_sensor_duration": <int, seconds, min=1, max=255, default=5> (required for motion_sensor_mode != off),
    "motion_sensor_ignore_time": <int, minutes, min=5, max=99, default=5> (required for motion_sensor_mode != off),
    "motion_sensor_double_check": <boolean, default=false> (required for motion_sensor_mode != off),
    "perimeter_mode": <string, off|once_triggering|permanent|point_displacement, default=off> (required),
    "perimeter_diameter": <int, kilometers, min=1, max=999, default=1> (required for perimeter_mode != off)
}
```

## harsh_behavior_suntech

Harsh driving settings for Suntech.
parameters:
01.name: mode
type: string
values range: [“enable”, “disable”]

02.name: max_acceleration_force
type: real
values range: [0.05 – 3.0] (inclusive)
units: g

03.name: max_braking_force
type: real
values range: [0.05 – 3.0] (inclusive)
units: g

04.name: max_cornering_force
type: real
values range: [0.05 – 3.0] (inclusive)
units: g

05.name: type
type: string
value must be always “harsh_behavior_suntech”

settings object example:

```json
{
    "mode": "enable",
    "max_acceleration_force": 1.5,
    "max_braking_force": 0.05,
    "max_cornering_force": 3,
    "type": "harsh_behavior_suntech"
}
```

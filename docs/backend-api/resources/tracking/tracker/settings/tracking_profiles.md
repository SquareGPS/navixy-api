---
title: Tracking profiles
description: Tracking profiles of all device models with description.  
---
# Tracking profiles

Contains tracking profiles of all device models with description.


### albatross_s6

Tracking profile for Albatross S6.

```json
{
    "tracking_interval": 30,
    "tracking_distance": 100
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.


### albatross_s8_5

Tracking profile for Albatross S8.5.

```json
{
    "tracking_interval": 30,
    "psm_interval": 60000,
    "psm_mode": 0
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.
* `psm_interval` - optional int. Duration in seconds for the device to stay in the deep sleep mode. Min=600, max=65535.
* `psm_mode` - int. Define the sleep level. Min=0, max=1.


### apkcom

Tracking profile for АПК КОМ ASC-2 GLONASS/GPS, АПК КОМ ASC-6 GLONASS/GPS, АПК КОМ ASC-7, АПК КОМ ASC-8.

```json
{
    "tracking_angle": 30,
    "tracking_interval": 30,
    "tracking_distance": 100
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=180.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=300.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=5000.


### arknav_x8

Tracking profile for Arknav RX8.

```json
{
    "tracking_angle": 30,
    "tracking_interval": 60,
    "tracking_distance": 150
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=180.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=65534.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65534.


### arnavi2

Arnavi 2 tracking profile.

```json
{
  "tracking_angle": 30,
  "tracking_distance": 100,
  "min_tracking_interval": 30,
  "max_tracking_interval": 300,
  "speed_change": 50,
  "freeze_by_speed": false,
  "freeze_by_motion": true,
  "freeze_by_ignition": false
}
```
* `tracking_angle` – int. Degrees 10-255, the device will send tracking data when course changing more than defined value. 
* `tracking_distance` – int. Distance in meters 50-65535, e.g. 100 means that the device will send data every 100 meters.
* `min_tracking_interval` – int. Min interval in seconds 30-255, e.g. 30 means that the device will send tracking data no more frequently than every 30 seconds.
* `max_tracking_interval` – int. Max interval in seconds 30-65535, e.g. 30 means that the device will send tracking data not less frequently than every 30 seconds.
* `speed_change` – int. Kph 3-255, the device will send tracking data when speed changing more than defined value.
* `freeze_by_speed` – boolean. Freeze coordinates when speed is less than 2kph.
* `freeze_by_motion` – boolean. Freeze coordinates when motion sensor detects no motion.
* `freeze_by_ignition` – boolean. Freeze coordinates when ignition is OFF.


### arnavi4

Tracking profile for Arnavi 4, Arnavi 5, Arnavi Integral, Arnavi Integral-2, Arnavi Integral-3.

```json
{
    "max_tracking_interval": 60,
    "min_tracking_interval": 5,
    "speed_change": 10,
    "tracking_angle": 30,
    "tracking_distance": 150
}
```

* `max_tracking_interval` – int. Max interval in seconds 30-65535, e.g. 30 means that the device will send tracking data not less frequently than every 30 seconds.
* `min_tracking_interval` – int. Min interval in seconds 30-255, e.g. 30 means that the device will send tracking data no more frequently than every 30 seconds.
* `speed_change` – int. Kph 3-255, the device will send tracking data when speed changing more than defined value.
* `tracking_angle` – int. Degrees 10-255, the device will send tracking data when course changing more than defined value. 
* `tracking_distance` – int. Distance in meters 50-65535, e.g. 100 means that the device will send data every 100 meters.


### atlanta

Tracking profile for Atlanta L-100, Atlanta O-300, Atlanta PT-100, Atlanta W-track, Atlanta WP-30C.

```json
{
    "tracking_distance": 150,
    "tracking_interval": 60
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65534.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### atlanta_pt100

Tracking profile for Atlanta PT-100.

```json
{
    "tracking_interval": 300
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=300, max=18000.


### atrack

ATrack tracking profile.

```json
{
    "control_mode": "acc",
    "tracking_interval": 30,
    "tracking_distance": 150,
    "tracking_angle" : 30,
    "psm_mode": 0,
    "psm_interval": 30,
    "on_stop_tracking_interval": 1
}
```
* `control_mode` - optional [enum](../../../../getting-started/introduction.md#data-types). Mode of tracking by the ACC or engine status. Can be "acc" | "engine_status".
* `tracking_interval` - optional int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535x10, default=300.
* `tracking_distance` - optional int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535, default=100.
* `tracking_angle` - optional int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=80, default=10.
* `psm_mode` - optional int. Define the sleep level, 0 – no sleeping, 1- light sleep (GPS Off, GPRS On, G-sensor On), 2- deep sleep (GPS Off, GPRS Off, G-sensor On). Min=0, max=2, default=0.
* `psm_interval` - optional int. Duration in seconds for the device to stay in the deep sleep mode. Min=30, max=65535x60, default=90x60.
* `on_stop_tracking_interval` - int. Minimum time in seconds that must elapse before reporting next position while the ACC is in Off status. "acc" in control_mode must be set in order to use this time interval. Min=1, max=65535x10, default=15x60.


### autofon

Autofon profile.

```json
{
    "type": "interval",
    "tracking_interval": 30,
    "online_on_ext_power": true,
    "timer1_time" : "2020-09-16 03:17:26",
    "timer1_interval": 15,
    "timer2_time" : "2020-09-18 03:17:26",
    "timer2_interval": 30
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Tracking type "interval" or "power_save".
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=240.
* `online_on_ext_power` - boolean. Connect to server when external power connected.
* `timer1_time` - date/time. Date/time for timer1 for checking incoming SMS commands.
* `timer1_interval` - int. Interval to wakeup for timer1, minutes, min=15.
* `timer2_time` - date/time. Date/time for timer2 for sending location.
* `timer2_interval` - int. Interval to wakeup for timer1, minutes, min=15.


### autoleaders_st901

Tracking profile for Auto Leaders ST-901, Auto Leaders ST-901M.

```json
{
    "psm_interval": 60,
    "psm_mode": 0,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=30, max=18000.
* `psm_mode` - int. Define the sleep level. Min=0, max=1.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### autoseeker_at17

Tracking profile for Autoseeker AT-17.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=1, max=18000.


### avlsat_neos

Tracking profile for AVLSAT NEO-S.

```json
{
    "tracking_interval": 60
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=60, max=599940.


### bitrek310

Tracking profile for BI 310 CICADA, NaviTrek 310 Cicada.

```json
{
    "psm_interval": 12000,
    "psm_mode": 0,
    "tracking_interval": 720
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=300, max=86400.
* `psm_mode` - int. Define the sleep level. Min=0, max=1.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=720, max=21600.


### bofan_pt521

Tracking profile for Bofan PT502, Bofan PT521.

```json
{
    "tracking_angle": 30,
    "tracking_distance": 100,
    "tracking_interval": 60,
    "type": "interval"
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=90.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=5000.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=1200.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".


### box

Tracking profile for BOX-tracker, BOXtracker 2, Galileosky Boxfinder v1.0.

```json
{
    "tracking_angle": 30,
    "tracking_interval": 120
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=4294968.


### boxfinder

Tracking profile for Galileosky Boxfinder v1.0.

```json
{
    "shock_value": 1.5,
    "sleep_timeout": 180
}
```

* `shock_value` - double. Can be min=0.5, max=4 g.
* `sleep_timeout` - int. Can be min=1, max=1440 minutes.


### bsj

Tracking profile for BSJ KM-01/02, Gosafe G1C.

```json
{
    "tracking_angle": 30,
    "tracking_interval": 150
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=180.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### c2stek_fl

Tracking profile for C2STEK FL10, C2STEK FL2000G.

```json
{
    "tracking_angle": 30,
    "tracking_distance": 300,
    "tracking_interval": 120
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=360.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=0, max=9999.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=0, max=9999.


### calamp

Tracking profile for CalAmp ATU-620, CalAmp LMU-1100, CalAmp LMU-1200, CalAmp LMU-200, CalAmp LMU-2030, CalAmp LMU-2600, CalAmp LMU-2630, CalAmp LMU-2720, CalAmp LMU-300, CalAmp LMU-3030, CalAmp LMU-3640, CalAmp LMU-400, CalAmp LMU-4200, CalAmp LMU-4230, CalAmp LMU-4520, CalAmp LMU-5530, CalAmp LMU-700, CalAmp LMU-800, CalAmp LMU-900, CalAmp TTU-1200, CalAmp TTU-2830, CalAmp TTU-700.

```json
{
    "psm_interval": 600,
    "tracking_angle": 30,
    "tracking_distance": 200,
    "tracking_interval": 60
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=30, max=86400.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=5000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### cantrack_t80

Tracking profile for Cantrack T80.

```json
{
    "tracking_interval": 10
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=1000.


### careu

Tracking profile for CAREU U1 Lite Plus, CAREU U1 Plus, CAREU UT1, CAREU UW1, CAREU Ucan, CAREU Ueco, CAREU Ugo, IntelliTrac A1, Intellitrac S1.

```json
{
    "tracking_angle": 45,
    "tracking_distance": 50,
    "tracking_interval": 20
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=25, max=50000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=65535.


### cargo

Tracking profile for Cargo Light 2, Cargo Mini 2, Cargo Pro 2.

```json
{
    "psm_interval": 600,
    "tracking_angle": 60,
    "tracking_distance": 100,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=30, max=86400.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=5000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### carscop_cctr800

Tracking profile for Carscop CCTR-808S, Carscop CCTR-809.

```json
{
    "psm_interval": 3600,
    "psm_mode": 1,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=3600, max=432000.
* `psm_mode` - int. Define the sleep level. Min=0, max=1.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=999.


### carscop_cctr830

Tracking profile for Carscop CCTR-830, Toptracking CCTR-830G.

```json
{
    "tracking_interval": 40
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=999.


### castel_idd

Tracking profile for Sinocastel IDD-213.

```json
{
    "sleep_report_interval": 120,
    "tracking_angle": 20,
    "tracking_distance": 500,
    "tracking_interval": 200,
    "upload_records_count": 1
}
```

* `sleep_report_interval` - int. Interval in minutes, e.g. 10 means that the device will send tracking data every 10 minutes in a sleep mode. Min=10, max=1440.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=90.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=5000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=600.
* `upload_records_count` - int. Count of uploaded records. Min =1, max=10.


### castel_interval

Tracking profile for Sinocastel MPIP-620, Sinocastel PT-690, Sinocastel PT-718S.

```json
{
    "tracking_interval": 60
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=18000.


### cguard

cGuard tracking profile.

```json
{
    "tracking_interval": 60,
    "tracking_distance": 100,
    "tracking_angle" : 15,
    "psm_interval": 300
}
```
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=0, max=65535, default=60.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=0, max=65535, default=100.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=180, default=15.
* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=0, max=65535, default=300.


### cguard_asset

cGuard tracking profile for asset trackers.
name: 'cguard_asset'

```json
{
    "tracking_interval": 60,
    "tracking_distance": 100,
    "tracking_angle" : 45,
    "psm_interval": 300,
    "mode": "ASSET",
    "wakeup_type": "PERIODICAL",
    "wakeup_day": "EVERYDAY",
    "wakeup_time": "12:00",
    "wakeup_period": 1440,
    "moving_detection": true
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=0, max=65535, default=60.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=0, max=65535, default=100.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=180, default=45.
* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=0, max=65535, default=300.
* `mode` - [enum](../../../../getting-started/introduction.md#data-types). Device working mode. `TRACKER` means that device work in the continuous mode. `ASSET` means that device work in the periodical mode and wakes up on schedule or by period.
* `wakeup_type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "SCHEDULED" | "PERIODICAL". How device wakes up in `ASSET` mode. default="PERIODICAL".
* `wakeup_day` - [enum](../../../../getting-started/introduction.md#data-types). Can be "EVERYDAY" | "MONDAY" | "TUESDAY" | "WEDNESDAY" | "THURSDAY" | "FRIDAY" | "SATURDAY" | "SUNDAY", default="EVERYDAY". What day to wake up if wakeup_type = `SCHEDULED`.
* `wakeup_time` - string. Specifies the time in minutes to wake up if wakeup_type = `SCHEDULED`. Format `HH:mm`, default="12:00"
* `wakeup_period` - int. Wakeup period in minutes. Min=15, max=65535, default=1440. Required if wakeup_type = `PERIODICAL`
* `moving_detection` - boolean. If `true` means that device will be wakes up at the beginning of the movement. Required if mode == 'ASSET'


### concox_distance_interval

Tracking profile for Concox X3.

```json
{
    "tracking_distance": 100,
    "tracking_interval": 30
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=10000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### concox_gt350

Tracking profile for Concox GT350.

```json
{
    "psm_interval": 600,
    "psm_mode": 1,
    "tracking_interval": 10
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=600, max=432000.
* `psm_mode` - int. Define the sleep level. Min=0, max=1.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=1800.


### concox_gt700

Tracking profile for Concox AT3, Concox AT4, Concox GT710.

```json
{
    "psm_interval": 2,
    "tracking_interval": 1,
    "type": "interval",
    "wakeup_time": "10:20"
}
```

* `psm_interval` - int. Duration in hours for the device to stay in the deep sleep mode. Min=1, max=24. Valid values are 1, 2, 3, 4, 6, 8, 12, 24.
* `tracking_interval` - int. Interval in minutes. Min=1, max=30.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".
* `wakeup_time` - string. Format `hh:mm`.


### concox_interval

Tracking profile for Concox GK309 , Concox GS503, Concox GT03A, Concox GT03C, Concox WeTrack Lite, Concox WeTrack2, Jimi JI09.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### concox_jv200

Tracking profile for Concox JV200.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### concox_qbit

Tracking profile for Concox QBIT.

```json
{
    "gps_tracking_interval": 10,
    "lbs_tracking_interval": 60,
    "mode": "lbs"
}
```

* `gps_tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds in `gps` mode. Min=30, max=18000.
* `lbs_tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds in `lbs` mode. Min=30, max=18000.
* `mode` - string. Can be "lbs" | "gps".


### concoxgt02

Tracking profile for Concox GT02 / TR02.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### concoxgt06

Tracking profile for Concox GV20, Concox X1, Protrack VT05.

```json
{
    "psm_interval": 3000,
    "tracking_angle": 120,
    "tracking_distance": 250,
    "tracking_interval": 30,
    "type": "intelligent"
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=30, max=65535.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=10000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".


### default

Default tracking profile.

```json
{
    "type": "interval",
    "tracking_interval": 30,
    "tracking_distance": 100
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" (send tracking data based on time intervals) or "distance" (send tracking data after passing specified distance).
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.


### default_angle

Default profile with optional angle-based tracking.

```json
{
    "type": "distance",
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" (send tracking data based on time intervals) or "distance" (send tracking data after passing specified distance).
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - optional int. If specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.


### default_powersave

Default powersave profile with optional angle-based tracking.
```json
{
    "type": "power_save",
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30,
    "psm_interval": 65535,
    "psm_mode": 2
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" (send tracking data based on time intervals) or "distance" (send tracking data after passing specified distance).
* `tracking_interval` - optional int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - optional int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - optional int. If specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
* `psm_interval` - optional int. Define the time interval in seconds (60-65535) which the unit stays in the sleeping state when type=`power_save`.
* `psm_mode` - optional int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep(GPS Off, GPRS Off, G-sensor On).


### defenstar_007

Tracking profile for Defenstar DS007.

```json
{
    "tracking_interval": 65534
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=60, max=65534.


### defenstar_008

Tracking profile for Defenstar DS008, Gubloos GPS-S1.

```json
{
    "tracking_interval": 1000
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=9999.


### digitalsystems_dsf22

Tracking profile for DigitalSystems DSF22.

```json
{
    "tracking_angle": 10,
    "tracking_interval": 120
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### distance_interval

Tracking profile with distance and interval.

```json
{
    "tracking_distance": 250,
    "tracking_interval": 3600
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=100000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### distance_interval_angle_ps

Tracking profile with distance, interval, angle and power save mode.

```json
{
    "psm_interval": 86400,
    "tracking_angle": 10,
    "tracking_distance": 100,
    "tracking_interval": 60
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=30, max=86400.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=100000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### distance_interval_angle

Tracking profile with distance, interval and angle.

```json
{
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.


### eelink

Tracking profile for Eelink GOT08, Eelink GOT10, Eelink GPT18, Eelink TK-319, Eelink TK116, Eelink TK119.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=18000.


### eelink_tk116

Tracking profile for Eelink TK116.

```json
{
    "tracking_interval": 3600
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=3600.


### eelink_v2

Tracking profile for Eelink GPT18, Eelink TK-319.

```json
{
    "active_tracking_interval": 30,
    "gps_working_mode": "always_on",
    "gsm_working_mode": "auto",
    "tracking_angle": 30,
    "tracking_distance": 50,
    "tracking_interval": 60
}
```

* `active_tracking_interval` - int. Active tracking interval in seconds. Min=30, max=65535.
* `gps_working_mode` - [enum](../../../../getting-started/introduction.md#data-types). Can be "always_on" | "auto".
* `gsm_working_mode` - [enum](../../../../getting-started/introduction.md#data-types). Can be "always_on" | "auto".
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=10000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.


### enfora

Tracking profile for Enfora MT-GL (GSM2218), Enfora MT-Gu (GSM2338), Novatel MT4100, SkyPatrol TT8740, SkyPatrol TT8750.

```json
{
    "tracking_distance": 100,
    "tracking_interval": 60
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=10000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### esino

Tracking profile for Esino ES-GP34, Esino ES-GT23.

```json
{
    "tracking_interval": 20
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=20, max=3600.


### etrack_tlt2h

Tracking profile for E-Track TLT-2H.

```json
{
    "tracking_interval": 600
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=59999.


### fifotrack

Tracking profile for Fifotrack A100, fifotrack A100 FW1.15+, fifotrack A300, fifotrack A300 FW1.23+, fifotrack A600 (FW before V1.07), fifotrack A600 FW1.07+.

```json
{
    "psm_interval": 3600,
    "psm_mode": 2,
    "tracking_angle": 45,
    "tracking_distance": 100,
    "tracking_interval": 60
}
```

* `psm_interval` - int. Duration in seconds for the device to stay in the deep sleep mode. Min=0, max=3932100.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep (GPS Off, GPRS Off, G-sensor On).
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=655350.


### genesis_g36

Tracking profile for Sinocastel HT-770, Ezlink T28, G36, Orion 7, XiLi Technologies PT100.

```json
{
    "tracking_interval": 1
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=1.


### gl200

Queclink/Ruslink GL200/GL300 profile

```json
{
    "type": "distance",
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30,
    "psm_interval": 600,
    "movement_detection": true,
    "non_movement_duration": 420
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Tracking type "distance" or "interval" or "power_save".
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
* `psm_interval` - int. Sending interval when the tracking type is "power_save", seconds.
* `movement_detection` - boolean.
* `non_movement_duration` - int. In seconds.


### gl500

Queclink/Ruslink GL500 profile.

```json
{
    "type": "interval",
    "tracking_interval": 1,
    "wakeup_time": "10:00",
    "psm_interval": 8
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Tracking type "interval" or "power save".
* `tracking_interval` - int. Interval in minutes.
* `wakeup_time` - int. Wakeup time for power_save mode in a format "HH:mm".
* `psm_interval` - int. Update interval in power_save mode, hours (1, 2, 3, 4, 6, 8, 12, 24).


### gt300

Queclink/Ruslink GT300 profile.

```json
{
    "tracking_interval": 5,
    "start_time": "0000",
    "end_time": "2359",
    "movement_detection": true,
    "min_speed": 10,
    "min_distance": 20
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=5, max=86400.
* `start_time` - string. Start time of scheduled fix timing report. The valid format is "HHMM" 0000-2359.
* `end_time` - string. End time of scheduled fix timing report. The valid format is "HHMM" 0000-2359.
* `movement_detection` - boolean. Enable suspend reports if the device at rest.
* `min_speed` - int. The speed threshold of movement detect, km/h 0-999.
* `min_distance` - int. The distance threshold of movement detect, meters 1-9099.


### gotoptk206_amgps_freko

Tracking profile for AMGPS Freko.

```json
{
    "tracking_interval": 10
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=3600.


### gv500

Queclink/Ruslink GV500 profile.

```json
{
    "type": "interval",
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30,
    "psm_mode": 1,
    "psm_interval": 600
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Tracking type when ignition is ON, "distance" or "interval".
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep(GPS Off, GPRS Off, G-sensor On).
* `psm_interval` - int. Sending interval when the engine is off, seconds.


### gv55lite

Queclink/Ruslink GV55Lite profile.

```json
{
    "type": "interval",
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30,
    "psm_mode": 1,
    "psm_interval": 600
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Tracking type when ignition is ON, "distance" or "interval".
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep(GPS Off, GPRS Off, G-sensor On).
* `psm_interval` - int. Sending interval when the engine is off, seconds.


### gubloost1

Tracking profile for Defenstar GPS668, Gubloos GPS-T1, MiniFinder Pico.

```json
{
    "tracking_interval": 10
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=9999.


### haicom_hi603x

Tracking profile for Haicom HI-603X.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=2592000.


### helioversal_m1

Tracking profile for Helioversal M1.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### hhd_g

Tracking profile for HHD G-400, HHD G-600.

```json
{
    "tracking_interval": 20
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=20.


### howen_herome

Tracking profile for Hero-ME31-08, Hero-ME32-04, Hero-ME41-04.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### hua_sheng_hs3000g

Tracking profile for Hua Sheng HS 3000G.

```json
{
    "psm_interval": 600,
    "tracking_angle": 10,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Sending interval when the engine is off, seconds. Min=60, max=86400.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=250.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=450.


### huabao

Tracking profile for Huabao HB-T10.
```json
{
    "tracking_interval": 1000
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=9999.


### intellitrac_x1

Tracking profile for IntelliTrac X1, IntelliTrac X1+.

```json
{
    "tracking_angle": 5,
    "tracking_distance": 100,
    "tracking_interval": 30,
    "type": "interval"
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=358.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=65534.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65534.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".


### interval

Tracking profile with an interval only.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30.


### interval_angle

Tracking profile with an interval and angle.

```json
{
    "tracking_interval": 30,
    "tracking_angle" : 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.


### interval_angle_powersave

Tracking profile with an interval, angle and powersave mode.

```json
{
    "psm_interval": 60,
    "tracking_angle": 55,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Sending interval when the engine is off, seconds. Min=60, max=86400.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=355.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=900.


### interval_powersave

Tracking profile with an interval and powersave mode.

```json
{
    "psm_interval": 3000,
    "psm_mode": 1,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Sending interval when the engine is off, seconds. Min=60, max=86400.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On).
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=180.


### jimi_jc100

Tracking profile for Jimi JC100.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### jinsheng_js810

Tracking profile for Jin Sheng JS810, Jin Sheng JS810S.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65534.


### jointech_gp

Tracking profile for Jointech GP4000, Jointech GP6000, Jointech GP6000F.

```json
{
    "psm_interval": 3600,
    "psm_mode": 1,
    "tracking_angle": 45,
    "tracking_distance": 150,
    "tracking_interval": 30,
    "type": "interval"
}
```

* `psm_interval` - int. Sending interval when the engine is off, seconds. Min=300, max=65535.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `1` - no sleeping, `2` - light sleep(GPS Off, GPRS On, G-sensor On), `3` - deep sleep(GPS Off, GPRS Off, G-sensor On).
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=90.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".


### jointech_jt701

Tracking profile for Jointech JT701.

```json
{
    "tracking_interval": 240
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=60000.


### jointech_jt703

Profile for Jointech JT703B

```json
{
    "tracking_interval": 10,
    "sleep_mode": "enabled",
    "wakeup_timers": ["10:00:00", "16:00:00"],
    "sleep_time_in_minutes": 60
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=60000.
* `sleep_mode` - [enum](../../../../getting-started/introduction.md#data-types). Can be "enabled" | "disabled".
* `wakeup_timers` - optional string. Define wake-up timers when the sleep mode enabled, 1-48 timers. Local time in a standard format `HH:mm:ss`.
* `sleep_time_in_minutes` - optional int. Define the time interval which the unit stays in the sleeping state when wake-up timers not defined. Min=10, max=1440.


### jointech_jt707

Tracking profile for Jointech JT707.

```json
{
    "psm_interval": 150,
    "psm_mode": 0,
    "tracking_interval": 60
}
```

* `psm_interval` - int. Sending interval when the engine is off, seconds. Min=10, max=1440.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On).
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=5, max=43200.


### keson_ks168

Tracking profile for Keson KS168.

```json
{
    "tracking_interval": 10
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=65535.


### laipacs911

Tracking profile for Laipac S911 Lola, Laipac-911BL.

```json
{
    "tracking_distance": 1000,
    "tracking_interval": 30,
    "type": "distance"
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=100000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=5, max=43200.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".


### lk200

Tracking profile for LKGPS LK209A, LKGPS LK209B, LKGPS LK210.

```json
{
    "tracking_interval": 45
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.


### logosoft

Tracking profile for Logosoft Log-101.

```json
{
    "type": "interval",
    "tracking_interval": 30,
    "tracking_distance": 300,
    "tracking_angle" : 10
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Tracking type "interval" or "distance" or "intelligent".
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=300.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10.


### m7

Profile for Navixy M7.

```json
{
    "type": "interval",
    "psm_mode": 1,
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30,
    "psm_interval": 600,
    "wakeup_timer1": "10:00",
    "wakeup_timer2": "16:00",
    "wakeup_timer3": "22:00"
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" (send tracking data based on time intervals), "distance" (send tracking data after passing specified distance).
* `psm_mode` - int. Power save mode, 0 - disable, 1 - powersave without timers, 2 - powersave with timers.
* `tracking_interval` - optional int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - optional int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - optional int. If specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
* `psm_interval` - optional int. Define the time interval in seconds (600-3932100) which the unit stays in the sleeping state.
* `wakeup_timer` - optional string. Timer 1-3.


### maxtrack_140

Tracking profile for Maxtrack MXT-140.

```json
{
    "tracking_angle": 60,
    "tracking_distance": 500,
    "tracking_interval": 20
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=0, max=25500.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=20, max=65535.


### megastek_gvt430

Tracking profile for Megastek GVT-430.

```json
{
    "tracking_angle": 25,
    "tracking_distance": 100,
    "tracking_interval": 30
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=60.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=1000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### megastek_mt

Tracking profile for Megastek MT-300, Megastek MT-90s, Megastek MT100.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### megastek_mt100

Tracking profile for Megastek MT100.

```json
{
    "tracking_distance": 50,
    "tracking_interval": 300,
    "type": "intelligent"
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=100000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".


### meiligaovt

Tracking profile for GoTop VT360, GoTop VT380, Meiligao VT310, Meitrack VT310, RedView VT310.

```json
{
    "tracking_angle": 30,
    "tracking_distance": 200,
    "tracking_interval": 10
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=5000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=655350.


### meitrack

Meitrack profile.

```json
{
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30,
    "psm_mode": 0,
    "psm_interval": 3600
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
* `psm_mode` - optional int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep(GPS Off, GPRS Off, G-sensor On).
* `psm_interval` - optional int. Define the time interval in seconds which the unit stays in the sleeping state.


### meitrack_asset

Tracking profile for Meitrack T355v2.

```json
{
    "psm_interval": 3932100,
    "psm_mode": 0,
    "tracking_angle": 10,
    "tracking_distance": 50,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=0, max=3932100.
* `psm_mode` - optional int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep(GPS Off, GPRS Off, G-sensor On).
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=655350.


### meitrack_vehicle

Tracking profile for Meitrack MVT100, Meitrack MVT340, Meitrack MVT380, Meitrack MVT600, Meitrack T1, Meitrack T3, Meitrack T333, Meitrack T366G, Meitrack T366L, Meitrack T622G, Meitrack TC68S, Meitrack TC68SG.

```json
{
    "on_stop_tracking_interval": 120,
    "psm_interval": 300,
    "psm_mode": 2,
    "tracking_angle": 45,
    "tracking_distance": 50,
    "tracking_interval": 30
}
```

* `on_stop_tracking_interval` - int. Tracking interval in seconds when the vehicle stopped. Min=0, max=655350.
* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=0, max=3932100.
* `psm_mode` - optional int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep(GPS Off, GPRS Off, G-sensor On).
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=655350.


### meitrack_without_ps

Tracking profile for Meitrack P66.

```json
{
    "tracking_angle": 45,
    "tracking_distance": 150,
    "tracking_interval": 60
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=655350.


### mictrack_mp90

Tracking profile for MicTrack MP-90.

```json
{
    "tracking_angle": 20,
    "tracking_interval": 60
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=20, max=180.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=65535.


### mika_g1

Tracking profile for MIKA G1.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=10000.


### mrd_100

Tracking profile for MRD-100.

```json
{
    "tracking_interval": 20
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=20, max=65535.


### mwp008_a

Tracking profile for Diwei TK116, Moralwinhk P008A, Moralwinhk P168.

```json
{
    "tracking_interval": 10
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=655350.


### myrope_m500

Tracking profile for MyRope M528, MyRope M588.
```json
{
    "psm_interval": 60,
    "tracking_distance": 10,
    "tracking_interval": 50
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=60, max=65535.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=1, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=1, max=65535.


### navisetgt

Tracking profile for Naviset GT-10, Naviset GT-20.

```json
{
    "tracking_angle": 120,
    "tracking_distance": 150,
    "tracking_interval": 240
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=255.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=300.


### noran

Tracking profile for Noran NR008, Noran NR024, Noran NR100.

```json
{
    "tracking_interval": 150
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=15, max=64800.


### oigo_ar2

Tracking profile for Oigo AR-2GM, Oigo AR-3HU.

```json
{
    "psm_interval": 60,
    "tracking_angle": 45,
    "tracking_distance": 300,
    "tracking_interval": 15
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=15, max=604800.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=0, max=60000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=15, max=604800.


### orange_tk103

Tracking profile for Orange TK-103.

```json
{
    "tracking_interval": 990
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=990.


### piccolo_atx

Tracking profile for Piccolo ATX.

```json
{
    "tracking_interval": 300
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=300, max=86400.


### piccolo_distance_interval_angle

Tracking profile for Piccolo ATX2S, Piccolo Hybrid+, Piccolo STX, Piccolo TMX+.

```json
{
    "tracking_angle": 30,
    "tracking_distance": 100,
    "tracking_interval": 30
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=30, max=150.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=10000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=65535.


### piccolo_plus

Profile Wireless Links for Piccolo Plus

```json
{
    "sleep_mode": "disabled",
    "track_by": "interval",
    "tracking_interval": 60,
    "tracking_distance": 100,
    "track_by_angle": true,
    "tracking_angle": 30,
    "asset_moving_interval": 300,
    "asset_stopped_interval": 86400
}
```

* `sleep_mode` - [enum](../../../../getting-started/introduction.md#data-types). Can be "disabled" | "engine" | "asset" | "hybrid".
* `track_by` - optional [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance". Need for disabled, engine, hybrid modes.
* `tracking_interval` - optional int. Interval in seconds, need for disabled, engine, hybrid modes. Min=60, max=86400.
* `tracking_distance` - optional int. Distance in meters, need for disabled, engine, hybrid modes. Min=100, max=10000.
* `track_by_angle` - optional boolean. Need for disabled, engine, hybrid modes.
* `tracking_angle` - optional int. If specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees, need for disabled, engine, hybrid modes. Min=30, max=150.
* `asset_moving_interval` - optional int. Need for asset and hybrid modes. Min=300, max=86400.
* `asset_stopped_interval` - optional int. Need for asset and hybrid modes. Min=300, max=86400.


### redview_vt680

Tracking profile for RedView VT680.

```json
{
    "tracking_angle": 60,
    "tracking_interval": 10
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=30, max=270.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=655350.


### sanfone

Tracking profile for Sanfone SF100, Sanfone SF700.

```json
{
    "tracking_angle": 120,
    "tracking_distance": 60,
    "tracking_interval": 60
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=360.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=30, max=60000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=999.


### satsol

Tracking profile for SAT-LITE 3, SAT-LITE 4, Sat Lite 2, Sat Pro, Super Lite.

```json
{
    "psm_interval": 30,
    "tracking_angle": 10,
    "tracking_distance": 50,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=30, max=86400.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=9999.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### senseitp211

```json
{
    "tracking_interval": 30,
    "gps_enabled": true
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30.
* `gps_enabled` - boolean.


### sheriff_awax12

Tracking profile for Sheriff AWAX12.

```json
{
    "tracking_interval": 900
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=900, max=86400.


### sinowell_g102

Tracking profile for Sinowell G102.

```json
{
    "psm_interval": 10,
    "tracking_angle": 5,
    "tracking_distance": 50,
    "tracking_interval": 10
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=10, max=65000.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=1000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=1000.


### skypatrol_tt8750plus

Tracking profile for SkyPatrol TT8750+.

```json
{
    "psm_interval": 30,
    "tracking_angle": 10,
    "tracking_distance": 100,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=30, max=18000.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=10000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=18000.


### sleep_active

Tracking profile for СКАТ-Маяк.

```json
{
    "active_time": 300,
    "sleep_time": 300
}
```

* `active_time` - int. Min=300, max=599940 seconds.
* `sleep_time` - int. Min=300, max=599940 seconds.


### spetrotec_iwatcher

Tracking profile for Spetrotec i-WATCHER AVL.

```json
{
    "tracking_distance": 100,
    "tracking_interval": 60,
    "type": "interval"
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=100000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=60, max=86400.
* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" | "distance" | "power_save" | "distance_interval_angle" | "interval_angle" | "intelligent".


### stab_liner

Tracking profile for M2M-Cyber GLX, STAB Liner 102.

```json
{
    "psm_interval": 3600,
    "tracking_angle": 10,
    "tracking_distance": 50,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=0, max=3600.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=100000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=0, max=3600.


### starcom_helios

Tracking profile for Starcom Helios Advanced, Starcom Helios Hybrid, Starcom Helios TT.

```json
{
    "tracking_interval": 10
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=0, max=432000.


### starline_m17

Tracking profile for Starline M17.

```json
{
    "psm_interval": 600,
    "psm_mode": 0,
    "tracking_interval": 100
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=60, max=3540.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On).
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=0, max=300.


### suntech_distance_interval_angle

Tracking profile for Suntech ST200, Suntech ST215, Suntech ST300, Suntech ST310U, Suntech ST340LC, Suntech ST600R, Suntech ST600V, Suntech ST650.

```json
{
    "tracking_angle": 30,
    "tracking_distance": 50,
    "tracking_interval": 20
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=60000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=20, max=60000.


### suntech_interval

Tracking profile for Suntech ST940.

```json
{
    "tracking_interval": 20
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=20, max=60000.


### syrus

Tracking profile for Syrus 2G.

```json
{
    "tracking_angle": 5,
    "tracking_distance": 200,
    "tracking_interval": 30
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=5, max=90.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=100, max=5000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=9999.


### telfm

Teltonika FM tracking profile.

```json
{
  "tracking_angle": 30,
  "tracking_distance": 100,
  "tracking_interval": 60,
  "on_stop_tracking_interval": 180,
  "sleep_mode": "disabled",
  "stop_detection": "ignition"
}
```
* `tracking_angle` – int. Degrees 10-255, the device will send tracking data when course changing more than defined value.
* `tracking_distance` – int. Distance in meters 50-65535, e.g. 100 means that the device will send data every 100 meters.
* `tracking_interval` – int. Interval in seconds 30-255, e.g. 30 means that the device will send tracking data no more frequently than every 30 seconds.
* `on_stop_tracking_interval` – int. On stop interval in seconds 30-65535, e.g. 30 means that the device will send tracking data not less frequently than every 30 seconds.
* `sleep_mode` – [enum](../../../../getting-started/introduction.md#data-types). Can be "disabled" | "soft_sleep".
* `stop_detection` – [enum](../../../../getting-started/introduction.md#data-types). Can be "ignition" | "g_sensor" | "gps".


### telfm5x

Tracking profile for Teltonika FM5500, Teltonika FM6320, Teltonika FMB630, Teltonika FMB640.

```json
{
    "sleep_mode": "disabled",
    "sleep_timeout": 300,
    "tracking_angle": 25,
    "tracking_distance": 50,
    "tracking_interval": 30
}
```

* `sleep_mode` – [enum](../../../../getting-started/introduction.md#data-types). Can be "disabled" | "soft_sleep".
* `sleep_timeout` - int. Can be min=300, max=2592000 seconds.
* `tracking_angle` – int. Degrees min=0, max=180, the device will send tracking data when course changing more than defined value.
* `tracking_distance` – int. Distance in meters min=50, max=65535, e.g. 100 means that the device will send data every 100 meters.
* `tracking_interval` – int. Interval in seconds min=30, max=2592000, e.g. 30 means that the device will send tracking data no more frequently than every 30 seconds.


### topfly

Tracking profile for TopFlyTech T8603, TopFlyTech T8608, TopFlyTech T8803, TopFlyTech T8803 Pro, TopFlyTech T8803+, TopFlyTech T8806, TopFlyTech T8806+, TopFlyTech T8806+R, TopFlyTech T8808A, TopFlyTech T8808A+, TopFlyTech T8808B, TopFlyTech T8808B+.

```json
{
    "psm_interval": 10000,
    "tracking_angle": 60,
    "tracking_distance": 50,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=0, max=65535.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=90.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=0, max=65535.


### topshine_distance_interval

Tracking profile for TopShine MT02, TopShine MT08, TopShine OGT100, TopShine VT1000, TopShine VT200W, TopShine VT900.

```json
{
    "tracking_distance": 50,
    "tracking_interval": 10
}
```

* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=655350.


### topshine_distance_interval_angle

Tracking profile for TopShine MT08, TopShine OGT100, TopShine VT1000.

```json
{
    "tracking_angle": 15,
    "tracking_distance": 50,
    "tracking_interval": 60
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=359.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=65535.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=655350.


### topten

Tracking profile for TopTen GT08, TopTen TK-510, TopTen TK228.

```json
{
    "tracking_angle": 25,
    "tracking_interval": 30
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=0, max=359.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=655350.


### totarget

Tracking profile for TT-08, VG-eLock7A.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=300.


### totem

Tracking profile for TotemTech AT05, TotemTech AT07.

```json
{
    "psm_interval": 15000,
    "tracking_angle": 10,
    "tracking_distance": 60,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=10, max=18000.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=180.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=10, max=18000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=10, max=18000.


### trackertech_msp320

Tracking profile for Tracker Technology MSP320.

```json
{
    "tracking_interval": 30
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### trackertech_msp340

Tracking profile for Tracker Technology MSP340.

```json
{
    "psm_interval": 180,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=180, max=86400.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### trackertech_msp350

Tracking profile for Tracker Technology MSP350.

```json
{
    "psm_interval": 2147483647,
    "psm_mode": 0,
    "tracking_distance": 50,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=60, max=2147483647.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On), `2` - deep sleep(GPS Off, GPRS Off, G-sensor On), `3` - ultra deep sleep.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=50, max=100000.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=86400.


### tramigo

Profile for Tramigo models that do not support the interval in seconds

```json
{
    "tracking_interval": 1,
    "tracking_distance": 0.5,
    "tracking_angle": 20,
    "on_stop_tracking_interval": 120,
    "sleep_mode": "disabled"
}
```

* `tracking_interval` - int. Interval in minutes, e.g. 30 means that the device will send tracking data every 30 minutes. Min=1, max=10080.
* `tracking_distance` - float. Distance in kilometers, e.g. 0.5 means that the device will send data every 500 meters. Min=0.5, max=20.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=20, max=180.
* `on_stop_tracking_interval` - int. Interval in minutes when not in a trip. Min=1, max=10080.
* `sleep_mode` - sting enum. Can be "disabled" | "enabled".


### tramigo_with_seconds

Profile for Tramigo models that do support the interval in seconds

```json
{
    "tracking_interval": 30,
    "tracking_distance": 20,
    "tracking_angle": 180,
    "on_stop_tracking_interval": 100,
    "sleep_mode": "enabled"
}
```

* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=604800.
* `tracking_distance` - float. Distance in kilometers, e.g. 0.5 means that the device will send data every 500 meters. Min=0.5, max=20.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=20, max=180.
* `on_stop_tracking_interval` - int. Interval in minutes when not in a trip. Min=1, max=10080.
* `sleep_mode` - sting enum. Can be "disabled" | "enabled".


### tt1

Profile for Navixy TT-1.

```json
{
    "type": "interval",
    "psm_mode": 2,
    "tracking_interval": 30,
    "tracking_distance": 100,
    "tracking_angle" : 30,
    "psm_interval": 60,
    "bat_voltage": "1.5",
    "bat_psm_interval": 600
}
```

* `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "interval" (send tracking data based on time intervals), "distance" (send tracking data after passing specified distance).
* `psm_mode` - int. power save mode, 0 - disable, 1 - powersave mode, 2 - Back-up Battery Power Saving Mode
* `tracking_interval` - optional int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds.
* `tracking_distance` - optional int. Distance in meters, e.g. 100 means that the device will send data every 100 meters.
* `tracking_angle` - optional int. If specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
* `psm_interval` - optional int. Define the time interval in seconds (600-3932100) which the unit stays in the sleeping state.
* `bat_voltage` - optional string. Threshold of low back-up battery voltage.
* `bat_psm_interval` - optional int. Sleeping duration when battery voltage below defined threshold, seconds.


### ulbotech_t300

Tracking profile for IMTSA TR2-OBD, Ulbotech T361, Ulbotech T381.

```json
{
    "tracking_angle": 3,
    "tracking_distance": 150,
    "tracking_interval": 30
}
```

* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=3, max=20.
* `tracking_distance` - int. Distance in meters, e.g. 100 means that the device will send data every 100 meters. Min=0, max=25500.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=900.


### vjoy

Tracking profile for Kingneed C30, Kingneed T0024 / T4024, Kingneed T0026, Kingneed T1124, Kingneed T12, Kingneed T16/T18/T19, Kingneed T300, Kingneed T3124 / T5124, Kingneed T500, Kingneed T6024, Kingneed T6124, Kingneed T630, Kingneed T8124, Kingneed TK10, Kingneed TK101, Kingneed TK20, Kingneed TK5, VJOYCAR T0026G, VJOYCAR T13G, VJOYCAR T13GSE, VJOYCAR T633G, VJOYCAR TK10SDC, VJoy T12, VJoy TK05, VJoy TK10GSE, VJoy TK10GSE Solar, VJoy TK20SE.

```json
{
    "continuous_report_interval": 10,
    "motion_interval": 30,
    "psm_mode": 1,
    "psm_wake_up_interval": 1
}
```

* `continuous_report_interval` - int. Min=10, max=5940 seconds.
* `motion_interval` - int. Min=30, max=999 seconds.
* `psm_mode` - int. Define the sleep level when type != `power_save`, `0` - no sleeping, `1` - light sleep(GPS Off, GPRS On, G-sensor On).
* `psm_wake_up_interval` - int. Min=1, max=99 hours.


### xirgo

Tracking profile for Xirgo XT-2050C, Xirgo XT-2060G, Xirgo XT-2150C, Xirgo XT-2160G, Xirgo XT-2450V, Xirgo XT-2460G, Xirgo XT-4750C, Xirgo XT-4760G, Xirgo XT-4850C.

```json
{
    "psm_interval": 2592000,
    "tracking_angle": 10,
    "tracking_distance": 1,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=60, max=2592000.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=180.
* `tracking_distance` - int. Distance in miles, e.g. 100 means that the device will send data every 100 miles. Min=1, max=100.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=2592000.


### xirgo_48

Tracking profile for Xirgo XT-4850C.

```json
{
    "psm_interval": 60,
    "tracking_angle": 10,
    "tracking_distance": 1,
    "tracking_interval": 30
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=60, max=2592000.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=180.
* `tracking_distance` - int. Distance in miles, e.g. 100 means that the device will send data every 100 miles. Min=1, max=100.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=2592000.


### xirgo_dist

Tracking profile for Xirgo XT-2050C, Xirgo XT-2060G, Xirgo XT-2450V, Xirgo XT-2460G, Xirgo XT-4750C, Xirgo XT-4760G.

```json
{
    "psm_interval": 60,
    "tracking_angle": 10,
    "tracking_distance": 2,
    "tracking_interval": 60
}
```

* `psm_interval` - int. Define the time interval in seconds which the unit stays in the sleeping state. Min=60, max=2592000.
* `tracking_angle` - int. The device will additionally send data when it changes direction to specified angle, e.g. 30 degrees. Min=10, max=180.
* `tracking_distance` - int. Distance in miles, e.g. 100 means that the device will send data every 100 miles. Min=1, max=100.
* `tracking_interval` - int. Interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds. Min=30, max=2592000.


### yatut_poisk

"Я ТУТ ПОИСК" tracking profile.
name: 'yatut_poisk'

```json
{
    "mode": "DAILY",
    "main_wakeup_time": "12:00",
    "wakeup_period": "24",
    "gps_determination_period": 0
}
```

* `mode` - [enum](../../../../getting-started/introduction.md#data-types). Device's working mode. Can be "DAILY" | "TEST" | "SEARCH", default="DAILY".
* `main_wakeup_time` - string. At what time to wake up if mode == "DAILY". Format `HH:mm`, default="12:00"
* `wakeup_period` - [enum](../../../../getting-started/introduction.md#data-types). Only values `8`, `12` or `24` (hours). Default="24"
* `gps_determination_period` - int. How often to determine the position by satellites (in days). Zero (0) means on each waking up. Min=0, max=30, default=0.

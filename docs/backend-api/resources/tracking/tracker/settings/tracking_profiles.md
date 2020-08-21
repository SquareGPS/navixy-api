---
title: Tracking profiles
description: Tracking profiles
---

### albatross_s6

Tracking profile for Albatross S6.
```json
{
    "tracking_interval": <int, second, min=30, max=65535>,
    "tracking_distance": <int, meter, min=50, max=65535>
}
```

### albatross_s8_5

Tracking profile for Albatross S8.5.
```json
{
    "tracking_interval": <int, second, min=30, max=65535>,
    "psm_interval": <int, second, min=600, max=65535> [optional],
    "psm_mode": <int, min=0, max=1>
}
```

### apkcom

Tracking profile for АПК КОМ ASC-2 GLONASS/GPS, АПК КОМ ASC-6 GLONASS/GPS, АПК КОМ ASC-7, АПК КОМ ASC-8.
```json
{
    "tracking_angle": <int, degree, min=5, max=180>,
    "tracking_interval": <int, second, min=10, max=300>,
    "tracking_distance": <int, meter, min=50, max=5000>
}
```

### arknav_x8

Tracking profile for Arknav RX8.
```json
{
    "tracking_angle": <int, degree, min=10, max=180>,
    "tracking_interval": <int, second, min=10, max=65534>,
    "tracking_distance": <int, meter, min=50, max=65534>
}
```

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
*   **tracking_angle** – **int** degrees 10-255, the device will send tracking data when course changing more than defined value
*   **tracking_distance** – **int** distance in meters 50-65535, e.g. 100 means that the device will send data every 100 meters
*   **min_tracking_interval** – **int** min interval in seconds 30-255, e.g. 30 means that the device will send tracking data no more frequently than every 30 seconds.
*   **max_tracking_interval** – **int** max interval in seconds 30-65535, e.g. 30 means that the device will send tracking data not less frequently than every 30 seconds.
*   **speed_change** – **int** kph 3-255, the device will send tracking data when speed changing more than defined value.
*   **freeze_by_speed** – **boolean**, freeze coordinates when speed is less than 2kph
*   **freeze_by_motion** – **boolean**, freeze coordinates when motion sensor detects no motion
*   **freeze_by_ignition** – **boolean**, freeze coordinates when ignition is OFF


### arnavi4

Tracking profile for Arnavi 4, Arnavi 5, Arnavi Integral, Arnavi Integral-2, Arnavi Integral-3.
```json
{
    "max_tracking_interval": <int, second, min=30, max=65535>,
    "min_tracking_interval": <int, second, min=5, max=255>,
    "speed_change": <int, km/h, min=3, max=255>,
    "tracking_angle": <int, degree, min=10, max=255>,
    "tracking_distance": <int, meter, min=50, max=65535>
}
```

### atlanta

Tracking profile for Atlanta L-100, Atlanta O-300, Atlanta PT-100, Atlanta W-track, Atlanta WP-30C.
```json
{
    "tracking_distance": <int, meter, min=100, max=10000>,
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### atlanta_pt100

Tracking profile for Atlanta PT-100.
```json
{
    "tracking_interval": <int, second, min=300, max=18000>
}
```

### atrack
ATrack tracking profile.
```json
{
    "control_mode": <string, acc | engine_status> [optional],
    "tracking_interval": <int, second, min=30, max=65535*10, default=300> [optional],
    "tracking_distance": <int, meter, min=50, max=65535, default=100> [optional],
    "tracking_angle" : <int, degree, min=10, max=80, default=10> [optional],
    "psm_mode": <int, min=0, max=2, default=0> [optional],
    "psm_interval": <int, second, min=30, max=65535*60, default=90*60> [optional],
    "on_stop_tracking_interval": <int, second, min=1, max=65535*10, default=15*60> (required)
}
```
*   **control_mode**: mode of tracking by ACC or engine status.
*   **tracking_interval**: interval in seconds, e.g. 30 means that the device will send traсking data every 30 seconds.
*   **tracking_distance**: distance in meters, e.g. 100 means that the device will send data every 100 meters.
*   **tracking_angle**: the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
*   **psm_mode**: optional, Define the sleep level, 0 – no sleeping, 1- light sleep (GPS Off, GPRS On, G-sensor On), 2- deep sleep (GPS Off, GPRS Off, G-sensor On).
*   **psm_interval**: duration in seconds for the device to stay in the deep sleep mode.
*   **on_stop_tracking_interval**: minimum time in seconds that must elapse before reporting next position while the ACC is in Off status. “acc” in control_mode must be set in order to use this time interval.

### autofon
Autofon profile.
```json
{
    "type": <string>,                 // tracking type "interval" or "power_save"
    "tracking_interval": <int>,       // interval in seconds, min=30, max=240
    "online_on_ext_power": <boolean>, // connect to server when external power is connected
    "timer1_time" : <date/time>,      // date/time for timer1 for checking incoming SMS commands
    "timer1_interval": <int>,         // interval to wakeup for timer1, minutes, min=15
    "timer2_time" : <date/time>       // date/time for timer2 for sending location
    "timer2_interval": <int>          // interval to wakeup for timer1, minutes, min=15
}
```

### autoleaders_st901

Tracking profile for Auto Leaders ST-901, Auto Leaders ST-901M.
```json
{
    "psm_interval": <int, second, min=30, max=18000>,
    "psm_mode": <int, min=0, max=1>,
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### autoseeker_at17

Tracking profile for Autoseeker AT-17.
```json
{
    "tracking_interval": <int, second, min=1, max=18000>
}
```

### avlsat_neos

Tracking profile for AVLSAT NEO-S.
```json
{
    "tracking_interval": <int, second, min=60, max=599940>
}
```

### bitrek310

Tracking profile for BI 310 CICADA, NaviTrek 310 Cicada.
```json
{
    "psm_interval": <int, second, min=300, max=86400>,
    "psm_mode": <int, min=0, max=1>,
    "tracking_interval": <int, second, min=720, max=21600>
}
```

### bofan_pt521

Tracking profile for Bofan PT502, Bofan PT521.
```json
{
    "tracking_angle": <int, degree, min=10, max=90>,
    "tracking_distance": <int, meter, min=50, max=5000>,
    "tracking_interval": <int, second, min=10, max=1200>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>
}
```

### box

Tracking profile for BOX-tracker, BOXtracker 2, Galileosky Boxfinder v1.0.
```json
{
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_interval": <int, second, min=30, max=4294968>
}
```

### boxfinder

Tracking profile for Galileosky Boxfinder v1.0.
```json
{
    "shock_value": <double, g, min=0.5, max=4>,
    "sleep_timeout": <int, minute, min=1, max=1440>
}
```

### bsj

Tracking profile for BSJ KM-01/02, Gosafe G1C.
```json
{
    "tracking_angle": <int, degree, min=5, max=180>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### c2stek_fl

Tracking profile for C2STEK FL10, C2STEK FL2000G.
```json
{
    "tracking_angle": <int, degree, min=0, max=360>,
    "tracking_distance": <int, meter, min=0, max=9999>,
    "tracking_interval": <int, second, min=0, max=9999>
}
```

### calamp

Tracking profile for CalAmp ATU-620, CalAmp LMU-1100, CalAmp LMU-1200, CalAmp LMU-200, CalAmp LMU-2030, CalAmp LMU-2600, CalAmp LMU-2630, CalAmp LMU-2720, CalAmp LMU-300, CalAmp LMU-3030, CalAmp LMU-3640, CalAmp LMU-400, CalAmp LMU-4200, CalAmp LMU-4230, CalAmp LMU-4520, CalAmp LMU-5530, CalAmp LMU-700, CalAmp LMU-800, CalAmp LMU-900, CalAmp TTU-1200, CalAmp TTU-2830, CalAmp TTU-700.
```json
{
    "psm_interval": <int, second, min=30, max=86400>,
    "tracking_angle": <int, degree, min=5, max=180>,
    "tracking_distance": <int, meter, min=50, max=5000>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### cantrack_t80

Tracking profile for Cantrack T80.
```json
{
    "tracking_interval": <int, second, min=10, max=1000>
}
```

### careu

Tracking profile for CAREU U1 Lite Plus, CAREU U1 Plus, CAREU UT1, CAREU UW1, CAREU Ucan, CAREU Ueco, CAREU Ugo, IntelliTrac A1, Intellitrac S1.
```json
{
    "tracking_angle": <int, degree, min=5, max=180>,
    "tracking_distance": <int, meter, min=25, max=50000>,
    "tracking_interval": <int, second, min=10, max=65535>
}
```

### cargo

Tracking profile for Cargo Light 2, Cargo Mini 2, Cargo Pro 2.
```json
{
    "psm_interval": <int, second, min=30, max=86400>,
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=100, max=100000>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### carscop_cctr800

Tracking profile for Carscop CCTR-808S, Carscop CCTR-809.
```json
{
    "psm_interval": <int, second, min=3600, max=432000>,
    "psm_mode": <int, min=0, max=1>,
    "tracking_interval": <int, second, min=30, max=999>
}
```

### carscop_cctr830

Tracking profile for Carscop CCTR-830, Toptracking CCTR-830G.
```json
{
    "tracking_interval": <int, second, min=30, max=999>
}
```

### castel_idd

Tracking profile for Castel IDD-213.
```json
{
    "sleep_report_interval": <int, minute, min=10, max=1440>,
    "tracking_angle": <int, degree, min=10, max=90>,
    "tracking_distance": <int, meter, min=50, max=5000>,
    "tracking_interval": <int, second, min=30, max=600>,
    "upload_records_count": <int, min=1, max=10>
}
```

### castel_interval

Tracking profile for Castel MPIP-620, Castel PT-690, Castel PT-718S.
```json
{
    "tracking_interval": <int, second, min=10, max=18000>
}
```

### cguard
cGuard tracking profile.

name: ‘cguard’
```json
{
    "tracking_interval": <int, second, min=0, max=65535, default=60> [required],
    "tracking_distance": <int, meter, min=0, max=65535, default=100> [required],
    "tracking_angle" : <int, degree, min=0, max=180, default=15> [required],
    "psm_interval": <int, second, min=0, max=65535, default=300> [required]
}
```
*   **tracking_interval**: interval in seconds, e.g. 30 means that the device will send traсking data every 30 seconds.
*   **tracking_distance**: distance in meters, e.g. 100 means that the device will send data every 100 meters.
*   **tracking_angle**: the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
*   **psm_interval**: duration in seconds for the device to stay in the deep sleep mode.

### cguard_asset

cGuard tracking profile for asset trackers.

name: ‘cguard_asset’
```json
{
    "tracking_interval": <int, second, min=0, max=65535, default=60> [required],
    "tracking_distance": <int, meter, min=0, max=65535, default=100> [required],
    "tracking_angle" : <int, degree, min=0, max=180, default=45> [required],
    "psm_interval": <int, second, min=0, max=65535, default=300> [required],
    "mode": <string, TRACKER|ASSET, default=ASSET> [required],
    "wakeup_type": <string, SCHEDULED|PERIODICAL, default=PERIODICAL> [required if mode == 'ASSET'],
    "wakeup_day": <string, EVERYDAY|MONDAY|TUESDAY|WEDNESDAY|THURSDAY|FRIDAY|SATURDAY|SUNDAY, default=EVERYDAY> [required if wakeup_type == 'SCHEDULED'],
    "wakeup_time": <string, format 'HH:mm', default='12:00'> [required if wakeup_type == 'SCHEDULED'],
    "wakeup_period": <int, minutes, min=15, max=65535, default=1440> [required if wakeup_type == 'PERIODICAL'],
    "moving_detection": <boolean, default='true'> [required if mode == 'ASSET'],
}
```
*   tracking_interval: interval in seconds, e.g. 30 means that the device will send traсking data every 30 seconds.
*   tracking_distance: distance in meters, e.g. 100 means that the device will send data every 100 meters.
*   tracking_angle: the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees.
*   psm_interval: duration in seconds for the device to stay in the deep sleep mode.
*   mode: device working mode. ‘TRACKER’ means that device work in continuous mode. ‘ASSET’ means that device work in periodical mode and wakes up on schedule or by period.
*   wakeup_type: how device wakes up in ‘ASSET’ mode.
*   wakeup_day: what day to wake up if wakeup_type == ‘SCHEDULED’.
*   wakeup_time: what time to wake up if wakeup_type == ‘SCHEDULED’.
*   moving_detection: ‘true’ means that device will be wakes up at the beginning of the movement.

### concox_distance_interval

Tracking profile for Concox X3.
```json
{
    "tracking_distance": <int, meter, min=100, max=10000>,
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### concox_gt350

Tracking profile for Concox GT350.
```json
{
    "psm_interval": <int, second, min=600, max=432000>,
    "psm_mode": <int, min=0, max=1>,
    "tracking_interval": <int, second, min=10, max=1800>
}
```

### concox_gt700

Tracking profile for Concox AT3, Concox AT4, Concox GT710.
```json
{
    "psm_interval": <int, min=1, max=24, valid_values=[1, 2, 3, 4, 6, 8, 12, 24]>,
    "tracking_interval": <int, min=1, max=30>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>,
    "wakeup_time": <string, pattern="hh:mm">
}
```

### concox_interval

Tracking profile for Concox GK309 , Concox GS503, Concox GT03A, Concox GT03C, Concox WeTrack Lite, Concox WeTrack2, Jimi JI09.
```json
{
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### concox_jv200

Tracking profile for Concox JV200.
```json
{
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### concox_qbit

Tracking profile for Concox QBIT.
```json
{
    "gps_tracking_interval": <int, second, min=10, max=18000>,
    "lbs_tracking_interval": <int, second, min=10, max=86400>,
    "mode": <string, lbs | gps>
}
```

### concoxgt02

Tracking profile for Concox GT02 / TR02.
```json
{
    "tracking_interval": <int, second, min=30>
}
```

### concoxgt06

Tracking profile for Concox GV20, Concox X1, Protrack VT05.
```json
{
    "psm_interval": <int, second, min=30, max=65535>,
    "tracking_angle": <int, degree, min=0, max=180>,
    "tracking_distance": <int, meter, min=50, max=10000>,
    "tracking_interval": <int, second, min=30, max=65535>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>
}
```

### default

Default tracking profile.
```json
{
    "type": <string>,           // can be "interval" (send tracking data based on time intervals) or "distance" (send tracking data after passing specified distance)
    "tracking_interval": <int>, // interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds
    "tracking_distance": <int>  // distance in meters, e.g. 100 means that the device will send data every 100 meters
}
```

### default_angle

Default profile with optional angle-based tracking.
```json
{
    "type": <string>,           // can be "interval" (send tracking data based on time intervals) or "distance" (send tracking data after passing specified distance)
    "tracking_interval": <int>, // interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds
    "tracking_distance": <int>, // distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>    // optional, if specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
}
```

### default_powersave

Default powersave profile with optional angle-based tracking.
```json
{
    "type": <string>,           // can be "interval" (send tracking data based on time intervals), "distance" (send tracking data after passing specified distance) or "power_save"
    "tracking_interval": <int>, // optional, interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds, can be absent if type=power_save
    "tracking_distance": <int>, // optional, distance in meters, e.g. 100 means that the device will send data every 100 meters, can be absent if type=power_save
    "tracking_angle" : <int>,   // optional, if specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
    "psm_interval": <int>,      // optional, Define the time interval in seconds (60-65535) which the unit stays in the sleeping state when type=power_save
    "psm_mode": <int>           // optional, Define the sleep level when type != power_save, 0 - no sleeping, 1 - light sleep(GPS Off, GPRS On, G-sensor On),
                                // 2- deep sleep(GPS Off, GPRS Off, G-sensor On)
}
```

### defenstar_007

Tracking profile for Defenstar DS007.
```json
{
    "tracking_interval": <int, second, min=60, max=65534>
}
```

### defenstar_008

Tracking profile for Defenstar DS008, Gubloos GPS-S1.
```json
{
    "tracking_interval": <int, second, min=10, max=9999>
}
```

### digitalsystems_dsf22

Tracking profile for DigitalSystems DSF22.
```json
{
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### distance_interval

Tracking profile with distance and interval.
```json
{
    "tracking_distance": <int, meter, min=50, max=100000>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### distance_interval_angle_ps

Tracking profile with distance, interval, angle and powersave mode.
```json
{
    "psm_interval": <int, second, min=30, max=86400>,
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=50, max=100000>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### distance_interval_angle

Tracking profile with distance, interval and angle.
```json
{
    "tracking_interval": <int>, // interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds
    "tracking_distance": <int>, // distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>    // device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
}
```

### eelink

Tracking profile for Eelink GOT08, Eelink GOT10, Eelink GPT18, Eelink TK-319, Eelink TK116, Eelink TK119.
```json
{
    "tracking_interval": <int, second, min=10, max=18000>
}
```

### eelink_tk116

Tracking profile for Eelink TK116.
```json
{
    "tracking_interval": <int, second, min=10, max=3600>
}
```

### eelink_v2

Tracking profile for Eelink GPT18, Eelink TK-319.
```json
{
    "active_tracking_interval": <int, second, min=30, max=65535>,
    "gps_working_mode": <string, always_on | auto>,
    "gsm_working_mode": <string, always_on | auto>,
    "tracking_angle": <int, degree, min=0, max=180>,
    "tracking_distance": <int, meter, min=50, max=10000>,
    "tracking_interval": <int, second, min=30, max=65535>
}
```

### enfora

Tracking profile for Enfora MT-GL (GSM2218), Enfora MT-Gu (GSM2338), Novatel MT4100, SkyPatrol TT8740, SkyPatrol TT8750.
```json
{
    "tracking_distance": <int, meter, min=100, max=10000>,
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### esino

Tracking profile for Esino ES-GP34, Esino ES-GT23.
```json
{
    "tracking_interval": <int, second, min=20, max=3600>
}
```

### etrack_tlt2h

Tracking profile for E-Track TLT-2H.
```json
{
    "tracking_interval": <int, second, min=10, max=59999>
}
```

### fifotrack

Tracking profile for fifotrack A100, fifotrack A100 FW1.15+, fifotrack A300, fifotrack A300 FW1.23+, fifotrack A600 (FW before V1.07), fifotrack A600 FW1.07+.
```json
{
    "psm_interval": <int, second, min=0, max=3932100>,
    "psm_mode": <int, min=0, max=2>,
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=30, max=655350>
}
```

### genesis_g36

Tracking profile for Castel HT-770, Ezlink T28, G36, Orion 7, XiLi Technologies PT100.
```json
{
    "tracking_interval": <int, second, min=1>
}
```

### gl200

Queclink/Ruslink GL200/GL300 profile
```json
{
    "type": <string>,               // tracking type "distance" or "interval" or "power_save"
    "tracking_interval": <int>,     // interval in seconds, e.g. 30 means that the device will send traсking data every 30 seconds
    "tracking_distance": <int>,     // distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>,       // the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
    "psm_interval": <int>,          // send interval when the tracking type is "power_save", seconds
    "movement_detection": <boolean>,
    "non_movement_duration": <int>, // in seconds
}
```

### gl500

Queclink/Ruslink GL500 profile.
```json
{
    "type": <string>,           // interval or power_save
    "tracking_interval": <int>, // interval in minutes
    "wakeup_time": <string>,    // wakeup time for power_save mode in format HH:mm
    "psm_interval": <int>,      // update interval in power_save mode, hours (1, 2, 3, 4, 6, 8, 12, 24)
}
```

### gt300

Queclink/Ruslink GT300 profile.
```json
{
    "tracking_interval": <int>,      // tracking interval in seconds, 5-86400 seconds
    "start_time": <string>,          // start time of scheduled fix timing report. The valid format is "HHMM" 0000-2359
    "end_time": <string>,            // end time of scheduled fix timing report. The valid format is "HHMM" 0000-2359
    "movement_detection": <boolean>, // enable suspend reports if the device at rest
    "min_speed": <int>,              // The speed threshold of movement detect, km/h 0-999
    "min_distance": <int>            // The distance threshold of movement detect, meters 1-9099
}
```

### gotoptk206_amgps_freko

Tracking profile for AMGPS Freko.
```json
{
    "tracking_interval": <int, second, min=10, max=3600>
}
```

### gv500

Queclink/Ruslink GV500 profile.
```json
{
    "type": <string>,           // tracking type when ignition is ON, "distance" or "interval"
    "tracking_interval": <int>, // interval in seconds, e.g. 30 means that the device will send traсking data every 30 seconds
    "tracking_distance": <int>, // distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>,   // the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
    "psm_mode": <int>,          // Define the power saving  mode, 0 - no sleeping,
                                // 1 - no GPS report when the device is a standstill or the engine is off,
                                // 2 - send GPS report with psm_interval when the engine is off
    "psm_interval": <int>       // send interval when the engine is off, seconds
}
```

### gv55lite
Queclink/Ruslink GV55Lite profile.
```json
{
    "type": <string>,           // tracking type when ignition is ON, "distance" or "interval"
    "tracking_interval": <int>, // interval in seconds, e.g. 30 means that the device will send traсking data every 30 seconds
    "tracking_distance": <int>, // distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>,   // the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
    "psm_mode": <int>,          // Define the power saving  mode, 0 - no sleeping,
                                // 1 - no GPS report when the device is a standstill or the engine is off,
                                // 2 - send GPS report with psm_interval when the engine is off
    "psm_interval": <int>       // send interval when the engine is off, seconds
}
```

### gubloost1

Tracking profile for Defenstar GPS668, Gubloos GPS-T1, MiniFinder Pico.
```json
{
    "tracking_interval": <int, second, min=10, max=9999>
}
```

### haicom_hi603x

Tracking profile for Haicom HI-603X.
```json
{
    "tracking_interval": <int, second, min=30, max=2592000>
}
```

### helioversal_m1

Tracking profile for Helioversal M1.
```json
{
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### hhd_g

Tracking profile for HHD G-400, HHD G-600.
```json
{
    "tracking_interval": <int, second, min=20>
}
```

### howen_herome

Tracking profile for Hero-ME31-08, Hero-ME32-04, Hero-ME41-04.
```json
{
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### hua_sheng_hs3000g

Tracking profile for Hua Sheng HS 3000G.
```json
{
    "psm_interval": <int, second, min=60, max=86400>,
    "tracking_angle": <int, degree, min=5, max=250>,
    "tracking_interval": <int, second, min=30, max=450>
}
```

### huabao

Tracking profile for Huabao HB-T10.
```json
{
    "tracking_interval": <int, second, min=10, max=9999>
}
```

### intellitrac_x1

Tracking profile for IntelliTrac X1, IntelliTrac X1+.
```json
{
    "tracking_angle": <int, degree, min=5, max=358>,
    "tracking_distance": <int, meter, min=100, max=65534>,
    "tracking_interval": <int, second, min=30, max=65534>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>
}
```

### interval

Tracking profile with interval only.
```json
{
    "tracking_interval": <int> // interval in seconds, min 30
}
```

### interval_angle

Tracking profile with interval and angle.
```json
{
    "tracking_interval": <int>, // interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds
    "tracking_angle" : <int>    // device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
}
```

### interval_angle_powersave

Tracking profile with interval, angle and powersave mode.
```json
{
    "psm_interval": <int, second, min=60, max=86400>,
    "tracking_angle": <int, degree, min=5, max=355>,
    "tracking_interval": <int, second, min=30, max=900>
}
```

### interval_powersave

Tracking profile with interval and powersave mode.
```json
{
    "psm_interval": <int, second, min=300, max=86400>,
    "psm_mode": <int, min=0, max=1>,
    "tracking_interval": <int, second, min=10, max=180>
}
```

### jimi_jc100

Tracking profile for Jimi JC100.
```json
{
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### jinsheng_js810

Tracking profile for Jin Sheng JS810, Jin Sheng JS810S.
```json
{
    "tracking_interval": <int, second, min=30, max=65534>
}
```

### jointech_gp

Tracking profile for Jointech GP4000, Jointech GP6000, Jointech GP6000F.
```json
{
    "psm_interval": <int, second, min=300, max=65535>,
    "psm_mode": <int, min=1, max=3>,
    "tracking_angle": <int, degree, min=10, max=90>,
    "tracking_distance": <int, meter, min=100, max=65535>,
    "tracking_interval": <int, second, min=30, max=65535>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>
}
```

### jointech_jt701

Tracking profile for Jointech JT701.
```json
{
    "tracking_interval": <int, second, min=10, max=60000>
}
```

### jointech_jt703
Profile for Jointech JT703B
```json
{
    "tracking_interval": <int, 10-60000>, // interval in seconds
    "sleep_mode": "enabled" | "disabled",
    "wakeup_timers": [<local time in standard format "HH:mm:ss">, ...] // optional, define wake-up timers when the sleep mode is enabled, 1-48 timers
    "sleep_time_in_minutes": <int, optional, 30-1440>, // define the time interval which the unit stays in the sleeping state when wake-up timers are not defined
}
```

### jointech_jt707

Tracking profile for Jointech JT707.
```json
{
    "psm_interval": <int, minute, min=10, max=1440>,
    "psm_mode": <int, min=0, max=1>,
    "tracking_interval": <int, second, min=5, max=43200>
}
```

### keson_ks168

Tracking profile for Keson KS168.
```json
{
    "tracking_interval": <int, second, min=10, max=65535>
}
```

### laipacs911

Tracking profile for Laipac S911 Lola, Laipac-911BL.
```json
{
    "tracking_distance": <int, meter, min=50, max=100000>,
    "tracking_interval": <int, second, min=30, max=86400>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>
}
```

### lk200

Tracking profile for LKGPS LK209A, LKGPS LK209B, LKGPS LK210.
```json
{
    "tracking_interval": <int, second, min=30, max=65535>
}
```

### logosoft

Tracking profile for Logosoft Log-101.
```json
{
    "type": <string>,           // tracking type "interval" or "distance" or "intelligent"
    "tracking_interval": <int>, // interval in seconds, min 30
    "tracking_distance": <int>, // distance in meters, min 300
    "tracking_angle" : <int>    // angle, degrees, min 10
}
```

### m7

Profile for Navixy M7.
```json
{
    "type": <string>,           // can be "interval" (send tracking data based on time intervals), "distance" (send tracking data after passing specified distance)
    "psm_mode": <int>,          // power save mode, 0 - disable, 1 - powersave without timers, 2 - powersave with timers
    "tracking_interval": <int>, // optional, interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds
    "tracking_distance": <int>, // optional, distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>,   // optional, if specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
    "psm_interval": <int>,      // optional, Define the time interval in seconds (600-3932100) which the unit stays in the sleeping state
    "wakeup_timer1": <string>,  // optional, timer 1
    "wakeup_timer2": <string>,  // optional, timer 2
    "wakeup_timer3": <string>   // optional, timer 3
}
```

### maxtrack_140

Tracking profile for Maxtrack MXT-140.
```json
{
    "tracking_angle": <int, degree, min=10, max=180>,
    "tracking_distance": <int, meter, min=0, max=25500>,
    "tracking_interval": <int, second, min=20, max=65535>
}
```

### megastek_gvt430

Tracking profile for Megastek GVT-430.
```json
{
    "tracking_angle": <int, degree, min=10, max=60>,
    "tracking_distance": <int, meter, min=100, max=1000>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### megastek_mt

Tracking profile for Megastek MT-300, Megastek MT-90s, Megastek MT100.
```json
{
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### megastek_mt100

Tracking profile for Megastek MT100.
```json
{
    "tracking_distance": <int, meter, min=50, max=100000>,
    "tracking_interval": <int, second, min=30, max=65535>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>
}
```

### meiligaovt

Tracking profile for GoTop VT360, GoTop VT380, Meiligao VT310, Meitrack VT310, RedView VT310.
```json
{
    "tracking_angle": <int, degree, min=0, max=359>,
    "tracking_distance": <int, meter, min=50, max=5000>,
    "tracking_interval": <int, second, min=10, max=655350>
}
```

### meitrack

Meitrack profile.
```json
{
    "tracking_interval": <int>, // interval in seconds, e.g. 30 means that the device will send traсking data every 30 seconds
    "tracking_distance": <int>, // distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>,   // the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
    "psm_mode": <int>,          // optional, Define the sleep level, 0 - no sleeping, 1- light sleep(GPS Off, GPRS On, G-sensor On),
                                // 2- deep sleep(GPS Off, GPRS Off, G-sensor On)
    "psm_interval": <int>       // duration in seconds for the device to stay in the deep sleep mode
}
```

### meitrack_asset

Tracking profile for Meitrack T355v2.
```json
{
    "psm_interval": <int, second, min=0, max=3932100>,
    "psm_mode": <int, min=0, max=2>,
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=30, max=655350>
}
```

### meitrack_vehicle

Tracking profile for Meitrack MVT100, Meitrack MVT340, Meitrack MVT380, Meitrack MVT600, Meitrack T1, Meitrack T3, Meitrack T333, Meitrack T366G, Meitrack T366L, Meitrack T622G, Meitrack TC68S, Meitrack TC68SG.
```json
{
    "on_stop_tracking_interval": <int, second, min=0, max=655350>,
    "psm_interval": <int, second, min=0, max=3932100>,
    "psm_mode": <int, min=0, max=2>,
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=30, max=655350>
}
```

### meitrack_without_ps

Tracking profile for Meitrack P66.
```json
{
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=30, max=655350>
}
```

### mictrack_mp90

Tracking profile for MicTrack MP-90.
```json
{
    "tracking_angle": <int, degree, min=20, max=180>,
    "tracking_interval": <int, second, min=10, max=65535>
}
```

### mika_g1

Tracking profile for MIKA G1.
```json
{
    "tracking_interval": <int, second, min=30, max=10000>
}
```

### mrd_100

Tracking profile for MRD-100.
```json
{
    "tracking_interval": <int, second, min=20, max=65535>
}
```

### mwp008_a

Tracking profile for Diwei TK116, Moralwinhk P008A, Moralwinhk P168.
```json
{
    "tracking_interval": <int, second, min=10, max=655350>
}
```

### myrope_m500

Tracking profile for MyRope M528, MyRope M588.
```json
{
    "psm_interval": <int, second, min=60, max=65535>,
    "tracking_distance": <int, meter, min=1, max=65535>,
    "tracking_interval": <int, second, min=1, max=65535>
}
```

### navisetgt

Tracking profile for Naviset GT-10, Naviset GT-20.
```json
{
    "tracking_angle": <int, degree, min=5, max=180>,
    "tracking_distance": <int, meter, min=50, max=255>,
    "tracking_interval": <int, second, min=10, max=300>
}
```

### noran

Tracking profile for Noran NR008, Noran NR024, Noran NR100.
```json
{
    "tracking_interval": <int, second, min=15, max=64800>
}
```

### oigo_ar2

Tracking profile for Oigo AR-2GM, Oigo AR-3HU.
```json
{
    "psm_interval": <int, second, min=15, max=604800>,
    "tracking_angle": <int, degree, min=0, max=180>,
    "tracking_distance": <int, meter, min=0, max=60000>,
    "tracking_interval": <int, second, min=15, max=604800>
}
```

### orange_tk103

Tracking profile for Orange TK-103.
```json
{
    "tracking_interval": <int, second, min=30, max=990>
}
```

### piccolo_atx

Tracking profile for Piccolo ATX.
```json
{
    "tracking_interval": <int, second, min=300, max=86400>
}
```

### piccolo_distance_interval_angle

Tracking profile for Piccolo ATX2S, Piccolo Hybrid+, Piccolo STX, Piccolo TMX+.
```json
{
    "tracking_angle": <int, degree, min=30, max=150>,
    "tracking_distance": <int, meter, min=100, max=10000>,
    "tracking_interval": <int, second, min=30, max=65535>
}
```

### piccolo_plus

Profile Wireless Links for Piccolo Plus
```json
{
    "sleep_mode": "disabled" | "engine" | "asset" | "hybrid",
    "track_by": "interval" | "distance", // optional, need for disabled, engine, hybrid modes
    "tracking_interval": <int, 60-86400>, // optional, interval in seconds, need for disabled, engine, hybrid modes
    "tracking_distance": <int, 100-10000>, // optional, distance in meters, need for disabled, engine, hybrid modes
    "track_by_angle": , // optional, need for disabled, engine, hybrid modes
    "tracking_angle": <int, 30-150>, // optional, if specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees, need for disabled, engine, hybrid modes
    "asset_moving_interval": <int, 300-86400>, // optional, need for asset and hybrid modes
    "asset_stopped_interval": <int, 300-86400> // optional, need for asset and hybrid modes
}
```

### redview_vt680

Tracking profile for RedView VT680.
```json
{
    "tracking_angle": <int, degree, min=30, max=270>,
    "tracking_interval": <int, second, min=10, max=655350>
}
```

### sanfone

Tracking profile for Sanfone SF100, Sanfone SF700.
```json
{
    "tracking_angle": <int, degree, min=10, max=360>,
    "tracking_distance": <int, meter, min=30, max=60000>,
    "tracking_interval": <int, second, min=30, max=999>
}
```

### satsol

Tracking profile for SAT-LITE 3, SAT-LITE 4, Sat Lite 2, Sat Pro, Super Lite.
```json
{
    "psm_interval": <int, second, min=30, max=86400>,
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=50, max=9999>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### senseitp211
```json
{
    "tracking_interval": <int>, // interval in seconds, min 30
    "gps_enabled": <boolean>
}
```

### sheriff_awax12

Tracking profile for Sheriff AWAX12.
```json
{
    "tracking_interval": <int, second, min=900, max=86400>
}
```

### sinowell_g102

Tracking profile for Sinowell G102.
```json
{
    "psm_interval": <int, second, min=10, max=65000>,
    "tracking_angle": <int, degree, min=5, max=180>,
    "tracking_distance": <int, meter, min=50, max=1000>,
    "tracking_interval": <int, second, min=10, max=1000>
}
```

### skypatrol_tt8750plus

Tracking profile for SkyPatrol TT8750+.
```json
{
    "psm_interval": <int, second, min=30, max=18000>,
    "tracking_angle": <int, degree, min=10, max=359>,
    "tracking_distance": <int, meter, min=100, max=10000>,
    "tracking_interval": <int, second, min=30, max=18000>
}
```

### sleep_active

Tracking profile for СКАТ-Маяк.
```json
{
    "active_time": <int, second, min=300, max=599940>,
    "sleep_time": <int, second, min=300, max=599940>
}
```

### spetrotec_iwatcher

Tracking profile for Spetrotec i-WATCHER AVL.
```json
{
    "tracking_distance": <int, meter, min=100, max=100000>,
    "tracking_interval": <int, second, min=60, max=86400>,
    "type": <string, interval | distance | power_save | distance_interval_angle | interval_angle | intelligent>
}
```

### stab_liner

Tracking profile for M2M-Cyber GLX, STAB Liner 102.
```json
{
    "psm_interval": <int, second, min=0, max=3600>,
    "tracking_angle": <int, degree, min=0, max=180>,
    "tracking_distance": <int, meter, min=50, max=100000>,
    "tracking_interval": <int, minute, min=0, max=3600>
}
```

### starcom_helios

Tracking profile for Starcom Helios Advanced, Starcom Helios Hybrid, Starcom Helios TT.
```json
{
    "tracking_interval": <int, second, min=0, max=432000>
}
```

### starline_m17

Tracking profile for Starline M17.
```json
{
    "psm_interval": <int, second, min=60, max=3540>,
    "psm_mode": <int, min=0, max=1>,
    "tracking_interval": <int, second, min=0, max=300>
}
```

### suntech_distance_interval_angle

Tracking profile for Suntech ST200, Suntech ST215, Suntech ST300, Suntech ST310U, Suntech ST340LC, Suntech ST600R, Suntech ST600V, Suntech ST650.
```json
{
    "tracking_angle": <int, degree, min=0, max=180>,
    "tracking_distance": <int, meter, min=50, max=60000>,
    "tracking_interval": <int, second, min=20, max=60000>
}
```

### suntech_interval

Tracking profile for Suntech ST940.
```json
{
    "tracking_interval": <int, second, min=20, max=60000>
}
```

### syrus

Tracking profile for Syrus 2G.
```json
{
    "tracking_angle": <int, degree, min=5, max=90>,
    "tracking_distance": <int, meter, min=100, max=5000>,
    "tracking_interval": <int, second, min=30, max=9999>
}
```

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
*   **tracking_angle** – **int**, degrees 10-255, the device will send tracking data when course changing more than defined value
*   **tracking_distance** – **int**, distance in meters 50-65535, e.g. 100 means that the device will send data every 100 meters
*   **tracking_interval** – **int**, interval in seconds 30-255, e.g. 30 means that the device will send tracking data no more frequently than every 30 seconds.
*   **on_stop_tracking_interval** – **int**, on stop interval in seconds 30-65535, e.g. 30 means that the device will send tracking data not less frequently than every 30 seconds.
*   **sleep_mode** – **string**, disabled | soft_sleep
*   **stop_detection** – **string**, ignition | g_sensor | gps

### telfm5x

Tracking profile for Teltonika FM5500, Teltonika FM6320, Teltonika FMB630, Teltonika FMB640.
```json
{
    "sleep_mode": <string, disabled | soft_sleep>,
    "sleep_timeout": <int, second, min=300, max=2592000>,
    "tracking_angle": <int, degree, min=0, max=180>,
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=30, max=2592000>
}
```

### topfly

Tracking profile for TopFlyTech T8603, TopFlyTech T8608, TopFlyTech T8803, TopFlyTech T8803 Pro, TopFlyTech T8803+, TopFlyTech T8806, TopFlyTech T8806+, TopFlyTech T8806+R, TopFlyTech T8808A, TopFlyTech T8808A+, TopFlyTech T8808B, TopFlyTech T8808B+.
```json
{
    "psm_interval": <int, second, min=0, max=65535>,
    "tracking_angle": <int, degree, min=0, max=90>,
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=0, max=65535>
}
```

### topshine_distance_interval

Tracking profile for TopShine MT02, TopShine MT08, TopShine OGT100, TopShine VT1000, TopShine VT200W, TopShine VT900.
```json
{
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=10, max=655350>
}
```

### topshine_distance_interval_angle

Tracking profile for TopShine MT08, TopShine OGT100, TopShine VT1000.
```json
{
    "tracking_angle": <int, degree, min=0, max=359>,
    "tracking_distance": <int, meter, min=50, max=65535>,
    "tracking_interval": <int, second, min=10, max=655350>
}
```

### topten

Tracking profile for TopTen GT08, TopTen TK-510, TopTen TK228.
```json
{
    "tracking_angle": <int, degree, min=0, max=359>,
    "tracking_interval": <int, second, min=10, max=655350>
}
```

### totarget

Tracking profile for TT-08, VG-eLock7A.
```json
{
    "tracking_interval": <int, second, min=30, max=300>
}
```

### totem

Tracking profile for TotemTech AT05, TotemTech AT07.
```json
{
    "psm_interval": <int, second, min=10, max=18000>,
    "tracking_angle": <int, degree, min=10, max=180>,
    "tracking_distance": <int, meter, min=10, max=18000>,
    "tracking_interval": <int, second, min=10, max=18000>
}
```

### trackertech_msp320

Tracking profile for Tracker Technology MSP320.
```json
{
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### trackertech_msp340

Tracking profile for Tracker Technology MSP340.
```json
{
    "psm_interval": <int, second, min=180, max=86400>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### trackertech_msp350

Tracking profile for Tracker Technology MSP350.
```json
{
    "psm_interval": <int, second, min=60, max=2147483647>,
    "psm_mode": <int, min=0, max=3>,
    "tracking_distance": <int, meter, min=50, max=100000>,
    "tracking_interval": <int, second, min=30, max=86400>
}
```

### tramigo

Profile for Tramigo models that do not support the interval in seconds
```json
{
    "tracking_interval": <int, 1-10080>, // interval in minutes
    "tracking_distance": <float, 0.5-20>, // distance in kilometers
    "tracking_angle": <int, 20-180>, // the device will additionally send data when it changes direction to specified angle
    "on_stop_tracking_interval": <int, 1-10080>, // interval in minutes when not in trip
    "sleep_mode": "disabled" | "enabled"
}
```

### tramigo_with_seconds
Profile for Tramigo models that do support the interval in seconds
```json
{
    "tracking_interval": <int, 30-604800>, // interval in seconds
    "tracking_distance": <float, 0.5-20>, // distance in kilometers
    "tracking_angle": <int, 20-180>, // the device will additionally send data when it changes direction to specified angle
    "on_stop_tracking_interval": <int, 1-10080>, // interval in minutes when not in trip
    "sleep_mode": "disabled" | "enabled"
}
```

### tt1

Profile for Navixy TT-1.
```json
{
    "type": <string>,           // can be "interval" (send tracking data based on time intervals), "distance" (send tracking data after passing specified distance)
    "psm_mode": <int>,          // power save mode, 0 - disable, 1 - powersave mode, 2 - Back-up Battery Power Saving Mode
    "tracking_interval": <int>, // optional, interval in seconds, e.g. 30 means that the device will send tracking data every 30 seconds
    "tracking_distance": <int>  // optional, distance in meters, e.g. 100 means that the device will send data every 100 meters
    "tracking_angle" : <int>,   // optional, if specified, the device will additionally send data when it changes direction to specified angle, e.g. 30 degrees
    "psm_interval": <int>,      // optional, Define the time interval in seconds (60-65535) which the unit stays in the sleeping state when powersave mode
    "bat_voltage": <string>,    // optional, Threshold of low back-up battery voltage
    "bat_psm_interval": <int>   // optional, sleeping duration when battery voltage below defined threshold, seconds
}
```

### ulbotech_t300

Tracking profile for IMTSA TR2-OBD, Ulbotech T361, Ulbotech T381.
```json
{
    "tracking_angle": <int, degree, min=3, max=20>,
    "tracking_distance": <int, meter, min=0, max=25500>,
    "tracking_interval": <int, second, min=30, max=900>
}
```

### vjoy

Tracking profile for Kingneed C30, Kingneed T0024 / T4024, Kingneed T0026, Kingneed T1124, Kingneed T12, Kingneed T16/T18/T19, Kingneed T300, Kingneed T3124 / T5124, Kingneed T500, Kingneed T6024, Kingneed T6124, Kingneed T630, Kingneed T8124, Kingneed TK10, Kingneed TK101, Kingneed TK20, Kingneed TK5, VJOYCAR T0026G, VJOYCAR T13G, VJOYCAR T13GSE, VJOYCAR T633G, VJOYCAR TK10SDC, VJoy T12, VJoy TK05, VJoy TK10GSE, VJoy TK10GSE Solar, VJoy TK20SE.
```json
{
    "continuous_report_interval": <int, second, min=10, max=5940>,
    "motion_interval": <int, second, min=30, max=999>,
    "psm_mode": <int, min=0, max=1>,
    "psm_wake_up_interval": <int, hour, min=1, max=99>
}
```

### xirgo

Tracking profile for Xirgo XT-2050C, Xirgo XT-2060G, Xirgo XT-2150C, Xirgo XT-2160G, Xirgo XT-2450V, Xirgo XT-2460G, Xirgo XT-4750C, Xirgo XT-4760G, Xirgo XT-4850C.
```json
{
    "psm_interval": <int, second, min=60, max=2592000>,
    "tracking_angle": <int, degree, min=10, max=180>,
    "tracking_distance": <int, mile, min=1, max=100>,
    "tracking_interval": <int, second, min=30, max=2592000>
}
```

### xirgo_48

Tracking profile for Xirgo XT-4850C.
```json
{
    "psm_interval": <int, second, min=600, min=60, max=2592000>,
    "tracking_angle": <int, degree, min=10, max=180>,
    "tracking_distance": <int, mile, min=1, max=100>,
    "tracking_interval": <int, second, min=30, max=2592000>
}
```

### xirgo_dist

Tracking profile for Xirgo XT-2050C, Xirgo XT-2060G, Xirgo XT-2450V, Xirgo XT-2460G, Xirgo XT-4750C, Xirgo XT-4760G.
```json
{
    "psm_interval": <int, second, min=60, max=2592000>,
    "tracking_angle": <int, degree, min=10, max=180>,
    "tracking_distance": <int, mile, min=1, max=100>,
    "tracking_interval": <int, second, min=30, max=2592000>
}
```

### yatut_poisk

"Я ТУТ ПОИСК" tracking profile.

name: ‘yatut_poisk’
```json
{
    "mode": <string, DAILY|TEST|SEARCH, default=DAILY> [required],
    "main_wakeup_time": <string, format 'HH:mm', default='12:00'> [required if mode == 'DAILY'],
    "wakeup_period": <string, 8|12|24, default=24> [required if mode == 'DAILY'],
    "gps_determination_period": <int, days, min=0, max=30, default=0> [required if mode == 'DAILY'],
}
```
*   **mode**: device working mode.
*   **main_wakeup_time**: what time to wake up if mode == ‘DAILY’.
*   **wakeup_period**: only values ‘8’, ’12’ or ’24’ (hours).
*   **gps_determination_period**: how often to determine the position by satellites (in days). Zero (0) means on the each waking up.

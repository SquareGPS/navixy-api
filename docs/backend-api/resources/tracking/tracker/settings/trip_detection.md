---
title: /trip_detection
description: /trip_detection
---

## read()
Get trip detection settings for the specified tracker.

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.

#### return
```javascript
{
    "success": true,
    "min_idle_duration_minutes": <int>,  // number of minutes the device must be idle before trip is considered finished, e.g. 5
    "idle_speed_threshold": <int>,        // speed (km/h) below which the device is marked as being idle
    "ignition_aware": <boolean>,        // check ignition state to detect trip
    "motion_sensor_aware": <boolean>,        // check motion sensor state to detect trip
}
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)

## update()
Get trip detection settings for the specified tracker.

**required subuser rights:** tracker_update

#### parameters
* **tracker_id** - **int**. Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **min_idle_duration_minutes** - **int**. see read(). min=1, max=1440
* **idle_speed_threshold** - **int**. see read(). min=0, max=200
* **ignition_aware** - **boolean**. see read().
* **motion_sensor_aware** - **boolean**. see read().

#### return
```javascript
{"success": true}
```

#### errors
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)


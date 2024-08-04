---
title: Parking detection
description: API calls for getting and changing parking detection for the tracker.
---

# Parking detection

Contains API calls for getting and changing parking detection for the tracker. It is responsible for the parking detection 
function in the UI. The monitoring system automatically detects the facts of parking (states without movement), for the 
following purposes:

* To split a movement trajectory to separate trips - for clear illustration and easy viewing in tabular reports;
* To capture "Trip end" / "Trip start" events - with possibility of Email/SMS notification.


## API actions

API base path: `/tracker/settings/trip_detection`.

### `read`

Gets parking detection settings for the specified tracker.

#### Parameters

| name       | description                                                                                     | type | format |
|:-----------|:------------------------------------------------------------------------------------------------|:-----|:-------|
| tracker_id | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int  | 123456 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/trip_detection/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/trip_detection/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### Response

```json
{
    "success": true,
    "min_idle_duration_minutes": 5,
    "idle_speed_threshold": 3,
    "ignition_aware": false,
    "motion_sensor_aware": false
}
```

* `min_idle_duration_minutes` - int. Number of minutes the device must be idle before a trip considered finished.
* `idle_speed_threshold` - int. Speed (km/h) below which the device marked as being idle.
* `ignition_aware` - boolean. Check ignition state to detect a trip.
* `motion_sensor_aware` - boolean. Check motion sensor state to detect a trip.

#### Errors

* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.


### `update`

Updates parking detection settings for the specified tracker.

**required sub-user rights:** `tracker_update`.

#### Parameters

| name                      | description                                                                                       | type    | format |
|:--------------------------|:--------------------------------------------------------------------------------------------------|:--------|:-------|
| tracker_id                | ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.   | int     | 123456 |
| min_idle_duration_minutes | Number of minutes the device must be idle before a trip considered finished. Min=1, max=1440.     | int     | 5      |
| idle_speed_threshold      | Speed (km/h) below which the device marked as being idle. Min=0, max=200. If 0 - will never idle. | int     | 3      |
| ignition_aware            | Check ignition state to detect a trip.                                                            | boolean | false  |
| motion_sensor_aware       | Check motion sensor state to detect a trip.                                                       | boolean | false  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/settings/trip_detection/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "min_idle_duration_minutes": "5", "idle_speed_threshold": "3", "ignition_aware": false, "motion_sensor_aware": false}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/settings/trip_detection/update?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&min_idle_duration_minutes=5&idle_speed_threshold=3&ignition_aware=false&motion_sensor_aware=false
    ```

#### Response

```json
{"success": true}
```

#### Errors

* 204 – Entity not found (if there is no tracker with such ID belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).


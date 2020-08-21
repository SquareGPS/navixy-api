---
title: /tracker
description: /tracker
---

# /status/tracker/
This resource contains methods to read and assign status of a particular tracker.

### assign
Assign a status to the tracker.

#### parameters
* **tracker_id** – **int**. ID of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked.
* **new_status_id** – **int**. ID of the status. Must belong to status listing assigned to this tracker.

#### response
```json
{
  "success": true,
  "last_change": { //object describing last change of the status. May be null
    "id": 11,
    "old_status_id": null, //previous status ID. May be null.
    "new_status_id": 2, //Current status ID. May be null.
    "location": { //Location and address at which status change occurred
      "lat": 11.0,
      "lng": 22.0,
      "address": "Jones st, 4"
    },
    "changed": "2015-11-22 02:02:02", //change date and time
    "origin": "supervisor" //origin – who changed the status ("employee" or "supervisor")
  }
}
```

#### errors
*   13 (Operation not permitted) – if status listing does not allow for supervisor to change status
*   201 (Not found in database) – if there is no tracker with such ID belonging to authorized user
*   204 (Entity not found) – if there is no listing assigned to this tracker containing with such ID
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if specified tracker is a clone
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available
*   263 (No change needed, old and new values are the same) – if new status is equal to current status of tracker

### list
Get current assigned statuses for the specified trackers.

#### parameters
* **trackers** – **array of int**. List of the tracker’s IDs belonging to authorized user.

#### response
```json
{
    "success": true,
    "value": {                       // Map with tracker's IDs as keys.
        "5344": {
            "current_status": {      // Status object showing current status of tracker. May be null.
                "id": 66,
                "label": "Busy",
                "color": "FFC107"
            },
            "last_change": {         // Object describing last change of the status. May be null.
                "id": 441,
                "old_status_id": 65, // Previous status ID. May be null.
                "new_status_id": 66, // Current status ID. May be null.
                "location": {        // Location and address at which status change occurred.
                    "lat": 55.60920599,
                    "lng": 37.71843797,
                    "address": "Moscow, Orekhovyy Bul'var, 14a"
                },
                "changed": "2017-05-02 07:40:39", // Change date and time.
                "origin": "supervisor"            // Origin – who changed the status ("employee" or "supervisor").
            }
        },
        "15595": {
            "current_status": null,
            "last_change": {
                "id": 123,
                "old_status_id": 67,
                "new_status_id": null,
                "location": {
                    "lat": 56.8267226,
                    "lng": 60.5947458,
                    "address": ""
                },
                "changed": "2016-03-14 04:58:32",
                "origin": "employee"
            }
        }
    }
}
```

#### errors
*   217 (Requested limit is too big) – limit is more than [maxHistoryLimit](../../../getting-started.md#constants)
*   221 (Device limit exceeded) – if device limit set for the user’s dealer has been exceeded
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with “statuses” tariff feature available

### read

Get current assigned status of the tracker.

#### parameters
* **tracker_id** – **int**. ID of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.

#### response
```json
{
  "success": true,
  "current_status": { //status object showing current status of tracker. May be null
    "id": 2,
    "label": "On duty",
    "color": "FFFF99"
  },
  "last_change": { //object describing last change of the status. May be null
    "id": 11,
    "old_status_id": null, //previous status ID. May be null.
    "new_status_id": 2, //Current status ID. May be null.
    "location": { //Location and address at which status change occurred
      "lat": 11.0,
      "lng": 22.0,
      "address": "Jones st, 4"
    },
    "changed": "2015-11-22 02:02:02", //change date and time
    "origin": "supervisor" //origin – who changed the status ("employee" or "supervisor")
  }
}
```

#### errors
*   201 (Not found in database) – if there is no tracker with such ID belonging to authorized user
*   208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason
*   219 (Not allowed for clones of the device) – if specified tracker is a clone
*   236 (Feature unavailable due to tariff restrictions) – if there is no trackers with "statuses" tariff feature available

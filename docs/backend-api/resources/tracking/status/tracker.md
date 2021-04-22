---
title: Tracker status
description: Tracker status
---

# Tracker status

This resource contains methods to read and assign status of a particular tracker.

API base path: `/status/tracker/`

### assign

Assign a status to the tracker.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |
| new_status_id | ID of the status. Must belong to status listing assigned to this tracker. | int | 5 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/tracker/assign' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456, "new_status_id": 5}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/tracker/assign?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456&new_status_id=5
    ```

#### response

```json
{
  "success": true,
  "last_change": {
    "id": 11,
    "old_status_id": null,
    "new_status_id": 2,
    "location": {
      "lat": 11.0,
      "lng": 22.0,
      "address": "Jones st, 4"
    },
    "changed": "2015-11-22 02:02:02",
    "origin": "supervisor"
  }
}
```

* `last_change` - object describing last change of the status. May be null.
    * `old_status_id` - int. Previous status ID. May be null.
    * `new_status_id` - int. Current status ID. May be null.
    * `location` - object. Location and address at which status change occurred.
    * `lat` - int. Latitude.
    * `lng` - int. Longitude.
    * `address` - string. Address of last change.
    * `changed` - [date/time](../../../getting-started.md#data-types). Change date and time.
    * `origin` - [enum](../../../getting-started.md#data-types). Origin – who changed the status ("employee" or "supervisor").

#### errors

* 13 (Operation not permitted) – if status listing does not allow for a supervisor to change status.
* 201 (Not found in the database) – if there is no tracker with such ID belonging to authorized user.
* 204 (Entity not found) – if there is no listing assigned to this tracker containing with such ID.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions or some other reason.
* 219 (Not allowed for clones of the device) – if specified tracker is a clone.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature 
available.
* 263 (No change needed, old and new values are the same) – if new status is equal to current status of tracker.

### list

Gets current assigned statuses for the specified trackers.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| trackers | List of the tracker's IDs belonging to authorized user. | int array | `[123456, 234567]` |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/tracker/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [123456,234567]}'
    ```

#### response

```json
{
    "success": true,
    "value": {
        "5344": {
            "current_status": {
                "id": 66,
                "label": "Busy",
                "color": "FFC107"
            },
            "last_change": {
                "id": 441,
                "old_status_id": 65,
                "new_status_id": 66,
                "location": {
                    "lat": 55.60920599,
                    "lng": 37.71843797,
                    "address": "Moscow, Orekhovyy Bul'var, 14a"
                },
                "changed": "2017-05-02 07:40:39",
                "origin": "supervisor"
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

* `value` - Map with a tracker's IDs as keys.
    * `current_status` - Status object showing current status of tracker. May be null.
    * `last_change` - Object describing last change of the status. May be null.
    * `old_status_id` - int. Previous status ID. May be null.
    * `new_status_id` - int. Current status ID. May be null.
    * `location` - Location and address at which status change occurred.
    * `changed` - [date/time](../../../getting-started.md#data-types). Date and time of change.
    * `origin` - [enum](../../../getting-started.md#data-types). Origin – who changed the status ("employee" or "supervisor").

#### errors

* 217 (Requested limit is too big) – limit is more than [history.maxLimit](../../commons/dealer.md).
* 221 (Device limit exceeded) – if device limit set for the user's dealer has been exceeded.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature
 available.

### read

Gets current assigned status of the tracker.

#### parameters

| name | description | type| format |
| :------ | :------ | :----- | :----- |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/status/tracker/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/status/tracker/read?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### response

```json
{
  "success": true,
  "current_status": {
    "id": 2,
    "label": "On duty",
    "color": "FFFF99"
  },
  "last_change": {
    "id": 11,
    "old_status_id": null,
    "new_status_id": 2,
    "location": {
      "lat": 11.0,
      "lng": 22.0,
      "address": "Jones st, 4"
    },
    "changed": "2015-11-22 02:02:02",
    "origin": "supervisor"
  }
}
```

* `current_status` - status object showing current status of tracker. May be null.
* `last_change` - object describing last change of the status. May be null.
    * `old_status_id` - int. Previous status ID. May be null.
    * `new_status_id` - int. Current status ID. May be null.
    * `location` - Location and address at which status change occurred.
    * `changed` - [date/time](../../../getting-started.md#data-types). Date and time of change.
    * `origin` - [enum](../../../getting-started.md#data-types). Origin – who changed the status ("employee" or "supervisor").

#### errors

* 201 (Not found in the database) – if there is no tracker with such ID belonging to authorized user.
* 208 (Device blocked) – if tracker exists but was blocked due to tariff restrictions, or some other reason.
* 219 (Not allowed for clones of the device) – if specified tracker is a clone.
* 236 (Feature unavailable due to tariff restrictions) – if there are no trackers with "statuses" tariff feature 
available.

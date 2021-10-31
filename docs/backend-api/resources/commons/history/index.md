---
title: Events history
description: Contains history entry object description and API calls to interact with it.
---

# Events history

Contains history entry object description and API calls to interact with it.

***

## Tracker history entry

```json
{
    "id": 1,
    "type": "tracker",
    "is_read": false,
    "message": "Alarm",
    "time": "2020-01-01 00:00:00",
    "event": "offline",
    "tracker_id": 2,
    "rule_id": 3,
    "track_id": 4,
    "location":{ 
        "lat": 50.0,
        "lng": 60.0,
        "precision": 50
    },
    "address": "address",
    "extra": {
        "task_id": null , 
        "parent_task_id": null,
        "counter_id": null,
        "service_task_id": null,
        "checkin_id": null,
        "place_ids": null,
        "last_known_location": false,
        "tracker_label": "Tracker label",
        "emergency": false,
        "employee_id": 4563
    }
}
```

* `id` - int. An id of event.
* `type` - [enum](../../../getting-started.md#data-types). Type of device. Can be "socket", "tracker", or "camera".
* `is_read` - boolean. If `true` the notification seen by user and marked as read.
* `message` - string. Notification message.
* `time` - [date/time](../../../getting-started.md#data-types). When this notification received.
* `event` - [enum](../../../getting-started.md#data-types). Type of history event extension. Available event types can be obtained by [/history/type/list](./history_type.md#list) action.
* `tracker_id` - int. An id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked.
* `rule_id` - int. An id of assigned rule.
* `track_id` - int. An id of a track on which the event happened.
* `location` - location object. Location where the event happened.
* `address` - string. Address of location or `""` (empty string) if no address for location.
* `extra` - object. Extra fields for events. Like for what task or tracker the event was.
    * `task_id` - int. Related task identifier.
    * `parent_task_id` - int. Related parent task identifier (for task checkpoint related history entries).
    * `counter_id` - int. Related counter identifier.
    * `service_task_id` - int. Related service task id.
    * `checkin_id` - int. Related check-in marker.
    * `place_ids` - int. Related place identifiers.
    * `last_known_location` - boolean. `true` if location may be outdated.
    * `tracker_label` - string. Tracker label.
    * `emergency` - boolean. `true` for emergency events with the same flag in a rule.
    * `employee_id` - int. Driver ID at the time of the event.

Date/time type described in [data types description section](../../../getting-started.md#data-types).

***

## API actions

API path: `/history`.

### read

Returns history entry with the specified id.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| id | [History entry](#tracker-history-entry) ID. | int |
| add_tracker_label | Optional. If `true` tracker label will be added to message. | boolean |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 11231, "add_tracker_label": true}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/history/read?hash=a6aa75587e5c59c32d347da438505fc3&id=11231&add_tracker_label=true
    ```

#### response

```json
{
    "success": true,
    "value": {
         "id": 1,
         "type": "tracker",
         "is_read": false,
         "message": "Alarm",
         "time": "2020-01-01 00:00:00",
         "event": "offline",
         "tracker_id": 2,
         "rule_id": 3,
         "track_id": 4,
         "location":{ 
             "lat": 50.0,
             "lng": 60.0,
             "precision": 50
         },
         "address": "address",
         "extra": {
             "task_id": null , 
             "parent_task_id": null,
             "counter_id": null,
             "service_task_id": null,
             "checkin_id": null,
             "place_ids": null,
             "last_known_location": false,
             "tracker_label": "Tracker label",
             "emergency": false,
             "employee_id": 4563
         }
    }
}
```

#### errors

* 201 – Not found in the database - when there are no history entries with that id.

***

### mark_read

Marks history entry as read by `id` (see: [Tracker history entry](#tracker-history-entry)).

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| id | [Tracker history entry](#tracker-history-entry) ID | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/mark_read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 11231}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/history/mark_read?hash=a6aa75587e5c59c32d347da438505fc3&id=11231
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database - when there are no history entries with that id.

***

### mark_read_all

Marks all the user's history entries read.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/mark_read_all' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/history/mark_read_all?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{ "success": true }
```

#### errors

* [General](../../../getting-started.md#error-codes) types only.
    

---
title: How to work with notifications
description: How to work with notifications that can be received by triggering alerts.
---

# How to work with notifications

Notifications important part of the tracking. A [created a rule](./use-rules.md#create) will track triggering of 
specified conditions and send events to emails and phones. It sends notifications to know that a condition triggered. 
Sometimes, necessary to store those notifications and history entries to use them in special reports, or they can be 
used for scripts build on APIs. Let's see how to work with them.

<hr>

## Obtain a list of history entries

### All unread events of user

Here can be used the call [history/unread/list](../resources/commons/history/history_unread.md#list) to get all unread events.

The call contains only two optional parameters:

* `limit` - int with a maximum count of entries in response
* `from` - a string containing the start [date/time](../getting-started.md#data-types) for searching. Without this parameter you will get all unread entries
 for the last 30 days.

In our example we need to obtain no more than 100 entries for last month. If today is 26-01-2021 then API request will be:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/unread/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "limit": 100, "from": "2020-12-26 00:00:00"}'
    ```

Response will contain a list of history entries with [information](../resources/commons/history/index.md#tracker-history-entry) 
that could be used for different purposes:

```json
{
    "success": true,
    "list": [{
         "id": 1,
         "type": "tracker",
         "is_read": false,
         "message": "Alarm",
         "time": "2020-12-31 00:00:00",
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
    }]
}
```

<hr>

### Events for specific trackers and time period

Here can be used the [history/tracker/list](../resources/commons/history/history_tracker.md#list) call to get all events 
for a specific tracker or trackers per necessary time period. Also, this call can return only specific event types with 
sorting by time if necessary.

The necessary parameters for the call:

* `trackers` - an int array. A list of [tracker ids](../resources/tracking/tracker/index.md#list) belong to user for which events will be searched.
* `from` - a string containing the start [date/time](../getting-started.md#data-types) for searching.
* `to` - a string containing the end [date/time](../getting-started.md#data-types) of searching. Must be after `from` date.

Optional parameters that could be used to get more specific information:

* `events` - a string array with necessary event types. All other events will be ignored. Default: all. To get the 
list of events use [tracker/history/type](../resources/commons/history/history_type.md#list) call. 
* `limit` - integer with a maximum count of entries in result.
* `ascending` - a boolean where sort ascending by time when it is `true` and descending when `false`.

In our example we need to obtain no more than 100 entries for December for one device sorted descending by time. Also, 
necessary to know only when the device entered and exited the geofence. API request will be:

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/tracker/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [123985], "from": "2020-12-01 00:00:00", "to": "2020-12-31 23:59:59", "events": ["inzone", "outzone"], "limit": 100, "ascending": false}'
    ```

Response will contain the [history entries](../resources/commons/history/index.md#tracker-history-entry) that match to our request.

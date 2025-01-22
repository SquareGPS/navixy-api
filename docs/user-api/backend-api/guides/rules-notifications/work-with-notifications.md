# Working with Notifications

Notifications are a crucial part of tracking. A [created rule](use-rules.md#creating-a-rule) tracks the triggering of specified conditions and sends events to emails and phones. Notifications alert users when a condition is triggered. Sometimes, it is necessary to store these notifications and history entries for special reports or for use in scripts built on APIs. This guide will show you how to work with them using the Navixy API.

## Obtain a List of History Entries

### All Unread Events of a User

Use the [`history/unread/list`](../../resources/commons/history/history_unread.md#list) call to get all unread events.

This call contains only two optional parameters:

- `limit`: An integer specifying the maximum count of entries in the response.
- `from`: A string containing the start [date/time](../../getting-started/introduction.md#data-types) for the search. Without this parameter, you will get all unread entries for the last 30 days.

Example: To obtain no more than 100 entries for the last month (assuming today's date is 2021-01-26), the API request will be:

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/history/unread/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "limit": 100, "from": "2020-12-26 00:00:00"}'
```

The response will contain a list of history entries with [information](../../resources/commons/history/index.md#tracker-history-entry) that can be used for various purposes:

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
         "location": { 
             "lat": 50.0,
             "lng": 60.0,
             "precision": 50
         },
         "address": "address",
         "extra": {
             "task_id": null, 
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

### Events for Specific Trackers and Time Period

Use the [`history/tracker/list`](../../resources/commons/history/history_tracker.md#list) call to get all events for specific trackers over a specified time period. This call can also return specific event types sorted by time if necessary.

### Required Parameters

- `trackers`: An array of integers. A [list of tracker IDs](../../resources/tracking/tracker/index.md#list) for which events will be searched.
- `from`: A string containing the start [date/time](../../getting-started/introduction.md#data-types) for the search.
- `to`: A string containing the end [date/time](../../getting-started/introduction.md#data-types) for the search. Must be after the `from` date.

### Optional Parameters

- `events`: An array of strings with the necessary event types. All other events will be ignored. Default is all. To get a list of events, use the [`tracker/history/type`](../../resources/commons/history/history_type.md#list) call.
- `limit`: An integer specifying the maximum count of entries in the result.
- `ascending`: A boolean that sorts the results in ascending order by time when `true` and descending when `false`.

Example: To obtain no more than 100 entries for December for one device, sorted in descending order by time, and to know only when the device entered and exited the geofence, the API request will be:

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/history/tracker/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [123985], "from": "2020-12-01 00:00:00", "to": "2020-12-31 23:59:59", "events": ["inzone", "outzone"], "limit": 100, "ascending": false}'
```

The response will contain the [history entries](../../resources/commons/history/index.md#tracker-history-entry) that match the request.

### All Events of a User for a Specific Time Period

To obtain a list of all tracker events for a user received between the specified "from" and "to" dates, use the [`history/user/list`](../../resources/commons/history/history_user.md#list) method. You can also filter the results to include only the necessary event types.

### Required Parameters

- `from`: A string containing the start [date/time](../../getting-started/introduction.md#data-types) for the search.
- `to`: A string containing the end [date/time](../../getting-started/introduction.md#data-types) for the search. Must be after the `from` date.

### Optional Parameters

- `events`: An array of strings with the necessary event types. All other events will be ignored. Default is all. To get a list of events, use the [`tracker/history/type`](../../resources/commons/history/history_type.md#list) call.
- `limit`: An integer specifying the maximum number of entries in the result.
- `ascending`: A boolean that sorts the results in ascending order by time when `true` and descending when `false`.

Example: To get state field events for the last five minutes on all trackers of a user, use `to`=CURRTIME and `from`=CURRTIME-5 minutes. Filter by `state_field_control` events.

=== "cURL"

```shell
curl -X POST '{{ extra.api_example_url }}/history/user/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "2023-06-13 18:42:10", "to": "2023-06-13 18:47:10", "events": ["state_field_control"], "limit": 100, "ascending": true}'
```

The response will contain the [history entries](../../resources/commons/history/index.md#tracker-history-entry) that match the request.
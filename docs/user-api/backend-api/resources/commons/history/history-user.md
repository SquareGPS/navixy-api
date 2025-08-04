---
title: User events
description: Contains list method to get user's events.
---

# User events

## API actions

API path: `/history/user/`.

### list

Lists less than or equal to `limit` of tracker events filtered by event types (`events`) between `from` date/time and `to` date/time sorted by **time** field.

Added more information about this API call usage in our guide.

**Parameters**

| name                | description                                                                                      | type             |
| ------------------- | ------------------------------------------------------------------------------------------------ | ---------------- |
| from                | Start date/time for searching.                                                                   | string date/time |
| to                  | End date/time for searching. Must be after "from" date.                                          | string date/time |
| events              | Optional. Default: all. List of history types.                                                   | string array     |
| limit               | Optional. Default: history.maxLimit. Max count of entries in result.                             | int              |
| ascending           | Optional. Default: `true`. Sort ascending by time when it is `true` and descending when `false`. | boolean          |
| only\_emergency     | Optional. Default: `false`. If `true`, only emergency events will be included.                   | boolean          |
| only\_unread        | Optional. Default: `false`. If `true`, only unread events will be included.                      | boolean          |
| add\_tracker\_label | Optional. Default: `true`. If `true`, tracker label will be added to "message" field.            | boolean          |
| add\_tracker\_files | Optional. Default: `false`. If `true`, tracker files info will be included.                      | boolean          |

If `events` (event types) not passed then list all event types.

Available event types can be obtained by /history/user/list action.

Default and max limit is 1000. (Note for StandAlone: this value configured by maxHistoryLimit config option).

**Example**

\=== "cURL"

{% code overflow="wrap" %}
```
curl -X POST '{{ extra.api_example_url }}/history/user/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "from": "2020-12-10 16:44:00", "to": "2020-12-22 16:44:00"}'
```
{% endcode %}

**Response**

```json
{
    "success": true,
    "list": [{
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
    }],
    "limit_exceeded": false,
    "total": 150,
    "total_unread": 10
}
```

* `list` - list of zero or more `history_entry` objects which described in Tracker history entry.
* `limit_exceeded` - boolean. It indicates if the response has exceeded the `store_period` limit, set in the user's tariff plan. Will be `true` if you request a period that exceeds what the user's plan allows.
* `total` - int. Amount of history entries satisfied with conditions.
* `total_unread` - int. Amount of unread history entries that satisfy the conditions.

**Errors**

* 211 – Requested time span is too big - time span between `from` and `to` is more than `report.maxTimeSpan` days.
* 212 – Requested `limit` is too big - `limit` is more than `history.maxLimit`.

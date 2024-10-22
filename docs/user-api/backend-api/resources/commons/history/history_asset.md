---
title: Asset events
description: Contains list method to get asset's events.
---

# Asset events

Contains list method to get asset's events.


## API actions

API path: `/asset/history/`.

### `list`

List less than or equal to `limit` of assets' events filtered by event types (`events`) between `from` date/time 
and `to` date/time sorted by **time** field. 

#### Parameters

| name              | description                                                                                                                                             | type                                                                    |
|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| assets            | Optional. Default: all. List of objects containing identifier and type to define a list of tracker identifiers. Permitted types: `vehicle`, `employee`. | object array                                                            |
| from              | Start date/time for searching.                                                                                                                          | string [date/time](../../../getting-started/introduction.md#data-types) |
| to                | End date/time for searching. Must be after "from" date.                                                                                                 | string [date/time](../../../getting-started/introduction.md#data-types) |
| events            | Optional. Default: all. List of history types.                                                                                                          | string array                                                            |
| limit             | Optional. Default: [history.maxLimit](../dealer.md). Max count of entries in result.                                                                    | int                                                                     |
| ascending         | Optional. Default: `true`. If `true`, ordering by time will be ascending, descending otherwise.                                                         | boolean                                                                 |
| only_emergency    | Optional. Default: `false`. If `true`, only emergency events will be included.                                                                          | boolean                                                                 |
| only_unread       | Optional. Default: `false`. If `true`, only unread events will be included.                                                                             | boolean                                                                 |
| add_tracker_label | Optional. Default: `true`. If `true`, tracker label will be added to "message" field.                                                                   | boolean                                                                 |
| add_tracker_files | Optional. Default: `false`. If `true`, tracker files info will be included.                                                                             | boolean                                                                 |

If `events` (event types) not passed then list all event types.

Available event types can be obtained by [/history/type/list](./history_type.md#list) action.

Default and max limit is 1000. (Note for StandAlone: this value configured by maxHistoryLimit config option).

Interval will be restricted by store period interval.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "assets": [{"id": 1683258, "type": "employee"}], "from": "2020-12-10 16:44:00", "to": "2020-12-22 16:44:00"}'
    ```

#### Response

```json
{
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
         },
         "asset": {
             "id": 1683258,
             "type": "employee"
         }
    }],
    "limit_exceeded": false,
    "total": 150,
    "total_unread": 10,
    "success": true
}
```

* `list` - list of zero or more history_entry` objects which described in [Tracker history entry](./index.md#tracker-history-entry) with additional asset parameter. 
* `limit_exceeded` - boolean. `false` when listed all history entries satisfied with conditions and `true` otherwise.
* `total` - int. Amount of history entries satisfied with conditions.
* `total_unread` - int. Amount of unread history entries satisfied with conditions.

#### Errors

* 212 – Requested `limit` is too big - `limit` is more than [history.maxLimit](../dealer.md).

---
title: Tracker events
description: Contains list method to get tracker's events.
---

# Tracker events

Contains list method to get tracker's events.


## API actions

API path: `/history/tracker/`.

### `list`

List less than or equal to `limit` of tracker events sorted by **time** field. 

Described this API call usage details in our [guide](../../../guides/rules-notifications/work-with-notifications.md#events-for-specific-trackers-and-time-period).

#### Parameters

| name              | description                                                                                      | type                                                                    |
|:------------------|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| trackers          | List of tracker's IDs.                                                                           | int array                                                               |
| from              | Start date/time for searching.                                                                   | string [date/time](../../../getting-started/introduction.md#data-types) |
| to                | End date/time for searching. Must be after "from" date.                                          | string [date/time](../../../getting-started/introduction.md#data-types) |
| events            | Optional. Default: all. List of event types.                                                     | string array                                                            |
| limit             | Optional. Default: [history.maxLimit](../dealer.md). Max count of entries in result.             | int                                                                     |
| ascending         | Optional. Default: `true`. Sort ascending by time when it is `true` and descending when `false`. | boolean                                                                 |
| only_emergency    | Optional. Default: `false`. If `true`, only emergency events will be included.                   | boolean                                                                 |
| only_unread       | Optional. Default: `false`. If `true`, only unread events will be included.                      | boolean                                                                 |
| add_tracker_label | Optional. Default: `true`. If `true`, tracker label will be added to "message" field.            | boolean                                                                 |
| add_tracker_files | Optional. Default: `false`. If `true`, tracker files info will be included.                      | boolean                                                                 |

Available event types can be obtained by [/history/type/list](history_type.md#list) action.

Default and max limit is 1000. (Note for StandAlone: this value configured by maxHistoryLimit config option).

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/tracker/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [131312, 123985], "from": "2020-12-10 16:44:00", "to": "2020-12-22 16:44:00"}'
    ```

#### Response

```json
{
  "success": true,
  "list": [
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
    }
  ],
  "limit_exceeded": false,
    "total": 150,
    "total_unread": 10
}
```

* `list` - list of zero or more history_entry` objects which described in [Tracker history entry](index.md#tracker-history-entry). 
* `limit_exceeded` - boolean. `false` when listed all history entries satisfied with conditions and `true` otherwise.
* `total` - int. Amount of history entries satisfied with conditions.
* `total_unread` - int. Amount of unread history entries satisfied with conditions.

#### Errors

* 211 – Requested time span is too big - time span between `from` and `to` is more than [report.maxTimeSpan](../dealer.md) days.
* 212 – Requested `limit` is too big - `limit` is more than [history.maxLimit](../dealer.md).
* 217 – List contains nonexistent entities – if one of the specified trackers does not exist or is blocked.

### `count`

Count total and unread number of tracker events.

#### Parameters

| name              | description                                                                                      | type                                                                    |
|:------------------|:-------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------|
| trackers          | List of tracker's IDs.                                                                           | int array                                                               |
| from              | Start date/time for searching.                                                                   | string [date/time](../../../getting-started/introduction.md#data-types) |
| to                | End date/time for searching. Must be after "from" date.                                          | string [date/time](../../../getting-started/introduction.md#data-types) |
| events            | Optional. Default: all. List of event types.                                                     | string array                                                            |
| only_emergency    | Optional. Default: `false`. If `true`, only emergency events will be included.                   | boolean                                                                 |
| only_unread       | Optional. Default: `false`. If `true`, only unread events will be included.                      | boolean                                                                 |

Available event types can be obtained by [/history/type/list](./history_type.md#list) action.

Interval will be restricted by store period interval.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/tracker/count' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [131312, 123985], "from": "2020-12-10 16:44:00", "to": "2020-12-22 16:44:00"}'
    ```

#### Response

```json
{
    "total": 150,
    "total_unread": 10,
    "success": true
}
```

* `total` - int. Number of events satisfied with conditions.
* `total_unread` - int. Number of unread events satisfied with conditions.

#### Errors

* 211 – Requested time span is too big - time span between `from` and `to` is more than [report.maxTimeSpan](../dealer.md) days.
* 217 – List contains nonexistent entities – if one of the specified trackers does not exist or is blocked.

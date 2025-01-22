---
title: Unread events
description: Contains API calls to interact with unread history entries.
---

# Unread events

Contains API calls to interact with unread history events.


## API actions

API path: `/history/unread`.

### `list`

List less than or equal to `limit` of the latest user's unread history events. Described how it works in our [guide](../../../guides/rules-notifications/work-with-notifications.md#all-unread-events-of-a-user).

#### Parameters

| name  | description                                                                                                                               | type      |
|:------|:------------------------------------------------------------------------------------------------------------------------------------------|:----------|
| limit | Optional. Limit of entries in response.                                                                                                   | int       |
| from  | Optional. Start [date/time](../../../getting-started/introduction.md#data-types) for searching. Default `from` is **now** minus one year. | date/time |

Default and max limit is [history.maxLimit](../dealer.md).

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/unread/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/history/unread/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

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

* `list` - array of objects. list of zero or more [Tracker history entry](index.md#tracker-history-entry) objects.

#### Errors

* 212 – Requested limit is too big (more [history.maxLimit](../dealer.md) config option).


### `count`

Get count of user's unread history messages starting `from` date.

#### Parameters

| name | description                                                                                                                                | type                                                        |
|:-----|:-------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------|
| from | Optional. Start [date/time](../../../getting-started/introduction.md#data-types) for searching.  Default `from` is **now** minus one year. | date/time                                                   |
| type | Optional. Type of devices that should be count. Can be "socket", "tracker", or "camera".                                                   | [enum](../../../getting-started/introduction.md#data-types) |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/unread/count' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/history/unread/count?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "count": 1
}
```

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.

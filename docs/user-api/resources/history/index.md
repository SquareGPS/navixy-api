---
title: Events history
description: Contains history entry object description and API calls to interact with it.
---

# Events history

Contains history entry object description and API calls to interact with it.

Find instructions on getting notifications [here](../../guides/rules-notifications/work-with-notifications.md).

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
```

* `id` - long. An ID of event.
* `type` - [enum](/broken/pages/ZecFmxN0cywjosU1jKcD#data-types). Type of device. Can be "socket", "tracker", or "camera".
* `is_read` - boolean. If `true` the notification seen by user and marked as read.
* `message` - string. Notification message shortened to 256 characters.
* `time` - [date/time](/broken/pages/ZecFmxN0cywjosU1jKcD#data-types). When this notification received.
* `event` - [enum](/broken/pages/ZecFmxN0cywjosU1jKcD#data-types). Type of history event extension. Available event types can be obtained by [/history/type/list](history_type.md#list) action.
* `tracker_id` - int. An ID of the tracker (aka "object\_id"). Tracker must belong to authorized user and not be blocked.
* `rule_id` - optional int. An ID of assigned rule.
* `track_id` - int. An ID of a track on which the event happened or `0` if no track is associated.
* `location` - location object. Location where the event happened.
* `address` - string. Address of location or `""` (empty string) if there is no address for location.
* `extra` - optional object. Extra fields for events. Like for what task or tracker the event was.
  * `task_id` - optional int. Related task ID.
  * `parent_task_id` - optional int. Related parent task ID (for task checkpoint related history entries).
  * `counter_id` - optional int. Related counter ID.
  * `service_task_id` - optional int. Related service task ID.
  * `checkin_id` - optional int. Related check-in marker.
  * `place_ids` - optional array of integers. Related place IDs.
  * `places_total_count` - optional int. Total count of places.
  * `last_known_location` - optional boolean. `true` if location may be outdated.
  * `tracker_label` - optional string. Related tracker label.
  * `emergency` - optional boolean. `true` for emergency events with the same flag in a rule.
  * `zone_ids` - optional array of integers. Related geofence IDs.
  * `zone_labels` - optional array of strings. Related geofence labels.
  * `proximity_object_id` - optional int. Proximity tracker ID.
  * `employee_id` - optional int. Driver ID at the time of the event.
  * `sensor_id` - optional int. Related sensor ID.
  * `sensor_name` - optional string. Related sensor name.
  * `sensor_calculated_value` - optional string. Related sensor value.
  * `full_message` - optional string. Full event message, included when the `message` was shortened.
  * `precision` - optional int. Precision of the location in meters.

Date/time type described in [data types description section](/broken/pages/ZecFmxN0cywjosU1jKcD#data-types).

## API actions

API path: `/history`.

### read

Returns history entry with the specified ID.

#### Parameters

| name                | description                                                 | type    |
| ------------------- | ----------------------------------------------------------- | ------- |
| id                  | [History entry](index.md#tracker-history-entry) ID.         | long    |
| add\_tracker\_label | Optional. If `true` tracker label will be added to message. | boolean |

#### Examples

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/history/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 11231, "add_tracker_label": true}'
```
````

\=== "HTTP GET"

````
```
{{ extra.api_example_url }}/history/read?hash=a6aa75587e5c59c32d347da438505fc3&id=11231&add_tracker_label=true
```
````

#### Response

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
}
```

#### Errors

* 201 – Not found in the database - when there are no history entries with that ID.

### unread/list

List less than or equal to `limit` of the latest user's unread history events. Described how it works in our [guide](../../guides/rules-notifications/work-with-notifications.md#all-unread-events-of-a-user).

#### Parameters

| name  | description                                                                                                                         | type      |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------- | --------- |
| limit | Optional. Limit of entries in response.                                                                                             | int       |
| from  | Optional. Start [date/time](/broken/pages/ZecFmxN0cywjosU1jKcD#data-types) for searching. Default `from` is **now** minus one year. | date/time |

Default and max limit is [history.maxLimit](../commons/settings/dealer.md).

#### Examples

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/history/unread/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
````

\=== "HTTP GET"

````
```
{{ extra.api_example_url }}/history/unread/list?hash=a6aa75587e5c59c32d347da438505fc3
```
````

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
  ]
}
```

* `list` - array of objects. list of zero or more [Tracker history entry](index.md#tracker-history-entry) objects.

#### Errors

* 212 – Requested limit is too big (more [history.maxLimit](../commons/settings/dealer.md) config option).

### unread/count

Get count of user's unread history messages starting `from` date.

#### Parameters

| name | description                                                                                                                         | type                                                  |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| from | Optional. Start [date/time](/broken/pages/ZecFmxN0cywjosU1jKcD#data-types) for searching. Default `from` is **now** minus one year. | date/time                                             |
| type | Optional. Type of devices that should be count. Can be "socket", "tracker", or "camera".                                            | [enum](/broken/pages/ZecFmxN0cywjosU1jKcD#data-types) |

#### Examples

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/history/unread/count' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
````

\=== "HTTP GET"

````
```
{{ extra.api_example_url }}/history/unread/count?hash=a6aa75587e5c59c32d347da438505fc3
```
````

#### Response

```json
{
  "success": true,
  "count": 1
}
```

#### Errors

* [General](../../../general/errors.md#error-codes) types only.

### mark\_read

Marks history entry as read by `id` (see: [Tracker history entry](index.md#tracker-history-entry)).

#### Parameters

| name | description                                                | type |
| ---- | ---------------------------------------------------------- | ---- |
| id   | [Tracker history entry](index.md#tracker-history-entry) ID | long |

#### Examples

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/history/mark_read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 11231}'
```
````

\=== "HTTP GET"

````
```
{{ extra.api_example_url }}/history/mark_read?hash=a6aa75587e5c59c32d347da438505fc3&id=11231
```
````

#### Response

```json
{
  "success": true
}
```

#### Errors

* 201 – Not found in the database - when there are no unread history entries with that ID.

### mark\_read\_all

Marks all the user's history entries read.

#### Parameters

Only API key `hash`.

#### Examples

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/history/mark_read_all' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
````

\=== "HTTP GET"

````
```
{{ extra.api_example_url }}/history/mark_read_all?hash=a6aa75587e5c59c32d347da438505fc3
```
````

#### Response

```json
{
  "success": true
}
```

#### Errors

* [General](../../../general/errors.md#error-codes) types only.

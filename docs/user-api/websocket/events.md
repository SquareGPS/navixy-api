---
title: WebSocket Events
description: >-
  Information about WebSocket events with conditions for obtaining and message
  samples.
---

# WebSocket Events

The server sends an `event message` through the WebSocket channel when an event occurs and client has subscription on this.\
All event messages contain the next fields:

* `type` – [enum](broken-reference). "event".
* `event` – [enum](broken-reference). Can be "state", "state\_batch", "readings\_batch", "lifecycle", or "logout".
* `data` – optional object. Specific event payload.

## State event

> Can be used for 100 devices. If there are more devices, please use state batch event.

These messages are coming from server if client [subscribed](subscription.md)\
to the `state` events of the specific tracker that not blocked. It occurs in the next cases:

* Tracker state changed.
* Immediately after subscription.
* Immediately after unblocking.

Message fields:

* `type` – "event".
* `event` – "state".
* `data` – depends on `format` request parameter:
  * "full" – [source state](../backend-api/websocket/broken-reference/).
  * "compact" – [compact source state](events.md#compact-source-state).
* `user_time` – current time in user's timezone.

Message sample:

```json
{
  "type": "event",
  "event": "state",
  "user_time": "2018-10-17 12:51:55",
  "data": {
    "source_id": 10284,
    "gps": {
      "updated": "2018-10-17 12:51:43",
      "signal_level": 100,
      "location": {
        "lat": 14.330065796228606,
        "lng": -90.99037259141691
      },
      "heading": 248,
      "speed": 0,
      "alt": 431
    },
    "connection_status": "active",
    "movement_status": "parked",
    "movement_status_update": "2018-10-04 22:47:07",
    "ignition": false,
    "ignition_update": "2018-10-04 22:47:07",
    "gsm": null,
    "last_update": "2018-10-17 12:51:46",
    "battery_level": null,
    "battery_update": null,
    "inputs": [false, false, false, false, false, false, false, false],
    "inputs_update": "2018-10-17 12:51:43",
    "outputs": [false, false, false, false, false, false, false, false],
    "outputs_update": "2018-10-17 12:51:43",
    "actual_track_update": "2018-10-04 22:47:07"
  }
}
```

> `source_id` is not a `tracker_id`.

## State batch event

These messages are coming from server if client [subscribed](subscription.md)\
to the `state_batch` events of the specific tracker that not blocked. It occurs in the next cases:

* Immediately after subscription.
* Tracker state changed. But no more frequently than the `rate_limit`.

Message fields:

* `type` – "event".
* `event` – "state\_batch".
* `data` – depends on `format` request parameter:
  * "full" – [source state](../backend-api/websocket/broken-reference/) array.
  * "compact" – [compact source state](events.md#compact-source-state) array.
* `user_time` – current time in user's timezone.

Message sample:

```json
{
  "type": "event",
  "event": "state_batch",
  "user_time": "2018-10-17 12:51:55",
  "data": [
    {
      "source_id": 10284,
      "gps": {
        "updated": "2018-10-17 12:51:43",
        "signal_level": 100,
        "location": {
          "lat": 14.330065796228606,
          "lng": -90.99037259141691
        },
        "heading": 248,
        "speed": 0,
        "alt": 431
      },
      "connection_status": "active",
      "movement_status": "parked",
      "movement_status_update": "2018-10-04 22:47:07",
      "ignition": false,
      "ignition_update": "2018-10-04 22:47:07",
      "gsm": null,
      "last_update": "2018-10-17 12:51:46",
      "battery_level": null,
      "battery_update": null,
      "inputs": [false, false, false, false, false, false, false, false],
      "inputs_update": "2018-10-17 12:51:43",
      "outputs": [false, false, false, false, false, false, false, false],
      "outputs_update": "2018-10-17 12:51:43",
      "actual_track_update": "2018-10-04 22:47:07"
    }
  ]
}
```

> `source_id` is not a `tracker_id`.

### Compact source state

Sample:

```json

{
  "source_id": 10284,
  "gps": {
    "updated": "2018-10-17 12:51:43",
    "signal_level": 100,
    "location": {
      "lat": 14.330065796228606,
      "lng": -90.99037259141691
    },
    "heading": 248,
    "speed": 0,
    "alt": 431
  },
  "connection_status": "active",
  "movement_status": "parked",
  "movement_status_update": "2018-10-04 22:47:07",
  "ignition": false,
  "ignition_update": "2018-10-04 22:47:07",
  "last_update": "2018-10-17 12:51:46"
}
```

## Readings batch event

These messages are coming from server if client [subscribed](subscription.md#the-readings_batch-event-subscription)\
to the `readings_batch` events of the specific tracker that not blocked. It occurs in the next cases:

* Immediately after subscription.
* Sensor data is updated, but no more frequently than the `rate_limit`.

Message fields:

* `type` – "event".
* `event` – "readings\_batch".
* `data` – [readings\_batch](../resources/tracker/sensor/readings.md#readings-batch-object) array. NOTE: Unlike a tracker/readings/batch\_list endpoint response in the common API, each item contains only modified objects.
* `user_time` – current time in user's timezone.

Message sample:

```json
{
  "type": "event",
  "event": "state_batch",
  "user_time": "2018-10-17 12:51:55",
  "data": [
    {<readings_batch>}
  ]
}
```

## Data Stream Analyzer event

You can receive Data Stream Analyser messages through websocket. These messages are coming from server if client [subscribed](subscription.md#the-iot_monitor-event-subscription)\
to the `iot_monitor` events of the specific tracker that is not blocked. These packets contain values\
of attributes from the latest messages sent by the selected tracker.\
It occurs in the next cases:

* Immediately after subscription.
* The latest attribute values are updated. But no more frequently than the `rate_limit`.

Message fields:

* `type` – "event".
* `event` – "iot\_monitor".
* `data`:
  * `iot_last_values` – list of objects:
    * `tracker_id` – tracker ID.
    * `nonnull_fields` – list of objects. Queue without data gaps – only messages where the specific attribute was present (not null).
      * `<field_name>` – name of the attribute.
        * `value` – value of attribute.
        * `msg_time` – message time.
        * `srv_time` – server time.
    * `all_fields` – list of objects. Queue with data gaps – if an attribute was missing in one of the last messages, a null value is recorded in the queue.
      * `<field_name>` – name of the attribute.
        * `value` – value of attribute.
        * `msg_time` – message time.
        * `srv_time` – server time.

Message sample:

```json
{
  "event": "iot_monitor",
  "type": "event",
  "data": {
    "iot_last_values": [
      {
        "tracker_id": 21080,
        "nonnull_fields": {
          "satellites": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": 10
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": 10
            }
          ],
          "heading": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": 7
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": 6
            }
          ],
          "latitude": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": "5.9654133"
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": "5.9646583"
            }
          ],
          "longitude": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": "6.5171267"
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": "6.5169383"
            }
          ],
          "lls_level_1": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": "262.9138"
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": "262.9945"
            }
          ],
          "speed": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": 43
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": 48
            }
          ]
        },
        "all_fields": {
          "satellites": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": 10
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": 10
            }
          ],
          "heading": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": 7
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": 6
            }
          ],
          "latitude": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": "5.9654133"
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": "5.9646583"
            }
          ],
          "longitude": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": "6.5171267"
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": "6.5169383"
            }
          ],
          "lls_level_1": [
            {
              "msg_time": "2025-02-11T15:12:59Z",
              "srv_time": "2025-02-11T15:12:59Z",
              "value": null
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": "262.9945"
            }
          ],
          "speed": [
            {
              "msg_time": "2025-02-11T15:12:58Z",
              "srv_time": "2025-02-11T15:12:58Z",
              "value": 43
            },
            {
              "msg_time": "2025-02-11T15:12:52Z",
              "srv_time": "2025-02-11T15:12:53Z",
              "value": 48
            }
          ]
        }
      }
    ]
  }
}
```

## Lifecycle event

These messages are coming from the server if client [subscribed](subscription.md)\
to the `state`, `state_batch` or `readings_batch` events of the specific tracker. It occurs in the next cases:

* Tracker blocked.
* Tracker unblocked.
* Tracker corrupted (removed).

Message fields:

* `type` – "event".
* `event` – "lifecycle".
* `data` – required object.
  * `source_id` – source ID.
  * `lifecycle_event` – lifecycle event type. Can be "block", "unblock", or "corrupt".

Message sample:

```json
{
  "type": "event",
  "event": "lifecycle",
  "data": {
    "source_id": 123456,
    "lifecycle_event": "block"
  }
}
```

## Logout event

These messages are coming from server if client [subscribed](subscription.md) to any event. It occurs in the next cases:

* User logged out.
* User session expired (did not renew during one month).
* Sub-user is blocked by master-user.
* User has restored his password.
* User has changed his password.
* User blocked from admin panel.
* User was corrupted (removed).

Message fields:

* `type` – "event".
* `event` – "logout".
* `data` – "session closed".

Message sample:

```json
{
  "type": "event",
  "event": "logout",
  "data": "session closed"
}
```

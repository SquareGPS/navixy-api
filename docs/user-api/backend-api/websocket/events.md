---
title: WebSocket Events
description: Information about WebSocket events with conditions for obtaining and message samples.
---

# WebSocket Events

The server sends an `event message` through the WebSocket channel when an event occurs and client has subscription on this. 
All event messages contain the next fields:

* `type` – [enum](../getting-started/introduction.md#data-types). "event".
* `event` – [enum](../getting-started/introduction.md#data-types). Can be "state", "state_batch", "readings_batch", "lifecycle", or "logout".
* `data` – optional object. Specific event payload. 

### `State event`

!!! note "Can be used for 100 devices. If there are more devices, please use state batch event"

These messages are coming from server if client [subscribed](subscription.md)
to the `state` events of the specific tracker that not blocked. It occurs in the next cases:

* Tracker state changed.
* Immediately after subscription.
* Immediately after unblocking.

#### Message

```json
{
  "type": "event",
  "event": "state",
  "data": {<source_state or compact_source_state>},
  "user_time": "2018-10-17 12:51:55"
}
```

* `type` – "event".
* `event` – "state".
* `data` – depends on `format` request parameter:
  * "full" – [source state](../resources/tracking/tracker/index.md#get_state).
  * "compact" – [compact source state](#compact-source-state).
* `user_time` – current time in user's timezone.

### `State batch event`

These messages are coming from server if client [subscribed](subscription.md)
to the `state_batch` events of the specific tracker that not blocked. It occurs in the next cases:

* Immediately after subscription.
* Tracker state changed. But no more frequently than the `rate_limit`.
* Tracker blocked.
* Tracker unblocked.
* Tracker corrupted (removed).

#### Message

```json
{
  "type": "event",
  "event": "state_batch",
  "data": [{<source_state_event or lifecycle_event>}]
}
```

* `type` – "event".
* `event` – "state_batch".
* `data` – array of [source state](#source-state-event) events and [lifecycle](#lifecycle-event) events.

#### Source state event

```json
{
  "type": "source_state_event",
  "state": {<source_state or compact_source_state>},
}
```

* `type` – "source_state_event".
* `state` – depends on `format` request parameter:
  * "full" – [source state](../resources/tracking/tracker/index.md#get_state).
  * "compact" – [compact source state](#compact-source-state).

#### Lifecycle event

```json
{
  "type": "lifecycle_event",
  "source_id": 123456,
  "lifecycle_event": "block",
  "timestamp": "2021-01-28 08:16:40"
}
```

* `type` – "lifecycle_event".
* `source_id` – source ID.
* `lifecycle_event` – lifecycle event type. Can be "block", "unblock", or "corrupt".
* `timestamp` – lifecycle event time.

#### Compact source state

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
  "inputs": [false, false, false],
  "inputs_update": "2022-08-31 13:47:09",
  "outputs": [true, false],
  "outputs_update": "2022-08-31 13:47:09",
  "last_update": "2018-10-17 12:51:46"
}
```

* `source_id` - int. Tracker data source ID (from "sources" table).
* `gps` - gps object.
  * `updated` - [date/time](../../../getting-started/introduction.md#data-types). Date of last gps coordinates update in a timezone of the user or null if there are
    no updates.
  * `signal_level` - int. GPS signal level in percent, e.g. 25, or null if device cannot provide such info.
  * `lat` - float. Latitude.
  * `lng` - float. Longitude.
  * `heading` int. Direction bearing in degrees (0-360).
  * `speed` - int. Speed in km/h, e.g. 20.
  * `alt` - int. Altitude in meters, e.g. 10.
  * `precision` - int. Optional. Precision in meters.
  * `gsm_lbs` - boolean. Optional. True if location detected by GSM LBS.
* `connection_status` - [enum](../../../getting-started/introduction.md#data-types). Device connection status, possible values: "signal_lost",
  "just_registered", "just_replaced", "offline", "idle", "active".
* `movement_status` - [enum](../../../getting-started/introduction.md#data-types). Movement status, possible values: "moving", "stopped", "parked".
* `movement_status_update` - [date/time](../../../getting-started/introduction.md#data-types). The date and time when the movement status was last changed or null if there are no changes.
* `ignition` - boolean. Optional. State of vehicle’s or virtual ignition sensor.
* `ignition_update` - [date/time](../../../getting-started/introduction.md#data-types). Optional. The date and time when the ignition state was last changed.
* `inputs` - array of boolean. States of all digital inputs. `[true, true, false]` means input 1 is on, input 2 is on,
  input 3 is off.
* `inputs_update` - [date/time](../../../getting-started/introduction.md#data-types). Date of last inputs update in a timezone of the user or null if there are no updates.
* `outputs` - array of boolean. States of all digital outputs. `[true, true, false]` means output 1 is on,
  output 2 is on, output 3 is off.
* `outputs_update` - [date/time](../../../getting-started/introduction.md#data-types). Date of last outputs update in a timezone of the user or null if there are no updates.
* `last_update` - [date/time](../../../getting-started/introduction.md#data-types). Date of last device state update in a timezone of the user or null if there are no updates.

### `Readings batch event`

These messages are coming from server if client [subscribed](subscription.md#the-readings_batch-event-subscription)
to the `readings_batch` events of the specific tracker that not blocked. It occurs in the next cases:

* Immediately after subscription.
* Sensor data is updated, but no more frequently than the `rate_limit`.
* Tracker blocked.
* Tracker unblocked.
* Tracker corrupted (removed).

#### Message

```json
{
  "type": "event",
  "event": "readings_batch",
  "data": [{<reading_event or lifecycle_event>}]
}
```

* `type` – "event".
* `event` – "readings_batch".
* `data` – array of [reading](#readings-event) events and [lifecycle](#lifecycle-event) events.

#### Readings event

```json
{
  "type": "readings_event",
  "tracker_id": 10181215,
  "inputs": [...],
  "states": [...],
  "virtual_sensors": [...],
  "counters": [...],
  "timestamp": "2021-01-28 08:16:40"
}
```

* `type` – "readings_event".
* `tracker_id` – tracker ID.
* `inputs, states, virtual_sensors, counters` - [readings_batch](../resources/tracking/tracker/readings.md#readings-batch-object) object fields.
* `timestamp` - readings event time.

!!! note "Unlike a tracker/readings/batch_list endpoint response in the common API, each item contains only modified objects."

### `IoT monitor event`

These messages are coming from server if client [subscribed](subscription.md#the-iot_monitor-event-subscription)
to the `iot_monitor` events of the specific tracker that not blocked. These packets contain values 
of attributes from the latest messages sent by the selected tracker.
It occurs in the next cases:

* Immediately after subscription.
* The latest attribute values are updated. But no more frequently than the `rate_limit`.

#### Message

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

### `Lifecycle event`

These messages are coming from the server if client [subscribed](subscription.md)
to the `state` events of the specific tracker. It occurs in the next cases:

* Tracker blocked.
* Tracker unblocked.
* Tracker corrupted (removed).

#### Message

```json
{
  "type": "event",
  "event": "lifecycle",
  "data": {<lifecycle_event>}
}
```

* `type` – "event".
* `event` – "lifecycle".
* `data` – [lifecycle](#lifecycle-event) event.

## Logout event

These messages are coming from server if client [subscribed](subscription.md) to any event. It occurs in the next cases:

* User logged out.
* User session expired (did not renew during one month).
* Sub-user is blocked by master-user.
* User has restored his password.
* User has changed his password.
* User blocked from admin panel.
* User was corrupted (removed).

#### Message

```json
{
  "type": "event",
  "event": "logout",
  "data": "session closed"
}
```

* `type` – "event".
* `event` – "logout".
* `data` – "session closed".

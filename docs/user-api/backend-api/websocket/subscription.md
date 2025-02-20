---
title: WebSocket Subscription
description: Information about WebSocket subscription and how to subscribe to every type of event.
---

# WebSocket Subscription

The `subscribe` and `unsubscribe` actions used by the client's side to subscribe on server 
events and unsubscribe from them. 
These actions are similar with any other [API REST actions](../getting-started/introduction.md) 
but must be sent inside open `WebSocket` channel and use only JSON format for messages between the client and server.


## Subscribe Action

The main difference between `state` and `state_batch` events is they can provide different amount of data every second.
Use 'state' event for smaller fleets since it supports sending data up to 350 entries per second.
For big or growing fleets better to use `state_batch` event since it supports sending data for up to 12000 entries per 
second.

### Request

Request parameters:

* `action` required, text: _"subscribe"_.
* `hash` – required, string, length=32. Session hash code obtained by [user/auth](../resources/commons/user/index.md#auth) action.
* `requests` – required, object array. See requests' structure below.

!!! warning "Deprecated"
    These parameters are deprecated and should not be used, please use `requests` instead:

    * `trackers` – required, int array, without nulls. List of tracker IDs for the events that require a subscription.
    * `events` – required, [enum](../getting-started/introduction.md#data-types) array, without nulls. List of events to subscribe. An event can only be a `state`.

#### The "state_batch" event subscription

After subscribing to "state_batch",
server will send the current states of all non-blocked trackers included in the subscription in a single packet.
Receiver must be able to parse data from different devices in this packet.
After each period equal to `rate_limit`,
the server will send a list of changed tracker states in the [event message](events.md#state-batch-event).

```json
{
  "action": "subscribe",
  "hash": "f4bf1b754034213653dad99c78c4b237",
  "requests": [
    {
      "type": "state_batch",
      "target": {
        "type": "all"
      },
      "rate_limit": "5s",
      "format": "compact"
    }
  ]
}
```

* `type` – required, text: _"state_batch"_. Event type.
* `target` – required, [target](#Request-targets). Trackers to subscribe.
* `rate_limit` – optional, string. A timespan for batching.
* `format` – optional, [enum](../getting-started/introduction.md#data-types), one of: "full" (default), "compact".

###### Request targets:

* All trackers:
    * `type` – required, text: _"all"_.
* Selected trackers:
    * `type` – required, text: _"selected"_.
    * `tracker_ids` – required, int array.

#### The "state" event subscription

After subscribing to "state",
server will send the current states of all non-blocked trackers included in the subscription in separate packets.
Receiver must be able to read information from these packets separately.
When changing the state of any tracker to which a subscription made,
the server will send a new state in the [event message](events.md#state-event).

```json
{
  "action": "subscribe",
  "hash": "4ce2b45d12a6c634154017511575369a",
  "requests": [
    {
      "type": "state",
      "trackers": [
        1701976,
        1701975
      ],
      "format": "compact"
    }]
}
```

* `type` – required, text: _"state"_. Event type.
* `trackers` – required, int array. List of tracker ids.
* `format` – optional, [enum](../getting-started/introduction.md#data-types), one of: "full" (default), "compact".

#### The "readings_batch" event subscription

After subscribing to "readings_batch",
server will send the current readings of all non-blocked trackers included in the subscription in a single packet.
Receiver must be able to parse data from different devices in this packet.
New data will arrive in real-time in the [event message](events.md#readings-batch-event), 
but no more frequently than the specified rate_limit.

```json
{
  "action": "subscribe",
  "hash": "f4bf1b754034213653dad99c78c4b237",
  "requests": [
    {
      "type": "readings_batch",
      "target": {
        "type": "all"
      },
      "rate_limit": "5s",
      "sensor_type": "temperature",
      "include_components": false
    }
  ]
}
```

* `type` – required, text: _"state_batch"_. Event type.
* `target` – required, [target](#Request-targets). Trackers to subscribe.
* `rate_limit` – optional, string. A timespan for batching.
* `sensor_type` – optional, [metering sensor type](../resources/tracking/tracker/sensor/index.md#metering-sensor-type-values) or [virtual sensor type](../resources/tracking/tracker/sensor/index.md#virtual-sensor-type-values).
  If specified, state values and counters will be omitted. Used to filter sensors by type.
* `include_components` – optional, boolean. Default is `true`. If set to `false`, parts of composite sensors will be excluded.


#### The "iot_monitor" event subscription

This subscription type is intended for the Data Stream Analyzer tool, 
which allows viewing the attribute values of the last N messages received from a tracker.
The server stores attributes for no more than the last 12 messages, sorted in descending order by message timestamp.
For each attribute, data is stored in two queues:

* Without data gaps – only messages where the specific attribute was present (not null).
* With data gaps – if an attribute was missing in one of the last messages, a null value is recorded in the queue.

After subscribing to "iot_monitor", server will send values of attributes from the latest messages for 
all non-blocked trackers included in the subscription in a single packet.
Receiver must be able to parse data from different devices in this packet.
New data will arrive in real-time in the [event message](events.md#iot-monitor-event), 
but no more frequently than the specified `rate_limit`.

```json
{
  "action": "subscribe",
  "hash": "6c638c52cb40729d5e6181a48f868649",
  "requests": [
    {
      "type": "iot_monitor",
      "target": {
        "type": "selected",
        "tracker_ids": [
          21080
        ]
      },
      "rate_limit": "5s"
    }
  ]
}
```

Request fields:

* `type` – required, text: _"iot_monitor"_. Event type.
* `target` – required, [target](#Request-targets). Trackers to subscribe. Maximum 10 trackers.
* `rate_limit` – optional, string. A timespan for batching.


### Response

Response parameters:

* `type` – required, text: _"response"_.
* `action` – required, text: _"subscription/subscribe"_.
* `events` – required, array of [enum](../getting-started/introduction.md#data-types), without nulls. List of the subscribed events types ("", "" or "iot_monitor").
* `data` – required, map <string, object>. Map with events subscription result. One key per subscribed event.
    * `state` – present if the "state" subscription requested, see sub response below.
    * `state_batch` – present if the "state_batch" subscription requested, see sub response below.
    * `readings_batch` – present if the "readings_batch" subscription requested, see sub response below.

Sub response:
* `success` – required, boolean.
* `value` – required, map <string, enum>, present if success. The current status of requested trackers.

Keys is a tracker IDs, values – one of the item:

* `normal` – non-blocked, normal status. [State events](events.md#state-event) for this
  tracker will be delivered to client.
* `blocked` – tracker blocked. [State events](events.md#state-event) for this tracker 
`will *not* be delivered to client. [Lifecycle events](events.md#lifecycle-event) will be delivered. After unblocking, 
current tracker state will be sent automatically.
* `unknown` – tracker ID missed in the database or not belong to current user.  
* `disallowed` – subscription for this tracker not allowed by the current session.

Response sample:

```json
{
  "type": "response",
  "action": "subscription/subscribe",
  "events": ["state"],
  "data": {
    "state": {
      "value": {
        "15564": "normal",
        "15565": "blocked",
        "15568": "unknown"
      },
      "success": true
    }
  }
}
```

### Automatic subscriptions

- Subscribing to a `state`, `state_batch`, `readings_batch` automatically creates a subscription to [lifecycle events](events.md#state-event).
- Subscribing to any event automatically creates a subscription to [logout events](events.md#logout-event).


## Unsubscribe Action

For structure see [Subscribe Action](#subscribe-action).


## Error Response

If something goes wrong, the server may respond with an error.
Error codes are similar to the [API errors codes](../getting-started/errors.md#error-codes).

Error response parameters:

* `type` – required, text: _"error"_.
* `action` – required, string – action from request (e.g. "subscription/subscribe") or "null" for some unexpected errors.
* `status` – required – error code and description:
    * `code` – required – error code (see [API errors codes](../getting-started/errors.md#error-codes)).
    * `description` – required, string – error description.
* `data` – optional string – part of parameters from request or some info for unexpected errors.

Error response sample:

```json
{
    "type": "error",
    "action": "subscription/subscribe",
    "status": {
        "code": 3,
        "description": "Wrong hash"
    },
    "data": {
        "events": ["state"],
        "trackers": [15564]
    }
}
```

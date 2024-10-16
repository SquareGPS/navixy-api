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

* `action` (text: "subscribe").
* `hash` - required, string, length=32. Session hash code obtained by [user/auth](../resources/commons/user/index.md#auth) action.
* `requests` - required, object array. See requests' structure below.

!!! warning "Deprecated"
    Parameters below are deprecated by `requests` and should not be used.

* `trackers` - required, int array, without nulls. List of tracker IDs for the events that require a subscription.
* `events` - required, [enum](../getting-started/introduction.md#data-types) array, without nulls. List of events to subscribe. Event can be one of: `state`.

#### Subscribe state_batch event sample:

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

If you use target 'trackers' for some devices and then subscribe again to other devices - in state_batch event you will 
receive data from all subscribed devices at once.

#### Subscribe state event sample

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
      "rate_limit": "5s",
      "format": "compact"
    }]
}
```

#### Sub requests:

* Batching (preferred):
    * `type` - required, text: _"state_batch"_.
    * `target` - required, object. One of targets below.
    * `rate_limit` - optional, string. A timespan for batching.
    * `format` - optional, [enum](../getting-started/introduction.md#data-types), one of: "full" (default), "compact".
* Simple:
    * `type` - required, text: _"state"_.
    * `trackers` - required, int array. List of tracker ids.
    * `format` - optional, [enum](../getting-started/introduction.md#data-types), one of: "full" (default), "compact".

Sample:

```json
{
  "type": "state_batch",
  "target": {
    "type": "selected",
    "tracker_ids": [15564, 15565, 15568]
  },
  "rate_limit": "5s",
  "format": "full"
}
```

##### Request targets:

* All trackers:
    * `type` - required, text: _"all"_.
* Selected trackers:
    * `type` - required, text: _"selected"_.
    * `tracker_ids` - required, int array.

Sample:

```json
{
  "type": "all"
}
```

### Response

Response parameters:

* `type` - required, text: _"response"_.
* `action` - required, text: _"subscription/subscribe"_.
* `events` - required, array of [enum](../getting-started/introduction.md#data-types), without nulls. List of the subscribed events. Event can be `state`.
* `data` - required, map <string, object>. Map with events subscription result. One key per subscribed event.
    * `state` - present if the "state" subscription requested, see sub response below.
    * `state_batch` - present if the "state_batch" subscription requested, see sub response below.

Sub response:
* `success` - required, boolean.
* `value` - required, map <string, enum>, present if success. The current status of requested trackers.

Keys is a tracker IDs, values - one of the item:

* `normal` - non-blocked, normal status. [State events](events.md#state-event) for this
  tracker will be delivered to client.
* `blocked` - tracker blocked. [State events](events.md#state-event) for this tracker 
  will *not* be delivered to client. 

[Lifecycle events](events.md#lifecycle-event) will be delivered. After unblocking, 
current tracker state will be sent automatically.

* `unknown` - tracker ID missed in the database or not belong to current user.  
* `disallowed` - subscription for this tracker not allowed by the current session.

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

### The "state" event subscription

After subscribe on the "state",
server will send the current states of all non-blocked trackers to which the subscription made in a separate packets.
Receiver must be able to read information from these packets separately.
When changing the state of any tracker to which a subscription made,
the server will send a new state in the [event message](events.md#state-event).

### The "state_batch" event subscription

After subscribe on the "state",
server will send the current states of all non-blocked trackers to which the subscription made in one packet.
Receiver must be able to parse data from different devices in this packet.
After each period equal to `rate_limit`,
the server will send a list of changed tracker states in the [event message](events.md#state-event).

### Automatic subscriptions

- Subscribing to a `state` or `state_batch` automatically creates a subscription to [lifecycle events](events.md#state-event).
- Subscribing to any event automatically creates a subscription to [logout events](events.md#logout-event).


## Unsubscribe Action

For structure see [Subscribe Action](#subscribe-action).


## Error Response

If something goes wrong, the server may respond with an error.
Error codes are similar to the [API errors codes](../getting-started/errors.md#error-codes).

Error response parameters:

* `type` - required, text: _"error"_.
* `action` - required, string - action from request (e.g. "subscription/subscribe") or "null" for some unexpected errors.
* `status` - required - error code and description:
    * `code` - required - error code (see [API errors codes](../getting-started/errors.md#error-codes)).
    * `description` - required, string - error description.
* `data` - optional string - part of parameters from request or some info for unexpected errors.

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

---
title: WebSocket Subscription
description: Information about WebSocket subscription and how to subscribe to every type of event.
---

# WebSocket Subscription

The `subscribe` and `unsubscribe` actions used by the client's side to subscribe on server 
events and unsubscribe from them. 
These actions are similar with any other [API REST actions](../getting-started.md) 
but must be sent inside open `WebSocket` channel and use only JSON format for messages between the client and server.

## Subscribe Action

### Request

Request parameters:

* `action` (text: "subscribe").
* `hash` - required, string, length=32. Session hash code obtained by [user/auth](../resources/commons/user/index.md#auth) action.
* `trackers` - required, array of int, can't be null. List of tracker ids for the events that require a subscription.
* `events` - required, array of string enum, can't be null. List of events to subscribe. Event can be one of: `state`.

Request sample:

```json
{
  "action": "subscribe",
  "hash": "f4bf1b75403d851653dad99c78c4b237",
  "events": ["state"],
  "trackers": [15564, 15565, 15568]
}
```

### Response

Response parameters:

* `type` - required, text: _"response"_.
* `action` - required, text: _"subscription/subscribe"_.
* `events` - required, array of string enum, can't be null. List of the subscribed events. Event can be `state`.
* `data` - required, map <string, object>, can't be null. Map with events subscription result. One key per subscribed event.
  * `state` - presented if the "state" subscription requested, map <string, enum> - the current status of requested trackers.

Keys is a tracker ids, values - one of the item:

* `normal` - non-blocked, normal status. [State events](./events.md#state-event) for this
  tracker will be delivered to client.
* `blocked` - tracker blocked. [State events](./events.md#state-event) for this tracker 
  will *not* be delivered to client. 

[Lifecycle events](./events.md#lifecycle-event) will be delivered. After unblocking, 
current tracker state will be sent automatically.

* `unknown` - tracker id missed in the database or not belong to current user.  
* `disallowed` - subscription for this tracker not allowed by the current session.

Response sample:

```json
{
  "type": "response",
  "action": "subscription/subscribe",
  "events": ["state"],
  "data": {
    "state": {
      "15564": "normal",
      "15565": "blocked",
      "15568": "unknown"
    }
  }
}
```

### The "state" event subscription

After subscribe on the "state", server will send the current states of all non-blocked trackers to 
which the subscription made.
When changing the state of any tracker to which a subscription made, the server will 
send a new state in the [event message](./events.md#state-event).

### Automatic subscriptions

- Subscribing to a `state` automatically creates a subscription to [lifecycle events](./events.md#state-event).
- Subscribing to any event automatically creates a subscription to [logout events](./events.md#logout-event).

## Unsubscribe Action

### Request

Request parameters:

* `action` - text: _"unsubscribe"_.
* `hash` - required, string, length=32. Session hash code gotten by [user/auth](../resources/commons/user/index.md#auth) action.
* `trackers` - required, array of int, without nulls. List of tracker ids for events that require an unsubscription.
* `events` - required, array of string enum, without nulls. List of events to unsubscribe. Event can be `state`.

Request sample:

```json
{
  "action": "unsubscribe",
  "hash": "f4bf1b75403d851653dad99c78c4b237",
  "events": ["state"],
  "trackers": [15568]
}
```

### Response

Response parameters:

* `type` - required, text: _"response"_.
* `action` - required, text: _"subscription/unsubscribe"_.
* `events` - required, array of string enum, without nulls. List of unsubscribed events. Event can be `state`.
* `data` - required, array of int, without nulls. List of tracker ids from request.

Response sample:

```json
{
  "type": "response",
  "action": "subscription/unsubscribe",
  "events": ["state"],
  "data": [15568]
}
```

## Error Response

If something goes wrong, the server may respond with an error.
Error codes are similar to the [API errors codes](../getting-started.md#error-codes).

Error response parameters:

* `type` - required, text: _"error"_.
* `action` - required, string - action from request (e.g. "subscription/subscribe") or "null" for some unexpected errors.
* `status` - required - error code and description:
  * `code` - required - error code (see [API errors codes](../getting-started.md#error-codes)).
  * `description` - required, string - error description.
* `data` - optional string - part of parameters from request or some info for unexpected errors.

Error response sample:

```json
{
    "type": "error",
    "action": "subscription/subscribe",
    "status": {
        "code": 3,
        "description": "Wrong user hash"
    },
    "data": {
        "events": ["state"],
        "trackers": [15564]
    }
}
```
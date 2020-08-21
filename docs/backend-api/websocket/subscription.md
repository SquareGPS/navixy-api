# WebSocket Subscription

The _subscribe_ and _unsubscribe_ actions are used by client-side to subscribe on server 
events and unsubscribe from them. 
This actions are similar with any other [API REST actions](../getting-started.md), 
but must be sending inside an open _WebSocket_ channel and use only JSON format for the 
messages between client and server.

## Subscribe Action

### Request

Request parameters:

* __action__ (text: _"subscribe"_).
* __hash__ (required, string, length=32): session hash code gotten by [user/auth](../resources/commons/user/index.md#auth) action.
* __trackers__ (required, int[], without nulls) - list of tracker ids for the events that require a subscription.
* __events__ (required, enum[], without nulls) - list of events to subscribe. Event can be one of: `state`.

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

* __type__ (required, text: _"response"_).
* __action__ (required, text: _"subscription/subscribe"_).
* __events__ (required, enum[], without nulls) - list of the subscribed events. Event can be one of: `state`.
* __data__ (required, map<string, object>, without nulls) - map with the events subscription result. One key on each subscribed event.
  * __state__ (presents if the "state" subscription requested, map<string, enum>) - the current status of requested trackers.

Keys is a tracker ids, values - one of the item:

* __normal__ - non-blocked, normal status. The [state events](./events.md#state-event) for this
  tracker will be delivered to client.
* __blocked__ - tracker is blocked. The [state events](./events.md#state-event) for this tracker 
  will *not* be delivered to client. 

The [lifecycle events](./events.md#lifecycle-event) will be delivered. After unblocking, 
current tracker state will be sent automatically.

* __unknown__ - tracker id is missed in database or not belong to current user.  
* __disallowed__ - subscription for this tracker is not allowed by current session.
   

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
which the subscription was made.
When changing the state of any tracker to which a subscription is made, the server will 
send a new state in [event message](./events.md#state-event).

### Automatic subscriptions

- Subscribing to a _state_ automatically creates a subscription to the [lifecycle events](./events.md#state-event).
- Subscribing to any event automatically creates a subscription to the [logout events](./events.md#logout-event).

## Unsubscribe Action
### Request
Request parameters:

* __action__ (text: _"unsubscribe"_).
* __hash__ (required, string, length=32): session hash code gotten by [user/auth](../resources/commons/user/index.md#auth) action.
* __trackers__ (required, int[], without nulls) - list of tracker ids for the events that require an unsubscription.
* __events__ (required, enum[], without nulls) - list of events to unsubscribe. Event can be one of: `state`.

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

* __type__ (required, text: _"response"_).
* __action__ (required, text: _"subscription/unsubscribe"_).
* __events__ (required, enum[], without nulls) - list of the unsubscribed events. Event can be one of: `state`.
* __data__ (required, int[], without nulls) - list of the tracker ids from request.

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

* __type__ (required, text: _"error"_).
* __action__ (required, string) - action from request (e.g. "subscription/subscribe") or "null" for some unexpected errors.
* __status__ (required) - error code and description:
  * __code__ (required) - error code (see [API errors codes](../getting-started.md#error-codes)).
  * __description__ (required, string) - error description.
* __data__ (optional, string) - part of parameters from request or some info for unexpected errors.

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


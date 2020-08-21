# WebSocket Events

The server sends an _event message_ through the WebSocket channel when an event occurs and client has subscription on this. 
All of the event messages contains the fields:

*   `type` - "event".
*   `event` - one of the items: "state", "lifecycle", "logout"
*   `data` (optional, object) - specific event payload. 

## State event

This messages are coming from server if client is [subscribed](./subscription.md). 
to the `state` events of the specific tracker and this tracker is not blocked. It's occur in the cases:

*   Tracker stated is changed.
*   Immediately after subscription.
*   Immediately after unblocking.

Message fields:

*   `type` - "event".
*   `event` - "state".
*   `data` - [source state](../resources/tracking/tracker/index.md#get_state).
*   `user_time` - current time in user's timezone.

Message sample:
```json5
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

Note: `source_id` is not a `tracker_id`.

## Lifecycle event

This messages are coming from server if client is [subscribed](./subscription.md). 
to the `state` events of the specific tracker. It's occur in the cases:

*   Tracker is blocked.
*   Tracker is unblocked.
*   Tracker is corrupted (removed).

Message fields:

*   `type` - "event".
*   `event` - "lifecycle".
*   `data` (required, object):
    *   `source_id` - source id.
    *   `lifecycle_event` - lifecycle event type. One of the items: "block", "unblock", "corrupt".

Message sample:
```json5
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

These messages are coming from server if client is [subscribed](./subscription.md). 
to the any event. It's occur in cases:

*   User logged out.
*   User session expired (did not renew during one month).
*   Sub-user is blocked by master-user.
*   User has restored his password.
*   User has changed his password.
*   User blocked from admin panel.
*   User was corrupted (removed).

Message fields:

*   `type` - "event".
*   `event` - "logout".
*   `data` - "session closed".

Message sample:
```json5
{
  "type": "event",
  "event": "logout",
  "data": "session closed"
}
```

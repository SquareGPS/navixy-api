# WebSocket API

## Introduction

__WebSocket__ is the alternate transport to getting data from the server. The process of notification about events occurs from the server to the client through a constantly open connection. This allows you to display changes in real time.

Currently, the [Atmosphere Framework](https://github.com/Atmosphere) used as an application layer library and protocol.

## Standard workflow

Let's describe a standard workflow for WebSocket API:

1.  Determine [API base URL](../../backend-api/getting-started.md#api-base-url). 
2.  Authorize with [user/auth](../resources/commons/user/index.md#auth). This API method will return the hash you should use for all your next API calls.
3.  Open WebSocket connection by the path [/event/subscription/](./subscription.md) with `Atmosphere` protocol parameters.
4.  Subscribe on events using [subscribe action](./subscription.md#subscribe-action).
5.  Listen and process the [incoming events](./events.md).
6.  Get the current tracker states after subscribe on a `state` event.
7.  Subscribe and unsubscribe on the events if needed.
8.  Unsubscribe when leaving monitoring page using [unsubscribe action](./subscription.md#unsubscribe-action).

Note what:
* The [subscription requests](./subscription.md) must contain the 
  `hash` parameter obtained through [user/auth](../resources/commons/user/index.md#auth) action.
* Responses and errors for the [subscribe](./subscription.md#subscribe-action) 
  and [unsubscribe](./subscription.md#unsubscribe-action) actions are similar 
  with common [API](../getting-started.md) format.
* All `WebSocket` frames use a `JSON` format. Exceptions are heartbeat frames containing "X".

## Open connection

In a simplified form, opening a websocket using [atmosphere-javascript](https://github.com/Atmosphere/atmosphere-javascript) looks like this:

```javascript
    var request = {
		url: 'https://domain.com/event/subscription',
        contentType: "application/json",
        transport: 'websocket'
	};
    atmosphere.subscribe(request);
```

Executing this code will lead to send a request

    ws://domain.com/event/subscription?X-Atmosphere-tracking-id=0&X-Atmosphere-Framework=2.3.6-javascript&X-Atmosphere-Transport=websocket&Content-Type=application/json&X-atmo-protocol=true

and upgrade the connection to websocket.
After what will be sent a first frame through opened websocket channel:

    b623a15d-9623-4fd8-a9d3-697036635c29|30000|X|

This is service message for the Atmosphere protocol negotiation.
Now everything is ready to [subscribe on events](./subscription.md#subscribe-action).

## Common fields

All messages from client side contain field _'action'_ with action name (e.g. "subscribe" or "unsubscribe").

All messages from server side contain field _'type'_ with message type ("event", "response" or "error") and _data_ with a payload.


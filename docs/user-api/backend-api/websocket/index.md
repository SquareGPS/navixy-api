---
title: WebSocket API
description: Information about WebSocket API and how to open connection.
---

# WebSocket API

Information about WebSocket API and how to open connection.


## Introduction

`WebSocket` is the alternate transport to getting data from the server. The process of notification about events occurs 
from the server to the client through a constantly open connection. This allows you to display changes in real time.

Currently, the [Atmosphere Framework](https://github.com/Atmosphere) used as an application layer library and protocol.


## Standard workflow

Let's describe a standard workflow for WebSocket API:

1. Determine [API base URL](../../backend-api/getting-started/introduction.md#api-base-url). 
2. Get the hash of an [API Key](../resources/commons/api-keys.md).
3. Open WebSocket connection by the path [/event/subscription/](subscription.md) with `Atmosphere` protocol parameters.
4. Subscribe on events using [subscribe action](subscription.md#subscribe-action).
5. Listen and process the [incoming events](events.md).
6. Get the current tracker states after subscribe on a `state` event.
7. Subscribe and unsubscribe on the events if needed.
8. Unsubscribe when leaving monitoring page using [unsubscribe action](subscription.md#unsubscribe-action).

!!! note
    * The [subscription requests](subscription.md) must contain the 
      `hash` of an [API Key](../resources/commons/api-keys.md).
    * Responses and errors for [subscribe](subscription.md#subscribe-action) 
      and [unsubscribe](subscription.md#unsubscribe-action) actions are similar 
      with common [API](../getting-started/introduction.md) format.
    * All `WebSocket` frames use a `JSON` format. Exceptions are heartbeat frames containing "X".


## Open connection

In a simplified form, opening the WebSocket using [atmosphere-javascript](https://github.com/Atmosphere/atmosphere-javascript) looks like this:

```js
  var subSocket;
  
  function sendSubsrcibeRequest() {
      console.log('sending subsrcibe action to websocket');
      subSocket.push(JSON.stringify({
          action: 'subscribe',
          hash: 'e4c24xxx4a08e9xxxc337xxxx5ca04e1',
          requests: [
              {
                  type: 'state_batch',
                  target: {
                      type: 'all'
                  }
              }
          ]
      }));
  }
  
  var request = {
      url: '{{ extra.api_example_url }}/event/subscription',
      contentType : "application/json",
      logLevel : 'debug',
      transport : 'websocket',
      trackMessageLength : false,
      reconnectInterval: 2000,
      onOpen: function(r) {
          console.log('onOpen', r);
          sendSubsrcibeRequest();
      },
      onReopen: function(r) {
          console.log('onReopen', r);
          sendSubsrcibeRequest();
      },
      onMessage: function (msg) {
          console.log('onMessage', msg);
      },
      onClientTimeout: function(r) {
          console.log('onClientTimeout', r);
      },
      onTransportFailure: function(errorMsg, request) {
          console.log('onTransportFailure', errorMsg);
      },
      onClose: function(r) {
          console.log('onClose', r);
      },
      onError: function(r) {
          console.log('onError', r);
      },
      onReconnect: function(request, response) {
          console.log('onReconnect', response);
      }
  };
  
  subSocket = atmosphere.subscribe(request);
```

Executing this code will lead to send a request

    wss://domain.com/event/subscription?X-Atmosphere-tracking-id=0&X-Atmosphere-Framework=2.3.6-javascript&X-Atmosphere-Transport=websocket&Content-Type=application/json&X-atmo-protocol=true

and upgrade the connection to the WebSocket.
After that, will be sent a first frame through the opened WebSocket channel:

    b623a15d-9623-4fd8-a9d3-697036635c29|30000|X|

This is service message for the Atmosphere protocol negotiation.
Now everything is ready to [subscribe on events](subscription.md#subscribe-action).


## Common fields

All messages from client side contain field `action` with action name (e.g. "subscribe" or "unsubscribe").

All messages from server side contain field `type` with message type ("event", "response" or "error") and `data` with a payload.


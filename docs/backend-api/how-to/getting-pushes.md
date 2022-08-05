---
title: Getting push notifications
description: This resource will describe - how to bind your app on getting push notifications about events.
---

# How to get push notifications for your app

You can subscribe your app to work with push notifications. They allow you to get new events immediately and without 
requesting such an event with an API call. These notifications could be used by your program for triggering some actions
with trackers, configs, tasks, sending them into your Telegram bot, etc.

Apps can be mobile or web-based. In each case, you need to subscribe it for push notifications differently. Let's examine
each of these cases separately.

***

## Mobile apps

To get push notifications on mobile devices, you need get app's push token. It may be done in several steps:

1. Contact Google if you're developing an android app, or from the AppStore for iOS app to get app's credentials.
2. Contact our support team (support@navixy.com) with these credentials.
3. We will provide you with the push_token and application for the API call. 
4. Then use the [push_token/bind](../resources/commons/user/session/push_token.md#bind) API call from your app. Substitute the provided push token and application ID into it

***

## Web apps

In order for your web application to start receiving pushes, do the following steps:

When creating a subscription, you must specify the 
[applicationServerKey](https://web.dev/push-notifications-subscribing-a-user/#applicationserverkey-option). It should be
in BYTEs, not as a base64 string.

Our public key in base64 is 

```BKPE9clw-_CxWE-WlqSkVpLnHT-7rE637udxtfGRUfXshjfCgatSNqNtRp5HjwEukACcdhIPMwPc9Ch7UsZXXY```

function example:

```java
return navigator.serviceWorker
    .register('/service-worker.js')
    .then(function (registration) {
      const subscribeOptions = {
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array(
          'BKPE9clw-_CxWE-WlqSkVpLnHT-7rE637udxtfGRUfXshjfCgatSNqNtRp5HjwEukACcdhIPMwPXc9Ch7UsZXxY'
        ),
      };

      return registration.pushManager.subscribe(subscribeOptions);
    })
    .then(function (pushSubscription) {
      console.log(
        'Received PushSubscription: ',
        JSON.stringify(pushSubscription),
      );
      return pushSubscription
    })
```

Take the endpoint and keys p256dh and auth from the pushSubscription object.

example:

```json
{
      "endpoint": "https://some.pushservice.com/something-unique",
      "keys": {
        "p256dh": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
        "auth":"FPssNDTKnInHVndSTdbKFw=="
      }
}
```

Use the [push_token/bind](../resources/commons/user/session/push_token.md#bind) API call with parameters:

* application=w3c_pushapi
* token=whole endpoint from pushSubscription, full URL like https://fcm.googleapis.com/fcm/send/f6kicrBn7S0:APA91b......
* parameters=object with keys from pushSubscription {"p256dh": "...", "auth":"..."}

You will receive the notification in event.data in JSON format.

# Receiving Push Notifications in Your App
Push notifications enable your app to receive new events instantly without requiring continuous polling via API calls. These notifications can be leveraged to trigger actions such as updates to trackers, configurations, tasks, or even to send alerts to platforms like Telegram.

Whether your app is mobile or web-based, the subscription process for push notifications varies. Below, we outline the specific steps for each case.

## Mobile Apps

The Navixy platform supports Firebase Cloud Messaging (FCM).

To get push notifications on mobile devices, follow these steps to obtain the app's push token:

1. Firebase projects support Google [service accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk), which you can use to call Firebase server APIs from the app server. To authenticate a service account and authorize it to access Firebase services, you must [generate a private key file in JSON format](https://firebase.google.com/docs/cloud-messaging/auth-server#provide-credentials-manually).
2. Contact our support team at support@navixy.com with the generated private key, platform (Android/iOS), and your app's name.
3. We will provide you with the application ID for an API call to bind your app.
4. Obtain the push token of your app from Google Play Market or App Store.
5. Use the `push_token/bind` API call from your app. Substitute the push token and the application ID received from our support team.

## Web Apps

To start receiving push notifications in your web application, follow these steps:

When creating a subscription, you must specify the [applicationServerKey](https://web.dev/push-notifications-subscribing-a-user/#applicationserverkey-option). It should be in bytes, not as a base64 string.

Our public key in base64 is:
```
BKPE9clw-_CxWE-WlqSkVpLnHT-7rE637udxtfGRUfXshjfCgatSNqNtRp5HjwEukACcdhIPMwPc9Ch7UsZXxY
```

Here is a function example:

```js
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
      return pushSubscription;
    });
```

Take the `endpoint` and keys `p256dh` and `auth` from the `pushSubscription` object.

Example:
```json
{
  "endpoint": "https://some.pushservice.com/something-unique",
  "keys": {
    "p256dh": "BIPUL12DLfytvTajnryr2PRdAgXS3HGKiLqndGcJGabyhHheJYlNGCeXl1dn18gSJ1WAkAPIxr4gK0_dQds4yiI=",
    "auth": "FPssNDTKnInHVndSTdbKFw=="
  }
}
```

Use the `push_token/bind` API call with parameters:

- `application=w3c_pushapi`
- `token=whole endpoint from pushSubscription, full URL like https://fcm.googleapis.com/fcm/send/f6kicrBn7S0:APA91b......`
- `parameters=object with keys from pushSubscription {"p256dh": "...", "auth":"..."}`

You will receive the notification in `event.data` in JSON format.

---
title: Push token
description: Contains API calls to interact with push token.
---

# Push token

Contains API calls to interact with push token. 

Find information about push token usage in our [instructions](../../../../guides/rules-notifications/get-push-notifications.md).


## API actions

API path: `/user/session/push_token`.

### `bind`

Binds Push token with a current session.

#### Parameters

| name            | description                                                                                                                              | type                                              |
|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------|
| application     | Application ID, "navixy_iphone_viewer" or "navixy_android_viewer" or "w3c_pushapi".                                                      | [enum](../../../../getting-started/introduction.md#data-types) |
| token           | Push token or endpoint from pushSubscription, full URL like https://fcm.googleapis.com/fcm/send/f6kicrBn7S0:APA91b if your app ID is " " | string                                            |
| parameters      | Should be used only with object with "w3c_pushapi". Contain keys from pushSubscription {"p256dh": "...", "auth":"..."}                   | JSON object                                       |
| category_filter | Optional. Push notifications category filter, default is `*`.                                                                            | string                                            |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/push_token/bind' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "application": "navixy_android_viewer", "token": "f4be7b9d04da2ce1af111b"}'
    ```

#### Response

```json
{ "success": true }
```

Using `category_filter` you can filter out unwanted notifications categories.

If `category_filter` equals to `*` this means all categories allowed.

Delimited with comma list means that allowed only listed categories i.e. `chat_message,history_rule`.

Prepended with minus and delimited with comma list means that all categories allowed except given i.e. – `history_task,history_rule`.

##### Possible categories:

* `chat_message` – notification about new chat message.
* `history_rule` – notifications related to rule actuation.
* `history_task` – notifications related to tasks.
* `history_info` – service information.
* `history_service_task` – service task notifications.
* `history_work_status` – work status notifications.

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.


### `delete`

Deletes push token bound with the session.

#### Parameters

Only session `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/push_token/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/session/push_token/delete?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{ "success": true }
```

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types only.


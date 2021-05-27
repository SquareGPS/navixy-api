---
title: Push token
description: Contains API calls to interact with push token.
---

# Push token

Contains API calls to interact with push token.

<hr>

## API actions

API path: `/user/session/push_token`.

### bind

Binds Push token with a current session.

#### parameters

| name | description | type |
| :----- | :-----  | :----- |
| application | Application ID, for now it's "navixy_iphone_viewer" or "navixy_android_viewer". | [enum](../../../../getting-started.md#data-types) |
| token | Push token. | string |
| category_filter | Optional. Push notifications category filter, default is `*`. | string |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/push_token/bind' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "application": "navixy_android_viewer", "token": "f4be7b9d04da2ce1af111b"}'
    ```

#### response

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

#### errors

* [General](../../../../getting-started.md#error-codes) types only.

<hr>

### delete

Deletes push token bound with the session.

#### parameters

Only session `hash`.

#### examples

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

#### response

```json
{ "success": true }
```

#### errors

[General](../../../../getting-started.md#error-codes) types only.
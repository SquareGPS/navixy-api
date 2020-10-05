---
title: Push token
description: Push token
---

# Push token

API path: `/user/session/push_token`.

### bind

Binds Push token with current session.

#### parameters

*   **application** (string) – Application ID, for now it’s “navixy_iphone_viewer” or “navixy_android_viewer”
*   **token** (string) – Push token
*   **category_filter** (string) – Push notifications category filter, default is *

#### response

```json
{ "success": true }
```

Using `category_filter` you can filter out unwanted notifications categories.

If `category_filter` equals to `*` this means all categories are allowed.

Delimited with comma list means that allowed only listed categories i.e. `chat_message,history_rule`.

Prepended with minus and delimited with comma list means that all categories are allowed except given i.e. – `history_task,history_rule`.


##### Possible categories:

* `chat_message` – notification about new chat message
* `history_rule` – notifications related to rule actuation
* `history_task` – notifications related to tasks
* `history_info` – service information
* `history_service_task` – service task notifications
* `history_work_status` – work status notifications


### delete


Deletes push token that bound with the session.

#### response

```json
{ "success": true }
```


#### errors

[General](../../../../getting-started.md#error-codes) types only.
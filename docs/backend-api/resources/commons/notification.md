---
title: Notification
description: Contains an API call to get list of user notifications.
---

# Notification

Contains an API call to get list of user notifications.

***

## API actions

API path: `/notification`.

### list

Lists user notifications.

#### parameters

Only API key `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/notification/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/notification/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
         "id": 12451529,
         "message": "notification",
         "show_till": "2020-12-31 17:27:28"
    }]
}
```

* `id` - int. An id of notification.
* `message` - string. Message of notification.
* `show_till` - date/time. Date until notification should be shown.

#### errors

* [General](../../getting-started.md#error-codes) types only.

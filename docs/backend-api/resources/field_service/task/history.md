---
title: Task history
description: Navixy platform tracks changes to task fields and state for your convenience. Contains API calls to get this information.
---

# Task history

Our platform tracks changes to task fields and state for your convenience. Contains API calls to get this information.


## History entry

```json
{
    "id": 22,
    "user_id": 3,
    "task_id": 1,
    "event_date": "2014-08-05 10:54:55",
    "operation": "assign",
    "payload": {
    "tracker_id": 2470
    }
}
```

* `id` - int. Entry ID.
* `user_id` - int. User ID.
* `task_id` - int. An ID of the task with which this entry associated.
* `event_date` - [date/time](../../../getting-started/introduction.md#data-types). Date when history event happened.
* `operation` - [enum](../../../getting-started/introduction.md#data-types). Operation which happened. Can be "create", "update", "assign" or "status_change".
* `payload` - depends on operation. Typically, contains fields which were changed during operation.


## API actions

API base path: `task/history`.

### `list`

Returns history for the task with the specified ID.

#### Parameters

| name    | description     | type | 
|:--------|:----------------|:-----|
| task_id | ID of the task. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/checkpoint/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint_id": 23144}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/checkpoint/delete?hash=a6aa75587e5c59c32d347da438505fc3&checkpoint_id=23144
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 22,
         "user_id": 3,
         "task_id": 1,
         "event_date": "2014-08-05 10:54:55",
         "operation": "assign",
         "payload": {
         "tracker_id": 2470
         }
    }]
}
```

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.

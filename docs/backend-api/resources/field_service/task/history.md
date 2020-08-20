---
title: Task history
description: Task history
---

# Task history

Our platform tracks changes to task fields and state for your convenience.

## API actions

API base path: `task/history`.

```js
<history_entry> =
    {
        "id": 22, //PK
        "user_id": 3, //user id
        "task_id": 1, //id of the task with which this entry is assciated
        "event_date": "2014-08-05 10:54:55", //date when history event happened
        "operation": "assign", //operation which happened: create, update, assign or status_change
        "payload": { //depends on operation. Typically contains fields which were changed during operation
        "tracker_id": 2470
    }
}
```



### list

Return history for the task with the specified id.

#### parameters

* **task_id** - (int) Id of the task

#### response

```js
{
    "success": true,
    "list": [ <history_entry>, ... ]
}
```

#### errors

No specific errors.

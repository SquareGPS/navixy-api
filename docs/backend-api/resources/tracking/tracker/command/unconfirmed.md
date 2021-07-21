---
title: Unconfirmed commands
description: API calls for to interact with unconfirmed SMS commands in the queue of the specified tracker.
---

# Unconfirmed commands

API calls for to interact with unconfirmed SMS commands in the queue of the specified tracker.

<hr>

## API actions

API path: `/tracker/command/unconfirmed`.

### count

Gets number of commands in queue for the specified tracker.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/command/unconfirmed/count' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/command/unconfirmed/count?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### response

```json
{
    "success": true,
    "count": 0
}
```

* `count` - int. Number of unconfirmed commands in a queue.

#### errors

* 204 – Entity not found - if there is no tracker with such id belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.

<hr>

### reset

Removes all pending SMS commands from the queue for the specified tracker.

**required sub-user rights:** `tracker_update`.

#### parameters

| name | description | type| format|
| :------ | :------ | :----- | :------ |
| tracker_id | Id of the tracker (aka "object_id"). Tracker must belong to authorized user and not be blocked. | int | 123456 |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tracker/command/unconfirmed/reset' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 123456}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tracker/command/unconfirmed/reset?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=123456
    ```

#### response

```json
{ "success": true }
```

#### errors

* 204 – Entity not found - if there is no tracker with such id belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.

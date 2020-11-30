---
title: Checkpoints
description: Checkpoints
---

# Task schedule checkpoints

These actions allow manipulating schedule checkpoint entries similarly to regular route checkpoints.

## API actions

API path: `/task/schedule/checkpoint`.

### delete

Deletes a checkpoint from route and reorder others.<br>
If route has two checkpoints then use transmute on the other checkpoint, because route must have
at least two checkpoints.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| checkpoint_id | Checkpoint ID. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/checkpoint/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint_id": 11231}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/schedule/checkpoint/delete?hash=a6aa75587e5c59c32d347da438505fc3&checkpoint_id=11231
    ```

#### response

```json
{ "success": true }
```

### transmute

Transmutes a checkpoint to task and delete its route and other checkpoints in the route.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| checkpoint_id | Checkpoint ID. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/checkpoint/transmute' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint_id": 11231}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/schedule/checkpoint/transmute?hash=a6aa75587e5c59c32d347da438505fc3&checkpoint_id=11231
    ```

#### response

```json
{ "success": true }
```

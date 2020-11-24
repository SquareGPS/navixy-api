---
title: Scheduling routes
description: Scheduling routes
---

# Scheduling routes

These actions allow creating scheduled routes similarly to regular routes.

## API actions

API base path: `/task/schedule/route`.

### create

Creates route schedule with checkpoints.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| route | [Route schedule entry](./index.md#route schedule entry) without fields which are *IGNORED*. | JSON object |
| checkpoints | Array of route's [checkpoints](./index.md#checkpoint schedule entry) without fields which are *IGNORED*. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route": {"tracker_id": 22, "label": "Shop", "description": "Buy things", "parameters": {"type": "month_days","month_days": [1, 10, 31]}}, "checkpoints": [{"tracker_id": 22, "label": "Shop", "description": "Buy things", "parent_id": 1, "order": 0, "location": { "lat": 56.5, "lng": 60.5, "address": "Moltkestrasse 32", "radius": 150}, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "from_time": "12:34:00", "duration": 60, "tags": [1, 2], "form_template_id": 1}]}'
    ```

#### response
```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An id of the created route schedule entry.

### delete

Deletes route schedule with checkpoints.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| id | Route schedule ID. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/route/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 23144}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/schedule/route/delete?hash=a6aa75587e5c59c32d347da438505fc3&id=23144
    ```

#### response
```json
{
    "success": true
}
```

### update

Updates route schedule with checkpoints. If checkpoint is being created, then it should have no id.
If checkpoint is being updated, then it should have an id. If old checkpoint is not present in request, then it
 will be deleted.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| route | [Route schedule entry](./index.md#route schedule entry) without fields which are *IGNORED*. | JSON object |
| checkpoints | Array of route's [checkpoints](./index.md#checkpoint schedule entry) without fields which are *IGNORED*. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route": {"id": 111, "tracker_id": 22, "label": "Shop", "description": "Buy things", "parameters": {"type": "month_days","month_days": [1, 10, 31]}}, "checkpoint": {"id": 111, "tracker_id": 22, "label": "Shop", "description": "Buy things", "parent_id": 1, "order": 0, "location": { "lat": 56.5, "lng": 60.5, "address": "Moltkestrasse 32", "radius": 150}, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "from_time": "12:34:00", "duration": 60, "tags": [1, 2], "form_template_id": 1}}'
    ```

#### response

```json
{ "success": true }
```

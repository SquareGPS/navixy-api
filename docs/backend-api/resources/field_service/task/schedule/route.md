---
title: Scheduling routes
description: These actions allow creating scheduled routes similarly to regular routes.
---

# Scheduling routes

These actions allow creating scheduled routes similarly to regular routes.


## Route schedule entry

 ```json
{
    "id": 111,
    "user_id": 3,
    "tracker_id": 22,
    "label": "Shop",
    "description": "Buy things",
    "parameters": {
      "type": "month_days",
      "month_days": [1, 10, 31]
    }
}
```

* `id` - int. Primary key. Used in the update call, *IGNORED* in create.
* `user_id` - int. User id. *IGNORED* in create/update.
* `tracker_id` - int. An ID of the tracker to which all generated tasks assigned. Nullable.
* `parameters` - schedule parameters can be "weekdays" or "month_days". Described below.


## Checkpoint schedule entry

```json
{
    "id": 111,
    "user_id": 3,
    "tracker_id": 22,
    "label": "Shop",
    "description": "Buy things",
    "parent_id": 1,
    "order": 0,
    "location": {
        "lat": 53.787154,
        "lng": 9.757980,
        "address": "Moltkestrasse 32",
        "radius": 150
    },
    "max_delay" : 5,
    "min_stay_duration": 0,
    "min_arrival_duration": 0,
    "from_time": "12:34:00",
    "duration": 60,
    "tags": [1, 2],
    "form_template_id": 1
}
```

* `id` - int. Primary key. Used in the update call, *IGNORED* in create.
* `user_id` - int. User id. *IGNORED* in create/update.
* `tracker_id` - int. An ID of the tracker to which all generated tasks assigned. Nullable.
* `location` - location associated with this task. Cannot be null.
    * `address` - string. Address of the location.
    * `radius` - int. Radius of location zone in meters.
* `max_delay` - int. Maximum allowed task completion delay in minutes.
* `min_stay_duration` - int. Minimum duration of stay in task zone for task completion, minutes.
* `min_arrival_duration` - int. Visits less than these values will be ignored, minutes.
* `from_time` - string time. Time of day which defines start of the task within the days.
* `duration` - int. Total duration in minutes between "from" and "to" for generated tasks.
* `tags` - int array. List of tag IDs.
* `form_template_id` - int. Form template id. Nullable.

`<schedule_parameters>` can be one of the following:

* weekdays - task creation based on week day.

```json
{
    "type": "weekdays",
    "weekdays": [1, 5, 6]
}
```

    * `weekdays` - int array. Week days on which tasks will be created (1 = Monday, ... 7 = Sunday)

* month_days - task creation based on day of month.

```json
{
    "type": "month_days",
    "month_days": [1, 10, 31]
}
```

    * `month_days` - int array. Days of month on which tasks will be created (1..31).


## API actions

API base path: `/task/schedule/route`.

### `create`

Creates route schedule with checkpoints.

#### Parameters

| name        | description                                                                                    | type        | 
|:------------|:-----------------------------------------------------------------------------------------------|:------------|
| route       | [Route schedule entry](#route-schedule-entry) without fields which are *IGNORED*.              | JSON object |
| checkpoints | Array of route's [checkpoints](#checkpoint-schedule-entry) without fields which are *IGNORED*. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/route/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route": {"tracker_id": 22, "label": "Shop", "description": "Buy things", "parameters": {"type": "month_days","month_days": [1, 10, 31]}}, "checkpoints": [{"tracker_id": 22, "label": "Shop", "description": "Buy things", "parent_id": 1, "order": 0, "location": { "lat": 53.787154, "lng": 9.757980, "address": "Moltkestrasse 32", "radius": 150}, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "from_time": "12:34:00", "duration": 60, "tags": [1, 2], "form_template_id": 1}]}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An ID of the created route schedule entry.

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types.


### `delete`

Deletes route schedule with checkpoints.

#### Parameters

| name | description        | type | 
|:-----|:-------------------|:-----|
| id   | Route schedule ID. | int  |

#### Examples

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

#### Response

```json
{
    "success": true
}
```

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types.


### `update`

Updates route schedule with checkpoints. If checkpoint is being created, then it should have no id.
If checkpoint is being updated, then it should have an ID. If old checkpoint is not present in request, then it
 will be deleted.

#### Parameters

| name        | description                                                                                    | type        | 
|:------------|:-----------------------------------------------------------------------------------------------|:------------|
| route       | [Route schedule entry](#route-schedule-entry) without fields which are *IGNORED*.              | JSON object |
| checkpoints | Array of route's [checkpoints](#checkpoint-schedule-entry) without fields which are *IGNORED*. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/route/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route": {"id": 111, "tracker_id": 22, "label": "Shop", "description": "Buy things", "parameters": {"type": "month_days","month_days": [1, 10, 31]}}, "checkpoints": {"id": 111, "tracker_id": 22, "label": "Shop", "description": "Buy things", "parent_id": 1, "order": 0, "location": { "lat": 53.787154, "lng": 9.757980, "address": "Moltkestrasse 32", "radius": 150}, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "from_time": "12:34:00", "duration": 60, "tags": [1, 2], "form_template_id": 1}}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types.

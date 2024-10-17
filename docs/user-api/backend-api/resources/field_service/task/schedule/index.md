---
title: Recurring tasks
description: API actions to interact with recurring tasks. Some tasks happen on regular basis, and it's tedious to create them by hand every time. Task schedules is the way to automate this process.
---

# Recurring tasks

Some tasks happen on regular basis, and it's tedious to create them by hand every time. Task schedules is the way to automate
this process. At the beginning of each day (moments after 00:00 AM according to [user's timezone setting](../../../commons/user/settings/index.md)),
schedule checked and if there are tasks which start at this day, they are created and assigned to employees (if assignee specified).

Schedule entries are very similar to tasks, main difference is that `from` and `to` containing specific date and time 
replaced with `from_time`, `duration` and `parameters`.


## Task schedule entry object

```json
{
    "id": 111,
    "user_id": 3,
    "tracker_id": 22,
    "location": {
        "lat": 53.787154,
        "lng": 9.757980,
        "address": "Moltkestrasse 32",
        "radius": 150
    },
    "label": "Shop",
    "description": "Buy things",
    "from_time": "12:34:00",
    "duration": 60,
    "max_delay" : 5,
    "min_stay_duration": 0,
    "min_arrival_duration": 0,
    "parameters": {
        "type": "weekdays",
        "weekdays": [1, 5, 6]
    },
    "tags": [1, 2],
    "form_template_id": 1
}
```

* `id` - int. Primary key. Used in the update call, *IGNORED* in create.
* `user_id` - int. User ID. *IGNORED* in create/update.
* `tracker_id` - int. An ID of the tracker to which all generated tasks assigned. Nullable.
* `location` - location associated with this task. Cannot be null.
    * `address` - string. Address of the location.
    * `radius` - int. Radius of location zone in meters.
* `from_time` - string time. Time of day which defines start of the task within the days.
* `duration` - int. Total duration in minutes between "from" and "to" for generated tasks.
* `max_delay` - int. Maximum allowed task completion delay in minutes.
* `min_stay_duration` - int. Minimum duration of stay in task zone for task completion, minutes.
* `min_arrival_duration` - int. Visits less than these values will be ignored, minutes.
* `parameters` - schedule parameters can be "weekdays" or "month_days". Described below.
* `tags` - int array. List of tag IDs.
* `form_template_id` - int. Form template ID. Nullable.


## API actions

API base path: `task/schedule`.

### `create`

Creates new task schedule entry.

**required sub-user rights**: `task_update`.

#### Parameters

| name     | description                                                 | type        | 
|:---------|:------------------------------------------------------------|:------------|
| schedule | `schedule_entry` object without fields which are *IGNORED*. | JSON object |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "schedule": {"tracker_id": 22, "location": {"lat": 53.787154, "lng": 9.757980, "address": "Moltkestrasse 32", "radius": 150}, "label": "Shop", "description": "Buy things", "from_time": "12:34:00", "duration": 60, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "parameters": {"type": "weekdays", "weekdays": [1, 5, 6]}, "tags": [1, 2], "form_template_id": 1}'
    ```

#### Response

```json
{
    "success": true,
    "id": 111
}
```

* `id` - int. An ID of the created schedule entry.

#### Errors

* 201 – Not found in the database - if schedule.tracker_id belongs to nonexistent tracker.
* 204 – Entity not found - if schedule.form_template_id belongs to nonexistent form template.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 236 – Feature unavailable due to tariff restrictions - if device's tariff does not allow usage of tasks.


### `delete`

Delete task schedule with the specified ID.

**required sub-user rights**: `task_update`.

#### Parameters

| name        | description                        | type | 
|:------------|:-----------------------------------|:-----|
| schedule_id | ID of the task schedule to delete. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "schedule_id": 23144}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/schedule/delete?hash=a6aa75587e5c59c32d347da438505fc3&schedule_id=23144
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no task schedule with such an ID.


### `list`

Get all task or route schedules belonging to user with optional filtering.<br>
Also this call returns all unassigned task schedules.

#### Parameters

| name     | description                                                                                                   | type         | 
|:---------|:--------------------------------------------------------------------------------------------------------------|:-------------|
| trackers | Optional. IDs of the trackers to which task schedule is assigned.                                             | int array    |
| filter   | Optional. Filter for task schedule label and description.                                                     | string       |
| tag_ids  | Optional. Tag IDs assigned to the task schedule. The schedules found must include all the tags from the list. | int array    |
| types    | Optional. Tasks of specific type will be returned in the list. Can be `task` or `route`. Default is `task`.   | string array |


#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/schedule/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 111,
         "user_id": 3,
         "tracker_id": 22,
         "location": {
             "lat": 53.787154,
             "lng": 9.757980,
             "address": "Moltkestrasse 32",
             "radius": 150
         },
         "label": "Shop",
         "description": "Buy things",
         "from_time": "12:34:00",
         "duration": 60,
         "max_delay" : 5,
         "min_stay_duration": 0,
         "min_arrival_duration": 0,
         "parameters": {
             "type": "weekdays",
             "weekdays": [1, 5, 6]
         },
         "tags": [1, 2],
         "form_template_id": 1
    }]
}
```

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types only.


### `read`

Gets task, route or checkpoint schedule by specified ID.

#### Parameters

| name | description                                  | type | 
|:-----|:---------------------------------------------|:-----|
| id   | An ID of task, route or checkpoint schedule. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 12314}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/schedule/read?hash=a6aa75587e5c59c32d347da438505fc3&id=12314
    ```

#### Response

```json
{
    "success": true,
    "value": {
         "id": 111,
         "user_id": 3,
         "tracker_id": 22,
         "label": "Shop",
         "description": "Buy things",
         "parameters": {
            "type": "weekdays",
            "weekdays": [1, 5, 6]
         }
    },
    "checkpoints": [{
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
    }]
}
```

* `value` - <schedule_entry> object.
* `checkpoints` - if value is <route_schedule_entry>.

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types only.


### `update`

Updates existing task schedule.

**required sub-user rights**: `task_update`.

#### Parameters

| name     | description                                                 | type        | 
|:---------|:------------------------------------------------------------|:------------|
| schedule | `schedule_entry` object without fields which are *IGNORED*. | JSON object |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/schedule/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "schedule": {"tracker_id": 22, "location": {"lat": 53.787154, "lng": 9.757980, "address": "Moltkestrasse 32", "radius": 150}, "label": "Shop", "description": "Buy things", "from_time": "12:34:00", "duration": 60, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "parameters": {"type": "weekdays", "weekdays": [1, 5, 6]}, "tags": [1, 2], "form_template_id": 1}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if schedule.tracker_id belongs to nonexistent tracker.
* 204 – Entity not found - if there is no task schedule with specified ID.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 236 – Feature unavailable due to tariff restrictions - if device's tariff does not allow usage of tasks.

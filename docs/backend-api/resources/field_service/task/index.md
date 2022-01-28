---
title: Working with tasks
description: API calls to work with tasks
---

# Working with tasks

You can assign task to any tracked device. If specified tracker visits task checkpoint at the specified time and meets other
conditions such as filling form or staying in the task zone for the specified time, the task completed. Otherwise,
the task either failed completely or completed with warnings.

If task assigned to a Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)),
it's available for viewing by app user. User will also receive notifications of newly assigned tasks, task changes, etc.

***

## Task object

```json
{
    "id": 111,
    "user_id": 3,
    "tracker_id": 22,
    "location": {
        "lat": 56.5,
        "lng": 60.5,
        "address": "Fichtenstrasse 11",
        "radius": 150
    },
    "label": "Deliver parcels",
    "description": "Quickly",
    "creation_date": "2014-01-02 03:04:05",
    "from": "2014-02-03 04:05:06",
    "to": "2014-03-04 05:06:07",
    "external_id": null,
    "status": "assigned",
    "status_change_date": "2014-01-02 03:04:05",
    "max_delay" : 5,
    "min_stay_duration": 0,
    "arrival_date": "2014-01-02 03:04:05",
    "stay_duration": 0,
    "origin": "imported",
    "tags": [1, 2],
    "type": "task",
    "form": <form_object>,
    "form_template_id": 13245,
    "fields": {
        "131312" : {
             "type": "text",
             "value":  "I love text!"
        }
   }
}
```

* `id` - int. Primary key. Used in task/update, *IGNORED* in task/create.
* `user_id` - int. User id. *IGNORED* in create/update.
* `tracker_id` - int. An id of the tracker to which task assigned. Can be null.  *IGNORED* in task/update.
* `location` - location associated with this task. Cannot be null.
    * `address` - string. Address of the location.
    * `radius`- int. Radius of location zone in meters.
* `creation_date` - [date/time](../../../getting-started.md#data-types). When task created. *IGNORED* in create/update.
* `from` - [date/time](../../../getting-started.md#data-types). Date AFTER which task zone must be visited.
* `to` - [date/time](../../../getting-started.md#data-types). Date BEFORE which task zone must be visited.
* `external_id` - string. Used if task imported from external system. Arbitrary text string. Can be null.
* `status` - [enum](../../../getting-started.md#data-types). Task status. *IGNORED* in create/update. Can have "unassigned" value (unassigned to any executor),
 "assigned", "done", "failed", "delayed", "arrived" (arrived to geofence but haven't done the task), "faulty" (with problems).
* `status_change_date` - [date/time](../../../getting-started.md#data-types). When task status changed. *IGNORED* in create/update.
* `max_delay` - int. Maximum allowed task completion delay in minutes.
* `min_stay_duration` - int. Minimum duration of stay in task zone for task completion, minutes.
* `arrival_date` - [date/time](../../../getting-started.md#data-types). When tracker has arrived to the task zone. *IGNORED* in create/update.
* `stay_duration` - int. Duration of stay in the task zone, seconds.
* `origin` - string. Task origin. *IGNORED* in create/update.
* `tags` - int array. List of tag ids.
* `form` - [form object](../form/index.md#form-object). If present.
* `form_template_id` - int. An id of form template. Used in create and update actions only if `create_form` parameter is `true` in them.
* `fields` - optional object. A map, each key of which is a custom field id *as a string*. See [entity/fields](../../commons/entity/fields.md)

!!! note "To associate the task with an address - this field should be added to the location object."

***

## API actions

API base path: `/task`.

### assign

(Re)assigns task to new tracker (or make it unassigned).

**required sub-user rights**: `task_update`.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| task_id | Id of the task to assign. | int |
| tracker_id | Id of the tracker. Tracker must belong to authorized user and not be blocked. If null, task will be assigned to no one. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/assign' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144, "tracker_id": 132421}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/assign?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144&tracker_id=132421
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no task with such an id).
* 204 – Entity not found (if there is no tracker with such id belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 255 – Invalid task state (if current task state is not "unassigned" or "assigned").
* 236 – Feature unavailable due to tariff restrictions (if device's tariff does not allow usage of tasks).

***

### batch_convert

Converts batch of tab-delimited tasks and return list of checked tasks with errors.

**required sub-user rights**: `task_update`.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| batch | Batch of tab-delimited tasks. | string |
| fields | Optional. Array of field names, default is `["label", "from", "to", "address", "lat", "lng", "description"]`. | string array |
| geocoder | Geocoder type. | [enum](../../../getting-started.md#data-types) |
| default_radius | Optional. Radius for point, default is 100. | int |
| default_max_delay | Optional. Max delay for tasks, default is 0. | int |
| default_duration | Optional. Duration for task in minutes, default is 60. | int
| default_min_stay_duration | Optional. Minimal stay duration for task in minutes, default is 0. | int |
| location_check_mode | Optional. One of "no_check", "entity_location", "parent_location" | [enum](../../../getting-started.md#data-types) |
| employee_ids | Optional. List of employee Ids to automatic assign | int array |
| vehicle_ids | Optional. List of vehicle Ids to automatic assign | int array |

In case of location_check_mode==entity_location – vehicle_ids will be ignored.

#### response

```json
{
    "success": true,
    "list": [{
         "id": 111,
         "user_id": 3,
         "tracker_id": 22,
         "location": {
             "lat": 56.5,
             "lng": 60.5,
             "address": "Fichtenstrasse 11",
             "radius": 150
         },
         "label": "Deliver parcels",
         "description": "Quickly",
         "creation_date": "2014-01-02 03:04:05",
         "from": "2014-02-03 04:05:06",
         "to": "2014-03-04 05:06:07",
         "external_id": null,
         "status": "assigned",
         "status_change_date": "2014-01-02 03:04:05",
         "max_delay" : 5,
         "min_stay_duration": 0,
         "arrival_date": "2014-01-02 03:04:05",
         "stay_duration": 0,
         "origin": "imported",
         "tags": [1, 2],
         "type": "task",
         "form": <form_object>,
         "errors": [<error_object>]
    }],
    "limit_exceeded": false
}
```

* `list` - list of checked task objects that contain all fields from task and field `errors`.
    * `errors` - array of objects. Optional. List of errors.
* `limit_exceeded` - boolean. `true` if given batch constrained by a limit.

#### errors

[General](../../../getting-started.md#error-codes) types only.

***

### count

Returns total number of tasks belonging to current user.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/count' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/count?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "count": 111
}
```

* `count` - int. Number of tasks.

***

### create

Creates a new task.

**required sub-user rights**: `task_update`.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| task | `task` object without fields which are **IGNORED** | JSON object |
| create_form | If `true` then check additional `form_template_id` field in `task` object and create form if it is not null. Default value is `false` for backward compatibility. | boolean |

Minimal JSON object to create a new task must contain:

```json
{
    "tracker_id": 22,
    "location": {
    "lat": 56.83717295,
    "lng": 60.59761920,
    "radius": 150
    },
    "label": "Name",
    "description": "Description example",
    "from": "2020-02-03 04:05:06",
    "to": "2020-03-04 05:06:07"
}
```

* `tracker_id` - int. Optional. if the field specified then the task will be assigned to the employee associated with
 the tracker, otherwise it won't be assigned to anybody.
* `location` - area (circle geofence), entering and leaving of geofence will be controlled.
    * `lat` - float. Latitude.
    * `lng` - float. Longitude.
    * `radius` - int. Radius in meters.
* `label` - string. Task name, length 1-200 characters.
* `description` - string. Task description, length 0-1024 characters.
* `from` - [date/time](../../../getting-started.md#data-types). Start date of the interval - when the specified location has to be visited (in the user's time zone).
* `to` - [date/time](../../../getting-started.md#data-types). End date of the interval - when the specified location has to be visited (in the user's time zone).

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/create' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task": {"tracker_id": 22, "location": {"lat": 56.83717295, "lng": 60.59761920, "radius": 150}, "label": "Name", "description": "Description example", "from": "2020-02-03 04:05:06", "to": "2020-03-04 05:06:07"}, "create_form": false}'
    ```
    
task/create call returns the identifier of the created task.
A returned object also can include "external_id_counts" field see task/route/create [method description](./route/index.md#create).

#### response

```json
{
    "success": true,
    "id": 111,
    "external_id_counts": [{
        "external_id": "456", 
        "count": 2
    }]
}
```

* `id` - int. An id of the created task.

**Note:** The "id" parameter is unique, it is automatically generated by the server when you create a task. Therefore, 
if you call task/create  two times with the same parameters, every time the new task will be created. These two tasks 
will differ only by an id. Respectively, if the created task has to be connected to a certain record in external system,
 you have to remember the id of this record to use it in future when you want to change/delete the associated task in our system.

#### errors

* 201 – Not found in the database (if task.tracker_id is not null and belongs to nonexistent tracker).
* 236 – Feature unavailable due to tariff restrictions (if device's tariff does not allow usage of tasks).

***

### delete

Deletes the task with the specified id.

**required sub-user rights**: `task_update`.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| task_id | Id of the task to delete. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/delete?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no task with such an id).

***

### list

Gets all task belonging to user with optional filtering.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| external_id | Optional. External task ID for search. | string |
| statuses | Optional. Default all. List of task statuses, e.g. `["unassigned","failed"]`. | string array |
| trackers | Optional. Ids of the trackers to which task assigned. | int array |
| from | Optional. Show tasks which are actual AFTER this date, e.g. "2020-07-01 00:00:00". | [date/time](../../../getting-started.md#data-types) |
| to | Optional. Show tasks which are actual BEFORE this date, e.g. "2020-07-01 00:00:00". | [date/time](../../../getting-started.md#data-types) |
| conditions | Optional. Search conditions to apply to list. Array of search conditions. | array of [SearchCondition](../../commons/entity/search_conditions.md) |
| filter | Optional. Filter for all built-in and custom fields. If used with conditions, both filter and conditions must match for every returned task. | string |
| filters | Optional. Filters for task label, description or address. | string array |
| tag_ids | Optional. Tag IDs assigned to the task. | int array |
| location | Optional. Location with radius, inside which task zone centers must reside. Example: ```{ "lat": 56.823777, "lng": 60.594164, "radius": 350 }``` | Location JSON |
| offset | Optional. Offset from start of the found tasks for pagination. | int |
| limit | Optional. Limit of the found tasks for pagination. | int |

##### condition fields

| Name | Type | Comment |
| :--- | :--- | :--- |
| id | number |  |
| employee | number | id |
| status | string |  |
| label | string |  |
| location | string | address |
| from | [date/time](../../../getting-started.md#data-types) |  |
| to | [date/time](../../../getting-started.md#data-types) |  |
| status_change_date | [date/time](../../../getting-started.md#data-types) |  |
| arrival_date | [date/time](../../../getting-started.md#data-types) |  |
| stay_duration | Seconds |  |
| description | string |  |
| external_id | string |  |
| form | number | template's id |

If **external_id**, **trackers**, **filters**, **from**, **to** or **tag_ids** is not passed or _null_ then appropriate 
condition not used to filter results.

If **offset** or **limit** is null then restrictions for pagination will not be applied.

##### sort: string[]?

set of sort options. Each option is a pair of column name and sorting direction, e.g. ["label=acs", "address=desc", "employee=desc"].

##### sort fields

| Name | Type | Comment |
| :--- | :--- | :--- |
| id | number |  |
| employee | string | full name or tracker label |
| status | string |  |
| label | string |  |
| location | string | address |
| from | [date/time](../../../getting-started.md#data-types) |  |
| to | [date/time](../../../getting-started.md#data-types) |  |
| status_change_date | [date/time](../../../getting-started.md#data-types) |  |
| arrival_date | [date/time](../../../getting-started.md#data-types) |  |
| stay_duration | Seconds |  |
| description | string |  |
| external_id | string |  |
| form | string | label |

If **external_id**, **trackers**, **filters**, **from**, **to** or **tag_ids** is not passed or _null_ then appropriate condition not used to filter results.

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/list' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true,
    "list": [{
        "id": 111,
        "user_id": 3,
        "tracker_id": 22, 
        "location": {
            "lat": 56.5,
            "lng": 60.5,
            "address": "Schulhof 2, Wien, Austria",
            "radius": 150
         },
         "label": "Name",
         "description": "Description example",
         "creation_date": "2014-01-02 03:04:05",
         "from": "2020-02-03 04:05:06",
         "to": "2020-03-04 05:06:07",
         "external_id": "01234567",
         "status": "assigned",
         "status_change_date": "2020-01-02 03:04:05",
         "max_delay": 5,
         "min_stay_duration": 0,
         "arrival_date": "2020-01-02 03:04:05",
         "stay_duration": 10,
         "origin": "manual",
         "type": "task"
    }],
    "count": 1
}
```

* `list` - array of `task` objects.
    * `id` - int. Task id.
    * `user_id` - int. User id (office). An unchangeable parameter.
    * `tracker_id` - int. Tracker ID. Indicator ID by which the implementation of this task will be controlled.
    * `location` - area (circle geofence), entering and leaving of geofence will be controlled.
    * `label` - string. Task name, length 1-200 characters.
    * `description` - string. Task description, length 0-1024 characters.
    * `creation_date` - [date/time](../../../getting-started.md#data-types). Date of creation of a task, unchangeable field.
    * `from` - [date/time](../../../getting-started.md#data-types). Start date of the interval - when the specified location has to be visited (in the user's time zone).
    * `to` - [date/time](../../../getting-started.md#data-types). End date of the interval - when the specified location has to be visited (in the user's time zone).
    * `external_id` - string. Text field for tracking of communication of the task with certain external systems 
    (for example, number of the order). Is for reference only.
    * `status` - [enum](../../../getting-started.md#data-types). Current status of a task, can have "unassigned" value (unassigned to any executor), 
    "assigned", "done", "failed", "delayed", "arrived" (arrived to geofence but haven't done the task), "faulty" (with problems).
    * `status_change_date` - [date/time](../../../getting-started.md#data-types). Date of the last change of the status of a task.
    * `max_delay` - int. The maximum time delay of the execution of the task, in minutes.
    * `min_stay_duration` - int. The minimum stay time in the area of the task in which the task has to be done, in minutes.
    * `arrival_date` - [date/time](../../../getting-started.md#data-types). Date and time of arrival in the area of the task. Can be null. If the executor has not visited it yet.
    * `stay_duration` - int. Number of seconds spent inside task zone.
    * `origin` - [enum](../../../getting-started.md#data-types). The way of creation of a task. Can be "manual", "scheduled" or "imported" (from excel).
    * `type` - string. Reserved.
* `count` - int. count of the all found tasks.

#### errors

[General](../../../getting-started.md#error-codes) types only.

***

### read

Gets task, checkpoint, or route with checkpoints by specified id.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| task_id | Id of the task, route or checkpoint. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/read?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144
    ```

#### response

```json
{
    "success": true,
    "value":  <task or checkpoint or route>,
    "checkpoints": [
        <checkpoint1>,
        <checkpoint2>
    ]

}
```

* `value` - JSON object. `task` described [here](#task-object).
* `checkpoints` - only returned if entity with specified id is a route. Contains all checkpoints of this route. `checkpoint`
object described [here](./checkpoint.md#checkpoint-object).

#### errors

* 201 – Not found in the database (if there is no task with such an id).

***

### transmute

Converts task into a route checkpoint.

**required sub-user rights**: `task_update`.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| task_id | Id of the task to convert. | int |
| route_id | Id of the route to attach to. | int |
| order | Zero-based index at which checkpoint should be inserted into route. | int |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/transmute' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144, "route_id": 12334, "order": 0}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/transmute?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144&route_id=12334&order=0
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 – Not found in the database (if there is no task or route with such an id, or tracker to which checkpoint 
assigned is unavailable to current sub-user).
* 255 – Invalid task state (if task or any of the checkpoints are not in unassigned or assigned state).

***

### update

Updates existing task. Note that you cannot change task owner using this method.

**required sub-user rights**: `task_update`.

#### parameters

| name | description | type | 
| :--- | :--- | :--- |
| task | `task` object without fields which are *IGNORED*. | JSON object |
| create_form | If `true` then check additional `form_template_id` field in `task` object and create, replace or delete task's form. Default value is `false` for backward compatibility. | boolean |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/update' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task": {"id": 22379, "location": {"lat": 56.83717295, "lng": 60.59761920, "radius": 150}, "label": "Name", "description": "Description example", "from": "2020-02-03 04:05:06", "to": "2020-03-04 05:06:07"}, "create_form": false}'
    ```


    
A returned object also can include "external_id_counts" field see task/route/create [method description](./route/index.md#create).

#### response

```json
{
    "success": true,
    "external_id_counts": [{
        "external_id": "456", 
        "count": 2
    }]
}
```

#### errors

* 201 – Not found in the database (if there is no task with such an id).
* 255 – Invalid task state (if current task state is not "unassigned" or "assigned").

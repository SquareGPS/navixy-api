---
description: API calls to work with tasks
---

# Task

## Working with tasks

You can assign task to any tracked device. If specified tracker visits task checkpoint at the specified time and meets other\
conditions such as filling form or staying in the task zone for the specified time, the task completed. Otherwise,\
the task either failed completely or completed with warnings.

If task assigned to a Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker\&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)),\
it's available for viewing by app user. User will also receive notifications of newly assigned tasks, task changes, etc.

Find more guides on working with tasks [there](../../../guides/field-service-management/manage-tasks.md).

## Task object

```json
{
    "id": 111,
    "user_id": 3,
    "tracker_id": 22,
    "location": {
        "lat": 51.283546,
        "lng": 7.301086,
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

* `id` - int. Primary key. Used in task/update, _IGNORED_ in task/create.
* `user_id` - int. User ID. _IGNORED_ in create/update.
* `tracker_id` - int. An ID of the tracker to which task assigned. Can be null. **IGNORED** in task/update.
* `location` - location associated with this task. Cannot be null.
  * `address` - string. Address of the location.
  * `radius`- int. Radius of location zone in meters.
* `creation_date` - [date/time](../../../#data-types). When task created. _IGNORED_ in create/update.
* `from` - [date/time](../../../#data-types). Date AFTER which task zone must be visited.
* `to` - [date/time](../../../#data-types). Date BEFORE which task zone must be visited.
* `external_id` - string. Used if task imported from external system. Arbitrary text string. Can be null.
* `status` - [enum](../../../#data-types). Task status. _IGNORED_ in create/update. Can have "unassigned" value (unassigned to any executor),\
  "assigned", "done", "failed", "delayed", "arrived" (arrived to geofence but haven't done the task), "faulty" (with problems).
* `status_change_date` - [date/time](../../../#data-types). When task status changed. _IGNORED_ in create/update.
* `max_delay` - int. Maximum allowed task completion delay in minutes.
* `min_stay_duration` - int. Minimum duration of stay in task zone for task completion, minutes.
* `arrival_date` - [date/time](../../../#data-types). When tracker has arrived to the task zone. _IGNORED_ in create/update.
* `stay_duration` - int. Duration of stay in the task zone, seconds.
* `origin` - string. Task origin. _IGNORED_ in create/update.
* `tags` - int array. List of tag IDs.
* `form` - [form object](../form/index.md#form-object). If present.
* `form_template_id` - int. An ID of form template. Used in create and update actions only if `create_form` parameter is `true` in them.
* `fields` - optional object. A map, each key of which is a custom field ID _as a string_. See [entity/fields](../../commons/entity/fields.md)

> To associate the task with an address - this field should be added to the location object.

## API actions

API base path: `/task`.

### assign

(Re)assigns task to new tracker (or make it unassigned).

**required sub-user rights**: `task_update`.

#### Parameters

| name        | description                                                                                                             | type |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- | ---- |
| task\_id    | ID of the task to assign.                                                                                               | int  |
| tracker\_id | ID of the tracker. Tracker must belong to authorized user and not be blocked. If null, task will be assigned to no one. | int  |

#### Examples

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/task/assign' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144, "tracker_id": 132421}'
```
{% endcode %}
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/task/assign?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144&tracker_id=132421
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database (if there is no task with such an ID).
* 204 – Entity not found (if there is no tracker with such ID belonging to authorized user).
* 208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason).
* 255 – Invalid task state (if current task state is not "unassigned" or "assigned").
* 236 – Feature unavailable due to tariff restrictions (if device's tariff does not allow usage of tasks).

### batch\_convert

Converts batch of tab-delimited tasks and return list of checked tasks with errors.

**required sub-user rights**: `task_update`.

#### Parameters

| name                         | description                                                                                                   | type                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| batch                        | Batch of tab-delimited tasks.                                                                                 | string                       |
| fields                       | Optional. Array of field names, default is `["label", "from", "to", "address", "lat", "lng", "description"]`. | string array                 |
| geocoder                     | Geocoder type.                                                                                                | [enum](../../../#data-types) |
| default\_radius              | Optional. Radius for point, default is 100.                                                                   | int                          |
| default\_max\_delay          | Optional. Max delay for tasks, default is 0.                                                                  | int                          |
| default\_duration            | Optional. Duration for task in minutes, default is 60.                                                        | int                          |
| default\_min\_stay\_duration | Optional. Minimal stay duration for task in minutes, default is 0.                                            | int                          |
| location\_check\_mode        | Optional. One of "no\_check", "entity\_location", "parent\_location"                                          | [enum](../../../#data-types) |
| employee\_ids                | Optional. List of employee IDs to automatic assign                                                            | int array                    |
| vehicle\_ids                 | Optional. List of vehicle IDs to automatic assign                                                             | int array                    |

In case of l`ocation_check_mode==entity_location – vehicle_ids` will be ignored.

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 111,
         "user_id": 3,
         "tracker_id": 22,
         "location": {
             "lat": 51.283546,
             "lng": 7.301086,
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

#### Errors

[General](../../../errors.md#error-codes) types only.

### count

Returns total number of tasks belonging to current user.

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/task/count' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
```http
{{ extra.api_example_url }}/task/count?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
    "success": true,
    "count": 111
}
```

* `count` - int. Number of tasks.

### create

Creates a new task.

**required sub-user rights**: `task_update`.

#### Parameters

| name         | description                                                                                                                                                       | type        |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| task         | `task` object without fields which are **IGNORED**                                                                                                                | JSON object |
| create\_form | If `true` then check additional `form_template_id` field in `task` object and create form if it is not null. Default value is `false` for backward compatibility. | boolean     |

Minimal JSON object to create a new task must contain:

```json
{
    "tracker_id": 22,
    "location": {
    "lat": 34.178868, 
    "lng": -118.599672,
    "radius": 150
    },
    "label": "Name",
    "description": "Description example",
    "from": "2020-02-03 04:05:06",
    "to": "2020-03-04 05:06:07"
}
```

* `tracker_id` - int. Optional. if the field specified then the task will be assigned to the employee associated with\
  the tracker, otherwise it won't be assigned to anybody.
* `location` - area (circle geofence), entering and leaving of geofence will be controlled.
  * `lat` - float. Latitude.
  * `lng` - float. Longitude.
  * `radius` - int. Radius in meters.
* `label` - string. Task name, length 1-200 characters.
* `description` - string. Task description, length 0-1024 characters.
* `from` - [date/time](../../../#data-types). Start date of the interval - when the specified location has to be visited (in the user's time zone).
* `to` - [date/time](../../../#data-types). End date of the interval - when the specified location has to be visited (in the user's time zone).

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/task/create' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task": {"tracker_id": 22, "location": {"lat": 34.178868, "lng": -118.599672, "radius": 150}, "label": "Name", "description": "Description example", "from": "2020-02-03 04:05:06", "to": "2020-03-04 05:06:07"}, "create_form": false}'
```
{% endcode %}

task/create call returns the identifier of the created task.\
A returned object also can include "external\_id\_counts" field see task/route/create [method description](route/index.md#create).

#### Response

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

* `id` - int. An ID of the created task.

{% hint style="info" %}
The "id" parameter is unique, it is automatically generated by the server when you create a task. Therefore, if you call task/create two times with the same parameters, every time the new task will be created. These two tasks will differ only by an ID. Respectively, if the created task has to be connected to a certain record in external system, you have to remember the ID of this record to use it in future when you want to change/delete the associated task in our system.
{% endhint %}

#### Errors

* 201 – Not found in the database (if task.tracker\_id is not null and belongs to nonexistent tracker).
* 236 – Feature unavailable due to tariff restrictions (if device's tariff does not allow usage of tasks).

### delete

Deletes the task with the specified ID.

**required sub-user rights**: `task_update`.

#### Parameters

| name     | description               | type |
| -------- | ------------------------- | ---- |
| task\_id | ID of the task to delete. | int  |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/task/delete' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/task/delete?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database (if there is no task with such an ID).

### list

Gets all task belonging to user with optional filtering.

#### Parameters

| name         | description                                                                                                                                                             | type                                                                  |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| external\_id | Optional. External task ID for search.                                                                                                                                  | string                                                                |
| statuses     | Optional. Default all. List of task statuses, e.g. `["unassigned","failed"]`.                                                                                           | string array                                                          |
| trackers     | Optional. IDs of the trackers to which task assigned.                                                                                                                   | int array                                                             |
| from         | Optional. Show tasks which are actual AFTER this date, e.g. "2020-07-01 00:00:00".                                                                                      | [date/time](../../../#data-types)                                     |
| to           | Optional. Show tasks which are actual BEFORE this date, e.g. "2020-07-01 00:00:00".                                                                                     | [date/time](../../../#data-types)                                     |
| conditions   | Optional. Search conditions to apply to list. Array of search conditions.                                                                                               | array of [SearchCondition](../../commons/entity/search_conditions.md) |
| filter       | Optional. Filter for all built-in and custom fields. If used with conditions, both filter and conditions must match for every returned task.                            | string                                                                |
| filters      | Optional. Filters for task label, description or address.                                                                                                               | string array                                                          |
| tag\_ids     | Optional. Tag IDs assigned to the task.                                                                                                                                 | int array                                                             |
| location     | Optional. Location with radius, inside which task zone centers must reside. Example: `{ "lat": 34.178868, "lng": -118.599672, "radius": 350 }`                          | Location JSON                                                         |
| sort         | Optional. Set of sort options. Each option is a pair of property name and sorting direction, e.g. `["status=asc", "stay_duration=desc"]`. Possible fields listed below. | string array                                                          |
| offset       | Optional. Offset from start of the found tasks for pagination.                                                                                                          | int                                                                   |
| limit        | Optional. Limit of the found tasks for pagination.                                                                                                                      | int                                                                   |

**condition fields**

| Name                 | Type                              | Comment       |
| -------------------- | --------------------------------- | ------------- |
| id                   | int                               |               |
| employee             | int                               | ID            |
| status               | string                            |               |
| label                | string                            |               |
| location             | string                            | address       |
| from                 | [date/time](../../../#data-types) |               |
| to                   | [date/time](../../../#data-types) |               |
| status\_change\_date | [date/time](../../../#data-types) |               |
| arrival\_date        | [date/time](../../../#data-types) |               |
| stay\_duration       | int                               | seconds       |
| description          | string                            |               |
| external\_id         | string                            |               |
| form                 | int                               | template's ID |

If **external\_id**, **trackers**, **filters**, **from**, **to** or **tag\_ids** is not passed or _null_ then appropriate\
condition not used to filter results.

If **offset** or **limit** is null then restrictions for pagination will not be applied.

**sort: string\[]?**

set of sort options. Each option is a pair of column name and sorting direction, e.g. \["label=asc", "address=desc", "employee=desc"].

**sort fields**

| Name                 | Type                              | Comment                    |
| -------------------- | --------------------------------- | -------------------------- |
| id                   | int                               |                            |
| employee             | string                            | full name or tracker label |
| status               | string                            |                            |
| label                | string                            |                            |
| location             | string                            | address                    |
| from                 | [date/time](../../../#data-types) |                            |
| to                   | [date/time](../../../#data-types) |                            |
| status\_change\_date | [date/time](../../../#data-types) |                            |
| arrival\_date        | [date/time](../../../#data-types) |                            |
| stay\_duration       | int                               | seconds                    |
| description          | string                            |                            |
| external\_id         | string                            |                            |
| form                 | string                            | label                      |

If **external\_id**, **trackers**, **filters**, **from**, **to** or **tag\_ids** is not passed or _null_ then appropriate condition not used to filter results.

{% tabs %}
{% tab title="Shell" %}
```bash
curl -X POST '{{ extra.api_example_url }}/task/list' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
{% endtab %}

{% tab title="HTTP GET" %}
```http
{{extra.api_example_url}}/task/list?hash=a6aa75587e5c59c32d347da438505fc3
```
{% endtab %}
{% endtabs %}

#### Response

```json
{
    "success": true,
    "list": [{
        "id": 111,
        "user_id": 3,
        "tracker_id": 22, 
        "location": {
            "lat": 48.210857,
            "lng": 16.369329,
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
  * `id` - int. Task ID.
  * `user_id` - int. User ID (office). An unchangeable parameter.
  * `tracker_id` - int. Tracker ID. Indicator ID by which the implementation of this task will be controlled.
  * `location` - area (circle geofence), entering and leaving of geofence will be controlled.
  * `label` - string. Task name, length 1-200 characters.
  * `description` - string. Task description, length 0-1024 characters.
  * `creation_date` - [date/time](../../../#data-types). Date of creation of a task, unchangeable field.
  * `from` - [date/time](../../../#data-types). Start date of the interval - when the specified location has to be visited (in the user's time zone).
  * `to` - [date/time](../../../#data-types). End date of the interval - when the specified location has to be visited (in the user's time zone).
  * `external_id` - string. Text field for tracking of communication of the task with certain external systems\
    (for example, number of the order). Is for reference only.
  * `status` - [enum](../../../#data-types). Current status of a task, can have "unassigned" value (unassigned to any executor),\
    "assigned", "done", "failed", "delayed", "arrived" (arrived to geofence but haven't done the task), "faulty" (with problems).
  * `status_change_date` - [date/time](../../../#data-types). Date of the last change of the status of a task.
  * `max_delay` - int. The maximum time delay of the execution of the task, in minutes.
  * `min_stay_duration` - int. The minimum stay time in the area of the task in which the task has to be done, in minutes.
  * `arrival_date` - [date/time](../../../#data-types). Date and time of arrival in the area of the task. Can be null. If the executor has not visited it yet.
  * `stay_duration` - int. Number of seconds spent inside task zone.
  * `origin` - [enum](../../../#data-types). The way of creation of a task. Can be "manual", "scheduled" or "imported" (from excel).
  * `type` - string. Reserved.
* `count` - int. count of the all found tasks.

#### Errors

[General](../../../errors.md#error-codes) types only.

### read

Gets task, checkpoint, or route with checkpoints by specified ID.

#### Parameters

| name     | description                          | type |
| -------- | ------------------------------------ | ---- |
| task\_id | ID of the task, route or checkpoint. | int  |

#### Examples

{% tabs %}
{% tab title="cURL" %}
```sh
curl -X POST '{{ extra.api_example_url }}/task/read' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144}'
```
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/task/read?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

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

* `value` - JSON object. `task` described [here](./#task-object).
* `checkpoints` - only returned if entity with specified ID is a route. Contains all checkpoints of this route. `checkpoint` object described [here](checkpoint.md#checkpoint-object).

#### Errors

* 201 – Not found in the database (if there is no task with such an ID).

### transmute

Converts task into a route checkpoint.

**required sub-user rights**: `task_update`.

#### Parameters

| name      | description                                                         | type |
| --------- | ------------------------------------------------------------------- | ---- |
| task\_id  | ID of the task to convert.                                          | int  |
| route\_id | ID of the route to attach to.                                       | int  |
| order     | Zero-based index at which checkpoint should be inserted into route. | int  |

#### Examples

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/task/transmute' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 23144, "route_id": 12334, "order": 0}'
```
{% endcode %}
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
{{ extra.api_example_url }}/task/transmute?hash=a6aa75587e5c59c32d347da438505fc3&task_id=23144&route_id=12334&order=0
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database (if there is no task or route with such an ID, or tracker to which checkpoint\
  assigned is unavailable to current sub-user).
* 255 – Invalid task state (if task or any of the checkpoints are not in unassigned or assigned state).

### update

Updates existing task. Note that you cannot change task owner using this method.

**required sub-user rights**: `task_update`.

#### Parameters

| name         | description                                                                                                                                                               | type        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| task         | `task` object without fields which are _IGNORED_.                                                                                                                         | JSON object |
| create\_form | If `true` then check additional `form_template_id` field in `task` object and create, replace or delete task's form. Default value is `false` for backward compatibility. | boolean     |

#### Example

cURL

{% code overflow="wrap" %}
```sh
curl -X POST '{{ extra.api_example_url }}/task/update' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task": {"id": 22379, "location": {"lat": 34.178868, "lng": -118.599672, "radius": 150}, "label": "Name", "description": "Description example", "from": "2020-02-03 04:05:06", "to": "2020-03-04 05:06:07"}, "create_form": false}'
```
{% endcode %}

A returned object also can include "external\_id\_counts" field see task/route/create [method description](route/index.md#create).

#### Response

```json
{
    "success": true,
    "external_id_counts": [{
        "external_id": "456", 
        "count": 2
    }]
}
```

#### Errors

* 201 – Not found in the database (if there is no task with such an ID).
* 255 – Invalid task state (if current task state is not "unassigned" or "assigned").

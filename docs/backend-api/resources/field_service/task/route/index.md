---
title: Routes
description: Routes basically named and ordered set of checkpoints. Each is essentially a task with an additional link to the parent route. Route completed if all the checkpoints completed and visited in the specified order. Otherwise, it is considered completed with warnings or failed.
---

# Routes

Routes basically named and ordered set of checkpoints. Each [checkpoint](../checkpoint.md#checkpoint-object) is 
essentially a task with an additional link to the parent route.

Route completed if all the checkpoints completed and visited in the specified order. Otherwise, it is considered
completed with warnings or failed.


## Route object

```json
{
    "id": 111,
    "user_id": 3,
    "tracker_id": 222653,
    "label": "Deliver parcels",
    "description": "Quickly",
    "creation_date": "2014-01-02 03:04:05",
    "from": "2014-02-03 04:05:06",
    "to": "2014-03-04 05:06:07",
    "external_id": null,
    "status": "assigned",
    "status_change_date": "2014-01-02 03:04:05",
    "origin": "imported",
    "tags": [1, 2],
    "checkpoint_ids": [2977,2978],
    "type": "route"
}
```

* `id` - int. Primary key used in route/update, *IGNORED* in route/create.
* `user_id` - int. User ID. *IGNORED* in route/create and route/update.
* `tracker_id` - int. An ID of the tracker to which route assigned. Can be null. *IGNORED* in route/update.
* `creation_date` - [date/time](../../../../getting-started/introduction.md#data-types). When route created. *IGNORED* in route/create, route/update.
* `from` - [date/time](../../../../getting-started/introduction.md#data-types). Date AFTER which first checkpoint zone must be visited, depends on first checkpoint `from`, *IGNORED* in route/create, route/update.
* `to` - [date/time](../../../../getting-started/introduction.md#data-types). Date BEFORE which last checkpoint zone must be visited, depends on last checkpoint `to`, *IGNORED* in route/create, route/update.
* `external_id` - string. Used if route imported from external system. arbitrary text string. Can be null.
* `status` - string. A route status. *IGNORED* in route/create, route/update.
* `status_change_date` - [date/time](../../../../getting-started/introduction.md#data-types). When route status changed. *IGNORED* in route/create, route/update.
* `origin` - string. A route origin. *IGNORED* in route/create, route/update.
* `tags` - int array. List of tag IDs.
* `checkpoint_ids` - int array. List of route checkpoint IDs in order of execution. *IGNORED* in route/create.


## API actions

API base path: `/task/route`.

### `assign`

(Re)assigns route to a new tracker (or make it unassigned).

**required sub-user rights**: `task_update`.

#### Parameters

| name       | description                                                                                                           | type | 
|:-----------|:----------------------------------------------------------------------------------------------------------------------|:-----|
| route_id   | ID of the route to assign.                                                                                            | int  |
| tracker_id | ID of the tracker. Tracker must belong to authorized user and not be blocked. If null, task will be assigned to none. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route_id": 11231, "tracker_id": 223465}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/route/assign?hash=a6aa75587e5c59c32d347da438505fc3&route_id=11231&tracker_id=223465
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no task with such an ID.
* 204 – Entity not found - if there is no tracker with such ID belonging to authorized user.
* 208 – Device blocked - if tracker exists but was blocked due to tariff restrictions or some other reason.
* 255 – Invalid task state - if current task state is not "unassigned" or "assigned".
* 236 – Feature unavailable due to tariff restrictions - if device's tariff does not allow usage of tasks.


### `create`

Creates a new route. One of checkpoints can have ID (in this case it must be a task) - it will be transmuted from
task to checkpoint.

**required sub-user rights**: `task_update`.

#### Parameters

| name        | description                                                                                                                                                                     | type                  | 
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------|
| route       | Route object without fields which are *IGNORED*.                                                                                                                                | JSON object           |
| checkpoints | Array of [checkpoint objects](../checkpoint.md#checkpoint-object) without fields which are *IGNORED*.                                                                           | array of JSON objects |
| create_form | If `true` then check additional `form_template_id` field in every **checkpoint** object and create form if it is not null. Default value is `false` for backward compatibility. | boolean               |

Minimal route object to create a new route must contain:

```json
{
"tracker_id": 223652,
"label": "Name",
"description": "Description example"
}
```

Also, need checkpoints list in order of execution, checkpoints `from` and `to` must be agreed with each other i.e. checkpoint `to` cannot be before 'from' of preceding items.

```json
{
    "tracker_id": 223652,
    "location": {
        "lat": 34.178868,
        "lng": -118.599672,
        "radius": 150
    },
    "label": "Name",
    "description": "Description example",
    "from": "2014-02-03 04:05:06",
    "to": "2014-03-04 05:06:07"
}
```

* `tracker_id` - int. Optional. If the field specified then the task will be assigned to the employee associated with the tracker, otherwise it won't be assigned to anybody.
* `location` - area (circle geofence), entering and leaving of geofence will be controlled.
    * `lat` - float. Latitude.
    * `lng` - float. Longitude.
    * `radius` - int. Radius in meters.
* `label` - string. Task name, length 1-200 characters.
* `description` - string. Task description, length 0-1024 characters.
* `from` - [date/time](../../../../getting-started/introduction.md#data-types). Start date of the interval - when the specified location has to be visited (in the user's time zone).
* `to` - [date/time](../../../../getting-started/introduction.md#data-types). End date of the interval - when the specified location has to be visited (in the user's time zone).

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route": {"tracker_id": 669673, "label": "Products delivery", "description": "12 trackers of model 1 and 37 trackers of model 2", "from": "2020-03-18 10:00:00", "to": "2020-03-18 16:00:00"}, "checkpoints": [{"tracker_id": 669673, "location": {"lat": 34.178868, "lng": -118.599672, "radius": 100}, "label": "Company1", "description": "5 trackers of model 1 and 15 trackers of model 2", "from": "2021-03-18 10:00:00", "to": "2021-03-18 12:00:00", "external_id": "10100", "max_delay": 0, "min_stay_duration": 10, "tags": [1, 4], "form_template_id": 132985}, {"tracker_id": 669673, "location": {"lat": 31.738386, "lng": -106.453854, "radius": 100}, "label": "Company2", "description": "4 trackers of model 1 and 12 trackers of model 2", "from": "2021-03-18 10:00:00", "to": "2021-03-18 14:00:00", "external_id": "10101", "max_delay": 0, "min_stay_duration": 10, "tags": [2, 4], "form_template_id": 132985}], "create_form": false}'
    ```

#### Response

Call returns JSON object of the created route.
In response there will be external IDs which have count greater than zero. 
There can be multiple external IDs in response because you can specify different external IDs in a task's checkpoint.
If there is nothing to return, then parameter "external_id_counts" will not be present in response.

```json
{
    "success": true,
    "result": {
        "id": 111,
        "user_id": 3,
        "tracker_id": 22,
        "label": "Deliver parcels",
        "description": "Quickly",
        "creation_date": "2014-01-02 03:04:05",
        "from": "2014-02-03 04:05:06",
        "to": "2014-03-04 05:06:07",
        "external_id": null,
        "status": "assigned",
        "status_change_date": "2014-01-02 03:04:05",
        "origin": "manual",
        "checkpoint_ids": [2977,2978],
        "type": "route"
    },
    "external_id_counts": [{"external_id": "456", "count": 2}]
}
```

* `checkpoint_ids` - int array. A list of route checkpoint IDs in order of execution.
* `external_id_counts` - optional object. Count of external IDs.
 
#### Errors

* 201 – Not found in the database - if task.tracker_id is not null and belongs to nonexistent tracker.
* 236 – Feature unavailable due to tariff restrictions - if device's tariff does not allow usage of tasks.


### `delete`

Deletes route (and its checkpoints) with the specified ID.

**required sub-user rights**: `task_update`.

#### Parameters

| name     | description                | type | 
|:---------|:---------------------------|:-----|
| route_id | ID of the route to delete. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route_id": 23144}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/route/delete?hash=a6aa75587e5c59c32d347da438505fc3&route_id=23144
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no route with such an ID.


### `list`

Get all routes belonging to user with optional filtering.

#### Parameters

| name     | description                                                                                                                                                                     | type                                                    | 
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------|
| statuses | Optional. List of task statuses, e.g. `["unassigned","failed"]`. Default all.                                                                                                   | [enum](../../../../getting-started/introduction.md#data-types) array |
| trackers | Optional. List of `tracker_id` to which task assigned.                                                                                                                          | int array                                               |
| from     | Optional. Show tasks which are actual AFTER this date, e.g. "2020-06-01 00:00:00".                                                                                              | [date/time](../../../../getting-started/introduction.md#data-types)  |
| to       | Optional. Show tasks which are actual BEFORE this date, e.g. "2020-07-01 00:00:00".                                                                                             | [date/time](../../../../getting-started/introduction.md#data-types)  |
| filter   | Optional. Filter for task label and description. If **trackers**, **filter**, **from** or **to** is not passed or _null_ then appropriate condition not used to filter results. | string                                                  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/route/list?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "list": [{
         "id": 111,
         "user_id": 3,
         "tracker_id": 222653,
         "label": "Deliver parcels",
         "description": "Quickly",
         "creation_date": "2014-01-02 03:04:05",
         "from": "2014-02-03 04:05:06",
         "to": "2014-03-04 05:06:07",
         "external_id": null,
         "status": "assigned",
         "status_change_date": "2014-01-02 03:04:05",
         "origin": "imported",
         "tags": [1, 2],
         "checkpoint_ids": [2977,2978],
         "type": "route"
    }]
}
```

#### Errors

[General](../../../../getting-started/errors.md#error-codes) types only.


### `read`

Gets route by specified ID.

#### Parameters

| name     | description      | type | 
|:---------|:-----------------|:-----|
| route_id | ID of the route. | int  |

#### Response

```json
{
    "success": true,
    "value":  {
          "id": 111,
          "user_id": 3,
          "tracker_id": 222653,
          "label": "Deliver parcels",
          "description": "Quickly",
          "creation_date": "2014-01-02 03:04:05",
          "from": "2014-02-03 04:05:06",
          "to": "2014-03-04 05:06:07",
          "external_id": null,
          "status": "assigned",
          "status_change_date": "2014-01-02 03:04:05",
          "origin": "imported",
          "tags": [1, 2],
          "checkpoint_ids": [2977,2978],
          "type": "route"
    }
}
```

* `value` - route object described [here](#route-object).

#### Errors

* 201 – Not found in the database - if there is no route with such an ID.


### `update`

Updates existing route. Note that you cannot change task owner using this method.<br>
Reordering checkpoint IDs in the `checkpoint_ids` array changes order of execution.

**required sub-user rights**: `task_update`.

#### Parameters

| name        | description                                                                                                                                                                                                                                                                                                                               | type             | 
|:------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
| route       | Route object without fields which are *IGNORED*.                                                                                                                                                                                                                                                                                          | JSON object      |
| checkpoints | List of [checkpoint objects](../checkpoint.md#checkpoint-object) objects. Should be null if **route**'s field **checkpoint_ids** is null, otherwise should be not null. If entry contains ID, then update existing checkpoint, else create a new one. Present route's checkpoints, which are not included in this array, will be deleted. | array of objects |
| create_form | If `true` then check additional `form_template_id` field in every **checkpoint** object and create, replace or delete checkpoint's form. Default value is `false` for backward compatibility.                                                                                                                                             | boolean          |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/route/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "route": {"id": 23785, "label": "Products delivery", "description": "12 trackers of model 1 and 37 trackers of model 2", "from": "2020-03-18 10:00:00", "to": "2020-03-18 16:00:00"}, "checkpoints": [{"id": 123, "tracker_id": 669673, "location": {"lat": 34.178868, "lng": -118.599672, "radius": 100}, "label": "Company1", "description": "5 trackers of model 1 and 15 trackers of model 2", "from": "2021-03-18 10:00:00", "to": "2021-03-18 12:00:00", "external_id": "10100", "max_delay": 0, "min_stay_duration": 10, "tags": [1, 4], "form_template_id": 132985}, {"id": 124, "tracker_id": 669673, "location": {"lat": 31.738386, "lng": -106.453854, "radius": 100}, "label": "Company2", "description": "4 trackers of model 1 and 12 trackers of model 2", "from": "2021-03-18 10:00:00", "to": "2021-03-18 14:00:00", "external_id": "10101", "max_delay": 0, "min_stay_duration": 10, "tags": [2, 4], "form_template_id": 132985}], "create_form": false}'
    ```

#### Response

JSON object of the updated route with `checkpoint_id`s

```json
{
        "success": true,
        "result": {
            "id": 111,
            "user_id": 3,
            "tracker_id": 22,
            "label": "Deliver parcels",
            "description": "Quickly",
            "creation_date": "2014-01-02 03:04:05",
            "from": "2014-02-03 04:05:06",
            "to": "2014-03-04 05:06:07",
            "external_id": null,
            "status": "assigned",
            "status_change_date": "2014-01-02 03:04:05",
            "origin": "manual",
            "checkpoint_ids": [2977,2978],
            "type": "route"
        }
}
```

#### Errors

* 201 – Not found in the database - if there is no task with such an ID.
* 255 – Invalid task state - if current task state is not "unassigned" or "assigned".

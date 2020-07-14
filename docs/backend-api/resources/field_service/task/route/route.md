---
title: /route
description: /route
---

# route/

```js
<route> = {
    "id": 111,   //primary key. used in route/update(...), *IGNORED* in route/create(...)
    "user_id": 3,   //user id. *IGNORED* in route/create(...) and route/update(...)
    "tracker_id": 22, //id of the tracker to which route is assigned. can be null.  *IGNORED* in route/update(...)
    "label": "Deliver parcels",
    "description": "Quickly",
    "creation_date": "2014-01-02 03:04:05", //when route was created. *IGNORED* in route/create(...), route/update(...)
    "from": "2014-02-03 04:05:06", //date AFTER which first checkpoint zone must be visited, depends on first checkpoint `from`, *IGNORED* in route/create(...), route/update(...)
    "to": "2014-03-04 05:06:07", //date BEFORE which last checkpoint zone must be visited, depends on last checkpoint `to`, *IGNORED* in route/create(...), route/update(...)
    "external_id": null,  //used if route was imported from external system. arbitrary text string. can be null
    "status": "assigned", //route status. *IGNORED* in route/create(...), route/update(...)
    "status_change_date": "2014-01-02 03:04:05", //when route status was changed. *IGNORED* in route/create(...), route/update(...)
    "origin": "imported",  //route origin. *IGNORED* in route/create(...), route/update(...)
    "tags": [1, 2] //array of tag ids,
    "checkpoint_ids": [2977,2978], // array of route checkpoint ids in order of execution. *IGNORED* in route/create(...)
    "type": "route"
}
```



---
## assign(…)

(Re)assign route to new tracker (or make it unassigned).

**required subuser rights**: task_update

#### parameters:

* **route_id** - (int) ID of the route to assign
* **tracker_id** - (int) ID of the tracker. Tracker must belong to authorized user and not be blocked. If null, task will be assigned to none.

#### return:

```js
{
    "success": true
}
```

#### errors:

*   201 – Not found in database (if there is no task with such id)
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   255 – Invalid task state (if current task state is not “unassigned” or “assigned”)
*   236 – Feature unavailable due to tariff restrictions (if device’s tariff does not allow usage of tasks)



---
## create(…)

Create new route. One of checkpoints can have id (in this case it must be a task) - it will be transmuted from
task to checkpoint.

**required subuser rights**: task_update

#### parameters:

* **route** - (JSON object) <route> object without fields which are *IGNORED*
* **checkpoints** - (JSON array) <checkpoints> array of checkpoints object without fields which are *IGNORED*
* **create_form** - **boolean**. If true then check additional form_template_id field in every **checkpoint** object 
and create form if it is not null. Default value is false for backward compatibility.

Minimal route object to create a new route must contain:

```js
{
"tracker_id": 22, //optional, if the field is specified then the task will be assigned to the employee associated with the tracker, otherwise it won't be assigned to anybody
"label": "Name", //task name, length 1-200 characters
"description": "Description example" //task description, length 0-1024 characters
}
```

Also need checkpoints list in order of execution, checkpoints `from` and `to` must be agreed with each other i.e. checkpoint `to` cannot be before ‘from’ of preceding items.

```js
{
    "tracker_id": 22, //optional, if the field is specified then the task will be assigned to the employee associated with the tracker, otherwise it won't be assigned to anybody
    "location": { //area (circle geofence), entering and leaving of geofence will be controlled
    "lat": 56.83717295, //latitude
    "lng": 60.59761920, //longitude
    "radius": 150 //radius in meters
    },
    "label": "Name", //task name, length 1-200 characters
    "description": "Description example", //task description, length 0-1024 characters
    "from": "2014-02-03 04:05:06", //start date of the interval - when the specified location has to be visited (in the user's time zone)
    "to": "2014-03-04 05:06:07"//end date of the interval - when the specified location has to be visited (in the user's time zone)
}
```

Call returns JSON object of the created route.
In response there will be external ids which have count greater than zero. 
There can be multiple external ids in response because you can specify different external ids in task's checkpoint.
If there nothing to return, then parameter "external_id_counts" will not be present in response.

```js
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
        "checkpoint_ids": [2977,2978], //array of route checkpoint ids in order of execution
        "type": "route"
    },
    "external_id_counts": [{external_id: "456", count: 2}] // optional
}
```

#### errors:

*   201 – Not found in database (if task.tracker_id is not null and belongs to nonexistent tracker)
*   236 – Feature unavailable due to tariff restrictions (if device’s tariff does not allow usage of tasks)



---
## delete(…)

Delete route (and its checkpoints) with the specified id.

**required subuser rights**: task_update

#### parameters:

* **route_id** - (int) ID of the route to delete.

#### return:

```js
{
    "success": true
}
```

#### errors:

*   201 – Not found in database (if there is no route with such id)



---
## list(…)

Get all routes belonging to user with optional filtering.

#### parameters:

*   **statuses** – **string[]**. (optional. default all) list of task statuses, e.g. [“unassigned”,”failed”]
*   **trackers** – **array of int**. (optional) ids of the trackers to which task is assigned
*   **from** – **string**. (optional) show tasks which are actual AFTER this date, e.g. “2014-07-01 00:00:00”
*   **to** – **string**. (optional) show tasks which are actual BEFORE this date, e.g. “2014-07-01 00:00:00”
*   **filter** – **string**. (optional) filter for task label and description<br>
    If **trackers**, **filter**, **from** or **to** is not passed or _null_ then appropriate condition not used to filter results.

#### return:

```js
{
    "success": true,
    "list": [ <route>, ... ]
}
```

#### errors:

general types only



---
## read(…)

Get route by id.

#### parameters:

* **route_id** - (int) ID of the route.

#### return:

```js
{
    "success": true,
    "value":  ${route} // JSON object
}
```

where **route** described [here](#route).

#### errors:

*   201 – Not found in database (if there is no route with such id)



---
## update(…)

Update existing route. Note that you cannot change task owner using this method.<br>
Reordering checkpoint IDs in the `checkpoint_ids` array changes order of execution.

**required subuser rights**: task_update

#### parameters:

* **route** - (JSON object) <route> object without fields which are *IGNORED*
* **checkpoints** - **checkpoint\_entry\[\]**. Array of [**checkpoint\_entry**](../checkpoint/checkpoint.md#checkpoint) objects. Should be null if **route**'s 
  field **checkpoint_ids** is null, otherwise should be not null. If entry contains id, then update
  existing checkpoint, else create a new one. Present route's checkpoints, which are not included in this array, will be deleted.
* **create_form** - **boolean**. If true then check additional form_template_id field in every **checkpoint** object 
  and create, replace or delete checkpoint's form. Default value is false for backward compatibility.

#### return:
JSON object of the updated route with checkpoint_ids
```js
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

#### errors:

*   201 – Not found in database (if there is no task with such id)
*   255 – Invalid task state (if current task state is not “unassigned” or “assigned”)

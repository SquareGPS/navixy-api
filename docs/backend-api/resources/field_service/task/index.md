---
title: Working with tasks
description: Working with tasks
---

# Working with tasks

You can assign task to any tracked device. If specified tracker visits task checkpoint at the specified time and meets other
conditions such as filling form or staying in the task zone for the specified time, the task is completed. Otherwise
the task is either failed completely or completed with warnings.

If task is assigned to a Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)),
it's available for viewing by app user. User will also receive notifications of newly assigned tasks, task changes, etc.

### Data structure

```json
<task> =
   {
        "id": 111,   //primary key. used in update, *IGNORED* in create
        "user_id": 3,   //user id. *IGNORED* in create/update
        "tracker_id": 22, //id of the tracker to which task is assigned. can be null.  *IGNORED* in update
        "location": {   //location associated with this task. cannot be null
            "lat": 56.5,
            "lng": 60.5,
            "address": "Fichtenstrasse 11", //address of the location
            "radius": 150  //radius of location zone in meters
        },
        "label": "Deliver parcels",
        "description": "Quickly",
        "creation_date": "2014-01-02 03:04:05", //when task was created. *IGNORED* in create/update
        "from": "2014-02-03 04:05:06", //date AFTER which task zone must be visited
        "to": "2014-03-04 05:06:07", //date BEFORE which task zone must be visited
        "external_id": null,  //used if task was imported from external system. arbitrary text string. can be null
        "status": "assigned", //task status. *IGNORED* in create/update. Can have "unassigned" value (unassigned to any executor), "assigned", "done", "failed", "delayed", "arrived" (arrived to geofence but haven't done the task), "faulty" (with problems)
        "status_change_date": "2014-01-02 03:04:05", //when task status was changed. *IGNORED* in create/update
        "max_delay" : 5, //maximum allowed task completion delay in minutes,
        "min_stay_duration": 0, //minumum duration of stay in task zone for task completion, minutes
        "arrival_date": "2014-01-02 03:04:05", //when tracker has arrived to the task zone. *IGNORED* in create/update
        "stay_duration": 0, //duration of stay in the task zone, seconds
        "origin": "imported",  //task origin. *IGNORED* in create/update
        "tags": [1, 2] //array of tag ids,
        "type": "task",
        "form": <form_object> // if present
    }
```


## API actions

API base path: `/task`.

### assign

(Re)assign task to new tracker (or make it unassigned).

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) Id of the task to assign.
* **tracker_id** - (int) Id of the tracker. Tracker must belong to authorized user and not be blocked. If null, task will be assigned to noone.

#### response

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no task with such id)
*   204 – Entity not found (if there is no tracker with such id belonging to authorized user)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   255 – Invalid task state (if current task state is not "unassigned" or "assigned")
*   236 – Feature unavailable due to tariff restrictions (if device's tariff does not allow usage of tasks)



### batch_convert

Convert batch of tab-delimited tasks and return list of checked tasks with errors.

**required subuser rights**: task_update

```json
<checked_task> =
    {
        ... //all fields from task
        "errors": <array of objects>//optional
    }
```

#### parameters

* **batch** - (String) batch of tab-delimited tasks.
* **fields** - (Array of String) Optional, array of field names, default is ["label", "from", "to", "address", "lat", "lng", "description"]
* **geocoder** - (String) geocoder type
* **default_radius** - (Integer) Optional, radius for point, default is 100
* **default_max_delay** - (Integer) Optional, max delay for tasks, default is 0
* **default_duration** - (Integer) Optional, duration for task in minutes, default is 60
* **default_min_stay_duration** - (Integer) Optional, minimal stay duration for task in minutes, default is 0
* **location_check_mode** - (String) Optional, one of "no_check", "entity_location", "parent_location"
* **employee_ids** - (Array of Integer) Optional, list of employee Ids to automatic assign
* **vehicle_ids** - (Array of Integer) Optional, list of vehicle Ids to automatic assign

In case of location_check_mode==entity_location – vehicle_ids will be ignored.

#### response

```json
{
    "success": true,
    "list": [ <checked_task>, ... ],
    "limit_exceeded": false // true if given batch constrained by limit
}
```

#### errors

[General](../../../getting-started.md#error-codes) types only.



### count

Return total number of tasks belonging to current user.

#### response

```json
{
    "success": true,
    "count": 111 //number of tasks
}
```



### create

Create new task.

**required subuser rights**: task_update

#### parameters

* **task** - (JSON object) <task> object without fields which are IGNORED
* **create_form** - **boolean**. If true then check additional form_template_id field in **task** object and create form
if it is not null. Default value is false for backward compatibility.

Minimal JSON object to create a new task must contain:

```json
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

task/create call returns the identifier of the created task.
Returned object also can include "external_id_counts" field see task/route/create [method description](./route/index.md#create)

```json
{
    "success": true,
    "id": 222,
    "external_id_counts": [{external_id: "456", count: 2}] // optional
}
```

#### response

```json
{
    "success": true,
    "id": 111, //id of the created task
    "external_id_counts": [{external_id: "456", count: 2}] // optional
}
```

**Note:** The "id" parameter is unique, it is automatically generated by the server when you create a task. Therefore, if you call task/create  two times with the same parameters, every time the new task will be created. These two tasks will differ only by id. Respectively, if the created task has to be connected to a certain record in external system, you have to remember the id of this record to use it in future when you want to change/delete the associated task in our system.

#### errors

*   201 – Not found in database (if task.tracker_id is not null and belongs to nonexistent tracker)
*   236 – Feature unavailable due to tariff restrictions (if device's tariff does not allow usage of tasks)



### delete

Delete task with the specified id.

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) Id of the task to delete

#### response

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no task with such id)



### list

Get all task belonging to user with optional filtering.

#### parameters

*   **external_id** – **string**. (optional) external task ID for search
*   **statuses** – **string[]**. (optional. default all) list of task statuses, e.g. ["unassigned","failed"]
*   **trackers** – **int[]**. (optional) ids of the trackers to which task is assigned
*   **from** – **string**. (optional) show tasks which are actual AFTER this date, e.g. "2014-07-01 00:00:00"
*   **to** – **string**. (optional) show tasks which are actual BEFORE this date, e.g. "2014-07-01 00:00:00"
*   **filters** – **string[]**. (optional) filters for task label, description or address
*   **tag_ids** – **int[]**. (optional) tag IDs assigned to the task

If **external_id**, **trackers**, **filters**, **from**, **to** or **tag_ids** is not passed or _null_ then appropriate condition not used to filter results.

*   **offset** – **int**. (optional) offset from start of the found tasks for pagination
*   **limit** – **int**. (optional) limit of the found tasks for pagination

If **offset** or **limit** is null then restrictions for paginations will not be applied.

*   **sort** – **string[]**. (optional) set of sort options. Each option is a pair of column name and sorting direction, e.g. ["label=acs", "address=desc", "employee=desc"]. Possible columns:<br>
    — _id_<br>
    — _address_ (location.address)<br>
    — _label_<br>
    — _from_<br>
    — _to_<br>
    — _status_<br>
    — _employee_ (employee.last_name, employee.first_name, employee.middle_name, tracker.label)<br>
    — *arrival_date*

#### response

```json
{
    "success": true,
    "list": [ <task>, ... ],
    "count: 1" // count of the all found tasks
}
```

#### Full JSON returned to the task/list

```json
{
   "id": 111, //task id
   "user_id": 3, //user id (office). Unchangeable parameter.
   "tracker_id": 22, //tracker ID. Indicator ID by which the implementation of this task will be controlled.
   "location": { //area (circle geofence), entering and leaving of geofence will be controlled
       "lat": 56.5, //latitude
       "lng": 60.5, //longitude
       "address": "Schulhof 2, Wien, Austria", //area address
       "radius": 150 //radius in meters
    },
    "label": "Name", //task name, length 1-200 characters
    "description": "Description example", //task description, length 0-1024 characters
    "creation_date": "2014-01-02 03:04:05", //date of creation of a task, unchangeable field
    "from": "2014-02-03 04:05:06", //start date of the interval - when the specified location has to be visited (in the user's time zone)
    "to": "2014-03-04 05:06:07"//end date of the interval - when the specified location has to be visited (in the user's time zone)
    "external_id": "01234567", //Text field for tracking of communication of the task with certain external systems (for example, number of the order). Is for reference only.
    "status": "assigned", //Current status of a task, can have "unassigned" value (unassigned to any executor), "assigned", "done", "failed", "delayed", "arrived" (arrived to geofence but haven't done the task), "faulty" (with problems)
    "status_change_date": "2014-01-02 03:04:05", //date of the last change of the status of a task
    "max_delay": 5, //the maximum time delay of the execution of the task, in minutes
    "min_stay_duration": 0, //the minimum stay time in the area of the task in which the task has to be done, in minutes
    "arrival_date": "2014-01-02 03:04:05", //date and time of arrival to the area of ​​the task, can be null, if the executor has not visited it yet
    "stay_duration": 10, //number of seconds spent inside task zone
    "origin": "manual", //the way of creation of a task, can be "manual", "scheduled" or "imported" (from excel)
    "type": "task" //reserved
}
```

#### errors

[General](../../../getting-started.md#error-codes) types only.



### read

Get task, checkpoint, or route with checkpoints by id.

#### parameters

* **task_id** - (int) Id of the task, route or checkpoint

#### response

```json
{
    "success": true,
    "value":  ${task, checkpoint or route}, // JSON object
    "checkpoints": [ //only returned if entity with specified id is a route
        ${checkpoint 1}, //contains all checkpoints of this route
        ...
    ]

}
```

where **task** described [here](#task).

#### errors

*   201 – Not found in database (if there is no task with such id)



### transmute

Convert task into a route checkpoint.

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) Id of the task to convert
* **route_id** - (int) Id of the route to attach to
* **order** - (int) zero-based index at which checkpoint should be inserted into route

#### response

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no task or route with such id, or tracker to which checkpoint is assigned is unavailable to current subuser)
*   255 – Invalid task state (if task or any of the checkpoints are not in unassigned or assigned state)



### update

Update existing task. Note that you cannot change task owner using this method.

**required subuser rights**: task_update

#### parameters

* **task** - (JSON object) <task> object without fields which are *IGNORED*
* **create_form** - **boolean**. If true then check additional form_template_id field in **task** object and create, 
replace or delete task's form. Default value is false for backward compatibility.

#### response

Returned object also can include "external_id_counts" field see task/route/create [method description](./route/index.md#create)

```json
{
    "success": true,
    "external_id_counts": [{external_id: "456", count: 2}] // optional
}
```

#### errors

*   201 – Not found in database (if there is no task with such id)
*   255 – Invalid task state (if current task state is not "unassigned" or "assigned")

---
title: Scheduling tasks
description: Scheduling tasks
---

# Scheduling tasks

Some tasks happen on regular basis, and it's tedious to create them by hand every time. Task schedules is the way to automate
this process. At the beginning of each day (moments after 00:00 AM according to [user's timezone setting](../../../commons/user/settings/index.md)),
schedule is checked and if there are tasks which start at this day, they are created and assigned to employees (if assignee is specified).

Schedule entries are very similar to tasks, main difference is that `from` and `to` containing specific date and time are
replaced with `from_time`, `duration` and `parameters`.

### Data structures

```json5
<task_schedule_entry> = {
    "id": 111,   //primary key. used in update, *IGNORED* in create
    "user_id": 3,   //user id. *IGNORED* in create/update
    "tracker_id": 22, //id of the tracker to which all generated tasks are assigned. nullable.
    "location": {   //location associated with this task. cannot be null
        "lat": 56.5,
        "lng": 60.5,
        "address": "Moltkestrasse 32", //address of the location
        "radius": 150  //radius of location zone in meters
    },
    "label": "Shop",
    "description": "Buy things",
    "from_time": "12:34:00",  //time of day which defines start of the task within the days
    "duration": 60, //total duration in minutes between "from" and "to" for generated tasks
    "max_delay" : 5, //maximum allowed task completion delay in minutes
    "min_stay_duration": 0, //minumum duration of stay in task zone for task completion, minutes
    "min_arrival_duration": 0, // visits less than this values will be ignored, minutes
    "parameters": <schedule_parameters>, // can be "weekdays" or "month_days"
    "tags": [1, 2], //array of tag ids
    "form_template_id": 1 //int, form template id, nullable
}

<route_schedule_entry> = {
    "id": 111,   //primary key. used in update, *IGNORED* in create
    "user_id": 3,   //user id. *IGNORED* in create/update
    "tracker_id": 22, //id of the tracker to which all generated tasks are assigned. nullable.
    "label": "Shop",
    "description": "Buy things",
    "parameters": <schedule_parameters>, // can be "weekdays" or "month_days"
}

<checkpoint_schedule_entry> = {
    "id": 111,   //primary key. used in update, *IGNORED* in create
    "user_id": 3,   //user id. *IGNORED* in create/update
    "tracker_id": 22, //id of the tracker to which all generated tasks are assigned. nullable.
    "label": "Shop",
    "description": "Buy things",
    "parent_id": 1,
    "order": 0,
    "location": {   //location associated with this task. cannot be null
        "lat": 56.5,
        "lng": 60.5,
        "address": "Moltkestrasse 32", //address of the location
        "radius": 150  //radius of location zone in meters
    },
    "max_delay" : 5, //maximum allowed task completion delay in minutes
    "min_stay_duration": 0, //minumum duration of stay in task zone for task completion, minutes
    "min_arrival_duration": 0б // visits less than this values will be ignored, minutes
    "from_time": "12:34:00",  //time of day which defines start of the task within the days
    "duration": 60, //total duration in minutes between "from" and "to" for generated tasks
    "tags": [1, 2], //array of tag ids,
    "form_template_id": 1 //int, form template id, nullable
}
```

`<schedule_parameters>` can be one of the following:
```json5
<weekdays> = { //task creation based on week day
    "type": "weekdays",
    "weekdays": [1, 5, 6] //week days on which tasks will be created (1 = Monday, ... 7 = Sunday)
}

<month_days> = { //task creation based on day of month
    "type": "month_days",
    "month_days": [1, 10, 31] //days of month on which tasks will be created (1..31)
}
```                            

## API actions

API base path: `task/schedule`.

### create

Create new task schedule entry.

**required subuser rights**: task_update

#### parameters

* **schedule** - (JSON object) <schedule_entry> object without fields which are *IGNORED*

#### response

```json5
{
    "success": true,
    "id": 111 //id of the created schedule entry
}
```

#### errors

*   201 – Not found in database (if schedule.tracker_id belongs to nonexistent tracker)
*   204 – Entity not found (if schedule.form_template_id belongs to nonexistent form template)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   236 – Feature unavailable due to tariff restrictions (if device’s tariff does not allow usage of tasks)



### delete

Delete task schedule with the specified id.

**required subuser rights**: task_update

#### parameters

* **schedule_id** - (int) Id of the task schedule to delete

#### response

```json5
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no task schedule with such id)



### list

Get all task or route schedules belonging to user with optional filtering.<br>
Also this call returns all unassigned task schedules.

#### parameters

* **trackers** - (array of Integer) Optional. Ids of the trackers to which task schedule is assigned
* **filter** - (String) Optional. Filter for task schedule label and description

#### response

```json5
{
    "success": true,
    "list": [ <task_schedule_entry> or <route_schedule_entry> with its checkpoints, ... ]
}
```

#### errors

general types only

### read

Get task, route or checkpoint schedule by id

#### parameters

* **id** - **int**. . Id of task, route or checkpoint schedule

#### response

```json5
{
    "success": true,
    "value": <task_schedule_entry> or <route_schedule_entry> or <checkpoint_schedule_entry>,
    "checkpoints": [<checkpoint_schedule_entry>, ...] // if value is <route_schedule_entry>
}
```

#### errors

general types only

### update

Update existing task schedule.

**required subuser rights**: task_update

#### parameters

* **schedule** - (JSON object) <schedule> object without fields which are *IGNORED*

#### response

```json5
{
    "success": true
}
```

#### errors

*   201 – Not found in database (if schedule.tracker_id belongs to nonexistent tracker)
*   204 – Entity not found (if there is no task schedule with specified id)
*   208 – Device blocked (if tracker exists but was blocked due to tariff restrictions or some other reason)
*   236 – Feature unavailable due to tariff restrictions (if device’s tariff does not allow usage of tasks)

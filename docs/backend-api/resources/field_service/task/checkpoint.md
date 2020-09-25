---
title: Checkpoints
description: Checkpoints
---

# Checkpoints

Every route consists of checkpoints. Using these actions, you can manipulate checkpoints individually.

## API actions

API base path: `/task/checkpoint`.

### Checkpoint object structure

```json
<checkpoint> =
    {
        "id": 111,   //primary key. used in checkpoint/update, *IGNORED* in checkpoint/create
        "user_id": 3,   //user id. *IGNORED* in checkpoint/create, checkpoint/update
        "tracker_id": 22, //id of the tracker to which task is assigned. can be null.  *IGNORED* in checkpoint/update
        "location": {   //location associated with this checkpoint. cannot be null
            "lat": 56.5,
            "lng": 60.5,
            "address": "Fichtenstrasse 11", //address of the location
            "radius": 150  //radius of location zone in meters
        },
        "label": "Deliver parcels",
        "description": "Quickly",
        "creation_date": "2014-01-02 03:04:05", //when checkpoint was created. *IGNORED* in checkpoint/create, checkpoint/update
        "from": "2014-02-03 04:05:06", //date AFTER which checkpoint zone must be visited
        "to": "2014-03-04 05:06:07", //date BEFORE which checkpoint zone must be visited
        "external_id": null,  //used if task was imported from external system. arbitrary text string. can be null
        "status": "assigned", //checkpoint status. *IGNORED* in checkpoint/create, checkpoint/update
        "status_change_date": "2014-01-02 03:04:05", //when checkpoint status was changed. *IGNORED* in checkpoint/create and checkpoint/update
        "max_delay" : 5, //maximum allowed checkpoint completion delay in minutes,
        "min_stay_duration": 0, //minumum duration of stay in checkpoint zone for checkpoint completion, minutes
        "arrival_date": "2014-01-02 03:04:05", //when tracker has arrived to the checkpoint zone. *IGNORED* in checkpoint/create, checkpoint/update
        "stay_duration": 0, //duration of stay in the checkpoint zone, seconds
        "origin": "imported",  //checkpoint origin. *IGNORED* in checkpoint/create, checkpoint/update
        "tags": [1, 2] //array of tag ids,
        "type": "checkpoint",
        "form": <form_object> // if present
    }
```



### create

Create new checkpoint.

**required subuser rights**: task_update

#### parameters

* **checkpoint** - (JSON object) <checkpoint> object without fields which are *IGNORED*

Inserts the specified checkpoint at the specified position (`order`) in the parent route checkpoints list. Shifts the checkpoint currently at that position (if any) and any subsequent checkpoints to the right (adds one to their orders).

Call returns the identifier of the created task in the form of JSON.
Returned object also can include "external_id_counts" field see `task/route/create` [method description](./route/index.md#create).

```json
{
    "success": true,
    "id": 222,
    "external_id_counts": [{external_id: "456", count: 2}] // optional
}
```

#### errors

*   201 – Not found in database (if task.tracker_id is not null and belongs to nonexistent tracker)
*   236 – Feature unavailable due to tariff restrictions (if device’s tariff does not allow usage of tasks)



### delete

Delete checkpoint with the specified id.

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) ID of the checkpoint to delete

#### response

```json
{ "success": true }
```

#### errors

*   201 – Not found in database (if there is no checkpoint with such id)



### list

Get checkpoints belonging to user with given ids

#### parameters

* **checkpoint_ids** – (array of int) IDs of checkpoints, e.g. [1,2]

#### response

```json
{
    "success": true,
    "list": [ <checkpoint>, ... ]
}
```

#### errors

general types only



### read

Get route checkpoint by id.

#### parameters

* **checkpoint_id** - (int) ID of the checkpoint

#### response

```json
{
    "success": true,
    "value":  ${checkpoint} // JSON object
}
```

where **checkpoint** described [here](#checkpoint).

#### errors

*   201 – Not found in database (if there is no checkpoint with such id)



### transmute

Convert route checkpoint into a standalone task. If it’s the only checkpoint in the route, the route is deleted.

**required subuser rights**: task_update

#### parameters

* **checkpoint_id** - (int) ID of the checkpoint

#### response

```json
{
    "success": true
}
```

#### errors

*   201 – Not found in database (if there is no checkpoint with such id, or tracker to which checkpoint is assigned is unavailable to current subuser)
*   255 – Invalid task state (if any of checkpoints are not in unassigned or assigned state)



### update

Update existing checkpoint.

**required subuser rights**: task_update

#### parameters

* **checkpoint** - (JSON object) <checkpoint> object without fields which are *IGNORED*

Changing `order` reorders all other checkpoints.

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
*   255 – Invalid task state (if current task state is not “unassigned” or “assigned”)

---
title: Scheduling routes
description: Scheduling routes
---

# Scheduling routes

These actions allow to create scheduled routes similarly to regular routes.

## API actions

API base path: `/task/schedule/route`.

### create

Create route schedule with checkpoints

#### parameters

* **route** - **route_schedule_entry**. Route schedule entry
* **checkpoints** - **checkpoint_schedule_entry\[\]**. Array of route's checkpoints.

#### response
```js
{
    "success": true,
    "id": 111 //id of the created route schedule entry
}
```


### delete

Delete route schedule with checkpoints

#### parameters

* **id** - **int**. Route schedule ID.

#### response
```js
{
    "success": true
}
```



### update

Update route schedule with checkpoints. If checkpoint is being created, then it should have no id.
If checkpoint is being updated, then it should have an id. If old checkpoint is not present in request, then
is will be deleted.

#### parameters

* **route** - **route_schedule_entry**. Route schedule entry
* **checkpoints** - **checkpoint_schedule_entry\[\]**. Array of route's checkpoints.

#### response
```json
{ "success": true }
```

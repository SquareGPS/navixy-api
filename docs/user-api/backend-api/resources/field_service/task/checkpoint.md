---
title: Checkpoints
description: Every route consists of checkpoints. Using these actions, you can manipulate checkpoints individually.
---

# Checkpoints

Every route consists of checkpoints. Using these actions, you can manipulate checkpoints individually.


## Checkpoint object

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
    "type": "checkpoint",
    "form": <form_object>,
    "form_template_id": 13245
}
```

* `id` - int. Primary key. Used in checkpoint/update. *IGNORED* in checkpoint/create.
* `user_id` - int. User ID. *IGNORED* in checkpoint/create, checkpoint/update.
* `tracker_id` - int. An ID of the tracker to which task assigned. Can be null.  *IGNORED* in checkpoint/update.
* `location` - location associated with this checkpoint. cannot be null.
    * `address` - string. Address of the location.
    * `radius` - int. Radius of location zone in meters.
* `creation_date` - [date/time](../../../getting-started/introduction.md#data-types). When checkpoint created. *IGNORED* in checkpoint/create, checkpoint/update.
* `from` - [date/time](../../../getting-started/introduction.md#data-types). Date AFTER which checkpoint zone must be visited.
* `to` - [date/time](../../../getting-started/introduction.md#data-types). Date BEFORE which checkpoint zone must be visited.
* `external_id` - int. Used if task imported from external system. Arbitrary text string. Can be null.
* `status` - [enum](../../../getting-started/introduction.md#data-types). Checkpoint status. *IGNORED* in checkpoint/create, checkpoint/update.
* `status_change_date` - [date/time](../../../getting-started/introduction.md#data-types). When checkpoint status changed. *IGNORED* in checkpoint/create and checkpoint/update.
* `max_delay` - int. Maximum allowed checkpoint completion delay in minutes.
* `min_stay_duration` - int. Minimum duration of stay in checkpoint zone for checkpoint completion, minutes.
* `arrival_date` - [date/time](../../../getting-started/introduction.md#data-types). Wen tracker has arrived to the checkpoint zone. *IGNORED* in checkpoint/create, checkpoint/update.
* `stay_duration` - int. Duration of stay in the checkpoint zone, seconds.
* `origin` - string. Checkpoint origin. *IGNORED* in checkpoint/create, checkpoint/update.
* `tags` - int array. List of tag IDs.
* `form` - [form object](../form/index.md#form-object). If present.
* `form_template_id` - int. An ID of form template. Used in create and update actions only if `create_form` parameter is `true` in them.

!!! note "To associate the task with an address - this field should be added to the location object."


## API actions

API base path: `/task/checkpoint`.

### `create`

Creates a new checkpoint.

**required sub-user rights**: `task_update`.

#### Parameters

| name       | description                                               | type        | 
|:-----------|:----------------------------------------------------------|:------------|
| checkpoint | A `checkpoint` object without fields which are *IGNORED*. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/checkpoint/create' \
      -H 'Content-Type: application/json' \
      -d '{"hash": "43c37b8d023272c5fd1b27d21244b", "checkpoint": {"tracker_id": 10179999, "label": "Shop 1", "description": "Description", "parent_id": 352665, "order": 0, "location": { "lat": 9.861999, "lng": -83.948999, "radius": 150}, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "from": "2022-12-14 11:00:00", "to": "2022-12-14 11:30:00", "duration": 60, "tags": [1, 2], "form_template_id": 1}}'
    ```

#### Response

Inserts the specified checkpoint at the specified position (`order`) in the parent route checkpoints list. Shifts the checkpoint currently at that position (if any) and any subsequent checkpoints to the right (adds one to their orders).

Call returns the identifier of the created task in the form of JSON.
The returned object also can include "external_id_counts" field see `task/route/create` [method description](route/index.md#create).

```json
{
    "success": true,
    "id": 222,
    "external_id_counts": [{
        "external_id": "456", 
        "count": 2
    }]
}
```

#### Errors

* 201 – Not found in the database - if task.tracker_id is not null and belongs to nonexistent tracker.
* 236 – Feature unavailable due to tariff restrictions - if device's tariff does not allow usage of tasks.


### `delete`

Deletes a checkpoint with the specified ID.

**required sub-user rights**: `task_update`.

#### Parameters

| name          | description                     | type | 
|:--------------|:--------------------------------|:-----|
| checkpoint_id | ID of the checkpoint to delete. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/checkpoint/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint_id": 23144}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/checkpoint/delete?hash=a6aa75587e5c59c32d347da438505fc3&checkpoint_id=23144
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 – Not found in the database - if there is no checkpoint with such an ID.


### `list`

Get checkpoints belonging to user with given IDs

#### Parameters

| name           | description                       | type      | 
|:---------------|:----------------------------------|:----------|
| checkpoint_ids | IDs of checkpoints, e.g. `[1,2]`. | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/checkpoint/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint_ids": [1,2]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/checkpoint/list?hash=a6aa75587e5c59c32d347da438505fc3&checkpoint_ids=[1,2]
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
         "type": "checkpoint"
    }]
}
```

#### Errors

[General](../../../getting-started/errors.md#error-codes) types only.


### `read`

Gets route checkpoint by specified ID.

#### Parameters

| name          | description           | type | 
|:--------------|:----------------------|:-----|
| checkpoint_id | ID of the checkpoint. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/checkpoint/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/checkpoint/read?hash=a6aa75587e5c59c32d347da438505fc3&checkpoint_id=111
    ```

#### Response

```json
{
    "success": true,
    "value":  {
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
          "type": "checkpoint",
          "form": <form_object>
    }
}
```

* `value` - `checkpoint` object described [here](#checkpoint-object).

#### Errors

* 201 – Not found in the database - if there is no checkpoint with such an ID.


### `transmute`

Convert route checkpoint into a standalone task. If it's the only checkpoint in the route, the route deleted.

**required sub-user rights**: `task_update`.

#### Parameters

| name          | description           | type | 
|:--------------|:----------------------|:-----|
| checkpoint_id | ID of the checkpoint. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/checkpoint/transmute' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint_id": 111}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/checkpoint/transmute?hash=a6aa75587e5c59c32d347da438505fc3&checkpoint_id=111
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no checkpoint with such an ID, or tracker to which checkpoint assigned is unavailable to current sub-user.
* 255 – Invalid task state - if any of checkpoints are not in unassigned or assigned state.


### `update`

Updates existing checkpoint.

**required sub-user rights**: `task_update`.

#### Parameters

| name       | description                                               | type        | 
|:-----------|:----------------------------------------------------------|:------------|
| checkpoint | A `checkpoint` object without fields which are *IGNORED*. | JSON object |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/checkpoint/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkpoint": {"id": 111, "tracker_id": 10179999, "label": "Shop 1", "description": "Description", "parent_id": 352665, "order": 0, "location": { "lat": 9.861999, "lng": -83.948999, "radius": 150}, "max_delay" : 5, "min_stay_duration": 0, "min_arrival_duration": 0, "from": "2022-12-14 11:00:00", "to": "2022-12-14 11:30:00", "duration": 60, "tags": [1, 2], "form_template_id": 1}}'
    ```

Changing `order` reorders all other checkpoints.

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

* `external_id_counts` - array of objects. Optional. A returned object also can include "external_id_counts" field see task/route/create [method description](route/index.md#create).

#### Errors

* 201 – Not found in the database - if there is no task with such an ID.
* 255 – Invalid task state - if current task state is not "unassigned" or "assigned".

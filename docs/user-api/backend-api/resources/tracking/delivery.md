---
title: Delivery info
description: API calls to get delivery states and tasks by IDs.  
---

# Delivery info

API calls to get delivery states and tasks by IDs.


## API actions

API base path: `/delivery`.

### `read`

Returns info sufficient for tracking certain task state, and the tracker assigned to it.
Search conducted only among tasks and checkpoints, which have start date less than or equal now and have statuses:
arrived, assigned or delayed.
If multiple tasks or checkpoints found, then return first task, otherwise checkpoint. 

#### session types:

In addition to standard user session, this call supports special *DELIVERY* session type.

#### Parameters

| name        | description             | type | format |
|-------------|-------------------------|------|--------|
| external_id | An external ID of task. | int  | 259876 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/delivery/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "external_id": 259876}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/delivery/read?hash=a6aa75587e5c59c32d347da438505fc3&external_id=259876
    ```

#### Response

```json
{
    "success": true,
    "user_id": 3,
    "task" : {<task_object>},
    "tracker" : {<tracker_object>},
    "restrictions": {<restrictions_object>},
    "first_name": "John",
    "middle_name": "Micheel",
    "last_name": "Johnson",
    "vehicle_label": "Service car 002",
    "estimated_time": 1122
}
```

* `user_id` - master ID of the user to which the task belongs to.
* `task` - a task object, for more info see [/task](../field_service/task/index.md#task-object) 
object structure.
* `tracker` - corresponding tracker object, for more info see
 [tracker/](tracker/index.md#tracker-object-structure) object structure.
* `restrictions` - tariff restrictions object, for more info see
 [user/get_tariff_restrictions](../commons/user/index.md#get_tariff_restrictions).
* `first_name` - string. The first name of employee assigned to the task, or null if missing.
* `middle_name` - string. The middle name of employee assigned to the task, or null if missing.
* `last_name` - string. The last name of employee assigned to the task, or null if missing.
* `vehicle_label` - string. A label of the vehicle assigned to the task, or null if missing.
* `estimated_time` - int. Estimated time of arrival in seconds, or null if unavailable.

#### Errors

* 201 – Not found in the database - when there is no task or checkpoint with specified conditions.


### `list`

External_id can be repeated, so this request will return all matching delivery. Returns info sufficient for tracking 
certain task state, and the tracker assigned to it. 
Search conducted only among tasks and checkpoints, which have start date less than or equal now and have statuses:
arrived, assigned or delayed. 

#### session types:

in addition to standard user session, this call supports special *DELIVERY* session type.

#### Parameters

| name        | description             | type | format |
|:------------|:------------------------|:-----|:-------|
| external_id | An external ID of task. | int  | 259876 |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/delivery/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "external_id": 259876}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/delivery/list?hash=a6aa75587e5c59c32d347da438505fc3&external_id=259876
    ```

#### Response

```json
{
    "success": true,
    "list": [{
        "task" : {
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
        },
        "tracker" : {
          "id": 123456,
          "label": "tracker label",
          "clone": false,
          "group_id": 167,
          "avatar_file_name" : "file name",
          "source": {
            "id": 234567,
            "device_id": 9999999988888,
            "model": "telfmb920",
            "blocked": false,
            "tariff_id": 345678,
            "status_listing_id": null,
            "creation_date": "2011-09-21",
            "tariff_end_date": "2016-03-24",
            "phone" : "+71234567890"
          },
          "tag_bindings": [{
            "tag_id": 456789,
            "ordinal": 4
          }]
        },
        "first_name": "John",
        "middle_name": "Micheel",
        "last_name": "Johnson",
        "vehicle_label": "Service car 002",
        "estimated_time": 1122
    }],
    "user_id": 3,
    "restrictions": {"restrictions_object":} 
}
```

* `task` - a task object, for more info see [/task](../field_service/task/index.md#task-object) object 
structure.
* `tracker` - corresponding tracker object, for more info see 
[tracker/](tracker/index.md#tracker-object-structure) object structure.
* `first_name` - string. The first name of employee assigned to the task, or null if missing.
* `middle_name` - string. The middle name of employee assigned to the task, or null if missing.
* `last_name` - string. The last name of employee assigned to the task, or null if missing.
* `vehicle_label` - string. A label of the vehicle assigned to the task, or null if missing.
* `estimated_time` - int. Estimated time of arrival in seconds, or null if unavailable.
* `user_id` - master ID of the user to which the task belongs to.
* `restrictions` - tariff restrictions object, for more info see 
[user/get_tariff_restrictions](../commons/user/index.md#get_tariff_restrictions).

#### Errors

* 201 – Not found in the database - when there is no task or checkpoint with specified conditions.

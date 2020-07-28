---
title: Delivery info
description: Delivery info
---

## read(...)

Returns info sufficient for tracking certain task state and the tracker assigned to it.
Search is conducted only among tasks and checkpoints, which have start date less than or equal now and have statuses:
arrived, assigned or delayed.
If multiple tasks or checkpoints were found, then return first task, otherwise checkpoint. 

#### session types:

in addition to standard user session, this call supports special *DELIVERY* session type

#### parameters:

|name |description |type |format |
|--- |--- |--- |--- |
| external_id | an external id of task | int | 259876 |

#### example:

```abap
$ curl -X POST 'https://api.navixy.com/v2/delivery/read' \
  -H 'Content-Type: application/json' \ 
  -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "external_id": "259876"}' 
```

#### response:

```js
{
    "success": true,
    "user_id": 3, // master id of the user to which the task belongs to
    "task" : ${task}, //a task object, for more info see task/ section
    "tracker" : ${tracker}, //corresponding tracker object, for more info see tracker/ section
    "restrictions": ${restrictions}, //tariff restrictions object, for more info see user/get_tariff_restrictions 
    "first_name": "John", //first name of employee assigned to the task, or null if missing
    "middle_name": "Micheel", //middle name of employee assigned to the task, or null if missing
    "last_name": "Johnson", //last name of employee assigned to the task, or null if missing
    "vehicle_label": "Service car 002", //label of the vehicle assigned to the task, or null if missing
    "estimated_time": 1122 //estimated time of arrival in seconds, or null if unavailable
}
```
 
#### errors:

*   201 – Not found in database (when there is no task or checkpoint with specified conditions)

## list(...)

External_id can be repeated, so this request will return all matching delivery. Returns info sufficient for tracking certain task state and the tracker assigned to it. 
Search is conducted only among tasks and checkpoints, which have start date less than or equal now and have statuses:
arrived, assigned or delayed. 

#### session types:

in addition to standard user session, this call supports special *DELIVERY* session type

#### parameters:

|name|description|type|format|
|--- |--- |--- |--- |
| external_id | an external id of task | int | 259876 |

#### example:

```abap
$ curl -X POST 'https://api.navixy.com/v2/delivery/list' \
  -H 'Content-Type: application/json' \ 
  -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "external_id": "259876"}' 
```

#### response:

```js
{
    "success": true,
    "list": [{
        "task" : ${task}, //a task object, for more info see task/ section
        "tracker" : ${tracker}, //corresponding tracker object, for more info see tracker/ section
        "first_name": "John", //first name of employee assigned to the task, or null if missing
        "middle_name": "Micheel", //middle name of employee assigned to the task, or null if missing
        "last_name": "Johnson", //last name of employee assigned to the task, or null if missing
        "vehicle_label": "Service car 002", //label of the vehicle assigned to the task, or null if missing
        "estimated_time": 1122 //estimated time of arrival in seconds, or null if unavailable
    }],
    "user_id": 3, // master id of the user to which the tasks belongs to
    "restrictions": ${restrictions}, //tariff restrictions object, for more info see user/get_tariff_restrictions 
}
```

#### errors:

*   201 – Not found in database (when there is no task or checkpoint with specified conditions)

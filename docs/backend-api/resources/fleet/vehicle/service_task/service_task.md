---
title: Vehicle service task
description: Vehicle service task
---

# Vehicle service task

API path: `/vehicle/service_task`.

#### Status

Task **status** may be one of:

*   **created** – initial state of task.
*   **notified** – one of conditions exceed notification limit.
*   **expired** – one of conditions exceeded.
*   **done** – user [set](#set_status) task as “done”.

### batch_create

Create multiple service tasks.

#### parameters

*   **vehicle_ids** – vehicle ids. Task will be created for every vehicle. 
*   **task** – service task to create. vehicle_id field in this objects should not be specified. JSON object:

```
{
    "description": "desc123",
    "cost": 100,
    "comment": "cccc",
    "conditions": {
      "mileage": {
            "limit": 100,
            "notification_interval": 3
          }
      },
    "notifications": {
      "sms_phones": ["88000000000"],
      "phones": [],
      "emails": []
      }
    ),
    "repeat": false,
    "unplanned": false,
    "file_ids": [1] // one file will be specified in many service tasks. If one of the tasks will be deleted, then file
                    // will remain in others. File will be deleted only when the last task will be deleted
}
```


### create

Create new vehicle service task. For vehicles with associated tracker only.

#### parameters

*   **task** – service task to create. JSON object:

```js
{
    "vehicle_id": 222, // id of associated vehicle
    "description": "Service task", // max 255 characters
    "comment": "", // max 255 characters
    "cost": 10050.0000, // for information only
    "conditions": { // task end conditions. at least one of fields (mileage or date or engine hours) must be passed.
        "mileage": { // optional
            "limit": 100, // task limit in kilometers
            "notification_interval": 10 // notify about task in specified number of kilometers
        },
        "date": { // optional
            "end": "2015-05-08 09:35:00", // task end date
            "notification_interval": 3 // notify about task in specified number of days
        },
        "engine_hours": { // optional
            "limit": 100, // task limit in hours
            "notification_interval": 10 // notify about task in specified number of hours
        },
    },
    "notifications": {
        "sms_phones": [ //array of phones in international format wo + sign
            "79221234567",
            "79227654321"
        ],
        "emails": [//array of email addresses
            "email@domain.tld",
            "email@mail.com"
        ],
        "push_enabled": true // enable/disable push notifications
    },
    "repeat": false, // if true then new task will be created when current task is done
    "unplanned": false, // boolean flag
    "file_ids": [1, 2] // file ids
}
```

#### response

    { "success": true }


#### errors

*   201 (Not found in database) – vehicle or tracker not found
*   214 (Requested operation or parameters are not supported by the device) – engine hours condition passed but tracker hasn’t ignition sensor


### delete

Delete vehicle service task.

#### parameters

Either **task_id** or **task_ids** should be specified
*   **task_id** – **int**. (optional) id of service task
*   **task_ids** – **int\[\]**. (optional) ids of service tasks

#### response

```json
{ "success": true }
```


### download

Create pdf report of service tasks

#### parameters

*   **order_by** - **string**. Sort option. Possible values:
    <br> — vehicle
    <br> — description
    <br> — status
    <br> — cost
*   **ascending** - **boolean** (optional, default **true**). Sort direction.
*   **group_by** - **string** (optional). Group by option. Possible values:
    <br> — vehicle
    <br> — status

#### response

Report file.


### list

List all service tasks of all user vehicles.

#### parameters

*   **return_prediction** – **boolean**. include legacy **prediction** field or not

#### response

```js
{
    "success": true,
    "list": [ // list of JSON objects:
        {
            "id": 725, // id of service task
            "vehicle_id": 222, // id of associated vehicle
            "vehicle_label": "AGV", // label of associated vehicle
            "status": "created", // task status
            "prediction": { // optional. legacy field, is not used anymore. check return_prediction parameter
                "end_date": "2015-05-03 09:35:00", // predicted end date
                "wear_percentage": 40 // wear percentage
            },
            "description": "Service task", // task description
            "cost": 10050.0, // task cost
            "completion": { // date and counter's values when the task was marked as done. Non-editable.
                "mileage": 31,
                "date": "2014-03-16 00:00:00",
                "engine_hours": 140
            },
            "completion_date" : "2014-03-16 00:00:00", // deprecated. use completion.date instead
            "conditions": { // task end conditions. at least one of fields (mileage or date) must be passed.
                "mileage": { // optional
                    "limit": 100, // task limit in kilometers. task end mileage = start.mileage + this limit
                    "notification_interval": 10 // notify about task in specified number of kilometers
                },
                "date": { // optional
                    "end": "2015-05-08 09:35:00", // task end date
                    "notification_interval": 3    // notify about task in specified number of days
                },
                "engine_hours": { // optional
                    "limit": 100, // task limit in hours. task end engine hours = start.engine_hours + this limit
                    "notification_interval": 10 // notify about task in specified number of hours
                },
            },
            "current_position": { // current position values
                "mileage": 11, // optional
                "date": "2012-03-06 15:55:03", // optional
                "engine_hours": 100 // optional
            },
            "start": {
                "mileage": 1230,              // initial odometer value. for tasks with mileage condition
                "date": "2015-05-01 17:46:44", // task creation date. for tasks with date condition
                "engine_hours": 50 // initial engine hours value. for tasks with engine hours condition
            },
            "repeat": false,
            "unplanned": false,
            "file_ids": [2, 3]
        }
    ]
}
```

About task **status** property see above.

#### errors

*   201 (Not found in database) – vehicle or tracker not found


### read

Get service task info by it’s id.

#### parameters

*   **task_id** – **int**. task id
*   **return_prediction** – **boolean**. include legacy **prediction** field or not

#### response

```js
{
    "success": true,
    "value": {
        "id": 725, // task id
        "vehicle_id": 222, // id of associated vehicle
        "status": "created", // task status
        "prediction": { // optional. legacy field, is not used anymore. check return_prediction parameter
            "end_date": "2015-05-03 09:35:00", // predicted end date
            "wear_percentage": 40 // wear percentage
        },
        "description": "Service task",
        "comment": "",
        "cost": 100500.0,
        "completion": { // date and counter's values when the task was marked as done. Non-editable.
            "mileage": 31,
            "date": "2014-03-16 00:00:00",
            "engine_hours": 140
        },
        "conditions": { // task end conditions. at least one of fields (mileage or date) must be passed.
            "mileage": { // optional
                "limit": 100, // task limit in kilometers. task end mileage = start.mileage + this limit
                "notification_interval": 10 // notify about task in specified number of kilometers
            },
            "date": { // optional
                "end": "2015-05-08 09:35:00", // task end date
                "notification_interval": 3    // notify about task in specified number of days
            },
            "engine_hours": { // optional
                "limit": 100, // task limit in hours. task end engine hours = start.engine_hours + this limit
                "notification_interval": 10 // notify about task in specified number of hours
            },
        },
        "start": {
            "mileage": 1230,              // initial odometer value. for tasks with mileage condition
            "date": "2015-05-01 17:46:44", // task creation date. for tasks with date condition
            "engine_hours": 50 // initial engine hours value. for tasks with engine hours condition
        },
        "notifications": {
            "sms_phones": [ //array of phones in international format wo + sign
                "79221234567",
                "79227654321"
            ],
            "emails": [//array of email addresses
                "email@domain.tld",
                "email@mail.com"
            ],
            "push_enabled": true // enable/disable push notifications
        },
        "completion_date" : "2014-03-16 00:00:00", // deprecated. use completion.date instead
        "repeat": false,
        "unplanned": false,
        "file_ids": [1, 2]
    },
    "files": [ <file_object> ]
}
```

About task **status** property see above.

#### errors

*   201 (Not found in database) – does not exists one of tracker’s counters which required to determine status
*   204 (Entity not found) – when vehicle or service task not found

### set_status

Update task status. And save (on **done** **status**) current date and values of used (in condition) counters for “freeze” wearing percent.

#### parameters

*   **task_id** – **int**, task id.
*   **status** – new task. Only `done` status allowed for now.

#### response

```json
{ "success": true }
```

#### errors

*   201 (Not found in database) – does not exists one of tracker’s counters which required to determine status
*   204 (Entity not found) – when vehicle or service task not found

### update

Update information fields and notification settings of vehicle service task.

#### parameters

*   **task** – JSON object:

```js
{
    "id": 4,  // id of service task to update
    "description": "service", // new description (max 255 characters)
    "comment": "comment", // new comment (max 255 characters)
    "cost": 99.95,  // new cost
    "conditions": { // task end conditions. at least one of fields (mileage or date) must be passed.
        "mileage": { // optional
            "limit": 100, // task limit in kilometers
            "notification_interval": 10 // notify about task in specified number of kilometers
        },
        "date": { // optional
            "end": "2015-05-08 09:35:00", // task end date
            "notification_interval": 3    // notify about task in specified number of days
        },
        "engine_hours": { // optional
            "limit": 100, // task limit in hours
            "notification_interval": 10 // notify about task in specified number of hours
        },
    },
    "notifications": {
        "sms_phones": [ //array of phones in international format wo + sign
            "79221234567",
            "79227654321"
        ],
        "emails": [],
        "push_enabled": true // enable/disable push notifications
    },
    "repeat": false,
    "unplanned": false,
    "file_ids": [3] // empty array means delete all files, null means do nothing with files (backward compatibility)
}
```

See [create](#create).

#### response

```json
{ "success": true }
```


#### errors

*   204 (Entity not found) – when vehicle or service task not found.
*   214 (Requested operation or parameters are not supported by the device) – engine hours condition passed but tracker hasn’t ignition sensor.

---
title: Service work
description: Contains service task object description and API calls to work with it.   
---

# Vehicle service work

Contains service task object description and API calls to interact with vehicle service works that is used for vehicle maintenance.
Vehicle maintenance feature helps to make sure that any scheduled maintenance or urgent repair is carried out in a timely manner.

***

## Service task object

```json
{
    "id": 725,
    "vehicle_id": 222,
    "status": "created",
    "prediction": {
      "end_date": "2015-05-03 09:35:00",
      "wear_percentage": 40
    },
    "description": "Service work",
    "comment": "",
    "cost": 100500.0,
    "completion": {
      "mileage": 31,
      "date": "2014-03-16 00:00:00",
      "engine_hours": 140
    },
    "conditions": {
      "mileage": {
        "limit": 100,
        "notification_interval": 10
      },
      "date": {
        "end": "2015-05-08 09:35:00",
        "notification_interval": 3,
        "repeat_interval": 42
      },
      "engine_hours": {
        "limit": 100,
        "notification_interval": 10
      }
    },
    "start": {
      "mileage": 1230,
      "date": "2015-05-01 17:46:44",
      "engine_hours": 50
    },
    "notifications": {
      "sms_phones": [
        "79221234567",
        "79227654321"
      ],
      "emails": [
        "email@domain.tld",
        "email@mail.com"
      ],
      "push_enabled": true
    },
    "completion_date" : "2014-03-16 00:00:00",
    "repeat": true,
    "unplanned": false,
    "file_ids": [1, 2]
}
```

* `id` - int. An id of created task.
* `vehicle_label` - string. Vehicle label.
* `status` - [enum](../../../../getting-started.md#data-types). [Status](#task-status).
* `prediction` - optional object. Legacy field, is not used anymore. check return_prediction parameter.
    * `end_date` - [date/time](../../../../getting-started.md#data-types). Predicted end date.
    * `wear_percentage` - int. Wear percentage.
* `completion` - object. Date and counter's values when the task marked as done. Non-editable.
* `completion_date` - [date/time](../../../../getting-started.md#data-types). Date when a service work completed.
* `current_position` - object. Current position values.
    * `mileage` - int. Current mileage.
    * `date` - [date/time](../../../../getting-started.md#data-types). Current date.
    * `engine_hours` - int. Current engine hours.
* `start` - object. Consists initial values.
    * `mileage` - int. Initial odometer value for tasks with mileage condition.
    * `date` - [date/time](../../../../getting-started.md#data-types). Task creation date for tasks with date condition.
    * `engine_hours` - int. Initial engine hours value for tasks with engine hours condition.
* `vehicle_id` - int. An id of associated vehicle.
* `description` - string. Name of a service work. Max 255 characters.
* `comment` - string. Comment for a task. Max 255 characters.
* `cost` - float. Cost in the currency of the user. For information only.
* `conditions` - task end conditions. At least one of fields ("mileage" or "date" or "engine_hours") must be passed.
    * `mileage` - optional object. Mileage condition.
        * `limit` - int. Task limit in kilometers.
        * `notification_interval` - int. Notify about task in specified number of kilometers.
        * `repeat_interval` - int. Interval in kilometers to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
    * `date` - optional date condition object.
        * `end` - [date/time](../../../../getting-started.md#data-types). Task end date.
        * `notification_interval` - int. Notify about task in specified number of days.
        * `repeat_interval` - int. Interval in days to calculate a new end date for repeatable tasks when they are completed. If this parameter is not specified, the interval will be calculated as the difference between the start date and the end date.
    * `engine_hours` - optional engine hours condition object.
        * `limit` - int. Task limit in hours.
        * `notification_interval` - int. Notify about task in specified number of hours.
        * `repeat_interval` - int. Interval in hours to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
* `notifications` - notifications object.
    * `sms_phones` - string array. Phones where sms notifications should be sent. In the international format wo
      `+` sign.
    * `emails` - string array. Email addresses where sms notifications should be sent.
    * `push_enabled` - boolean. If `true` push notifications enabled.
* `repeat` - boolean. If `true` then new task will be created when current task done.
* `unplanned` - boolean. If `true` service work is unplanned. For information only.
* `file_ids` - int array. One file will be specified in many service works. If one of the tasks will be deleted,
  then file will remain in others. File will be deleted only when the last task with it will be deleted.

***

## Task status

Task **status** may be one of:

* `created` – initial state of task.
* `notified` – one of conditions exceed notification limit.
* `expired` – one of conditions exceeded.
* `done` – user [set](#set_status) task as "done".

***

## API actions

API path: `/vehicle/service_task`.

### batch_create

Creates multiple service works.

#### parameters


| name | description | type |
| :------ | :------ | :----- |
| vehicle_ids | List of vehicle ids. Task will be created for every vehicle.  | int array |
| task | Service work to create. `vehicle_id` field in these objects should not be specified. | JSON object |

A `task` object is:

```json
{
    "description": "Service work",
    "comment": "",
    "cost": 10050.0000,
    "conditions": {
        "mileage": {
            "limit": 100,
            "notification_interval": 10
        },
        "date": {
            "end": "2015-05-08 09:35:00",
            "notification_interval": 3
        },
        "engine_hours": {
            "limit": 100,
            "notification_interval": 10
        }
    },
    "notifications": {
        "sms_phones": [
            "79221234567",
            "79227654321"
        ],
        "emails": [
            "email@domain.tld",
            "email@mail.com"
        ],
        "push_enabled": true
    },
    "repeat": false,
    "unplanned": false,
    "file_ids": [1, 2]
}
```

* `description` - string. Name of a service work. Max 255 characters.
* `comment` - string. Comment for a task. Max 255 characters.
* `cost` - float. Cost in the currency of the user. For information only.
* `conditions` - task end conditions. At least one of fields ("mileage" or "date" or "engine_hours") must be passed.
    * `mileage` - optional object. Mileage condition.
        * `limit` - int. Task limit in kilometers.
        * `notification_interval` - int. Notify about task in specified number of kilometers.
    * `date` - optional date condition object.
        * `end` - [date/time](../../../../getting-started.md#data-types). Task end date.
        * `notification_interval` - int. Notify about task in specified number of days.
    * `engine_hours` - optional engine hours condition object.
        * `limit` - int. Task limit in hours.
        * `notification_interval` - int. Notify about task in specified number of hours.
* `notifications` - notifications object.
    * `sms_phones` - string array. Phones where sms notifications should be sent. In the international format without
      `+` sign.
    * `emails` - string array. Email addresses where sms notifications should be sent.
    * `push_enabled` - boolean. If `true` push notifications enabled.
* `repeat` - boolean. If `true` then new task will be created when current task done.
* `unplanned` - boolean. If `true` service work is unplanned. For information only.
* `file_ids` - int array. One file will be specified in many service works. If one of the tasks will be deleted,
  then file will remain in others. File will be deleted only when the last task with it will be deleted.
  
#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/batch/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "vehicle_ids": [76801, 76449], "task": {"comment": "", "conditions": {"date": {"end": "2020-12-10 23:59:59", "notification_interval": 3}}, "cost": 100, "description": "service1", "file_ids": [], "notifications": {"sms_phones": [], "emails": [], "push_enabled": true}, "repeat": false, "unplanned": false}'
    ```

#### response

```json
{"success":true}
```

#### errors

* [General](../../../../getting-started.md#error-codes) types only.

***

### create

Creates a new vehicle service work. For vehicles with associated tracker only.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| task | Service work to create. | JSON object |

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "task": {"vehicle_id": 76801, "comment": "", "conditions": {"date": {"end": "2020-12-10 23:59:59", "notification_interval": 3}}, "cost": 100, "description": "service1", "file_ids": [], "notifications": {"sms_phones": [], "emails": [], "push_enabled": true}, "repeat": false, "unplanned": false}'
    ```

#### response

```json
{
  "success":true,
  "id": 33777
}
```

* `id` - int. An id of created task.

#### errors

* 201 - Not found in the database – vehicle or tracker not found.
* 214 - Requested operation or parameters not supported by the device – engine hours condition passed but tracker hasn't ignition sensor.

***

### delete

Deletes a vehicle service work.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| task_id | Optional. Id of service work. | int |
| task_ids |  Optional. Ids of service works. | int array |

Either **task_id** or **task_ids** should be specified.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "task_id": 33777}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/service_task/delete?hash=a6aa75587e5c59c32d347da438505fc3&task_id=33777
    ```

#### response

```json
{ "success": true }
```

#### errors

* [General](../../../../getting-started.md#error-codes) types only.

***

### download

Downloads pdf report of service works.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| order_by | Sort option. Possible values listed below. | [enum](../../../../getting-started.md#data-types) |
| ascending | Optional. Default is `true`. Sort direction. | boolean |
| group_by | Optional. Group by option. Can be "vehicle" or "status". | [enum](../../../../getting-started.md#data-types) |

* `order_by` possible values:
    * "vehicle" - order by `vehicle_id`.
    * "description" - order by `description`.
    * "status" - order by `status`.
    * "cost" - order by `cost`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "order_by": "vehicle", "group_by": "status"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/service_task/download?hash=a6aa75587e5c59c32d347da438505fc3&order_by=vehicle&group_by=status
    ```

#### response

Report file.

#### errors

* [General](../../../../getting-started.md#error-codes) types only.

***

### list

List all service works of all user vehicles.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| return_prediction | Include legacy **prediction** field or not. | boolean |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "return_prediction": false}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/service_task/list?hash=a6aa75587e5c59c32d347da438505fc3&return_prediction=false
    ```

#### response

```json
{
    "success": true,
    "list": [
        {
            "id": 725,
            "vehicle_id": 222,
            "vehicle_label": "AGV",
            "status": "created",
            "prediction": {
                "end_date": "2015-05-03 09:35:00",
                "wear_percentage": 40
            },
            "description": "Service work",
            "cost": 10050.0,
            "completion": {
                "mileage": 31,
                "date": "2014-03-16 00:00:00",
                "engine_hours": 140
            },
            "completion_date" : "2014-03-16 00:00:00",
            "conditions": { 
                "mileage": {
                    "limit": 100,
                    "notification_interval": 10
                },
                "date": {
                    "end": "2015-05-08 09:35:00",
                    "notification_interval": 3
                },
                "engine_hours": {
                    "limit": 100,
                    "notification_interval": 10
                }
            },
            "current_position": {
                "mileage": 11,
                "date": "2012-03-06 15:55:03",
                "engine_hours": 100
            },
            "start": {
                "mileage": 1230,
                "date": "2015-05-01 17:46:44",
                "engine_hours": 50
            },
            "repeat": false,
            "unplanned": false,
            "file_ids": [2, 3]
        }
    ]
}
```

* list - array of vehicle objects described [here](#service-task-object).

#### errors

* 201 - Not found in the database – vehicle or tracker not found.

***

### read

Get service work info by its id.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| task_id | Id of service work. | int |
| return_prediction | Include legacy **prediction** field or not. | boolean |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "task_id": 37577, "return_prediction": false}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/service_task/read?hash=a6aa75587e5c59c32d347da438505fc3&task_id=37577&return_prediction=false
    ```

#### response

```json
{
    "success": true,
    "value": {
        "id": 725,
        "vehicle_id": 222,
        "status": "created",
        "prediction": {
            "end_date": "2015-05-03 09:35:00",
            "wear_percentage": 40
        },
        "description": "Service work",
        "comment": "",
        "cost": 100500.0,
        "completion": {
            "mileage": 31,
            "date": "2014-03-16 00:00:00",
            "engine_hours": 140
        },
        "conditions": {
            "mileage": {
                "limit": 100,
                "notification_interval": 10
            },
            "date": {
                "end": "2015-05-08 09:35:00",
                "notification_interval": 3
            },
            "engine_hours": {
                "limit": 100,
                "notification_interval": 10
            }
        },
        "start": {
            "mileage": 1230,
            "date": "2015-05-01 17:46:44",
            "engine_hours": 50
        },
        "notifications": {
            "sms_phones": [
                "79221234567",
                "79227654321"
            ],
            "emails": [
                "email@domain.tld",
                "email@mail.com"
            ],
            "push_enabled": true
        },
        "completion_date" : "2014-03-16 00:00:00",
        "repeat": false,
        "unplanned": false,
        "file_ids": [1, 2]
    },
    "files": [<file_object>]
}
```

All parameters described in a [here](#service-task-object).

#### errors

* 201 Not found in the database – does not exist one of tracker's counters which required to determine status.
* 204 Entity not found – when vehicle or service work not found.

***

### set_status

Updates task status, and saved (on `done` **status**) current date and values of used (in condition) counters for 
"freeze" wearing percent.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| task_id | Id of service work. | int |
| status | A new task status. Only `done` status allowed for now. | [enum](../../../../getting-started.md#data-types) |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/set_status' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "task_id": 37577, "status": "done"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/service_task/set_status?hash=a6aa75587e5c59c32d347da438505fc3&task_id=37577&status=done
    ```

#### response

```json
{ "success": true }
```

#### errors

* 201 - Not found in the database – does not exist one of tracker's counters which required to determine status.
* 204 - Entity not found – when vehicle or service work not found.

***

### update

Updates information fields and notification settings of vehicle service work.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| task | Service work to create. | JSON object |

A [task object](#create) described in a task create. 

#### example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "task": {"vehicle_id": 76801, "comment": "", "conditions": {"date": {"end": "2020-12-10 23:59:59", "notification_interval": 3}}, "cost": 100, "description": "service1", "file_ids": [], "notifications": {"sms_phones": [], "emails": [], "push_enabled": true}, "repeat": false, "unplanned": false}'
    ```

#### response

```json
{ "success": true }
```

#### errors

* 204 - Entity not found – when vehicle or service work not found.
* 214 - Requested operation or parameters not supported by the device – engine hours condition passed but tracker
 hasn't ignition sensor.

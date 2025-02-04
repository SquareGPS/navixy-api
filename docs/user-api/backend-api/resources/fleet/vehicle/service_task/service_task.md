---
title: Service work
description: Contains service task object description and API calls to work with it.   
---

# Vehicle service work

Contains service task object description and API calls to interact with vehicle service works that is used for vehicle maintenance.
Vehicle maintenance feature helps to make sure that any scheduled maintenance or urgent repair is carried out in a timely manner.

Described step-by-step about service task APIs in our [guides](../../../../guides/fleet-management/service-works.md).


## Service task object

```json
{
  "id": 725,
  "repeat": true,
  "unplanned": false,
  "completion_date" : "2014-03-16 00:00:00",
  "vehicle_id": 222,
  "cost": 100500.0,
  "start": {
    "mileage": 1230,
    "date": "2015-05-01 17:46:44",
    "engine_hours": 50
  },
  "completion": {
    "mileage": 31,
    "date": "2014-03-16 00:00:00",
    "engine_hours": 140
  },
  "conditions": {
    "mileage": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
    },
    "date": {
      "end": "2015-05-08 09:35:00",
      "notification_interval": 3,
      "repeat_interval": 42
    },
    "engine_hours": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
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
  "status": "created",
  "description": "Service work",
  "comment": "",
  "file_ids": [1, 2],
  "vehicle_label": "Service car 002",
  "prediction": {
    "end_date": "2015-05-03 00:59:59",
    "wear_percentage": 40
  },
  "current_position": {
    "mileage": 1300,
    "date": "2015-06-01 17:46:44",
    "engine_hours": 70
  }
}
```

* `id` - int. An ID of service work.
* `repeat` - boolean. If `true` then new task will be created when current task done.
* `unplanned` - boolean. If `true` service work is unplanned. For information only.
* `completion_date` - [date/time](../../../../getting-started/introduction.md#data-types). Date when a service work completed.
* `vehicle_id` - int. An ID of associated vehicle.
* `cost` - float. Cost in the currency of the user. For information only.
* `start` - object. Consists initial values.
    * `mileage` - int. Initial odometer value for tasks with mileage condition.
    * `date` - [date/time](../../../../getting-started/introduction.md#data-types). Task creation date for tasks with date condition.
    * `engine_hours` - int. Initial engine hours value for tasks with engine hours condition.
* `completion` - object. Date and counter's values when the task marked as done. Non-editable.
    * `mileage` - int. Odometer value when the task marked as done.
    * `date` - [date/time](../../../../getting-started/introduction.md#data-types). Date when the task marked as done.
    * `engine_hours` - int. Engine hours value when the task marked as done.
* `conditions` - task end conditions. At least one of fields ("mileage" or "date" or "engine_hours") must be passed.
    * `mileage` - optional object. Mileage condition.
        * `limit` - int. Task limit in kilometers.
        * `notification_interval` - int. Notify about task in specified number of kilometers.
        * `repeat_interval` - int. Interval in kilometers to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
    * `date` - optional date condition object.
        * `end` - [date/time](../../../../getting-started/introduction.md#data-types). Task end date.
        * `notification_interval` - int. Notify about task in specified number of days.
        * `repeat_interval` - int. Interval in days to calculate a new end date for repeatable tasks when they are completed. If this parameter is not specified, the interval will be calculated as the difference between the start date and the end date.
    * `engine_hours` - optional engine hours condition object.
        * `limit` - int. Task limit in hours.
        * `notification_interval` - int. Notify about task in specified number of hours.
        * `repeat_interval` - int. Interval in hours to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
* `notifications` - notifications object.
    * `sms_phones` - string array. Phones where sms notifications should be sent. In the international format without `+` sign.
    * `emails` - string array. Email addresses where sms notifications should be sent.
    * `push_enabled` - boolean. If `true` push notifications enabled.
* `status` - [enum](../../../../getting-started/introduction.md#data-types). [Status](#task-status).
* `description` - string. Name of a service work. Max 255 characters.
* `comment` - string. Comment for a task. Max 255 characters.
* `file_ids` - int array. One file will be specified in many service works. If one of the tasks will be deleted,
  then file will remain in others. File will be deleted only when the last task with it will be deleted.
* `vehicle_label` - string. Vehicle label.
* `prediction` - optional object. Legacy field, is not used anymore. check return_prediction parameter.
    * `end_date` - [date/time](../../../../getting-started/introduction.md#data-types). Predicted end date.
    * `wear_percentage` - int. Wear percentage.
* `current_position` - object. Current position values.
    * `mileage` - int. Current mileage.
    * `date` - [date/time](../../../../getting-started/introduction.md#data-types). Current date.
    * `engine_hours` - int. Current engine hours.


## Task status

Task **status** may be one of:

* `created` – initial state of task.
* `notified` – one of conditions exceed notification limit.
* `expired` – one of conditions exceeded.
* `done` – user [set](#set_status) task as "done".


## API actions

API path: `/vehicle/service_task`.

### `batch_create`

Creates multiple service works.

#### Parameters


| name        | description                                                  | type        |
|:------------|:-------------------------------------------------------------|:------------|
| vehicle_ids | List of vehicle IDs. Task will be created for every vehicle. | int array   |
| task        | Service work to create.                                      | JSON object |

A `task` object is:

```json
{
  "repeat": false,
  "unplanned": false,
  "cost": 10050.0000,
  "conditions": {
    "mileage": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
    },
    "date": {
      "end": "2015-05-08 09:35:00",
      "notification_interval": 3,
      "repeat_interval": 42
    },
    "engine_hours": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
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
  "description": "Service work",
  "comment": "",
  "file_ids": [1, 2]
}
```

* `repeat` - boolean. If `true` then new task will be created when current task done.
* `unplanned` - boolean. If `true` service work is unplanned. For information only.
* `cost` - float. Cost in the currency of the user. For information only.
* `conditions` - task end conditions. At least one of fields ("mileage" or "date" or "engine_hours") must be passed.
    * `mileage` - optional object. Mileage condition.
        * `limit` - int. Task limit in kilometers.
        * `notification_interval` - int. Notify about task in specified number of kilometers.
        * `repeat_interval` - int. Interval in kilometers to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
    * `date` - optional date condition object.
        * `end` - [date/time](../../../../getting-started/introduction.md#data-types). Task end date.
        * `notification_interval` - int. Notify about task in specified number of days.
        * `repeat_interval` - int. Interval in days to calculate a new end date for repeatable tasks when they are completed. If this parameter is not specified, the interval will be calculated as the difference between the start date and the end date.
    * `engine_hours` - optional engine hours condition object.
        * `limit` - int. Task limit in hours.
        * `notification_interval` - int. Notify about task in specified number of hours.
        * `repeat_interval` - int. Interval in hours to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
* `notifications` - notifications object.
    * `sms_phones` - string array. Phones where sms notifications should be sent. In the international format without `+` sign.
    * `emails` - string array. Email addresses where sms notifications should be sent.
    * `push_enabled` - boolean. If `true` push notifications enabled.
* `description` - string. Name of a service work. Max 255 characters.
* `comment` - string. Comment for a task. Max 255 characters.
* `file_ids` - int array. One file will be specified in many service works. If one of the tasks will be deleted,
  then file will remain in others. File will be deleted only when the last task with it will be deleted.
  
#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/batch/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "vehicle_ids": [76801, 76449], "task": {"comment": "", "conditions": {"date": {"end": "2020-12-10 23:59:59", "notification_interval": 3}}, "cost": 100, "description": "service1", "file_ids": [], "notifications": {"sms_phones": [], "emails": [], "push_enabled": true}, "repeat": false, "unplanned": false}'
    ```

#### Response

```json
{"success":true}
```

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.


### `create`

Creates a new vehicle service work. For vehicles with associated tracker only.

#### Parameters

| name | description             | type        |
|:-----|:------------------------|:------------|
| task | Service work to create. | JSON object |

A `task` object is:

```json
{
  "repeat": false,
  "unplanned": false,
  "vehicle_id": 222,
  "cost": 10050.0000,
  "conditions": {
    "mileage": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
    },
    "date": {
      "end": "2015-05-08 09:35:00",
      "notification_interval": 3,
      "repeat_interval": 42
    },
    "engine_hours": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
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
  "description": "Service work",
  "comment": "",
  "file_ids": [1, 2]
}
```

* `repeat` - boolean. If `true` then new task will be created when current task done.
* `unplanned` - boolean. If `true` service work is unplanned. For information only.
* `vehicle_id` - int. An ID of associated vehicle.
* `cost` - float. Cost in the currency of the user. For information only.
* `conditions` - task end conditions. At least one of fields ("mileage" or "date" or "engine_hours") must be passed.
    * `mileage` - optional object. Mileage condition.
        * `limit` - int. Task limit in kilometers.
        * `notification_interval` - int. Notify about task in specified number of kilometers.
        * `repeat_interval` - int. Interval in kilometers to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
    * `date` - optional date condition object.
        * `end` - [date/time](../../../../getting-started/introduction.md#data-types). Task end date.
        * `notification_interval` - int. Notify about task in specified number of days.
        * `repeat_interval` - int. Interval in days to calculate a new end date for repeatable tasks when they are completed. If this parameter is not specified, the interval will be calculated as the difference between the start date and the end date.
    * `engine_hours` - optional engine hours condition object.
        * `limit` - int. Task limit in hours.
        * `notification_interval` - int. Notify about task in specified number of hours.
        * `repeat_interval` - int. Interval in hours to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
* `notifications` - notifications object.
    * `sms_phones` - string array. Phones where sms notifications should be sent. In the international format without `+` sign.
    * `emails` - string array. Email addresses where sms notifications should be sent.
    * `push_enabled` - boolean. If `true` push notifications enabled.
* `description` - string. Name of a service work. Max 255 characters.
* `comment` - string. Comment for a task. Max 255 characters.
* `file_ids` - int array. One file will be specified in many service works. If one of the tasks will be deleted,
  then file will remain in others. File will be deleted only when the last task with it will be deleted.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "task": {"vehicle_id": 76801, "comment": "", "conditions": {"date": {"end": "2020-12-10 23:59:59", "notification_interval": 3}}, "cost": 100, "description": "service1", "file_ids": [], "notifications": {"sms_phones": [], "emails": [], "push_enabled": true}, "repeat": false, "unplanned": false}'
    ```

#### Response

```json
{
  "success":true,
  "id": 33777
}
```

* `id` - int. An ID of created task.

#### Errors

* 201 - Not found in the database – vehicle or tracker not found.
* 214 - Requested operation or parameters not supported by the device – engine hours condition passed but tracker hasn't ignition sensor.


### `delete`

Deletes a vehicle service work.

#### Parameters

| name     | description                     | type      |
|:---------|:--------------------------------|:----------|
| task_id  | Optional. ID of service work.   | int       |
| task_ids | Optional. IDs of service works. | int array |

Either **task_id** or **task_ids** should be specified.

#### Examples

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

#### Response

```json
{ "success": true }
```

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.


### `download`

Downloads report of service works.

#### Parameters

| name                | description                                                                                                                                            | type                                                                     |
|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| only_unplanned      | Optional. Default is `false`. Service works filter. If `true`, only unplanned service works will be included.                                          | boolean                                                                  |
| vehicle_ids         | Optional. Service works filter. If not empty, service works will be filtered by vehicle ids.                                                           | int array                                                                |
| statuses            | Optional. Service works filter. If not empty, service works will be filtered by statuses. Possible values are "created", "notified","done", "expired". | [enum](../../../../getting-started/introduction.md#data-types)           |
| conditions          | Optional. [Search conditions](#condition-fields) to apply to list.                                                                                     | array of [SearchCondition](../../../commons/entity/search_conditions.md) |
| filter              | Optional. Text filter string. If used with conditions, both filter and conditions must match for every returned service task.                          | string                                                                   |
| sort                | Optional. Set of [sort options](#sort-fields). Each option is a pair of property name and sorting direction, e.g. `["status=asc", "cost=desc"]`.       | string array                                                             |
| limit               | Optional. Maximum number of returned service works.                                                                                                    | int                                                                      |
| offset              | Optional. Offset from start of found service works for pagination.                                                                                     | int                                                                      |
| add_filename_header | Optional. Option to include header. Default is `false`. If `true`, Content-Disposition header will be appended to the response.                        | boolean                                                                  |
| format              | Optional. Default is "pdf". Report format. Possible values are "pdf", "xls","xlsx".                                                                    | [enum](../../../../getting-started/introduction.md#data-types)           |
| group_by            | Optional. Group by option. Possible values are "vehicle", "status".                                                                                    | [enum](../../../../getting-started/introduction.md#data-types)           |


#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "group_by": "status"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/service_task/download?hash=a6aa75587e5c59c32d347da438505fc3&group_by=status
    ```

#### Response

Report file.

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.


### `list`

List all service works of all user vehicles.

#### Parameters


| name                | description                                                                                                                                                    | type                                                                     |
|:--------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
| only_unplanned      | Optional. Default is `false`. Service works filter. If `true`, only unplanned service works will be included.                                                  | boolean                                                                  |
| vehicle_ids         | Optional. Service works filter. If not empty, service works will be filtered by vehicle ids.                                                                   | int array                                                                |
| statuses            | Optional. Service works filter. If not empty, service works will be filtered by statuses. Possible values are "created", "notified","done", "expired".         | [enum](../../../../getting-started/introduction.md#data-types)           |
| conditions          | Optional. Search conditions to apply to list. Possible fields listed below.                                                                                    | array of [SearchCondition](../../../commons/entity/search_conditions.md) |
| filter              | Optional. Text filter string. If used with conditions, both filter and conditions must match for every returned service task.                                  | string                                                                   |
| sort                | Optional. Set of sort options. Each option is a pair of property name and sorting direction, e.g. `["status=asc", "cost=desc"]`. Possible fields listed below. | string array                                                             |
| limit               | Optional. Maximum number of returned service works.                                                                                                            | int                                                                      |
| offset              | Optional. Offset from start of found service works for pagination.                                                                                             | int                                                                      |
| add_filename_header | Optional. Default is `false`. Option to include header. If `true`, Content-Disposition header will be appended to the response.                                | boolean                                                                  |
| return_prediction   | Optional. Default is `true`. Option to include legacy **prediction** field or not.                                                                             | boolean                                                                  |

##### condition fields

| Name           | Type                                                                |
|:---------------|:--------------------------------------------------------------------|
| vehicle        | string                                                              |
| vehicle_id     | int                                                                 |
| description    | string                                                              |
| comment        | string                                                              |
| creation_date  | [date/time](../../../../getting-started/introduction.md#data-types) |
| status         | string                                                              |
| cost           | float                                                               |
| predicted_date | [date/time](../../../../getting-started/introduction.md#data-types) |

##### sort fields

| Name           | Type                                                                |
|:---------------|:--------------------------------------------------------------------|
| id             | int                                                                 |
| vehicle        | string                                                              |
| vehicle_id     | int                                                                 |
| description    | string                                                              |
| comment        | string                                                              |
| creation_date  | [date/time](../../../../getting-started/introduction.md#data-types) |
| status         | string                                                              |
| cost           | float                                                               |
| predicted_date | [date/time](../../../../getting-started/introduction.md#data-types) |

#### Examples

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

#### Response

```json
{
  "success": true,
  "list": [<service_work>]
}
```

* list - array of service works objects described [here](#service-task-object).

#### Errors

* 201 - Not found in the database – vehicle or tracker not found.


### `read`

Gets service work info by its id.

#### Parameters

| name              | description                                                                        | type    |
|:------------------|:-----------------------------------------------------------------------------------|:--------|
| task_id           | ID of service work.                                                                | int     |
| return_prediction | Optional. Default is `true`. Option to include legacy **prediction** field or not. | boolean |

#### Examples

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

#### Response

```json
{
  "success": true,
  "value": {<service_work>}
}
```
* value - service work object described [here](#service-task-object).

#### Errors

* 201 Not found in the database – does not exist one of tracker's counters which required to determine status.
* 204 Entity not found – when vehicle or service work not found.


### `set_status`

Updates task status, and saved (on `done` **status**) current date and values of used (in condition) counters for 
"freeze" wearing percent.

#### Parameters

| name    | description                                            | type                                                           |
|:--------|:-------------------------------------------------------|:---------------------------------------------------------------|
| task_id | ID of service work.                                    | int                                                            |
| status  | A new task status. Only `done` status allowed for now. | [enum](../../../../getting-started/introduction.md#data-types) |

#### Examples

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

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – does not exist one of tracker's counters which required to determine status.
* 204 - Entity not found – when vehicle or service work not found.


### `update`

Updates information fields and notification settings of vehicle service work.

#### Parameters

| name | description             | type        |
|:-----|:------------------------|:------------|
| task | Service work to update. | JSON object |

A `task` object is:

```json
{
  "id": 725,
  "repeat": true,
  "unplanned": false,
  "vehicle_id": 222,
  "cost": 100500.0,
  "conditions": {
    "mileage": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
    },
    "date": {
      "end": "2015-05-08 09:35:00",
      "notification_interval": 3,
      "repeat_interval": 42
    },
    "engine_hours": {
      "limit": 100,
      "notification_interval": 10,
      "repeat_interval": 42
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
  "description": "Service work",
  "comment": "",
  "file_ids": [1, 2]
}
```

* `id` - int. An ID of service work.
* `repeat` - boolean. If `true` then new task will be created when current task done.
* `unplanned` - boolean. If `true` service work is unplanned. For information only.
* `vehicle_id` - int. An ID of associated vehicle.
* `cost` - float. Cost in the currency of the user. For information only.
* `conditions` - task end conditions. At least one of fields ("mileage" or "date" or "engine_hours") must be passed.
    * `mileage` - optional object. Mileage condition.
        * `limit` - int. Task limit in kilometers.
        * `notification_interval` - int. Notify about task in specified number of kilometers.
        * `repeat_interval` - int. Interval in kilometers to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
    * `date` - optional date condition object.
        * `end` - [date/time](../../../../getting-started/introduction.md#data-types). Task end date.
        * `notification_interval` - int. Notify about task in specified number of days.
        * `repeat_interval` - int. Interval in days to calculate a new end date for repeatable tasks when they are completed. If this parameter is not specified, the interval will be calculated as the difference between the start date and the end date.
    * `engine_hours` - optional engine hours condition object.
        * `limit` - int. Task limit in hours.
        * `notification_interval` - int. Notify about task in specified number of hours.
        * `repeat_interval` - int. Interval in hours to set `limit` for a new repeatable task when current one is completed. If this parameter is not set, the initial `limit` value will be used.
* `notifications` - notifications object.
    * `sms_phones` - string array. Phones where sms notifications should be sent. In the international format without `+` sign.
    * `emails` - string array. Email addresses where sms notifications should be sent.
    * `push_enabled` - boolean. If `true` push notifications enabled.
* `description` - string. Name of a service work. Max 255 characters.
* `comment` - string. Comment for a task. Max 255 characters.
* `file_ids` - int array. One file will be specified in many service works. If one of the tasks will be deleted,
  then file will remain in others. File will be deleted only when the last task with it will be deleted.

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/service_task/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "task": {"vehicle_id": 76801, "comment": "", "conditions": {"date": {"end": "2020-12-10 23:59:59", "notification_interval": 3}}, "cost": 100, "description": "service1", "file_ids": [], "notifications": {"sms_phones": [], "emails": [], "push_enabled": true}, "repeat": false, "unplanned": false}'
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 204 - Entity not found – when vehicle or service work not found.
* 214 - Requested operation or parameters not supported by the device – engine hours condition passed but tracker
 hasn't ignition sensor.

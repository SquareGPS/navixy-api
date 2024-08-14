---
title: Task form actions
description: This document describes API actions specific to working with task forms (except task/form/list which can return all kinds of forms).
---

# Working with task forms

Forms can be attached to tasks to be filled by field employees using Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)).
This document describes API actions specific to working with task forms (except `task/form/list` which can return all 
kinds of forms).

For `<form_field>` and `<form_value>` object description, see [form fields and values](../../form/field-types.md#form-fields-and-values).

For `<form>` object description, see [forms](../../form/index.md).

Contains API calls related to forms associated with tasks.


## API actions

API path: `/task/form`.

### `create`

Attaches new form to the existing task or checkpoint. Form always created on the basis of form template.

**required sub-user rights**: `task_update`.

#### Parameters

| name        | description                  | type |
|:------------|:-----------------------------|:-----|
| task_id     | An ID of the task to assign. | int  |
| template_id | An ID of the form template.  | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/form/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 11231, "template_id": 12548}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/form/create?hash=a6aa75587e5c59c32d347da438505fc3&task_id=11231&template_id=12548
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no task or template with such an ID, or task has the "route" type.
* 247 – Entity already exists - if task already has form attached to it.
* 255 – Invalid task state - if current task state is not `unassigned`, `assigned` or `arrived`.


### `delete`

Deletes a form (detach it from the task).<br>
All form data will be lost!

**required sub-user rights**: `task_update`.

#### Parameters

| name    | description                                  | type |
|:--------|:---------------------------------------------|:-----|
| task_id | An ID of the task to which form is attached. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/form/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 11231}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/form/delete?hash=a6aa75587e5c59c32d347da438505fc3&task_id=11231
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - if there is no task with such an ID, or task has the "route" type, or it has no form
 attached.
* 255 – Invalid task state - if current task state is not `unassigned`, `assigned` or `arrived`.


### `download`

Retrieves attached form as file.

#### Parameters

| name    | description                                                | type                                              |
|:--------|:-----------------------------------------------------------|:--------------------------------------------------|
| task_id | An ID of the task.                                         | int                                               |
| format  | Format of the download file. Can be "xls", "csv" or "pdf". | [enum](../../../../getting-started/introduction.md#data-types) |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/form/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 11231, "format": "pdf"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/form/download?hash=a6aa75587e5c59c32d347da438505fc3&task_id=11231&format=pdf
    ```
    
#### Response

A form rendered to file (standard file download).

#### Errors

* 201 – Not found in the database - if task does not exist or does not have attached form.


### `list`

Returns descriptions of forms, created on the basis of specified form template. In addition to the data on the forms, 
the list contains data on the objects related to each form – tracker / vehicle / employee, task.

#### Parameters

*   **template_id** (*integer, optional*). The returned list will contain forms, related to that template.<br>
    **warning:** at least one of **template_id** and **task_ids** parameters must be not null.
*   **task_ids** (*list of integers, optional*). Maximum size of list is 5000 elements. List of task IDs. The returned list will contain forms, related to tasks, which IDs specified in this parameter.<br>
    **warning:** at least one of **template_id** and **task_ids** parameters must not be null.
*   **order_by** (*optional, default = submitted*). Data field for list sorting. Available values:
    *   *task_id*
    *   *created*
    *   *submitted*
    *   *task_address*
    *   *submit_address*
    *   *employee_full_name*
    *   *vehicle_label*
    *   *tracker_label*
    *   *task_label*
    *   *task_creation_date*
    *   *task_from*
    *   *task_to*
    *   *task_arrival_date*
    *   *task_completion_date*
    *   *form_label*
    *   *form_description*
*   **ascending** (_boolean, required_). Sorting direction (ascending / descending).
*   **include_unsubmitted** (_boolean, required_). If true, unsubmitted forms shall be included in the list.
*   **filters** (_object, optional_). Specifies the criteria for filtering the list based on the values of the data fields. Conditions are combined by logical AND.\Filters object contains following optional elements:

```json
{
    "employee_full_name": "John Dow", // a sequence of characters for partial matching (against the name of the associated employee)
    "form_description": "Description",
    "form_label": "Form Label",
    "submit_address": "Submit Address",
    "task_id": 123, // strict match
    "task_address": "Task Address",
    "task_label": "Task Label",
    "tracker_label": "Tracker label",
    "vehicle_label": "Vehicle label",
}
```

*   **submit_period** (*period_object, optional*).
*   **task_creation_period** (*period_object, optional*).
*   **task_from_period** (*period_object, optional*).
*   **task_to_period** (*period_object, optional*).
*   **task_arrival_period** (*period_object, optional*).
*   **task_completion_period** (*period_object, optional*).

where period_object is:

```json
    {
        "from": "2020-02-03 03:00:00", // string <date/time>
        "to": "2020-02-03 08:00:00" // string <date/time>
    }
```

*   **offset, limit** (*integers, optional*). Specify which subset of elements from all matching results will be included in the returned list.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/form/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "ascending": true, "include_unsubmitted": true}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/form/list?hash=a6aa75587e5c59c32d347da438505fc3&ascending=true&include_unsubmitted=true
    ```
    
#### Response

```json
{
    "success": true,
    "count": 2,
    "list": [{
        "employee": {
            "id": 13,
            "first_name": "John",
            "middle_name": "",
            "last_name": "Dow"
        },
        "task": {
            "id": 7867,
            "label": "My task 3",
            "from": "2017-07-27 15:00:00",
            "to": "2017-07-28 14:59:59",
            "creation_date": "2017-07-27 12:12:23",
            "arrival_date": "2017-07-27 15:14:07",
            "address": "Moltkestrasse 32",
            "status": "done",
            "completion_date": "2017-07-28 14:36:28",
            "fact_duration": "PT22M21S"
        },
        "tracker": {
            "id": 15620,
            "label": "Navixy A6"
        },
        "vehicle": null,
        "form": {
            "id": 1012,
            "label": "A form",
            "description": "",
            "fields": [],
            "created": "2017-07-28 03:48:06",
            "submit_in_zone": false,
            "task_id": 7867,
            "template_id": 449,
            "values": null,
            "submitted": "2017-03-21 18:40:54", 
            "submit_location": {
            	"lat": 26.826762,
            	"lng": 20.5947311,
            	"address": "Partizan st., 4"
            }
        },
        "submit_places": {
			"location": {
				"lat": 26.826762,
				"lng": 20.5947311,
				"address": "Partizan st., 4"
			},
			"places": [{
				"id": 38,
				"label": "Office sweet office"
			}],
			"zones": [{
				"id": 18404,
				"label": "Zone 51"
			}]
        }
    }
]}
```

* `count` - int. Total number of forms matching the query.
* `form` - [form object](../../form/index.md#form-object), non-null.
* `submit_places` - additional info about places/zones related to form submission, can be null.
    * `places` - list of places associated with zone submission location. Can be empty.
    * `zones` - list of zones associated with zone submission location. Can be empty.

#### Errors

* 204 – Not found - if there is no form template with such ID belonging to authorized user.
* [General](../../../../getting-started/errors.md#error-codes) types of errors.


### `read`

Gets form associated with the specified task.

#### Parameters

| name    | description        | type |
|:--------|:-------------------|:-----|
| task_id | An ID of the task. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/form/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 12546}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/form/read?hash=a6aa75587e5c59c32d347da438505fc3&task_id=12546
    ```

#### Response

```json
{
    "success": true,
    "value" : <form>,
    "files" : [
        {
            "id": 16,
            "storage_id": 1,
            "user_id": 12203,
            "type": "image",
            "created": "2020-09-06 11:54:28",
            "uploaded": "2020-09-06 11:55:14",
            "name": "lala.jpg",
            "size": 72594,
            "mime_type": "image/png",
            "metadata": {
                         "orientation":  1
                        },
            "state": "uploaded",
            "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg",
            "bindings": {
                "form_field": {
                    "form_id": 40,
                    "field_id": "2222",
                    "submitted": false
                }
            },
            "previews": [
                {
                    "download_url": "https://localhost:8084/file/preview/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
                }
            ]
        }
   ]
}
```

* `value` - [form object](../../form/index.md#form-object), or null if no form attached.
* `files` - list of files, both submitted and unsubmitted, associated with this form's fields.
    * `id` - int. File ID.
    * `type` - [enum](../../../../getting-started/introduction.md#data-types). Can be "image" or "file".
    * `created` - [date/time](../../../../getting-started/introduction.md#data-types). Date when file created.
    * `uploaded` - [date/time](../../../../getting-started/introduction.md#data-types). Date when file uploaded, can be null if file not yet uploaded.
    * `name` - string. Filename.
    * `size` - int. Size in bytes. If file not uploaded, show maximum allowed size for the upload.
    * `metadata` - metadata object.
    * `orientation` - int. Image exif orientation.
    * `state` - [enum](../../../../getting-started/introduction.md#data-types). Can be "created", "in_progress", "uploaded", "deleted".
    * `download_url` - string. Actual URL at which file is available. Can be null if file not yet uploaded.
    * `bindings` - all entities to which this file linked.
    * `previews` - available preview images for the file. Can be null or empty for any file in any state.

#### Errors

* 201 – Not found in the database - if there is no task with such an ID, or task assigned to tracker unavailable to 
current sub-user.

---
title: Task form actions
description: Task form actions
---

# Working with task forms

Forms can be attached to tasks to be filled by field employees using Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)).
This document describes API actions specific to working with task forms (except `task/form/list` which can return all 
kinds of forms).

For `<form_field>` and `<form_value>` object description, see [form fields and values](../../form/field-types.md#form-fields-and-values).

For `<form>` object description, see [forms](../../form/index.md).

## API actions

API path: `/task/form`.

Contains API calls related to forms associated with tasks.

### create

Attach new form to the existing task or checkpoint. Form is always created on the basis of form template.

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) Id of the task to assign
* **template_id** - (int) Id of the form template

#### response

```js
{
    "success": true
}
```

#### errors

*   201 – Not found in database (if there is no task or template with such id, or task has the “route” type)
*   247 – Entity already exists (if task already has form attached to it)
*   255 – Invalid task state (if current task state is not “unassigned”, “assigned” or “arrived”)



### delete

Delete form (detach it from the task).<br>
All form data will be lost!

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) Id of the task to which form is attached

#### response

```js
{
    "success": true
}
```

#### errors

*   201 – Not found in database (if there is no task with such id, or task has the “route” type, or it has no form attached)
*   255 – Invalid task state (if current task state is not “unassigned”, “assigned” or “arrived”)



### download

Retrieve attached form as file.

#### parameters

* **task_id**
* **format**

#### response

    A form rendered to file (standard file download).

#### errors

*   201 – Not found in database (if task does not exist or does not have attached form)


### list

Returns descriptions of forms, created on the basis of specified form template. In addition to the data on the forms, the list contains data on the objects related to each form – tracker / vehicle / employee, task.

#### parameters

*   **form_template_id** (*integer, optional*). The returned list will contain forms, related to that template.<br>
    **warning:** at least one of **form_template_id** and **task_ids** parameters must be not null.
*   **task_ids** (*list of integers, optional*). Maximum size of list is 500 elements. List of task ids. The returned list will contain forms, related to tasks, which ids are specified in this parameter.<br>
    **warning:** at least one of **form_template_id** and **task_ids** parameters must be not null.
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
*   **filters** (_object, optional_). Specifies the criteria for filtering the list based on the values of the data fields. Conditions are combined by logical AND.\ Filters object contains following optional elements:

```js
{
    "employee_full_name": , // a sequence of characters for partial matching (against the name of the associated employee)
    "form_description": ,
    "form_label": ,
    "submit_address": ,
    "task_id": // strict match
    "task_address": ,
    "task_label": ,
    "tracker_label": ,
    "vehicle_label": ,
}
```

*   **submit_period** (*&lt;period_object&gt;, optional*).
*   **task_creation_period** (*&lt;period_object&gt;, optional*).
*   **task_from_period** (*&lt;period_object&gt;, optional*).
*   **task_to_period** (*&lt;period_object&gt;, optional*).
*   **task_arrival_period** (*&lt;period_object&gt;, optional*).
*   **task_completion_period** (*&lt;period_object&gt;, optional*).

```js
<period_object>=
    {
        "from": <date/time>,
        "to": <date/time>
    }
```

*   **offset, limit** (*integers, optional*). Specify which subset of elements from all matching results will be included in the returned list.

#### response

```js
{
    "success": true,
    "count": N, //total number of forms matching the query
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
        "form": { //<form> object, non-null
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
        "submit_places": { //additional info about places/zones related to form submission, can be null
			"location": {
				"lat": 26.826762,
				"lng": 20.5947311,
				"address": "Partizan st., 4"
			},
			"places": [{ //list of places associated with zone submission location. Can be empty
				"id": 38,
				"label": "Office sweet office"
			}],
			"zones": [{ //list of zones associated with zone submission location. Can be empty
				"id": 18404,
				"label": "Zone 51"
			}]
        }
    },…
]}
```

#### errors

*   204 – Not found (if there is no form template with such id belonging to authorized user)
*   General types of errors.



### read

Get form associated with the specified task.

#### parameters

* **task_id** - (int) Id of the task

#### response

```js
{
    "success": true,
    "value" : <form>, //form object, or null if no form is attached
    "files" : [ //list of files, both submitted and unsibmitted, associated with this form's fields
        {
            "id": 16, //file id
            "storage_id": 1,
            "user_id": 12203,
            "type": "image", //"image" or "file"
            "created": "2017-09-06 11:54:28", //date when file was created
            "uploaded": "2017-09-06 11:55:14", //date when file was uploaded, can be null if file is not yet uploaded
            "name": "lala.jpg", //filename
            "size": 72594, //in bytes. If file not uploaded, show maximum allowed size for upload
            "mime_type": "image/png",
            "metadata": <nullable, metadata object>,
            "state": "uploaded", //can be "created", "in_progress", "uploaded", "deleted"
            //actual url at which file is available. Can be null if file is not yet uploaded
            "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg",
            "bindings": { //all entities to which this file is linked
                "form_field": {
                    "form_id": 40,
                    "field_id": "2222",
                    "submitted": false
                }
            },
            "previews": [ //available preview images for file. Can be null or empty for any file in any state.
                {
                    "download_url": "https://localhost:8084/file/preview/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
                }
            ]
        },
        ...
   ]
}
```

metadata object:

```js
{
 "orientation":  <int, image exif orientation>,
}
```

For **form** object description, see [task/form/](#form-object-structure).

#### errors

*   201 – Not found in database (if there is no task with such id, or task is assigned to tracker unavailable to current subuser)

---
title: Task form
description: Task form
---

# Task form

API path: `/task/form`.

Contains API calls related to forms associated with tasks.

See [forms](../../form/form.md).

#### Form object structure

```js
<form> =
{
    "id": 2, //form unique id
    "label": "Order form", //user-defined form label, from 1 to 100 characters
    "fields": [  //multiple <form_field> objects can be here
      {
        "id": "111-aaa-whatever", //id must be unique across form fields
        "label": "Name",
        "description": "Your full name",
        "required": true,
        "min_length": 5,
        "max_length": 255,
        "type": "text"
      }
    ],
    "created": "2017-03-15 12:36:27", //date when this form was created (attached to the task). Read-only field
    "submit_in_zone": true, //if true, form can be submitted only in task zone
    "task_id": 1, //id of the task to which this form is attached
    "template_id": 1, //id of the form template on which this form is based. Can be null if template was deleted.
    "values": { //A map with field ids as keys and <field_value> objects as values
      "111-aaa-whatever": { //key is used to link field and its corresponding value
        "type": "text", //value type and field type must match
        "value": "John Doe" //the rest of value object is field type-specific
      }
    },
    "submitted": "2017-03-21 18:40:54", //date when form values were last submitted
    "submit_location": { //location at which form values were last submitted
      "lat": 11.0,
      "lng": 22.0,
      "address": "Wall Street, NY"
    }
}
```

For **form_field** and **form_value** object description, see [form fields and values](../../form/field-types.md#form-fields-and-values).



## create()

Attach new form to the existing task or checkpoint. Form is always created on the basis of form template.

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) Id of the task to assign
* **template_id** - (int) Id of the form template

#### return

```js
{
    "success": true
}
```

#### errors

*   201 – Not found in database (if there is no task or template with such id, or task has the “route” type)
*   247 – Entity already exists (if task already has form attached to it)
*   255 – Invalid task state (if current task state is not “unassigned”, “assigned” or “arrived”)



## delete()

Delete form (detach it from the task).<br>
All form data will be lost!

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) Id of the task to which form is attached

#### return

```js
{
    "success": true
}
```

#### errors

*   201 – Not found in database (if there is no task with such id, or task has the “route” type, or it has no form attached)
*   255 – Invalid task state (if current task state is not “unassigned”, “assigned” or “arrived”)



## download()

Retrieve attached form as file.

#### parameters

* **task_id**
* **format**

#### return

    A form rendered to file (standard file download).

#### errors

*   201 – Not found in database (if task does not exist or does not have attached form)



## list()

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

#### return

```js
{
    "success": true,
    "count": N,
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



## read()

Get form associated with the specified task.

#### parameters

* **task_id** - (int) Id of the task

#### return

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

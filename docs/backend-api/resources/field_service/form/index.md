---
title: About forms
description: About forms
---

Forms are used to provide additional information, such as user name, phone, delivery date, etc. upon task completion
or check-in from iOS/Android mobile tracker app.
Forms are attached to tasks. If form is attached to task, this task cannot be completed without form submission.

* Each form must be created from template, read more at [Templates](./template.md)
* For description of `<form_field>` and `<field_value>`, see [Form fields and values](./field-types.md)
* Using web API, it's now possible to only attach/fill forms with tasks (checkin forms are created through 
Android/iOS tracker applications). See [Task form actions](../task/form/index.md) to use forms with tasks.

<b>Form object structure</b>
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
    "created": "2017-03-15 12:36:27", //date when this form was created (or attached to the task). Read-only field
    "submit_in_zone": true, //if true, form can be submitted only in task zone
    "task_id": 1, //id of the task to which this form is attached
    "template_id": 1, //id of the form template on which this form is based. Can be null if template was deleted.
    "values": { //A map with field ids as keys and <field_value> objects as values. Can be null if form is not filled.
      "111-aaa-whatever": { //key is used to link field and its corresponding value
        "type": "text", //value type and field type must match
        "value": "John Doe" //the rest of value object is field type-specific
      },
      ...
    },
    "submitted": "2017-03-21 18:40:54", //date when form values were last submitted
    "submit_location": { //location at which form values were last submitted
      "lat": 11.0,
      "lng": 22.0,
      "address": "Wall Street, NY"
    }
}
```    

`<form_file>` is:

```js
{
    "id": 16, // file id
    "storage_id": 1,
    "user_id": 12203,
    "type": "image", // "image" or "file"
    "created": "2017-09-06 11:54:28", // date when file was created
    "uploaded": "2017-09-06 11:55:14", // date when file was uploaded, can be null if file is not yet uploaded
    "name": "lala.jpg", // filename
    "size": 72594, // in bytes. If file not uploaded, show maximum allowed size for upload
    "mime_type": "image/png",
    "metadata": nullable, <metadata_object>,
    "state": "uploaded", // can be "created", "in_progress", "uploaded", "deleted"
    "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg", // actual url at which file is available. Can be null if file is not yet uploaded
}
```

# API actions

API path: `/form`.

## read

Get form by an id.

#### parameters

| name | description | type | 
| :--- | :--- | :--- | 
| id | id of the form | int | 

#### example

    https://api.navixy.com/v2/form/read?hash=22eac1c27af4be7b9d04da2ce1af111b&id=132215

#### response
```js
{
    "success": true,
    "value": <form>, // marker on map (see below)
    "files": [<form_file>, ... ] //files used in values of this form. Can be null or empty.
}
```    

#### errors
* 201 – Not found in database (if there is no form with such an id)

## download

Download form as a file by an id.

#### parameters

| name | description | type | 
| :--- | :--- | :--- | 
| id | id of the form | int | 
| format | file format | "pdf" or "xlsx" | 

#### example

    https://api.navixy.com/v2/form/download?hash=22eac1c27af4be7b9d04da2ce1af111b&id=132215&format=pdf

#### response
Regular file download, or JSON with an error.    

#### errors
* 201 – Not found in database (if there is no form with such an id)

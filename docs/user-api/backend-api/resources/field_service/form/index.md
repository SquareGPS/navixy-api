---
title: About forms
description: Forms used to provide additional information, such as user's name, phone, delivery date, etc. upon task completion or check-in from iOS/Android mobile tracker app. Forms can be attached to tasks. If form attached to task, this task cannot be completed without form submission.
---

# About forms

Forms used to provide additional information, such as user's name, phone, delivery date, etc. upon task completion
or check-in from iOS/Android mobile tracker app.
Forms can be attached to tasks. If form attached to task, this task cannot be completed without form submission.

* Each form must be created from template, read more at [Templates](template.md)
* For description of `<form_field>` and `<field_value>`, see [Form fields and values](field-types.md)
* Using web API, it's now possible to only attach/fill forms with tasks (checkin forms are created through 
Android/iOS tracker applications). See [Task form actions](../task/form/index.md) to use forms with tasks.

Find comprehinsive information on forms usage in our [instructions](../../../guides/field-service-management/create-forms.md).

## Form object

```json
{
    "id": 2,
    "label": "Order form",
    "fields": [
      {
        "id": "111-aaa-whatever",
        "label": "Name",
        "description": "Your full name",
        "required": true,
        "min_length": 5,
        "max_length": 255,
        "type": "text"
      }
    ],
    "created": "2017-03-15 12:36:27",
    "submit_in_zone": true,
    "task_id": 1,
    "template_id": 1,
    "values": {
      "111-aaa-whatever": {
        "type": "text",
        "value": "John Doe"
      }
    },
    "submitted": "2017-03-21 18:40:54",
    "submit_location": {
      "lat": 11.0,
      "lng": 22.0,
      "address": "Wall Street, NY"
    }
}
```    

* `id` - int. Form unique ID.
* `label` - string. User-defined form label, from 1 to 100 characters.
* `fields` - array of multiple [form_field](field-types.md) objects. 
* `created` - [date/time](../../../getting-started/introduction.md#data-types). Date when this form created (or attached to the task). The read-only field.
* `submit_in_zone` - boolean. If `true`, form can be submitted only in task zone.
* `task_id` - int. An ID of the task to which this form attached.
* `template_id` - int. An ID of the form template on which this form based. Can be null if template deleted.
* `values` - a map with field IDs as keys and [field_value](field-types.md) objects as values. Can be null if form not filled.
    * `key` - string. Key used to link field and its corresponding value.
* `submitted` - [date/time](../../../getting-started/introduction.md#data-types). Date when form values last submitted.
* `submit_location` - location at which form values last submitted.


## Form file object

```json
{
    "id": 16,
    "storage_id": 1,
    "user_id": 12203,
    "type": "image",
    "created": "2017-09-06 11:54:28",
    "uploaded": "2017-09-06 11:55:14",
    "name": "lala.jpg",
    "size": 72594,
    "mime_type": "image/png",
    "metadata": <metadata_object>,
    "state": "uploaded",
    "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
}
```

* `id` - int. File ID.
* `type` - [enum](../../../getting-started/introduction.md#data-types). Can be "image" or "file".
* `created` - [date/time](../../../getting-started/introduction.md#data-types). Date when file created.
* `uploaded` - [date/time](../../../getting-started/introduction.md#data-types). Date when file uploaded. Can be null if file not yet uploaded.
* `name` - string. A filename.
* `size` - int. Size in bytes. If file not uploaded, show maximum allowed size for the upload.
* `metadata` - nullable metadata object.
* `state` - [enum](../../../getting-started/introduction.md#data-types). Can be "created" | "in_progress" | "uploaded" | "deleted".
* `download_url` - string. Actual URL at which file is available. Can be null if file not yet uploaded.


## API actions

API path: `/form`.

### `read`

Gets form by an ID.

#### Parameters

| name | description     | type  |
|:-----|:----------------|:------|
| id   | ID of the form. | int   |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 2}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/form/read?hash=a6aa75587e5c59c32d347da438505fc3&id=2
    ```

#### Response

```json
{
    "success": true,
    "value": {
         "id": 2,
         "label": "Order form",
         "fields": [
           {
             "id": "111-aaa-whatever",
             "label": "Name",
             "description": "Your full name",
             "required": true,
             "min_length": 5,
             "max_length": 255,
             "type": "text"
           }
         ],
         "created": "2017-03-15 12:36:27",
         "submit_in_zone": true,
         "task_id": 1,
         "template_id": 1,
         "values": {
           "111-aaa-whatever": {
             "type": "text",
             "value": "John Doe"
           }
         },
         "submitted": "2017-03-21 18:40:54",
         "submit_location": {
           "lat": 11.0,
           "lng": 22.0,
           "address": "Wall Street, NY"
         }
    },
    "files": [{
      "id": 16,
      "storage_id": 1,
      "user_id": 12203,
      "type": "image",
      "created": "2017-09-06 11:54:28",
      "uploaded": "2017-09-06 11:55:14",
      "name": "lala.jpg",
      "size": 72594,
      "mime_type": "image/png",
      "metadata": {
       "orientation":  1
      },
      "state": "uploaded",
      "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
    }]
}
``` 

* `value` - A [form object](#form-object).
* `files` - list of [form_file objects](#form-file-object). Files used in values of this form. Can be null or empty.

#### Errors

* 201 – Not found in the database - if there is no form with such an ID.


### `download`

Downloads form as a file by an ID.

#### Parameters

| name   | description                          | type                                           |
|:-------|:-------------------------------------|:-----------------------------------------------|
| id     | ID of the form.                      | int                                            |
| format | File format. Can be "pdf" or "xlsx". | [enum](../../../getting-started/introduction.md#data-types) |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/form/download' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "id": 2, "format": "pdf"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/form/download?hash=a6aa75587e5c59c32d347da438505fc3&id=2&format=pdf
    ```

#### Response

Regular file download, or JSON with an error.    

#### Errors

* 201 – Not found in the database - if there is no form with such an ID.

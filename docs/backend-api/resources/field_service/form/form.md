---
title: About forms
description: About forms
---

# About forms

Forms are used to provide additional information, such as user name, phone, delivery date, etc. upon task completion
or check-in from iOS/Android mobile tracker app.
Forms are attached to tasks. If form is attached to task, this task cannot be completed without form submission.

* Each form must be created from template, read more at [Templates](./template.md)
* For description of `<form_field>` and `<field_value>`, see [Form fields and values](./field-types.md)
* Using web API, it's now possible to only attach/fill forms with tasks (checkin forms are created through 
Android/iOS tracker applications). See [Task form actions](../task/form/form.md) to use forms with tasks.

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

---
title: Updating task form values
description: Updating task form values
---

# Updating task form values

API path: `/task/form/values`.

## update

Update existing form values of given task.

**required subuser rights**: task_update

##### parameters

* **task_id** - (int) task id
* **values** - (JSON object) map of field_id-value object

values object example

```js
{
    "111-aaa-whatever": {
      "type": "text",
      "value": "text field value"
    }
}
```

For **value** object description, see [form/form-fields-and-values/](../../form/field-types.md#form-fields-and-values).

#### return

```js
{
    "success": true
}
```

#### errors

*   101 – In demo mode this function is disabled (if current user has “demo” flag)
*   201 – Not found in database (if task with the specified id does not exist)
*   255 – Invalid task state (if task has already done or failed or no values was submitted)
*   242 – There were errors during content validation (if given values are invalid for the form). Example:

```js
{
    "success": false,
    "status": {
        "code": 242,
        "description": "There were errors during content validation"
    },
    "errors": [
        {
            "field_id": "111-aaa-whatever",
            "code": 5,
            "error": "text length constraints are not met"
        }
    ]
}
```

Validation error codes:

*   1 – field is required but has no value
*   2 – field value type doesn’t match field type
*   3 – field value is null
*   4 – value index out of bounds
*   5 – invalid value size
*   6 – value less than minimum
*   7 – value more than maximum
*   8 – field contains invalid references
*   9 – invalid file type
*   10 – invalid file state

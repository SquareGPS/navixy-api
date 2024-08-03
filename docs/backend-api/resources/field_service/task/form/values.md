---
title: Updating task form values
description: API call for updating task form values. Task form values can be submitted using web API only if there was a submission using Mobile Tracker App.
---

# Updating task form values

Task form values can only be submitted using the web API if there was a previous submission using the Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)). The purpose of this feature is to correct any incorrectly filled data that was accidentally submitted. It is not intended for filling out an empty form from scratch. This action can only be used if the task status is "assigned," and the device must not be deleted. It will not work for any other task statuses.


## API actions

API path: `/task/form/values`.

### `update`

Updates existing form values of given task.

**required sub-user rights**: `task_update`.

##### Parameters

| name    | description                   | type        |
|:--------|:------------------------------|:------------|
| task_id | An ID of the task.            | int         |
| values  | Map of field_id-value object. | JSON object |


where values object is:

```json
{
    "text1": {
      "type": "text",
      "value": "text field value"
    }
}
```

For **value** object description, see [form/form-fields-and-values/](../../form/field-types.md#form-fields-and-values).

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/form/values/update' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 12546, "value": {"text1": {"type": "text", "value": "text field value"}}}'
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 101 – In demo mode this function disabled - if current user has "demo" flag.
* 201 – Not found in the database - if task with the specified ID does not exist.
* 255 – Invalid task state - if task has already done or failed or no values submitted.
* 242 – There were errors during content validation - if given values are invalid for the form. Example:

```json
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

* 1 – field required but has no value.
* 2 – field value type doesn't match field type.
* 3 – field value is null.
* 4 – value index out of bounds.
* 5 – invalid value size.
* 6 – value less than minimum.
* 7 – value more than maximum.
* 8 – field contains invalid references.
* 9 – invalid file type.
* 10 – invalid file state.

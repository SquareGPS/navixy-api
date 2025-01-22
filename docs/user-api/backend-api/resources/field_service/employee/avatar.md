---
title: Changing avatar
description: API calls to assign and upload avatars. Avatars can't be changed through `/employee/update`, you must use either `assign` (to set avatar to one of preset icons), or `upload` (to upload your own image).
---

# Changing avatar

Avatars can't be changed through `/employee/update`, you must use either `assign` (to set avatar to one of preset icons),
or `upload` (to upload your own image). 


## API actions

API path: `/employee/avatar`.

### `assign`

Assign `icon_id` (from standard icon set) to this employee/driver. 
The `icon_id` can be `null` – this means that uploaded avatar should be used instead of icon.

**required sub-user rights**: `employee_update`.

#### Parameters

| name        | description                                             | type |
|:------------|:--------------------------------------------------------|:-----|
| employee_id | ID of the employee/driver to whom the icon will assign. | int  |
| icon_id     | ID of the icon.                                         | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/employee/avatar/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "employee_id": 2132, "icon_id": 3654}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/employee/avatar/assign?hash=a6aa75587e5c59c32d347da438505fc3&employee_id=2132&icon_id=3654
    ```

#### Response

```json
{ "success": true }
```
    
#### Errors

* 201 – Not found in the database - when employee/driver with `employee_id` not found.


### `upload`

Uploads avatar image for specified employee/driver.
Then it will be available from /employee/avatars/
e.g. `{{ extra.api_example_url }}/static/employee/avatars/abcdef123456789.png`.

**required sub-user rights**: `employee_update`.

**avatar_file_name** returned in response and will be returned from [/employee/list](index.md#list).

**MUST** be a POST multipart request (multipart/form-data),
with one of the parts being an image file upload (with the name `file`).

File part **mime** type must be one of:

* `image/jpeg`
* `image/pjpeg`
* `image/png`
* `image/gif`
* `image/webp`

#### Parameters

| name            | description                                                            | type   |
|:----------------|:-----------------------------------------------------------------------|:-------|
| employee_id     | ID of the employee/driver to whom the icon will assign.                | int    |
| file            | Image file.                                                            | string |
| redirect_target | Optional. URL to redirect. If passed returns redirect to `?response=`. | string |

#### Response

```json
{
    "success": true,
    "value": "picture.png"
}
```

* `value` - string. Uploaded file name.

#### Errors

* 201 – Not found in the database - when employee/driver with `employee_id` not found.
* 233 – No data file - if `file` part not passed.
* 234 – Invalid data format - if passed `file` with unexpected `mime` type.
* 254 – Cannot save file - on some file system errors.

---
title: Changing avatar
description: Changing avatar
---

# Changing avatar

Avatars are not changed through `/employee/update`, you must use either `assign` (to set avatar to one of preset icons),
or `upload` (to upload your own image). 

## API actions

API base path: `/employee/avatar`.

### assign

Assign `icon_id` (from standard icon set) to this employee. 
The `icon_id` can be `null` – this means that uploaded avatar should be used instead of icon.

**required subuser rights**: employee_update

#### parameters

*   `employee_id`
*   `icon_id`

#### response

```json
{ "success": true }
```
    

#### errors

*   201 – Not found in database (when employee with **employee_id** not found in db)


### upload

Upload avatar image for specified employee.
Then it will be available from /employee/avatars/
e.g. `{{ extra.api_example_url }}/static/employee/avatars/abcdef123456789.png`.

**required subuser rights**: `employee_update`

**avatar_file_name** returned in response and will be returned from [/employee/list](./index.md#list).

**MUST** be a POST multipart request (multipart/form-data),
with one of the parts being an image file upload (with the name `file`).

File part **mime** type must be one of:

*   **image/jpeg** or **image/pjpeg**
*   **image/png**
*   **image/gif**

#### parameters

*   **employee_id** – employee id
*   **file** – image file
*   **redirect_target** – (optional) URL to redirect
    If **redirect_target** passed return redirect to `?response=`

#### response

```json
{
    "success": true,
    "value": <string> // avatar file name
}
```

#### errors

*   201 – Not found in database (when employee with **employee_id** not found in db)
*   233 – No data file (if **file** part not passed)
*   234 – Invalid data format (if passed **file** with unexpected **mime** type)
*   254 – Cannot save file (on some file system errors)

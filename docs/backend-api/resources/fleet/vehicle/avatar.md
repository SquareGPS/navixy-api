---
title: Vehicle avatar
description: API calls to upload and assign avatar to the vehicle.
---

# Vehicle avatar

API calls to upload and assign avatar to the vehicle.

<hr>

## API actions

API path: `/vehicle/avatar`.

### assign

Assigns `icon_id` (from standard icon set) to specified vehicle.

**required sub-user rights**: `vehicle_update`

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| vehicle_id | Id of the vehicle.| int |
| icon_id | Id of the icon. | int |

`icon_id` can be null – this means that uploaded avatar should be used instead of icon.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/vehicle/avatar/assign' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "a6aa75587e5c59c32d347da438505fc3", "vehicle_id": 127722, "icon_id": 1342}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/vehicle/avatar/assign?hash=a6aa75587e5c59c32d347da438505fc3&vehicle_id=127722&icon_id=1342
    ```

##### response

```json
{ "success": true }
```

##### errors

* 201 – Not found in the database - when vehicle with `vehicle_id` not found.

<hr>

### upload

Uploads avatar image for specified vehicle.
Then it will be available from `[api_base_url]/<api_static_path>/vehicle/avatars/<file_name>`
e.g. `{{ extra.api_example_url }}/static/vehicle/avatars/abcdef123456789.png`.

**required sub-user rights**: `vehicle_update`

**avatar_file_name** returned in response and will be returned from [/vehicle/list](./index.md#list).

**MUST** be a POST multipart request (multipart/form-data),
with one of the parts being an image file upload (with the name "file").

File part **mime** type must be one of :

* **image/jpeg** or **image/pjpeg**
* **image/png**
* **image/gif**

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| tag_id | Tag id. | int |
| file | Image file. | string |
| redirect_target | Optional. URL to redirect. | string |

If `redirect_target` passed a return redirect to `response=<urlencoded response json>`.

#### response

```json
{
    "success": true,
    "value": "abcdef123456789.png"
}
```

* `value` - string. Avatar file name.

#### errors

* 201 – Not found in the database - when vehicle with `tag_id` not found.
* 233 – No data file - if `file` part not passed.
* 234 – Invalid data format - if passed `file` with unexpected **mime** type.
* 254 – Cannot save file - on some file system errors.

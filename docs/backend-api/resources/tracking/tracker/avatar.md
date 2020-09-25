---
title: Avatar for the tracker
description: Avatar for the tracker
---
# Avatar for the tracker

API base path: `/tracker/avatar`

### upload

Uploads avatar image for specified tracker.
Then it will be available from `{{ extra.api_example_url }}/[api_static_path]/tracker/avatars/<file_name>`
e.g. `{{ extra.api_example_url }}/static/tracker/avatars/abcdef123456789.png`.

**required sub-user rights:** `tracker_update`

**MUST** be a POST multipart request (multipart/form-data),
with one of the parts being an image file upload (with the name “file”).

File part **mime** type must be one of (see: [source:api-server/src/main/java/com/navixy/common/util/ImageFormats.java ImageFormats.IMAGE_FORMATS]):

* **image/jpeg** or **image/pjpeg**
* **image/png**
* **image/gif**

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| tracker_id | Id of the tracker (aka “object_id”). Tracker must belong to authorized user and not be blocked. | int |
| file | image file. | string |
| redirect_target | (optional) URL to redirect If redirect_target passed return redirect to ?response=. | URL |

#### response

```json
{
    "success": true,
    "value": "file name"
}
```

* `value` - avatar file name.

#### errors

* 201 – Not found in the database (when tracker with a tracker_id not found in the database).
* 208 – Device blocked.
* 233 – No data file (if file part not passed).
* 234 – Invalid data format (if passed file with unexpected mime type).
* 254 – Cannot save file (on some file system errors).

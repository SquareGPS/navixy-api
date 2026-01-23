---
title: Avatar for the tracker
description: Contains API call to upload avatar for the tracker.
---

# Avatar for the tracker

## API actions

API base path: `/tracker/avatar`.

### upload

Uploads avatar image for specified tracker. \
Then it will be available from `https://api.eu.navixy.com/v2/[api_static_path]/tracker/avatars/<file_name>`\
e.g. `https://api.eu.navixy.com/v2/static/tracker/avatars/abcdef123456789.png`.

**required sub-user rights:** `tracker_update`.

**MUST** be a POST multipart request (multipart/form-data),\
with one of the parts being an image file upload (with the name "file").

File part **mime** type must be one of (see: \[source:api-server/src/main/java/com/navixy/common/util/ImageFormats.java ImageFormats.IMAGE\_FORMATS]):

* `image/jpeg`
* `image/pjpeg`
* `image/png`
* `image/gif`
* `image/webp`

#### Parameters

| name             | description                                                                                      | type   |
| ---------------- | ------------------------------------------------------------------------------------------------ | ------ |
| tracker\_id      | ID of the tracker (aka "object\_id"). Tracker must belong to authorized user and not be blocked. | int    |
| file             | image file.                                                                                      | string |
| redirect\_target | Optional. URL to redirect If `redirect_target` passed return redirect to `?response=`.           | URL    |

#### Response

```json
{
  "success": true,
  "value": "file name"
}
```

* `value` - avatar file name.

#### Errors

* 201 – Not found in the database - when tracker with a `tracker_id` not found in the database.
* 208 – Device blocked.
* 233 – No data file - if file part not passed.
* 234 – Invalid data format - if passed file with unexpected mime type.
* 254 – Cannot save file - on some file system errors.

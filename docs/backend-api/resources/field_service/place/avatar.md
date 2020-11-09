---
title: Changing avatar
description: Changing avatar
---

# Changing place avatar

Avatars are not changed through `/place/update`, you must use either `assign` (to set avatar to one of preset icons),
or `upload` (to upload your own image). 

## API actions

API path: `/place/avatar`.

### upload

Upload avatar image for specified place.

**required subuser rights:** place_update

Then it will be available from `[api_base_url]/<api_static_uri>/place/avatars/<file_name>`
e.g. `{{ extra.api_example_url }}/static/place/avatars/abcdef123456789.png`.

**avatar_file_name** returned in response and will be returned from [place/list](./index.md#list).

**MUST** be a POST multipart request (multipart/form-data),
with one of the parts being an image file upload (with the name "file").

File part **mime** type must be one of:

* _image/jpeg_ or _image/pjpeg_
* _image/png_
* _image/gif_

#### parameters
name | description | type
--- | --- | ---
place_id | ID of the place | int
file | image file | File upload
redirect_target | (optional) URL to redirect. If **redirect_target** passed return redirect to `<redirect_target>?response=<urlencoded_response_json>` | String

#### response
```json
{
    "success": true,
    "value": <string> // avatar file name
}
```

#### errors

* 201 (Not found in database) – when place with place_id not found in db
* 233 (No data file) – if file part not passed
* 234 (Invalid data format) – if passed file with unexpected mime type
* 254 (Cannot save file) – on some file system errors

### assign
Assign icon_id (from standard icon set) to this place. Icon_id can be null – this means that uploaded avatar should be used instead of icon.

**required subuser rights:** place_update

#### parameters
name | description | type
--- | --- | ---
place_id | ID of the place | int
icon_id | optional, ID of the icon from standard icon set | int

#### response
```json
{ "success": true }
```

#### errors

* 201 (Not found in database) – when place with place_id not found in db

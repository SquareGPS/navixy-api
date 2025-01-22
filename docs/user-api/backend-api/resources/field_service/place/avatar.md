---
title: Changing POI avatar
description: API calls to upload and assign avatars for POIs. Avatars don't change through `/place/update`, you must use either `assign` (to set avatar to one of preset icons), or `upload` (to upload your own image).
---

# Changing POI avatar

Avatars don't change through `/place/update`, you must use either `assign` (to set avatar to one of preset icons),
or `upload` (to upload your own image). 


## API actions

#### upload

Uploads avatar image for specified POI.

**required sub-user rights:** `place_update`.

Then it will be available from `[api_base_url]/<api_static_uri>/place/avatars/<file_name>`
e.g. `{{ extra.api_example_url }}/static/place/avatars/abcdef123456789.png`.

**avatar_file_name** returned in response and will be returned from [place/list](index.md#list).

**MUST** be a POST multipart request (multipart/form-data),
with one of the parts being an image file upload (with the name "file").

File part **mime** type must be one of:

* `image/jpeg`
* `image/pjpeg`
* `image/png`
* `image/gif`
* `image/webp`

##### Parameters

| name            | description                                                                                                                         | type        |
|:----------------|:------------------------------------------------------------------------------------------------------------------------------------|:------------|
| place_id        | ID of the POI.                                                                                                                      | int         |
| file            | Image file.                                                                                                                         | File upload |
| redirect_target | Optional URL to redirect. If **redirect_target** passed return redirect to `<redirect_target>?response=<urlencoded_response_json>`. | string      |

##### Response

```json
{
    "success": true,
    "value": "Avatar file name"
}
```

* `value` - string. Avatar file name.

#### Errors

* 201 - Not found in the database – when POI with place_id not found.
* 233 - No data file – if file part not passed.
* 234 - Invalid data format – if passed file with unexpected mime type.
* 254 - Cannot save file – on some file system errors.


### `assign`

Assigns `icon_id` (from standard icon set) to this POI. `icon_id` can be null – this means that uploaded avatar should
 be used instead of icon.

**required sub-user rights:** `place_update`.

#### Parameters

| name     | description                                      | type |
|:---------|:-------------------------------------------------|:-----|
| place_id | ID of the POI.                                   | int  |
| icon_id  | Optional. ID of the icon from standard icon set. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/place/avatar/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place_id": 122304, "icon_id": 1}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/place/avatar/assign?hash=a6aa75587e5c59c32d347da438505fc3&place_id=122304&icon_id=1
    ```

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – when POI with `place_id` not found.

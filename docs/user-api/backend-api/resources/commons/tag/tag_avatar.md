---
title: Tag avatar
description: Contains API calls to interact with tag avatars.
---

# Tag avatar

Contains API calls to interact with tag avatars.


## API actions

API path: `/tag/avatar`.

### `assign`

Assigns icon_id (from standard icon set) to specified tag.

**required sub-user rights**: `tag_update`.

#### Parameters

| name    | description                                                                                          | type |
|:--------|:-----------------------------------------------------------------------------------------------------|:-----|
| tag_id  | ID of the tag to assign.                                                                             | int  |
| icon_id | Icon to assign to tag. Can be null – this means that uploaded avatar should be used instead of icon. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/tag/avatar/assign' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tag_id": 1, "icon_id": 14}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/tag/avatar/assign?hash=a6aa75587e5c59c32d347da438505fc3&tag_id=1&icon_id=14
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 201 – Not found in the database - when vehicle with specified `tag_id` not found.


### `upload`

Uploads avatar image for specified tag.<br>
Then it will be available from `[api_base_url]/[api_static_path]/tag/avatars/<file_name>`<br>
e.g. `{{ extra.api_example_url }}/static/tag/avatars/abcdef123456789.png`.

**required sub-user rights**: `tag_update`.

**avatar_file_name** returned in response and will be returned from [/tag/list](index.md#list).

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being an image file upload (with the name `file`).

File part **mime** type must be one of:

* `image/jpeg`
* `image/pjpeg`
* `image/png`
* `image/gif`
* `image/webp`

#### Parameters

| name            | description                                                                                                                       |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------|
| tag_id          | ID of the tag to upload.                                                                                                          |
| file            | Image file.                                                                                                                       |
| redirect_target | Optional. URL to redirect. If `redirect_target` passed return redirect to `<redirect_target>?response=<urlencoded response json>` |

#### Response

```json
{
    "success": true,
    "value": "avatar.jpg"
}
```

* `value` - string. Avatar file name.

#### Errors

* 201 – Not found in the database - when tag with specified `tag_id` not found.
* 233 – No data file - if `file` part not passed.
* 234 – Invalid data format - if passed `file` with unexpected `mime` type.
* 254 – Cannot save file - on some file system errors.
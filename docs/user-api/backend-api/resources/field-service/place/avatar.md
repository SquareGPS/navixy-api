---
title: Changing POI avatar
description: API calls to upload and assign avatars for POIs.
---

# Changing POI avatar

Avatars don't change through `/place/update`, you must use either `assign` (to set avatar to one of preset icons), or `upload` (to upload your own image).

## API actions

#### upload

Uploads avatar image for specified POI.

**required sub-user rights:** `place_update`.

Then it will be available from `[api_base_url]/<api_static_uri>/place/avatars/<file_name>`\
e.g. `https://api.eu.navixy.com/v2/static/place/avatars/abcdef123456789.png`.

**avatar\_file\_name** returned in response and will be returned from [place/list](work-with-poi.md#list).

**MUST** be a POST multipart request (multipart/form-data),\
with one of the parts being an image file upload (with the name "file").

File part **mime** type must be one of:

* `image/jpeg`
* `image/pjpeg`
* `image/png`
* `image/gif`
* `image/webp`

**Parameters**

| name             | description                                                                                                                          | type        |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| place\_id        | ID of the POI.                                                                                                                       | int         |
| file             | Image file.                                                                                                                          | File upload |
| redirect\_target | Optional URL to redirect. If **redirect\_target** passed return redirect to `<redirect_target>?response=<urlencoded_response_json>`. | string      |

**Response**

```json
{
    "success": true,
    "value": "Avatar file name"
}
```

* `value` - string. Avatar file name.

#### Errors

* 201 - Not found in the database – when POI with place\_id not found.
* 233 - No data file – if file part not passed.
* 234 - Invalid data format – if passed file with unexpected mime type.
* 254 - Cannot save file – on some file system errors.

### assign

Assigns `icon_id` (from standard icon set) to this POI. `icon_id` can be null – this means that uploaded avatar should\
be used instead of icon.

**required sub-user rights:** `place_update`.

#### Parameters

| name      | description                                      | type |
| --------- | ------------------------------------------------ | ---- |
| place\_id | ID of the POI.                                   | int  |
| icon\_id  | Optional. ID of the icon from standard icon set. | int  |

#### Examples

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}
```sh
curl -X POST 'https://api.eu.navixy.com/v2/place/avatar/assign' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "place_id": 122304, "icon_id": 1}'
```
{% endcode %}
{% endtab %}

{% tab title="HTTP GET" %}
{% code overflow="wrap" %}
```http
https://api.eu.navixy.com/v2/place/avatar/assign?hash=a6aa75587e5c59c32d347da438505fc3&place_id=122304&icon_id=1
```
{% endcode %}
{% endtab %}
{% endtabs %}

#### Response

```json
{ "success": true }
```

#### Errors

* 201 - Not found in the database – when POI with `place_id` not found.

---
title: Image
description: API calls for interaction with images that used for branding of the panel.
---

# Image

API calls for interaction with images that used for branding of the panel.

***

## API actions

API path: `panel/dealer/settings/image`.

### delete 

Deletes an image of specified `type`. 

*required permissions*: `service_settings: "update"`.

#### parameters

| name | description | type|
| :------ | :------ | :----- |
| type | Image type to delete. Can be one of `logo`, `favicon`, `login_wallpaper`, `desktop_wallpaper`, `document_logo`. | string |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/dealer/settings/image/delete' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "fa7bf873fab9333144e171372a321b06", "type": "logo"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/dealer/settings/image/delete?hash=fa7bf873fab9333144e171372a321b06&type=logo
    ```

#### response

```json
{
    "success": true
}
```
    
#### errors

* 201 - Not found in the database - when there are no settings for a dealer in the db.

***

### upload

Uploads image of specified `type`. 

**MUST** be a POST multipart request (multipart/form-data), 
with one of the parts being an image file upload (with the name "file"). 

File part **mime** type must be one of:

* `image/jpeg`
* `image/pjpeg`
* `image/png`
* `image/gif`
* `image/webp`
* `image/x-icon` (for favicon type)

*required permissions*: `service_settings: "update"`.

#### parameters


| name | description | type|
| :------ | :------ | :----- |
| type | Image type to delete. Can be one of `logo`, `favicon`, `login_wallpaper`, `desktop_wallpaper`, `document_logo`. | string |
| file | Image file. | string |
| redirect_target | Optional. An URL to redirect. | string | 

If `redirect_target` passed a return redirect to `response=<urlencoded response json>`.

#### response

```json
{
    "success": true
}
```    

#### errors

* 201 - Not found in the database - when there are no settings for dealer in the db.
* 233 - No data file - if `file` part not passed.
* 234 - Invalid data format - if passed `file` with unexpected `mime` type.
* 236 - Feature unavailable due to tariff restrictions - if branding feature disabled for this dealer.
* 254 - Cannot save file - on some file system errors.

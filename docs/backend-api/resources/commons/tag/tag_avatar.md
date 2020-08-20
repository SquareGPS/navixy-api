---
title: Tag avatar
description: Tag avatar
---

# Tag avatar

API path: `/tag/avatar`.


### assign

**required subuser rights**: tag_update

#### parameters

* **tag_id**
* **icon_id**

Assign icon_id (from standard icon set) to this tag. Icon_id can be null – this means that uploaded avatar should be used instead of icon.

#### return

```js
{
    "success": true
}
```

#### errors

* 201 – Not found in database (when vehicle with **tag_id** not found in db)



### upload

Upload avatar image for specified tag.<br>
Then it will be available from `<api_url>/<api.static.uri>/tag/avatars/<file_name>`<br>
e.g. `http://saas.navixy.com/api-v2/static/tag/avatars/abcdef123456789.png`.

**required subuser rights**: tag_update

**avatar_file_name** returned in response and will be returned from [/tag/list](index.md#list).

**MUST** be a POST multipart request (multipart/form-data), with one of the parts being an image file upload (with the name 'file').

File part **mime** type must be one of:

*   **image/jpeg** or **image/pjpeg**
*   **image/png**
*   **image/gif**

#### parameters

*   **tag_id** – tag id
*   **file** – image file
*   **redirect_target** – (optional) URL to redirect. If **redirect_target** passed return redirect to `<redirect_target>?response=<urlencoded response json>`

#### return

```js
{
    "success": true,
    "value": <string> // avatar file name
}
```

#### errors

Here is the list of errors that might occurred:

*   201 – Not found in database (when tag with **tag_id** not found in db)
*   233 – No data file (if **file** part not passed)
*   234 – Invalid data format (if passed **file** with unexpected **mime** type)
*   254 – Cannot save file (on some file system errors)

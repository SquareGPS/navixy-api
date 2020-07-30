---
title: /image
description: /image
---

## delete ()

Delete image of specified **type**. 

#### required permissions: 
* **service_settings**: "update"

#### parameters
* **type** - **string**. image type. one of: **logo**, **favicon**, **login_wallpaper**, **desktop_wallpaper**, **document_logo**

#### return

    { "success": true }
    
    
#### errors
* 201 - Not found in database (when there are no settings for dealer in db)

## upload()

Upload image of specified **type**. 

**MUST** be a POST multipart request (multipart/form-data), 
with one of the parts being an image file upload (with the name "file"). 

File part **mime** type must be one of :

* **image/jpeg** or **image/pjpeg**
* **image/png**
* **image/gif**
* **image/x-icon** (for favicon type)

#### required permissions:

* **service_settings**: “update”

#### parameters

* **type** – **string**. image type. one of: **logo**, **favicon**, **login_wallpaper**, **desktop_wallpaper**
* **file** – image file
* **redirect_target** – **string** (optional). URL to redirect

If **redirect_target** passed return redirect to ?response=

#### return

    { "success": true }
    

#### errors

* 201 - Not found in database (when there are no settings for dealer in db)
* 233 - No data file (if **file** part not passed)
* 234 - Invalid data format (if passed **file** with unexpected **mime** type)
* 236 - Feature unavailable due to tariff restrictions (if branding is disabled for this dealer)
* 254 - Cannot save file (on some file system errors)

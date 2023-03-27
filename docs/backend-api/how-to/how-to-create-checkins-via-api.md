---
title: How to create check-ins via API
description: How to create check-ins via API
---
!!! note "Important"
    Check-ins are created using X-GPS Tracker. 
    All the description below is necessary only for exceptional cases, such as creating your Mobile Tracker app.

Step 1. Create a form from a template with [checkin/form/create](../resources/field_service/checkin.md#formcreate)
API call. 
In the X-GPS Tracker, the form is created when the template is selected by a user.

Step 2. Create files for photos of check-in with [checkin/image/create](../resources/field_service/checkin.md#imagecreate) and upload photo data (see [How to upload file data](../resources/field_service/task/form/file.md#how-to-upload-file-data)). 
In the X-GPS Tracker, checkin photos are created as each photo is added.

Step 3. Create form files with [checkin/form/file](../resources/field_service/checkin.md#formfilecreate) API call and upload their data (see [How to upload file data](../resources/field_service/task/form/file.md#how-to-upload-file-data)). 
In the X-GPS Tracker, form files are created when they are added when the form is filled out.

Step 4. Create a check-in itself with [checkin/create](../resources/field_service/checkin.md#create) API call, where all the data is attached.

---
title: Task form file
description: Task form file
---

# Task form file

API path: `/task/form/file`.

Contains API calls which manipulate files attached to form’s fields.



## create()

Create a new file entry associated with form’s field. By making this call you basically “request permission” to upload a file. In return you are provided with upload credentials (url, form fields, etc.).<br>
Note that in order to actually “include” file as form field’s value, creating and uploading file is not enough. You must then submit a form with file id as a value of corresponding form field.

If file was created but was not uploaded, it will be deleted after date/time specified in “expires” response field. If file was uploaded but was not included as form field’s value, it will be deleted on next form submission.

**required subuser rights**: task_update

#### parameters

* **task_id** - (int) ID of the task to which form is attached.
* **field_id** - (String) ID of the form’s field to which a new file should be attached.
* **size** - (int) Maximum size in bytes for the file which will be uploaded. This is needed to “reserve” the space for file in user’s disk space quota.
* **filename** - (String?) Optional. If specified, uploaded file will have the specified name. If not, name will be taken from actual file upload form.
* **metadata** - (JSON object?) Optional.metadata object.

#### return

```js
{
  "success": true,
  "value": {
    "file_id": 111, //this value will be submited as form's field value
    "url": "http://bla.org/bla", //an url to which POST form-data with file contents should be executed
    "expires": "2016-02-03 03:04:00", //after this date file record wil expire and upload requests will be rejected
    "file_field_name": "file", //name for file field in POST upload request
    "fields": { //these fields should be passed as addational fields in POST upload request, field with file must be the last one
      "token": "wewerwerwerwerwerwerwewerwe" //used for authentication of upload
    }
  }
}
```

#### errors

*   201 – Not found in database (if there is no task with such id, or task doesn’t have form, or form has no field with such field_id)
*   231 – Entity type mismatch (if form field is not file-based, i.e. doesn’t use file id as its value)
*   255 – Invalid task state (if current task state is not “unassigned”, “assigned” or “arrived”, or if task’s form was not submitted at least once)
*   267 – Too many entities (if there’s 6 or more unsubmitted files already associated with this form’s field)
*   268 – File cannot be create due to quota violation
*   271 - File size is larger than the maximum allowed (by default 16 MB) 

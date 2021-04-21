---
title: Attaching files
description: Attaching files
---

# Attaching files

When submitting form values of type [file](../../form/field-types.md#file), [photo](../../form/field-types.md#photo) or
[signature](../../form/field-types.md#signature), you need to provide file id. To obtain it, first you [create](#create) 
a file entry, then upload a file using provided credentials. File must adhere to limitations specified in the form field.
Note that each file consumes space and contributes to file storage limit associated with user's account.

## API actions

API path: `/task/form/file`.

Contains API calls which manipulate files attached to form's fields.

### create

Creates a new file entry associated with form's field. By making this call you basically "request permission" to upload
 a file. In return, you are provided with upload credentials (url, form fields, etc.).<br>
Note that in order to actually "include" file as form field's value, creating and uploading file is not enough.
 You must then submit a form with file id as a value of corresponding form field.

If file created but not uploaded, it will be deleted after date/time specified in "expires" response field.
 If file uploaded but not included as form field's value, it will be deleted on next form submission.

**required sub-user rights**: `task_update`.

#### parameters

| name | description | type |
| :--- | :--- | :--- |
| task_id | ID of the task to which form attached. | int |
| field_id | ID of the form's field to which a new file should be attached. | string |
| size | Maximum size in bytes for the file which will be uploaded. This is needed to "reserve" the space for a file in user's disk space quota. | int |
| filename | Optional. If specified, uploaded file will have the specified name. If not, name will be taken from actual file upload form. | string |
| metadata | Optional. Metadata object (for images only). | JSON object |

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/task/form/file' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "task_id": 11231, "field_id": "file1", "size": 10}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/task/form/file?hash=a6aa75587e5c59c32d347da438505fc3&task_id=11231&field_id=file1&size=10
    ```

#### response

```json
{
  "success": true,
  "value": {
    "file_id": 111,
    "url": "http://bla.org/bla",
    "expires": "2020-02-03 03:04:00",
    "file_field_name": "file1",
    "fields": {
      "token": "a43f43ed4340b86c808ac"
    }
  }
}
```

* `file_id` - int. This value will be submitted as form's field value.
* `url` - string. An url to which POST form-data with file contents should be executed.
* `expires` - date/time. After this date file record wil expire and upload requests will be rejected.
* `file_field_name` - string. Name for file field in POST upload request.
* `fields` - these fields should be passed as additional fields in POST multipart upload request, field with a file 
must be the last one.
* `token` - string. Used for authentication of upload.

Here's an example of upload you must make after receiving such response (assuming you uploading image named `actual_file_name.png`):

```  
POST /bla HTTP/1.1
Host: bla.org
Content-Length: 1325
Origin: http://bla.org
... other headers ...
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryePkpFF7tjBAqx29L

------WebKitFormBoundaryePkpFF7tjBAqx29L
Content-Disposition: form-data; name="token"

a43f43ed4340b86c808ac
------WebKitFormBoundaryePkpFF7tjBAqx29L
Content-Disposition: form-data; name="file"; filename="actual_file_name.png"
Content-Type: image/png

... contents of file goes here ...
------WebKitFormBoundaryePkpFF7tjBAqx29L--
```

#### errors

* 201 – Not found in the database - if there is no task with such an id, or task doesn't have form, or form has no
 field with such a field_id.
* 231 – Entity type mismatch - if form field is not file-based, i.e. doesn't use file id as its value.
* 255 – Invalid task state - if current task state is not "unassigned", "assigned" or "arrived", or if task's form 
not submitted at least once.
* 267 – Too many entities - if there 6 or more unsubmitted files already associated with this form's field.
* 268 – File cannot be created due to quota violation.
* 271 - File size is larger than the maximum allowed (by default 16 MB).

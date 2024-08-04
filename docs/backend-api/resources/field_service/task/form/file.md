---
title: Attaching files
description: Contains API calls which manipulate files attached to form's fields.
---

# Attaching files

When submitting form values of type [file](../../form/field-types.md#file), [photo](../../form/field-types.md#photo) or
[signature](../../form/field-types.md#signature), you need to provide file ID. To obtain it, first you [create](#create) 
a file entry, then upload a file using provided credentials. File must adhere to limitations specified in the form field.
Note that each file consumes space and contributes to file storage limit associated with user's account.


## API actions

API path: `/task/form/file`.

### `create`

Creates a new file entry associated with form's field. By making this call you basically "request permission" to upload
 a file. In return, you are provided with upload credentials (URL, form fields, etc.).<br>
Note that in order to actually "include" file as form field's value, creating and uploading file is not enough.
 You must then submit a form with file ID as a value of corresponding form field.

If file created but not uploaded, it will be deleted after date/time specified in "expires" response field.
 If file uploaded but not included as form field's value, it will be deleted on next form submission.

**required sub-user rights**: `task_update`.

#### Parameters

| name     | description                                                                                                                             | type        |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------|:------------|
| task_id  | ID of the task to which form attached.                                                                                                  | int         |
| field_id | ID of the form's field to which a new file should be attached.                                                                          | string      |
| size     | Maximum size in bytes for the file which will be uploaded. This is needed to "reserve" the space for a file in user's disk space quota. | int         |
| filename | Optional. If specified, uploaded file will have the specified name. If not, name will be taken from actual file upload form.            | string      |
| metadata | Optional. Metadata object (for images only).                                                                                            | JSON object |

#### Examples

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

#### Response

when using internal storage:
```json
{
  "success": true,
  "value": {
    "file_id": 111,
    "url": "http://bla.org/bla",
    "expires": "2020-02-03 03:04:00",
    "file_field_name": "file",
    "fields": {
      "token": "a43f43ed4340b86c808ac"
    }
  }
}
```

when using the Amazon S3:
```json
{
  "success": true,
  "value": {
    "file_id": 111,
    "url": "https://bla.s3.amazonaws.com/",
    "expires": "2020-02-03 03:04:00",
    "file_field_name": "file",
    "fields": {
      "policy": "<Base64-encoded policy string>",
      "key": "user/user1/${filename}",
      "success_action_status": "200",
      "x-amz-algorithm": "AWS4-HMAC-SHA256",
      "x-amz-credential": "AKIAIOSFODNN7EXAMPLE/20151229/us-east-1/s3/aws4_request",
      "x-amz-date": "20151229T000000Z",
      "x-amz-signature": "<signature-value>",
      "x-amz-server-side-encryption": "AES256",
      "content-type": "image/png"
    }
  }
}
```

* `file_id` - int. This value will be submitted as form's field value.
* `url` - string. A URL to which POST form-data with file contents should be executed.
* `expires` - date/time. After this date file record wil expire and upload requests will be rejected.
* `file_field_name` - string. Name for file field in POST upload request.
* `fields` - these fields should be passed as additional fields in POST multipart upload request, field with a file 
must be the last one.

#### How to upload file data

Here's an example of upload you must make after receiving such response (assuming you uploading image named `actual_file_name.png`):

Internal storage example:
```http
POST /bla HTTP/1.1
Host: bla.org
Content-Length: 1325
Origin: http://bla.org
... other headers ...
Content-Type: multipart/form-data; boundary=WebAppBoundary

--WebAppBoundary
Content-Disposition: form-data; name="token"

a43f43ed4340b86c808ac
--WebAppBoundary
Content-Disposition: form-data; name="file"; filename="actual_file_name.png"
Content-Type: image/png

... contents of file goes here ...
--WebAppBoundary--
```

Amazon S3 example:
```http
POST / HTTP/1.1
Host:  https://bla.s3.amazonaws.com
Content-Length: 1972
Origin: https://bla.s3.amazonaws.com/
... other headers ...
Content-Type: multipart/form-data; boundary=WebAppBoundary

--WebAppBoundary
Content-Disposition: form-data; name="policy"
Content-Type: text/plain

eyJleHBpcmF0aW9uIjogIjIwMjMtMDMtMjdUMjE6MTU6MzYuMDczWiIsImNvbmRpdGlvbnMiOiNbeyJidWNrZXQiOiAibmF2aXh5LWZpbGVzLXRlc3QtZXUifSxbInN0YXJ0cy13aXRoIiwgIiRrZXkiLCAiIl0seyJzdWNjZXNzX2FjdGlvbl9zdGF0dXMiOiAiMjAwIn0seyJ4LWFtei1hbGdvcml0aG0iOiAiQVdTNC1ITUFDLVNIQTI1NiJ9LHsieC1hbXotY3JlZGVudGlhbCI6ICJBS0lBSUJRNlNSQjY1RVZTU1JNQS8yMDIzMDMyNy9ldS1jZW50cmFsLTEvczMvYXdzNF9yZXF1ZXN0In0seyJ4LWFtei1kYXRlIjogIjIwMjMwMzI3VDIxMDAzNloifSx7IngtYW16LXNlcnZlci1zaWRlLWVuY3J5cHRpb24iOiAiQUVTMjU2In1dfQ==
--WebAppBoundary
Content-Disposition: form-data; name="key"
Content-Type: text/plain

nj9relv6m52qp01t0wv47wyk1ozd309g/${filename}
--WebAppBoundary
Content-Disposition: form-data; name="success_action_status"
Content-Type: text/plain

200
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-algorithm"
Content-Type: text/plain

AWS4-HMAC-SHA256
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-credential"
Content-Type: text/plain

AKIAIBQ6SRB65EVSSRMA/20230327/eu-central-1/s3/aws4_request
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-date"
Content-Type: text/plain

20230327T210036Z
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-signature"
Content-Type: text/plain

2df7efa0c0e0c5b97d0d9483acd77c9ec37360df921b019a4c4a93180a6136ad
--WebAppBoundary
Content-Disposition: form-data; name="x-amz-server-side-encryption"
Content-Type: text/plain

AES256
--WebAppBoundary
Content-Disposition: form-data; name="file"; filename="actual_file_name.png"
Content-Type: image/png

... contents of file goes here ...
--WebAppBoundary--
```

#### Errors

* 201 – Not found in the database - if there is no task with such an ID, or task doesn't have form, or form has no
 field with such a field_id.
* 231 – Entity type mismatch - if form field is not file-based, i.e. doesn't use file ID as its value.
* 255 – Invalid task state - if current task state is not "unassigned", "assigned" or "arrived", or if task's form 
not submitted at least once.
* 267 – Too many entities - if there are 6 or more unsubmitted files already associated with this form's field.
* 268 – File cannot be created due to quota violation.
* 271 - File size is larger than the maximum allowed (by default 16 MB).

---
title: Check-ins
description: API actions to interact with check-ins
---

# Check-ins

Here's the corrected version:

---

Check-ins are created using the Mobile Tracker App ([Android](https://play.google.com/store/apps/details?id=com.navixy.xgps.tracker&hl=ru) / [iOS](https://apps.apple.com/us/app/x-gps-tracker/id802887190)). They contain date/time, address, coordinates, and additional information (comment, photo, filled form) provided by the app user after pressing "Check-in" in the tracker app. 

Using check-ins, field personnel can provide real-time information to their HQ while on site. For example, they can provide photo proof of work completed or notify about a malfunction, along with a filled form describing the issue.

Check-ins cannot be created using the web API ([create](#create) is needed for exceptional cases and described in the [guide](../../guides/field-service-management/check-ins.md)), so all actions are read-only.


## Check-in object

```json
{
    "id": 1,
    "marker_time": "2017-03-15 12:36:27",
    "user_id": 111,
    "tracker_id": 222,
    "employee_id": 333,
    "location": {
        "lat": 53.787154,
        "lng": 9.757980,
        "address": "Moltkestrasse 32",
        "precision": 150
    },
    "comment": "houston, we have a problem",
    "files": [{
        "id": 16,
        "storage_id": 1,
        "user_id": 12203,
        "type": "image",
        "created": "2017-09-06 11:54:28",
        "uploaded": "2017-09-06 11:55:14",
        "name": "lala.jpg",
        "size": 72594,
        "mime_type": "image/png",
        "metadata": {
          "orientation": 1
        },
        "state": "uploaded",
        "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
    }],
    "form_id": 23423,
    "form_label": "Service request form"
}
```    

* `id` - int. An ID of a check-in.
* `marker_time` - [date/time](../../getting-started/introduction.md#data-types). Non-null. The time of check-in creation.
* `user_id` - int. Non-null. An ID of the master user.
* `tracker_id` - int. Non-null. An ID of the tracker which created this check-in.
* `employee_id` - optional int. An ID of the employee assigned to the tracker.
* `location` - non-null object. Location associated with this check-in marker.
    * `address` - string. Address of the location.
* `comment` - optional string. A comment provided by app user.
* `files` - list of <check-in_file> objects. Non-null. May be empty.
    * `id` - int. File ID.
    * `storage_id` - int. Storage ID.
    * `user_id` - int. An ID of the user.
    * `type` - [enum](../../getting-started/introduction.md#data-types). Can be "image" | "file".
    * `created` - [date/time](../../getting-started/introduction.md#data-types). Date when file created.
    * `uploaded` - [date/time](../../getting-started/introduction.md#data-types). Date when file uploaded, can be null if file not yet uploaded.
    * `name` - string. A name of the file.
    * `size` int. File size in bytes. If file not uploaded, show maximum allowed size for an upload.
    * `metadata` - metadata object. 
        * `orientation` - int. Image exif orientation.
    * `state` - [enum](../../getting-started/introduction.md#data-types). Can be "created" | "in_progress" | "uploaded" | "deleted".
    * `download_url` - string. Actual URL at which file is available. Can be null if file not yet uploaded.
* `form_id` - int. An ID of the form which was sent along with a check-in, can be null.
* `form_label` - string. Label of the form which was sent along with a check-in, can be null.


## API actions

API path: `/checkin`.

### `read`

Get check-in which ID is equal to `checkin_id`.
 
**required sub-user rights:** `employee_update`.

#### Parameters

| name       | description               | type |
|:-----------|:--------------------------|:-----|
| checkin_id | ID of the check-in entry. | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkin_id": 1}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/checkin/read?hash=a6aa75587e5c59c32d347da438505fc3&checkin_id=1
    ```

#### Response

```json
{
    "success": true,
    "value": {
        "id": 1,
        "marker_time": "2017-03-15 12:36:27",
        "user_id": 111,
        "tracker_id": 222,
        "employee_id": 333,
        "location": {
         "lat": 53.787154, 
         "lng": 9.757980,
         "address": "Moltkestrasse 32",
         "precision": 150
        },
        "comment": "houston, we have a problem",
        "files": [{
         "id": 16,
         "storage_id": 1,
         "user_id": 12203,
         "type": "image",
         "created": "2017-09-06 11:54:28",
         "uploaded": "2017-09-06 11:55:14",
         "name": "lala.jpg",
         "size": 72594,
         "mime_type": "image/png",
         "metadata": {
           "orientation": 1
         },
         "state": "uploaded",
         "download_url": "https://static.navixy.com/file/dl/1/0/1g/01gw2j5q7nm4r92dytolzd6koxy9e38v.png/lala.jpg"
        }],
        "form_id": 23423,
        "form_label": "Service request form"
    }
}
```

#### Errors

* 7 – Invalid parameters.
* 204 – Entity not found – when the marker entry is not exists.


### `list`

Gets marker entries on a map for trackers and for the specified time interval.

**required sub-user rights:** `employee_update`.

#### Parameters

| name       | description                                                                                                                                                                         | type                                                                               |
|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| trackers   | Optional. Array of tracker IDs. All trackers must not be deleted or blocked (if list_blocked=false). If not specified, all available trackers will be used as value.                | int array                                                                          |
| from       | Optional. Start date/time for searching.                                                                                                                                            | [date/time](../../getting-started/introduction.md#data-types)                                   |
| to         | Optional. End date/time for searching. Must be after "from" date.                                                                                                                   | [date/time](../../getting-started/introduction.md#data-types)                                   |
| conditions | Optional. Search conditions to apply to list. See [Search conditions](../commons/entity/search_conditions.md). Allowed fields are `employee`, `location`, `marker_time`, `comment`. | string array                                                                       |
| sort       | Optional. List of sort expressions. See below.                                                                                                                                      | string array                                                                       |
| location   | Optional, location with radius, inside which check-ins must reside.                                                                                                                 | Location JSON. For example, `{ "lat": 53.787154, "lng": 9.757980, "radius": 350 }` | 
| limit      | Optional. Max number of records to return.                                                                                                                                          | int                                                                                |
| offset     | Optional, offset (starting index of first returned record), default is 0.                                                                                                           | int                                                                                |
| format     | Optional. If empty, JSON will be returned. Otherwise server will return file download in specified format. Can be "pdf" or "xlsx".                                                  | string                                                                             |

##### condition fields

| Name        | Type     | Comment       |
|:------------|:---------|:--------------|
| employee    | number   | ID            |
| tracker_id  | number   |               |
| marker_time | DateTime |               |
| location    | string   | address       |
| comment     | string   |               |
| form        | number   | template's ID |

##### sort 

It's a set of sort options. Each option is a pair of field name and sorting direction, e.g. `["location=asc", "employee=desc", "marker_time=desc"]`. 

##### sort fields

| Name        | Type     | Comment   |
|:------------|:---------|:----------|
| employee    | string   | full name |
| tracker_id  | number   |           |
| marker_time | DateTime |           |
| location    | string   | address   |
| comment     | string   |           |
| form        | string   | label     |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "trackers": [616384,345623], "from": "2020-08-05 03:06:00", "to": "2020-09-05 03:00:00", "offset": 20, "limit": 100, "format": "xlsx"}'
    ```

#### Response

```json
{
    "success": true,
    "list": [<checkin>],
    "count": 22
}
```

* `list` - list of check-in objects.
* `count` - int. Total number of check-ins (ignoring offset and limit).

#### Errors

* 7 – Invalid parameters.
* 211 – Requested time span is too big.
* 217 – The list contains non-existent entities – if one of the specified trackers does not exist, is blocked or 
doesn't have required tariff features.
* 221 – Device limit exceeded - if device limit set for the user's dealer has been exceeded.


### `delete`

Deletes check-ins with the specified IDs.

**required sub-user rights:** `checkin_update`.

#### Parameters

| name        | description           | type      |
|:------------|:----------------------|:----------|
| checkin_ids | List of check-in IDs. | int array |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/delete' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkin_ids": [2132,4533]}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/checkin/delete?hash=a6aa75587e5c59c32d347da438505fc3&checkin_ids=[2132,4533]
    ```

#### Response

```json
{
    "success": true
}
```

#### Errors

* 7 – Invalid parameters.
* 201 – Not found in the database - check-ins with the specified IDs don't exist, or their corresponding 
trackers are not available to current sub-user.


### `create`

Creates a new check-in. Needed for exceptional cases.

**required sub-user rights**: `checkin_update`.

#### Parameters

| name            | description                                                                                                                                                                                                     | type        |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------|
| tracker_id      | ID of the tracker. Tracker must belong to authorized user and not be blocked.                                                                                                                                   | int         |
| location        | Location coordinates (see: [data types description section](../../getting-started/introduction.md#data-types) section).                                                                                                      | JSON object |
| comment         | Optional.                                                                                                                                                                                                       | string      |
| file_ids        | Optional. IDs of files created by checkin/image/create).                                                                                                                                                        | int array   |
| form_submission | Optional, only present when sending form along with check-in. If the form includes optional fields that should be left empty for your check-in, refrain from adding these fields to the form submission object. | JSON object |

where `form_submission` type is JSON object:

```json
{
  "form_id": <int>, // id of the form previously created with checkin/form/create
  "values": {
    // map which contains values for form fields
  }
}
```

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 22, "location": { "lat": 9.861999, "lng": -83.948999 }, "comment": "houston, we have a problem", "file_ids": [11, 22], "form_submission": { "form_id": 23423, "values": {"111-aaa-whatever": { "type": "text", "value": "John Doe" }} }}'
    ```

#### Response

```json
{
  "success": true,
  "id": 111
}
```

#### Errors
* 7 – Invalid parameters.
* 201 – Not found in the database - form with the specified IDs don't exist, or their corresponding
  trackers are not available to current sub-user.
* 242 – There were errors during content validation, if given values are invalid for the form.


### `image/create`

Creates an image for check-in. If you have multiple files to upload, be sure to add a brief delay between uploading each one to ensure a smooth process.

#### Parameters

| name     | description                                                                                                                             | type        |
|:---------|:----------------------------------------------------------------------------------------------------------------------------------------|:------------|
| size     | Maximum size in bytes for the file which will be uploaded. This is needed to "reserve" the space for a file in user's disk space quota. | int         |
| filename | Optional. If specified, uploaded file will have the specified name. If not, name will be taken from actual file upload form.            | string      |
| metadata | Optional. Metadata object (for images only).                                                                                            | JSON object |

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

* 268 – File cannot be created due to quota violation.
* 271 – File size is larger than the maximum allowed (by default 16 MB).


### `form/create`

Creates a new form that can be attached to a check-in. Form always created on the basis of form template.

#### Parameters

| name        | description                                                                   | type |
|:------------|:------------------------------------------------------------------------------|:-----|
| tracker_id  | ID of the tracker. Tracker must belong to authorized user and not be blocked. | int  |
| template_id | ID of the form template.                                                      | int  |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/form/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "tracker_id": 22, "template_id": 12548}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/checkin/form/create?hash=a6aa75587e5c59c32d347da438505fc3&tracker_id=22&template_id=12548
    ```

#### Response

```json
{
  "success": true,
  "id": 23423
}
```

#### Errors

* 201 – Not found in the database - if there is no template with such an ID.


### `form/file/create`

Creates a new file entry associated with form's field. If you have multiple files to upload, be sure to add a brief delay between uploading each one to ensure a smooth process.

#### Parameters

| name       | description                                                                                                                             | type        |
|:-----------|:----------------------------------------------------------------------------------------------------------------------------------------|:------------|
| checkin_id | ID of the check-in to which form attached.                                                                                              | int         |
| form_id    | ID of the form.                                                                                                                         | int         |
| field_id   | ID of the form's field to which a new file should be attached.                                                                          | string      |
| size       | Maximum size in bytes for the file which will be uploaded. This is needed to "reserve" the space for a file in user's disk space quota. | int         |
| filename   | Optional. If specified, uploaded file will have the specified name. If not, name will be taken from actual file upload form.            | string      |
| metadata   | Optional. Metadata object (for images only).                                                                                            | JSON object |

* Use only one parameter `checkin_id` or `form_id`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/checkin/form/file/create' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "checkin_id": 1, "field_id": "111-aaa-whatever", "size": 101}'
    ```

#### Response

The response and update process are same to [image/create](#imagecreate).

* `file_id` - int. This value will be submitted as form's field value.
* `url` - string. A URL to which POST form-data with file contents should be executed.
* `expires` - date/time. After this date file record wil expire and upload requests will be rejected.
* `file_field_name` - string. Name for file field in POST upload request.
* `fields` - these fields should be passed as additional fields in POST multipart upload request, field with a file
  must be the last one.

#### Errors

* 201 – Not found in the database - if there is no check-in with such an ID, or check-in doesn't have form, or form has no
  field with such a field_id.
* 231 – Entity type mismatch - if form field is not file-based, i.e. doesn't use file ID as its value.
* 267 – Too many entities - if there are 6 or more unsubmitted files already associated with this form's field.
* 268 – File cannot be created due to quota violation.
* 271 – File size is larger than the maximum allowed (by default 16 MB).

---
title: Service task file
description: Service task file creation API call.
---

# Vehicle service task file

API path: `/vehicle/service_task/file`.

Contains call for creation the service task file.

### create

Creates a file to specify its id in service task later.

#### parameters

| name | description | type |
| :------ | :------ | :----- |
| filename | Optional. If specified, uploaded file will have the specified name. If not, name will be taken from actual file upload form. | string |
| size | Maximum size in bytes for the file which will be uploaded. This is needed to "reserve" the space for file in user's disk space quota. | int |
| metadata | Optional. Metadata object. See [task/form](../../../field_service/task/form/index.md#read). | JSON object |
| type | Can be "image" or "file". Default is "file". | [enum](../../../../getting-started.md#data-types) |

#### response

```json
{
  "success": true,
  "value": {
    "file_id": 111, 
    "url": "http://example.com",
    "expires": "2016-02-03 03:04:00",
    "file_field_name": "file",
    "fields": {
      "token": "skrjsokqsi21lskkwl1783sl2k5"
    }
  }
}
```

* `file_field_name` - string. Name for file field in POST upload request.
* `fields` - object. These fields should be passed as additional fields in POST upload request, field with a file must be the last one.
    * `token` - string. Used for authentication of upload.
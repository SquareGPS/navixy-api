---
title: Vehicle service task file
description: Vehicle service task file
---

# Vehicle service task file

API path: `/vehicle/service_task/file`.

### create

Create file to specify its id in service task later

#### parameters

*   **filename** – (String?) Optional. If specified, uploaded file will have the specified name. If not, name will be taken from actual file upload form.
*   **size** - (int) Maximum size in bytes for the file which will be uploaded. This is needed to “reserve” the space for file in user’s disk space quota. 
*   **metadata** - (JSON object?) Optional.metadata object. see [task/form](../../../field_service/task/form/index.md#read).
*   **type** - "image" or "file". Default is "file".

#### response
```json5
{
  "success": true,
  "value": {
    "file_id": 111, 
    "url": "http://example.com",
    "expires": "2016-02-03 03:04:00",
    "file_field_name": "file", //name for file field in POST upload request
    "fields": { //these fields should be passed as additional fields in POST upload request, field with file must be the last one
      "token": "wewerwerwerwerwerwerwewerwe" //used for authentication of upload
    }
  }
}
```

---
title: Custom Field File
description: Custom Field File
---

# Custom Field File

API path: `/custom_field/file`.

### create

#### parameters

* filename – **string**, optional
* size – **integer**
* metadata – **object**, optional
* type – **"image" | "file"**
* entity_type – **string**, see [entity types](../entity/index.md)

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

#### errors

* 268 – File cannot be created due to quota violation.
* 271 - File size is larger than the maximum allowed (by default 16 MB).

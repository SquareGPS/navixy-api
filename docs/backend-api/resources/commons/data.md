---
title: Data
description: API call to parse the spreadsheet data
---

# Data

API call to parse the spreadsheet data.

***

### /data/spreadsheet/parse

Parse spreadsheet file (.xlsx, .xls, .csv) and store it in internal storage.

#### parameters

| name          | description                                                                                                                           | type        |
|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------|:------------|
| file          | File to upload.                                                                                                                       | file        |
| preview_count | Size of preview. Min=1, max=20.                                                                                                       | int         |
| parse_header  | Parse first row as header.                                                                                                            | boolean     |
| header_map    | If `parse_header` is `true` should contains map of matching column name to field identifier, `{"Label": "label", "Latitude": "lat"}`. | JSON object |

If `parse_header` is set to `true`, first row of the uploaded file will be treated as header corresponding to given `header_map`.

#### response

```json
{
    "file_id": "568539",
    "header": ["header1", "header2"],
    "preview": ["preview of file 1", "preview of file 2"]
}
```

* `file_id` - string. Unique file ID.
* `header` - optional string array. List of files' headers.
* `preview` - string array. First N rows of file.

#### errors

* 234 – Invalid data format.
---
title: Data
description: Parse the spreadsheet data
---

# Data

### /data/spreadsheet/parse

Parse spreadsheet file (.xlsx, .xls, .csv) and store it in internal storage.

#### parameters

| name | description | type |
| :----- | :------------ | :----- |
| file | File to upload. | file |
| preview_count | Size of preview. Min=1, max=20. | int |
| parse_header | Parse first row as header. | boolean |
| header_map | If `parse_header` is `true` should contains map of matching column name to field identifier, `{"Label": "label", "Latitude": "lat"}`. | JSON object |

If `parse_header` is set to `true`, first row of the uploaded file will be treat as header corresponding to given `header_map`.

#### response

```json
{
    "file_id": "568539",
    "header": ["header1", "header2"],
    "preview": ["preview of file 1", "preview of file 2"]
}
```

* `file_id` - string. Unique file id.
* `header` - optional array of string. List of files' headers.
* `preview` - array of string. First N rows of file.

#### errors

* 234 – Invalid data format.
---
title: Data
description: Parse the spreadsheet data
---

# Data

### /data/spreadsheet/parse

Parse spreadsheet file (.xlsx, .xls, .csv) and store it in internal storage.

```json
{
    "file_id": <string, unique file id>,
    "header": <optional, array of string>,
    "preview":<array of array of string, first N rows of file>
}
```

#### parameters

| name | description | type
|------|-------------|-----
| file | File to upload | File
| preview_count | size of preview, min=1, max=20 | Integer
| parse_header | parse first row as header? | Boolean
| header_map | if parse_header is true should contains map of matching column name to field identifier, `{“Label”: “label”, “Latitude”: “lat”}` | Object

If `parse_header` is set to true, first row of the uploaded file will be treat as header corresponding to given `header_map`.

#### response

```json
{
    "file_id": <string, unique file id>,
    "header": <optional, array of string>,
    "preview": <array of array of string, first N rows of file>
}
```

#### errors

234 – Invalid data format.
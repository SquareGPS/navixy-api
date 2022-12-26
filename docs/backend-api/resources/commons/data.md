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

### /data/import/list

Returns the list of the user's import processes.

#### parameters

| name  | description                                                               | type         |
|:------|:--------------------------------------------------------------------------|:-------------|
| types | Optional. Types of the imported entities, e.g. `["vehicle", "employee"]`. | string array |


#### response

```json
{
  "success" : true,
  "list" : [ {
    "id": <int>,
    "user_id": <int>,
    "created": <date>,
    "type": <string>, // vehicle | employee
    "params": {
      "headers": [<string>, <string>,...] // List of files' headers
    },
    "filename": <string>, // Name of preloaded TSV.
    "status": <string>, // created | in_progress | done | failed
    "status_change_date": <date>,
    "progress": {
      "imported": <int>,
      "failed": <int>,
      "percent": <int>, // approximate percentage of processed
      "processed_lines": <int>,
      "warnings": [{line:<int>, error: <string>}], // first 25
      "errors": [{line:<int>, error: <string>}], // first 25
    }
  }, ...]
}
```

#### example

=== "cURL"

```bash
curl -X POST "{{ extra.api_example_url }}/data/import/list" \
    -H "Content-Type: application/json" \
    -d '{
          "hash": "a6aa75587e5c59c32d347da438505fc3"
        }'
```

### read

Returns an import process with specified ID.

#### parameters

| name       | description                   | type   |
|:-----------|:------------------------------|:-------|
| process_id | Process ID                    | int    |
| type       | Type of the imported entities | string |

#### response

```json
{
  "success": true,
  "value": {
    "id": <int>,
    "user_id": <int>,
    "created": <date>,
    "type": <string>, // vehicle | employee
    "params": {
      "headers": [<string>, <string>,...] // List of files' headers
    },
    "filename": <string>, // Name of preloaded TSV.
    "status": <string>, // created | in_progress | done | failed | finished
    "status_change_date": <date>,
    "progress": {
      "imported": <int>,
      "failed": <int>,
      "percent": <int>, // approximate percentage of processed
      "processed_lines": <int>,
      "warnings": [{line:<int>, error: <string>}], // first 25
      "errors": [{line:<int>, error: <string>}], // first 25
    }
  }
}
```

#### example

=== "cURL"

```bash
curl -X POST "{{ extra.api_example_url }}/vehicle/import/read" \
    -H "Content-Type: application/json" \
    -d '{
          "hash": "a6aa75587e5c59c32d347da438505fc3",
          "type": "employee"
          "process_id": 1
        }'
```

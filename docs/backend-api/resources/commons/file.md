---
title: File
description: Contains an API call to get user's file statistic.
---

# File

Contains an API call to get user's file statistic.

<hr>

## API actions

API path: `/file`.

### stats/read

Gets user's files statistic.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/file/stats/read' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/file/stats/read?hash=
    ```

#### response

```json
{
  "success": true,
  "value": {
    "file_count": 10,
    "total_size": 3320542,
    "quota": 1073741824
  }
}
```

* `file_count` - int. Count of all uploaded files.
* `total_size` - int. Total files size in bytes.
* `quota` - int. Space available to the user in bytes.

#### errors

* [General](../../getting-started.md#error-codes) types only.

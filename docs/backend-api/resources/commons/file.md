---
title: File
description: Contains an API call to get user's file statistic.
---

# File

Contains an API call to get user's file statistic.


## API actions

API path: `/file`.

### `stats/read`

Gets user's files statistic.

#### Parameters

Only API key `hash`.

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/file/stats/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/file/stats/read?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### Response

```json
{
    "success": true,
    "value": {
        "file_count": 24,
        "total_size": 40192953,
        "quota": 104857600
    }
}
```

* `file_count` - int. Count of all uploaded files.
* `total_size` - int. Total files size in bytes.
* `quota` - int. Space available to the user in bytes.

#### Errors

* [General](../../getting-started/errors.md#error-codes) types only.
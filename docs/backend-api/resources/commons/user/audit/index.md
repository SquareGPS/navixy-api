---
title: User audit
description: Contains user audit checkin method that calls when user opens UI.
---

# User audit

API path: `/user/audit`.

Contains user audit checkin method that calls when user opens UI.

### checkin

This method calls when user opens UI.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/audit/checkin' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/audit/checkin?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{
    "success": true
}
```

#### errors

* [General](../../../../getting-started.md#error-codes) types only.
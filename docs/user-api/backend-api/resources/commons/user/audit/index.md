---
title: User audit
description: Contains user audit check-in method that calls when user opens UI.
---

# User audit

Contains user audit check-in method that calls when user opens UI or activates the UI tab in the browser after it hasn't been used for more than 2 hours.


## API actions

API path: `/user/audit`.

### `checkin`

This action occurs when a customer opens the UI or activates the UI tab in the browser after it hasn't been used for more than 2 hours.
Works only with standard user session (not with API key).
This action type may be in the [user audit log](audit_log.md#list).

#### Parameters

Only session `hash`.

#### Examples

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

#### Response

```json
{
    "success": true
}
```

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.

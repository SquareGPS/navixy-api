---
title: User session
description: Contains a call to prolong user session.
---

# User session

Contains a call to prolong user session.

API path: `/user/session`.

### renew

Prolongs current user session.

#### parameters

Only session `hash`.

#### examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/session/renew' \
        -H 'Content-Type: application/json' \ 
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
    ```
    
=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/user/session/renew?hash=a6aa75587e5c59c32d347da438505fc3
    ```

#### response

```json
{ "success": true }
```

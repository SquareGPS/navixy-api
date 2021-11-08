---
title: User session
description: Contains a call to prolong user session.
---

# User session

Contains a call to prolong user session.

!!! warning "Session hash is deprecated"
    To work with the API, it is necessary to use the [API key](../../api-keys.md), not the user's session hash.
    Work with API through the user's session is deprecated and will be disabled in the future.
    The only thing that API calls with a user session will work for is creating,
    reading, and deleting API keys.

***

## API actions

API path: `/user/session`.

### renew

Prolongs current user session.
Works only with standard user session (not with API key).

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


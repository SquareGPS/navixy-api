---
title: Base
description: Contains API calls to health-check.
---

# Health check

## API actions

API path: `/base`.

### nothing

The report for health-check. It will do nothing.

#### Parameters

Only API key `hash`.

#### Examples

\=== "cURL"

````
```shell
curl -X POST '{{ extra.api_example_url }}/base/nothing' \
    -H 'Content-Type: application/json' \
    -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b"}'
```
````

\=== "HTTP GET"

````
```
{{ extra.api_example_url }}/base/nothing?hash=a6aa75587e5c59c32d347da438505fc3
```
````

#### Response

```json
{
  "success": true
}
```

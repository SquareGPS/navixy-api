---
title: User UI settings
description: The user interface settings intended for storing settings of client applications that use the API. 
             One can imagine that this works similarly to the browser cache/local storage mechanism. The feature is that long-term 
             storage of these settings provided but not guaranteed - when the quota exceeded, data could be deleted. 
---

# User UI settings

The user interface settings intended for storing settings of client applications that use the API. 
One can imagine that this works similarly to the browser cache/local storage mechanism. The feature is that long-term 
storage of these settings provided but not guaranteed - when the quota exceeded, data could be deleted.


## API actions

API path: `/user/settings/ui`.

### `read`

Reads setting value by key.

#### Parameters

| name | description                                                                                                | type   |
|:-----|:-----------------------------------------------------------------------------------------------------------|:-------|
| key  | Length should be between 1 and 50 is 50 symbols, should only contain English letters, digits, `_` and `-`. | string |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/user/settings/ui/read' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "key": "tracker-icons"}'
    ```

#### Responses:

```json
{
  "success": true,
  "value": "previously saved value"
}
```

When nonexistent key provided:

```json
{
  "success": false,
  "status": {
    "code": 201,
    "description": "Not found in database"
  }
}
```

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types only.


### `update`

Sets setting value.

#### Parameters

| name  | description                                                                                                | type   |
|:------|:-----------------------------------------------------------------------------------------------------------|:-------|
| key   | Length should be between 1 and 50 is 50 symbols, should only contain English letters, digits, `_` and `-`. | string |
| value | A new UI config value. Length should be between 0 and 8192 symbols.                                        | string |

#### Responses:

```json
{ "success": true }
```

#### Errors

* [General](../../../../getting-started/errors.md#error-codes) types.
* 268 - over quota. The amount of storage available for the user for these settings has been exhausted. New settings 
cannot be added until the amount of stored data has been reduced.

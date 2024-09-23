---
title: Event type
description: Contains list method to get event types available to user with localized descriptions.
---

# Event type

Contains list method to get event types available to user with localized descriptions.


## API actions

API path: `/history/type`.

### `list`

Returns available history event types with localized descriptions.

#### Parameters

| name                | description                                                                  | type                                           |
|:--------------------|:-----------------------------------------------------------------------------|:-----------------------------------------------|
| locale              | Locale code to set language of descriptions.                                 | [enum](../../../getting-started/introduction.md#data-types) |
| only_tracker_events | Optional. Default is `true`. Will return only tracker type events if `true`. | boolean                                        |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/history/type/list' \
        -H 'Content-Type: application/json' \
        -d '{"hash": "22eac1c27af4be7b9d04da2ce1af111b", "locale": "En-en"}'
    ```

#### Response

```json
{
    "success": true, 
    "list": [{
         "type": "alarmcontrol",
         "description": "Car alarm" 
    }]
}
```

* `type` - string. History event type.
* `description` - string. Localized description.

#### Errors

* [General](../../../getting-started/errors.md#error-codes) types only.

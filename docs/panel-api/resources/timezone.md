---
title: Timezone
description: API call to get information about all supported timezones for the specified locale.
---

# Timezone

API call to get information about all supported timezones for the specified locale.


## API actions

API path: `panel/timezone`.

### `list`

Gets information about all supported timezones for the specified locale. Does not require authorization.

#### Parameters

| name   | description                                  | type                                                                          |
|:-------|:---------------------------------------------|:------------------------------------------------------------------------------|
| locale | Locale code to set language of descriptions. | [enum](../../user-api/backend-api/getting-started/introduction.md#data-types) |

#### Examples

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/panel/timezone/list' \
        -H 'Content-Type: application/json' \
        -d '{"locale": "en"}'
    ```

=== "HTTP GET"

    ```
    {{ extra.api_example_url }}/panel/timezone/list?locale=en
    ```

#### Response

```json
{
    "success": true,
    "list": [{
      "zone_id": "America/Tijuana",
      "description": "Tijuana",
      "base_offset": -8.0,
      "dst_offset": 1,
      "country_code": "MX",
      "alt_ids": [
          "America/Ensenada",
          "America/Santa_Isabel"
      ]
    }]
}
```

* `zone_id` - string. Timezone ID, which is used throughout the API.
* `description` - string. Localized description of the timezone.
* `description` - int. Base timezone offset in hours, e.g. 1 for London. May be negative.
* `description` - int. DST offset in hours. `0` if no DST rules for this timezone.
* `description` - string. ISO country code for the timezone.
* `alt_ids` - string array. List of string, optional, alternative timezone IDs.

#### Errors

[General](../../user-api/backend-api/getting-started/errors.md#error-codes) types only.

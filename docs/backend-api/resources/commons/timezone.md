---
title: Timezone
description: Contains an API call to get information about all supported timezones.
---

# Timezone

Contains an API call to get information about all supported timezones.


## API actions

API path: `/timezone`.

### `list`

Information about all supported timezones for the specified locale. Does not require user authorization.

#### parameter

| name   | description     | type                                        |
|:-------|:----------------|:--------------------------------------------|
| locale | Name of locale. | [enum](../../getting-started/introduction.md#data-types) |

#### Example

=== "cURL"

    ```shell
    curl -X POST '{{ extra.api_example_url }}/timezone/list' \
        -H 'Content-Type: application/json' \
        -d '{"locale": "En-en"}'
    ```

#### Response

```json
{
    "success": true,
    "list": [{
        "zone_id": "Australia/Sydney",
        "description": "Sydney",
        "base_offset": 10.0,
        "dst_offset": 1,
        "country_code": "AU",
        "alt_ids": ["Australia/ACT", "Australia/Canberra", "Australia/NSW"]
    }]
}
```

* `zone_id` - string. Timezone ID, which is used throughout the API.
* `description` - string. Localized description of the timezone.
* `base_offset` - double. Base timezone offset in hours, e.g. 10 means UTC +10. May be negative or fractional!
* `dst_offset` - int. DST offset in hours (0 if no DST rules for this timezone).
* `country_code` - string. ISO country code for the timezone.
* `alt_ids` - string array. List of strings, optional, alternative timezone IDs.

#### Errors

* [General](../../getting-started/errors.md#error-codes) types only.

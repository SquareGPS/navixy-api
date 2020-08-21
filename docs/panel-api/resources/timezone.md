---
title: /timezone
description: /timezone
---

## list

`list(locale)`

Information about all supported timezones for the specified locale.

Does not require user authorization.

### Return value

```json
{
    "success": true,
    "list": [ {
        "zone_id": <string>,     // timezone ID, which is used throughout the API, e.g. "Africa/Dar_es_Salaam"
        "description": <string>, // Localized description of the timezone, e.g. "Hamburg"
        "base_offset": <int>,    // base timezone offset in hours, e.g. 1 for London. May be negative!
        "dst_offset": <int>,     // DST offset in hours (0 if no DST rules for this timezone).
        "country_code": <string> // ISO country code for timezone, e.g. "DE"
    }]
}
```

### Errors

Only [standard errors](../../backend-api/getting-started.md#error-codes).
